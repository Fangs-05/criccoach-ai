# Multi-Shot Configuration Dictionary
SHOT_BENCHMARKS = {
    'Stance': {
        'lead_elbow': {'ideal_min': 90, 'ideal_max': 140, 'description': 'Lead Elbow', 'tip_low': 'Lead elbow is too bent. Extend slightly for better control.', 'tip_high': 'Lead elbow is too straight. Bend slightly for power.', 'tip_good': 'Good lead elbow position.'},
        'back_elbow': {'ideal_min': 85, 'ideal_max': 135, 'description': 'Back Elbow', 'tip_low': 'Back elbow is too tucked. Give it space.', 'tip_high': 'Back elbow is flaring open.', 'tip_good': 'Good back elbow position.'},
        'lead_knee': {'ideal_min': 140, 'ideal_max': 175, 'description': 'Lead Knee Flex', 'tip_low': 'Over-flexed on the front leg.', 'tip_high': 'Front leg is too stiff. Add slight bend.', 'tip_good': 'Good lead knee flex.'},
        'back_knee': {'ideal_min': 130, 'ideal_max': 170, 'description': 'Back Knee Flex', 'tip_low': 'Crouching too low on the back leg.', 'tip_high': 'Back leg is too stiff. Lower your base.', 'tip_good': 'Good back knee flex.'},
        'trunk_lean': {'ideal_min': 150, 'ideal_max': 180, 'description': 'Trunk Lean', 'tip_low': 'Leaning too far forward.', 'tip_high': 'Too upright. Lean slightly toward the ball.', 'tip_good': 'Excellent posture.'},
        'shoulder_alignment': {'ideal_min': 0, 'ideal_max': 15, 'description': 'Shoulder Level', 'tip_low': 'Shoulders are dipping.', 'tip_high': 'Shoulders are uneven.', 'tip_good': 'Shoulders are perfectly level.'},
        'head_position': {'ideal_min': 140, 'ideal_max': 180, 'description': 'Head Position', 'tip_low': 'Head is dropping.', 'tip_high': 'Head is leaning back.', 'tip_good': 'Head is still and upright.'}
    },
    'Forward Defense': {
        'lead_knee': {'ideal_min': 120, 'ideal_max': 150, 'description': 'Lead Knee Stride', 'tip_low': 'Lunging too far.', 'tip_high': 'Not striding to the pitch of the ball.', 'tip_good': 'Solid stride to smother the spin/seam.'},
        'trunk_lean': {'ideal_min': 120, 'ideal_max': 150, 'description': 'Weight Transfer', 'tip_low': 'Falling completely over.', 'tip_high': 'Weight stuck on the back foot.', 'tip_good': 'Weight transferred perfectly over the front foot.'},
        'head_position': {'ideal_min': 140, 'ideal_max': 170, 'description': 'Head over Ball', 'tip_low': 'Head dropping too low.', 'tip_high': 'Head left behind the pad.', 'tip_good': 'Head right on top of the ball.'}
    },
    'Cover Drive': {
        'lead_elbow': {'ideal_min': 130, 'ideal_max': 175, 'description': 'Lead Elbow (Drive)', 'tip_low': 'Lead arm must extend fully into the shot.', 'tip_high': 'Arm is hyper-extended.', 'tip_good': 'High, beautiful lead elbow.'},
        'back_elbow': {'ideal_min': 90, 'ideal_max': 140, 'description': 'Back Elbow (Drive)', 'tip_low': 'Back elbow is cramped.', 'tip_high': 'Back elbow flying open.', 'tip_good': 'Back elbow tucked nicely in the swing.'},
        'lead_knee': {'ideal_min': 90, 'ideal_max': 140, 'description': 'Lead Knee Stride', 'tip_low': 'Collapsing on the front knee.', 'tip_high': 'Not striding forward enough.', 'tip_good': 'Great stride and knee flex.'},
        'back_knee': {'ideal_min': 140, 'ideal_max': 180, 'description': 'Back Leg Extension', 'tip_low': 'Weight is stuck on the back foot.', 'tip_high': 'Back leg is too stiff.', 'tip_good': 'Back leg extended naturally.'},
        'trunk_lean': {'ideal_min': 130, 'ideal_max': 160, 'description': 'Weight Transfer', 'tip_low': 'Leaning too far over.', 'tip_high': 'Not leaning into the shot enough.', 'tip_good': 'Leaning beautifully into the drive.'}
    },
    'Straight Drive': {
        'lead_elbow': {'ideal_min': 140, 'ideal_max': 180, 'description': 'High Lead Elbow', 'tip_low': 'Elbow dropping, causing a cross-batted swing.', 'tip_high': 'Hyper-extended arm.', 'tip_good': 'Textbook high elbow presenting a straight face.'},
        'lead_knee': {'ideal_min': 100, 'ideal_max': 145, 'description': 'Straight Stride', 'tip_low': 'Over-striding.', 'tip_high': 'Playing too far away from the body.', 'tip_good': 'Perfect stride down the pitch.'},
        'head_position': {'ideal_min': 150, 'ideal_max': 180, 'description': 'Head Alignment', 'tip_low': 'Head falling to the off-side.', 'tip_high': 'Leaning back.', 'tip_good': 'Head perfectly still and aligned.'}
    },
    'On Drive': {
        'lead_knee': {'ideal_min': 110, 'ideal_max': 150, 'description': 'Leg-side Stride', 'tip_low': 'Lunging and losing balance.', 'tip_high': 'Not getting to the pitch.', 'tip_good': 'Good stride to open the hips.'},
        'trunk_lean': {'ideal_min': 140, 'ideal_max': 170, 'description': 'Balance', 'tip_low': 'Falling over to the off-side.', 'tip_high': 'Weight on the heels.', 'tip_good': 'Excellent balance playing through the leg side.'}
    },
    'Pull Shot': {
        'lead_elbow': {'ideal_min': 130, 'ideal_max': 180, 'description': 'Lead Arm Extension', 'tip_low': 'Arm too bent, swinging from underneath.', 'tip_high': 'Too stiff.', 'tip_good': 'Good extension on the pull.'},
        'lead_knee': {'ideal_min': 140, 'ideal_max': 180, 'description': 'Front Leg Clearing', 'tip_low': 'Front leg collapsing.', 'tip_high': 'Front leg too rigid.', 'tip_good': 'Front leg cleared well.'},
        'back_knee': {'ideal_min': 100, 'ideal_max': 150, 'description': 'Back Foot Base', 'tip_low': 'Crouching too low.', 'tip_high': 'Not transferring weight back.', 'tip_good': 'Strong base on the back foot.'},
        'trunk_lean': {'ideal_min': 160, 'ideal_max': 180, 'description': 'Upright Posture', 'tip_low': 'Falling over to the off-side.', 'tip_high': 'Leaning too far back.', 'tip_good': 'Tall, commanding posture.'}
    },
    'Square Cut': {
        'back_knee': {'ideal_min': 120, 'ideal_max': 160, 'description': 'Back Foot Weight', 'tip_low': 'Squatting too deep.', 'tip_high': 'Not rocking back enough.', 'tip_good': 'Weight transferred perfectly to the back foot.'},
        'lead_elbow': {'ideal_min': 150, 'ideal_max': 180, 'description': 'Arm Extension', 'tip_low': 'Cramped swing.', 'tip_high': 'Over-reaching.', 'tip_good': 'Great extension to meet the wide ball.'}
    },
    'Hook Shot': {
        'back_knee': {'ideal_min': 110, 'ideal_max': 160, 'description': 'Back Foot Base', 'tip_low': 'Losing balance on the short ball.', 'tip_high': 'Too stiff, getting under the bounce.', 'tip_good': 'Strong base to control the high bounce.'},
        'head_position': {'ideal_min': 140, 'ideal_max': 180, 'description': 'Eye Tracking', 'tip_low': 'Taking eyes off the ball.', 'tip_high': 'Leaning back blindly.', 'tip_good': 'Eyes right behind the bounce.'}
    },
    'Standard Sweep': {
        'lead_knee': {'ideal_min': 40, 'ideal_max': 90, 'description': 'Kneeling Base', 'tip_low': 'Knee crashing into the ground.', 'tip_high': 'Not dropping low enough for the sweep.', 'tip_good': 'Perfect low base for the spin.'},
        'lead_elbow': {'ideal_min': 120, 'ideal_max': 170, 'description': 'Horizontal Swing', 'tip_low': 'Bat coming from too high.', 'tip_high': 'Swinging wildly.', 'tip_good': 'Great horizontal bat path.'}
    },
    'Slog Sweep': {
        'lead_knee': {'ideal_min': 50, 'ideal_max': 100, 'description': 'Aggressive Base', 'tip_low': 'Losing balance forward.', 'tip_high': 'Not getting under the ball.', 'tip_good': 'Strong kneeling position.'},
        'trunk_lean': {'ideal_min': 150, 'ideal_max': 180, 'description': 'Lofting Posture', 'tip_low': 'Leaning forward, hitting it flat.', 'tip_high': 'Leaning back too far.', 'tip_good': 'Creating great leverage to clear the ropes.'}
    },
    'Helicopter Shot': {
        'back_knee': {'ideal_min': 110, 'ideal_max': 160, 'description': 'Deep Crease Base', 'tip_low': 'Squatting too far.', 'tip_high': 'Legs too stiff to dig out the yorker.', 'tip_good': 'Excellent base deep in the crease.'},
        'lead_elbow': {'ideal_min': 90, 'ideal_max': 160, 'description': 'Whip Follow-through', 'tip_low': 'Not generating enough wrist speed.', 'tip_high': 'Losing control of the bat.', 'tip_good': 'Incredible bat speed and whip.'}
    }
}

