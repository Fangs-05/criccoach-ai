import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import urllib.request
import os

# New MediaPipe Tasks API
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode
PoseLandmark = mp.tasks.vision.PoseLandmark
drawing_utils = mp.tasks.vision.drawing_utils
drawing_styles = mp.tasks.vision.drawing_styles
PoseLandmarksConnections = mp.tasks.vision.PoseLandmarksConnections

# Model path
MODEL_PATH = "pose_landmarker_full.task"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading pose model (~25MB)...")
        url = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/latest/pose_landmarker_full.task"
        urllib.request.urlretrieve(url, MODEL_PATH)
        print("Model downloaded!")

download_model()

# Key landmark indices
LANDMARK_NAMES = {
    0:  'NOSE',
    7:  'LEFT_EAR',
    8:  'RIGHT_EAR',
    11: 'LEFT_SHOULDER',
    12: 'RIGHT_SHOULDER',
    13: 'LEFT_ELBOW',
    14: 'RIGHT_ELBOW',
    15: 'LEFT_WRIST',
    16: 'RIGHT_WRIST',
    23: 'LEFT_HIP',
    24: 'RIGHT_HIP',
    25: 'LEFT_KNEE',
    26: 'RIGHT_KNEE',
    27: 'LEFT_ANKLE',
    28: 'RIGHT_ANKLE',
}

def analyze_pose(image_input):
    """
    Takes PIL Image or numpy array
    Returns: annotated_image, landmarks_dict, success_bool
    """
    # Convert to numpy RGB array safely
    try:
        if isinstance(image_input, Image.Image):
            image_np = np.array(image_input.convert('RGB'))
        else:
            image_np = image_input

        # Create MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=image_np
        )

        # Run detection
        options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=MODEL_PATH),
            running_mode=RunningMode.IMAGE,
            num_poses=1,
            min_pose_detection_confidence=0.5,
            min_pose_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        with PoseLandmarker.create_from_options(options) as landmarker:
            result = landmarker.detect(mp_image)

        if not result.pose_landmarks or len(result.pose_landmarks) == 0:
            return image_np, None, False

        landmarks = result.pose_landmarks[0]

        # Draw skeleton
        annotated = draw_skeleton(image_np.copy(), landmarks)

        # Build coords dictionary with VISIBILITY CHECK
        coords = {}
        for idx, name in LANDMARK_NAMES.items():
            if idx < len(landmarks):
                lm = landmarks[idx]
                # If MediaPipe can't clearly see the joint, mark it missing
                if getattr(lm, 'visibility', 1.0) > 0.5:
                    coords[name] = (lm.x, lm.y)
                else:
                    coords[name] = None
            else:
                coords[name] = None

        return annotated, coords, True

    except Exception as e:
        print(f"Pose Analysis Error: {e}")
        # Return the original image untouched if analysis fails completely
        fallback_img = np.array(image_input) if isinstance(image_input, Image.Image) else image_input
        return fallback_img, None, False


def draw_skeleton(image, landmarks):
    """Draw pose skeleton on image"""
    h, w = image.shape[:2]

    # Define connections manually
    connections = [
        (11, 12),  # shoulders
        (11, 13),  # left shoulder to elbow
        (13, 15),  # left elbow to wrist
        (12, 14),  # right shoulder to elbow
        (14, 16),  # right elbow to wrist
        (11, 23),  # left shoulder to hip
        (12, 24),  # right shoulder to hip
        (23, 24),  # hips
        (23, 25),  # left hip to knee
        (25, 27),  # left knee to ankle
        (24, 26),  # right hip to knee
        (26, 28),  # right knee to ankle
        (0, 7),    # nose to left ear
        (0, 8),    # nose to right ear
    ]

    # Draw connections
    for start_idx, end_idx in connections:
        if start_idx < len(landmarks) and end_idx < len(landmarks):
            start = landmarks[start_idx]
            end = landmarks[end_idx]
            # Only draw line if both points are reasonably visible
            if getattr(start, 'visibility', 1.0) > 0.5 and getattr(end, 'visibility', 1.0) > 0.5:
                pt1 = (int(start.x * w), int(start.y * h))
                pt2 = (int(end.x * w), int(end.y * h))
                cv2.line(image, pt1, pt2, (0, 200, 255), 3)

    # Draw landmark dots
    for idx in LANDMARK_NAMES.keys():
        if idx < len(landmarks):
            lm = landmarks[idx]
            if getattr(lm, 'visibility', 1.0) > 0.5:
                cx = int(lm.x * w)
                cy = int(lm.y * h)
                cv2.circle(image, (cx, cy), 6, (0, 255, 0), -1)
                cv2.circle(image, (cx, cy), 6, (0, 0, 0), 1)

    return image


def get_all_key_landmarks(coords):
    return coords