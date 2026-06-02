from pose_analyzer import analyze_pose, get_all_key_landmarks
from angle_calculator import calculate_all_batting_angles, BATTING_BENCHMARKS
from PIL import Image

image = Image.open("test_cricket.jpg")
annotated, coords, success = analyze_pose(image)

if success:
    angles = calculate_all_batting_angles(coords)
    print("\n=== BATTING ANGLES DETECTED ===\n")
    for angle_name, value in angles.items():
        bench = BATTING_BENCHMARKS.get(angle_name, {})
        desc = bench.get('description', angle_name)
        ideal_min = bench.get('ideal_min', 0)
        ideal_max = bench.get('ideal_max', 180)
        status = "✅ GOOD" if ideal_min <= value <= ideal_max else "❌ NEEDS WORK"
        print(f"{desc}: {value}° {status} (ideal: {ideal_min}°-{ideal_max}°)")
else:
    print("No pose detected")