# Bowling Action Configuration Dictionary
BOWLING_BENCHMARKS = {
    'Pace - Stock Delivery': {
        'lead_knee': {'ideal_min': 155, 'ideal_max': 180, 'description': 'Braced Front Knee', 'tip_low': 'Front knee is collapsing on landing. Brace it straight.', 'tip_high': 'Hyperextended front leg.', 'tip_good': 'Excellent braced front leg.'},
        'lead_elbow': {'ideal_min': 165, 'ideal_max': 180, 'description': 'Bowling Arm Extension', 'tip_low': 'Elbow is bent at release. Keep it fully straight.', 'tip_high': 'Hyperextended arm.', 'tip_good': 'Beautiful high, straight release.'},
        'trunk_lean': {'ideal_min': 65, 'ideal_max': 95, 'description': 'Trunk Lean', 'tip_low': 'Falling away too sideways at release.', 'tip_high': 'Too upright at release.', 'tip_good': 'Great forward torso crunch.'}
    },
    'Pace - Yorker': {
        'lead_knee': {'ideal_min': 160, 'ideal_max': 180, 'description': 'Stiff Front Brace', 'tip_low': 'You need maximum resistance to drive the ball into the toes. Brace harder.', 'tip_high': 'Hyperextended.', 'tip_good': 'Perfect stiff brace for a yorker.'},
        'lead_elbow': {'ideal_min': 150, 'ideal_max': 180, 'description': 'Delayed Arm Elevation', 'tip_low': 'Arm dropping too low, causing a full toss.', 'tip_high': 'Releasing too early.', 'tip_good': 'Great delayed release angle.'},
        'trunk_lean': {'ideal_min': 30, 'ideal_max': 55, 'description': 'Aggressive Forward Crunch', 'tip_low': 'Falling completely over.', 'tip_high': 'Not driving forward enough. Crunch aggressively toward the stumps.', 'tip_good': 'Excellent forward momentum to dig out the yorker.'}
    },
    'Pace - Bouncer': {
        'lead_knee': {'ideal_min': 150, 'ideal_max': 180, 'description': 'Base Stability', 'tip_low': 'Collapsing knee ruins the bounce. Stay tall.', 'tip_high': 'Hyperextended.', 'tip_good': 'Strong, tall base.'},
        'lead_elbow': {'ideal_min': 165, 'ideal_max': 180, 'description': 'High Release Point', 'tip_low': 'Arm is too low, you will drag it down instead of bouncing it.', 'tip_high': 'Hyperextended.', 'tip_good': 'Perfect high release to bang it into the pitch.'},
        'trunk_lean': {'ideal_min': 65, 'ideal_max': 85, 'description': 'Upright Posture', 'tip_low': 'Leaning too far forward. Stay taller to hit the deck hard.', 'tip_high': 'Leaning backward, losing pace.', 'tip_good': 'Excellent upright posture for the short ball.'}
    },
    'Spin - Off-Spin': {
        'lead_knee': {'ideal_min': 140, 'ideal_max': 165, 'description': 'Front Leg Pivot', 'tip_low': 'Too much knee bend, losing pivot energy.', 'tip_high': 'Too stiff for a spin action.', 'tip_good': 'Great front leg block to pivot over.'},
        'shoulder_rotation': {'ideal_min': 55, 'ideal_max': 90, 'description': 'Front-on Chest', 'tip_low': 'Action is too closed/side-on for off-spin. Open your chest toward the batter.', 'tip_high': 'Over-rotating.', 'tip_good': 'Excellent front-on chest position.'},
        'trunk_lean': {'ideal_min': 75, 'ideal_max': 100, 'description': 'Upright Posture', 'tip_low': 'Falling away. Stay taller to get over the ball.', 'tip_high': 'Leaning too far back.', 'tip_good': 'Good upright posture.'}
    },
    'Spin - Leg-Spin': {
        'lead_knee': {'ideal_min': 135, 'ideal_max': 160, 'description': 'Front Leg Pivot', 'tip_low': 'Sinking too low on the front knee.', 'tip_high': 'Too stiff.', 'tip_good': 'Strong block to rip the ball over.'},
        'shoulder_rotation': {'ideal_min': 0, 'ideal_max': 35, 'description': 'Side-on Alignment', 'tip_low': 'Over-rotating.', 'tip_high': 'Action is too front-on for leg-spin. Stay side-on longer to generate torque.', 'tip_good': 'Beautiful side-on position.'},
        'trunk_lean': {'ideal_min': 70, 'ideal_max': 95, 'description': 'Body Pivot', 'tip_low': 'Collapsing sideways.', 'tip_high': 'Too upright, drive through the action.', 'tip_good': 'Excellent body alignment through the crease.'}
    },
    'Pace - Sling Action': {
        'lead_knee': {
            'ideal_min': 150, 
            'ideal_max': 180, 
            'description': 'Braced Front Knee', 
            'tip_low': 'Front knee is collapsing. Even slingers need a rock-solid base to transfer energy.', 
            'tip_high': 'Hyperextended front leg.', 
            'tip_good': 'Excellent braced front leg to support the sling action.'
        },
        'lead_elbow': {
            'ideal_min': 145, 
            'ideal_max': 180, 
            'description': 'Whip Extension', 
            'tip_low': 'Elbow is too bent. Keep the slinging arm extended to maximize the whip effect.', 
            'tip_high': 'Hyperextended arm.', 
            'tip_good': 'Great arm extension through the horizontal release.'
        },
        'trunk_lean': {
            'ideal_min': 65, 
            'ideal_max': 110, 
            'description': 'Lateral Torso Bend', 
            'tip_low': 'Falling over too far horizontally. Keep the head steady.', 
            'tip_high': 'Too upright for a slinger. Drop the non-bowling shoulder to create the horizontal arm path.', 
            'tip_good': 'Perfect unorthodox slinging posture.'
        }
    }
}

