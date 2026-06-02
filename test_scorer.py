from pose_analyzer import analyze_pose
from angle_calculator import calculate_all_batting_angles
from scorer import score_angles, get_performance_label, get_priority_feedback
from PIL import Image

image = Image.open("test_cricket.jpg")
annotated, coords, success = analyze_pose(image)

if success:
    angles = calculate_all_batting_angles(coords)
    scores, feedback, overall = score_angles(angles)
    label, color = get_performance_label(overall)
    tips = get_priority_feedback(feedback, scores)

    print(f"\n{'='*45}")
    print(f"  CRICCOACH AI — TECHNIQUE REPORT")
    print(f"{'='*45}")
    print(f"  Overall Score: {overall}/100  {label}")
    print(f"{'='*45}\n")

    print("DETAILED BREAKDOWN:")
    print("-" * 45)
    for name, data in scores.items():
        bar = "█" * data['score'] + "░" * (10 - data['score'])
        print(f"{data['description']:<22} {bar} {data['score']}/10")

    print(f"\n{'='*45}")
    print("COACHING FEEDBACK (Priority Order):")
    print("="*45)
    for i, tip in enumerate(tips, 1):
        icon = "❌" if tip['score'] < 8 else "✅"
        print(f"\n{i}. {icon} {tip['area']}")
        print(f"   Your angle : {tip['your_angle']}°")
        print(f"   Ideal range: {tip['ideal']}")
        print(f"   Coach says : {tip['tip']}")
else:
    print("No pose detected")