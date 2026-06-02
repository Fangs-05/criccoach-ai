import numpy as np

def calculate_angle(point_a, point_b, point_c):
    """
    Calculates angle at point_b formed by a->b->c
    Returns angle in degrees
    """
    a = np.array(point_a)
    b = np.array(point_b)
    c = np.array(point_c)

    ba = a - b
    bc = c - b

    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    cosine = np.clip(cosine, -1.0, 1.0)
    angle = np.degrees(np.arccos(cosine))

    return round(angle, 2)


def get_landmark_roles(handedness):
    """
    Maps left/right MediaPipe landmarks to lead/back cricketing roles 
    based on the batter's handedness.
    """
    is_right = (handedness.lower() == "right")
    
    return {
        'lead_shoulder': 'LEFT_SHOULDER' if is_right else 'RIGHT_SHOULDER',
        'back_shoulder': 'RIGHT_SHOULDER' if is_right else 'LEFT_SHOULDER',
        'lead_elbow': 'LEFT_ELBOW' if is_right else 'RIGHT_ELBOW',
        'back_elbow': 'RIGHT_ELBOW' if is_right else 'LEFT_ELBOW',
        'lead_wrist': 'LEFT_WRIST' if is_right else 'RIGHT_WRIST',
        'back_wrist': 'RIGHT_WRIST' if is_right else 'LEFT_WRIST',
        'lead_hip': 'LEFT_HIP' if is_right else 'RIGHT_HIP',
        'back_hip': 'RIGHT_HIP' if is_right else 'LEFT_HIP',
        'lead_knee': 'LEFT_KNEE' if is_right else 'RIGHT_KNEE',
        'back_knee': 'RIGHT_KNEE' if is_right else 'LEFT_KNEE',
        'lead_ankle': 'LEFT_ANKLE' if is_right else 'RIGHT_ANKLE',
        'back_ankle': 'RIGHT_ANKLE' if is_right else 'LEFT_ANKLE',
    }


def calculate_all_batting_angles(coords, handedness="Right"):
    """
    Calculates key batting form angles from landmark coords.
    Adapts dynamically to left or right-handed batters.
    Returns dictionary of angles. Missing landmarks gracefully return None.
    """
    angles = {}
    roles = get_landmark_roles(handedness)

    def safe_angle(p1_key, p2_key, p3_key):
        """Helper to calculate angle safely. Returns None if landmarks are obscured."""
        try:
            if all(coords.get(k) for k in [p1_key, p2_key, p3_key]):
                return calculate_angle(coords[p1_key], coords[p2_key], coords[p3_key])
        except Exception:
            pass
        return None

    # 1. LEAD ELBOW
    angles['lead_elbow'] = safe_angle(roles['lead_shoulder'], roles['lead_elbow'], roles['lead_wrist'])

    # 2. BACK ELBOW
    angles['back_elbow'] = safe_angle(roles['back_shoulder'], roles['back_elbow'], roles['back_wrist'])

    # 3. LEAD KNEE
    angles['lead_knee'] = safe_angle(roles['lead_hip'], roles['lead_knee'], roles['lead_ankle'])

    # 4. BACK KNEE
    angles['back_knee'] = safe_angle(roles['back_hip'], roles['back_knee'], roles['back_ankle'])

    # 5. TRUNK LEAN
    angles['trunk_lean'] = safe_angle(roles['lead_shoulder'], roles['lead_hip'], roles['lead_knee'])

    # 6. SHOULDER ALIGNMENT
    try:
        if all(coords.get(k) for k in [roles['lead_shoulder'], roles['back_shoulder']]):
            ls = coords[roles['lead_shoulder']]
            rs = coords[roles['back_shoulder']]
            dx = rs[0] - ls[0]
            dy = rs[1] - ls[1]
            angles['shoulder_alignment'] = round(abs(np.degrees(np.arctan2(dy, dx))), 2)
        else:
            angles['shoulder_alignment'] = None
    except Exception:
        angles['shoulder_alignment'] = None

    # 7. HEAD POSITION
    angles['head_position'] = safe_angle('NOSE', roles['lead_shoulder'], roles['lead_hip'])

    # 8. HIP ALIGNMENT
    try:
        if all(coords.get(k) for k in [roles['lead_hip'], roles['back_hip']]):
            lh = coords[roles['lead_hip']]
            rh = coords[roles['back_hip']]
            dx = rh[0] - lh[0]
            dy = rh[1] - lh[1]
            angles['hip_alignment'] = round(abs(np.degrees(np.arctan2(dy, dx))), 2)
        else:
            angles['hip_alignment'] = None
    except Exception:
        angles['hip_alignment'] = None

    return angles