def score_angles(angles, shot_type="Stance"):
    """
    Scores each angle against specific shot benchmarks.
    Safely handles obscured/None angles.
    """
    scores = {}
    feedback = {}
    total = 0
    count = 0

    # ROUTING LOGIC: Choose between Batting or Bowling benchmarks
    if shot_type in BOWLING_BENCHMARKS:
        benchmarks = BOWLING_BENCHMARKS[shot_type]
    else:
        # Fallback to a safe baseline if the exact shot type isn't found
        benchmarks = SHOT_BENCHMARKS.get(shot_type, SHOT_BENCHMARKS['Stance'])

    for angle_name, value in angles.items():
        bench = benchmarks.get(angle_name)
        if not bench:
            continue
            
        # Handle obscured/missing joints safely
        if value is None:
            scores[angle_name] = {
                'score': 0,
                'value': 'Obscured',
                'description': bench['description'],
                'status': 'obscured',
                'ideal_min': bench['ideal_min'],
                'ideal_max': bench['ideal_max'],
            }
            feedback[angle_name] = "Camera could not see this area clearly."
            continue

        ideal_min = bench['ideal_min']
        ideal_max = bench['ideal_max']
        desc = bench['description']

        if ideal_min <= value <= ideal_max:
            score = 10
            tip = bench['tip_good']
            status = 'good'
        else:
            if value < ideal_min:
                deviation = ideal_min - value
                tip = bench['tip_low']
            else:
                deviation = value - ideal_max
                tip = bench['tip_high']

            if deviation <= 10:
                score = 8
            elif deviation <= 20:
                score = 6
            elif deviation <= 35:
                score = 4
            elif deviation <= 50:
                score = 2
            else:
                score = 1

            status = 'needs_work'

        scores[angle_name] = {
            'score': score,
            'value': value,
            'description': desc,
            'status': status,
            'ideal_min': ideal_min,
            'ideal_max': ideal_max,
        }
        feedback[angle_name] = tip
        
        # Only tally scores for visible joints
        total += score
        count += 1

    max_possible = count * 10
    overall = round((total / max_possible) * 100) if max_possible > 0 else 0

    return scores, feedback, overall


