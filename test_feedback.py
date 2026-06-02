from pose_analyzer import analyze_pose
from angle_calculator import calculate_all_batting_angles
from scorer import score_angles, get_priority_feedback
from feedback_engine import generate_coaching_report, format_report_text
from PIL import Image

image = Image.open("test_cricket.jpg")
annotated, coords, success = analyze_pose(image)

if success:
    angles = calculate_all_batting_angles(coords)
    scores, feedback, overall = score_angles(angles)
    tips = get_priority_feedback(feedback, scores)
    report = generate_coaching_report(tips, overall, "Shri")
    print(format_report_text(report))
else:
    print("No pose detected")