def calculate_all_bowling_angles(coords, bowler_arm="Right-Arm"):
    """
    Calculates key fast bowling release angles from landmark coords.
    Adapts dynamically to left or right-arm bowlers.
    Returns dictionary mapping to 'lead_elbow', 'lead_knee', and 'trunk_lean'.
    """
    angles = {}

    def safe_angle(p1_key, p2_key, p3_key):
        """Helper to calculate angle safely. Returns None if landmarks are obscured."""
        try:
            if all(coords.get(k) for k in [p1_key, p2_key, p3_key]):
                return calculate_angle(coords[p1_key], coords[p2_key], coords[p3_key])
        except Exception:
            pass
        return None

    # 1. Determine which side is bowling vs bracing
    is_right = (bowler_arm == "Right-Arm")
    
    # For a Right-Arm bowler, the bowling arm is RIGHT, but the bracing leg is LEFT.
    bowl_shoulder = 'RIGHT_SHOULDER' if is_right else 'LEFT_SHOULDER'
    bowl_elbow = 'RIGHT_ELBOW' if is_right else 'LEFT_ELBOW'
    bowl_wrist = 'RIGHT_WRIST' if is_right else 'LEFT_WRIST'
    
    brace_hip = 'LEFT_HIP' if is_right else 'RIGHT_HIP'
    brace_knee = 'LEFT_KNEE' if is_right else 'RIGHT_KNEE'
    brace_ankle = 'LEFT_ANKLE' if is_right else 'RIGHT_ANKLE'

    # 2. Calculate the core physics angles
    # Bowling Arm Extension (Mapped to 'lead_elbow' for the scorer)
    angles['lead_elbow'] = safe_angle(bowl_shoulder, bowl_elbow, bowl_wrist)

    # Braced Front Leg (Mapped to 'lead_knee' for the scorer)
    angles['lead_knee'] = safe_angle(brace_hip, brace_knee, brace_ankle)

    # 3. Trunk Lean / Torso Crunch
    try:
        if all(coords.get(k) for k in [brace_hip, bowl_shoulder]):
            hip_pos = coords[brace_hip]
            shoulder_pos = coords[bowl_shoulder]
            
            # Create a virtual point straight up from the hip for vertical reference
            vertical_pt = [hip_pos[0], hip_pos[1] - 0.1]
            
            angles['trunk_lean'] = calculate_angle(vertical_pt, hip_pos, shoulder_pos)
        else:
            angles['trunk_lean'] = None
    except Exception:
        angles['trunk_lean'] = None
    
    # 4. Shoulder Rotation Index (Front-on vs Side-on)
    try:
        if all(coords.get(k) for k in ['LEFT_SHOULDER', 'RIGHT_SHOULDER', brace_hip]):
            ls_x = coords['LEFT_SHOULDER'][0]
            rs_x = coords['RIGHT_SHOULDER'][0]
            
            # Use hip-to-shoulder vertical distance as a scale reference
            torso_length = abs(coords[bowl_shoulder][1] - coords[brace_hip][1]) + 1e-6
            
            # Ratio of shoulder width to torso length
            # ~0.0 means side-on (shoulders overlapping), high ratio means front-on
            rotation_ratio = abs(ls_x - rs_x) / torso_length
            
            # Convert this to an artificial "Angle" (0 to 90) for the scorer
            # 0 = perfectly side-on, 90 = perfectly front-on
            # A standard human chest maxes out around a 0.5 ratio
            normalized_angle = min((rotation_ratio / 0.5) * 90, 90)
            angles['shoulder_rotation'] = round(normalized_angle, 2)
        else:
            angles['shoulder_rotation'] = None
    except Exception:
        angles['shoulder_rotation'] = None

    return angles