def get_performance_label(overall_score):
    """Returns performance label based on score"""
    if overall_score >= 85:
        return "🏆 Excellent", "#00C851"
    elif overall_score >= 70:
        return "✅ Good", "#33b5e5"
    elif overall_score >= 55:
        return "⚠️ Average", "#ffbb33"
    elif overall_score >= 40:
        return "❌ Needs Work", "#ff8800"
    else:
        return "🔴 Poor", "#CC0000"


def get_priority_feedback(feedback, scores):
    """
    Returns feedback sorted by priority (worst areas first).
    Ignores obscured angles in the priority queue.
    """
    # Filter out obscured angles before sorting
    visible_scores = {k: v for k, v in scores.items() if v['status'] != 'obscured'}
    
    sorted_items = sorted(
        visible_scores.items(),
        key=lambda x: x[1]['score']
    )

    priority_tips = []
    
    # Needs Work
    for angle_name, score_data in sorted_items:
        if score_data['status'] == 'needs_work':
            priority_tips.append({
                'area': score_data['description'],
                'score': score_data['score'],
                'tip': feedback[angle_name],
                'your_angle': score_data['value'],
                'ideal': f"{score_data['ideal_min']}° - {score_data['ideal_max']}°"
            })

    # Good
    for angle_name, score_data in sorted_items:
        if score_data['status'] == 'good':
            priority_tips.append({
                'area': score_data['description'],
                'score': score_data['score'],
                'tip': feedback[angle_name],
                'your_angle': score_data['value'],
                'ideal': f"{score_data['ideal_min']}° - {score_data['ideal_max']}°"
            })

    # Append warnings for obscured areas at the bottom
    for angle_name, score_data in scores.items():
        if score_data['status'] == 'obscured':
             priority_tips.append({
                'area': score_data['description'] + " [Obscured]",
                'score': 10, # Neutral score placeholder
                'tip': feedback[angle_name],
                'your_angle': 'N/A',
                'ideal': f"{score_data['ideal_min']}° - {score_data['ideal_max']}°"
            })

    return priority_tips