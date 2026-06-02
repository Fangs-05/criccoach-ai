from pose_analyzer import analyze_pose, get_all_key_landmarks
from PIL import Image
import matplotlib.pyplot as plt
import urllib.request
import os

# Using local image

# Load and analyze
image = Image.open("test_cricket.jpg")
annotated, landmarks, success = analyze_pose(image)

print("Detection success:", success)

if success:
    coords = get_all_key_landmarks(landmarks)
    print("\nKey landmarks detected:")
    for name, coord in coords.items():
        if coord:
            print(f"  {name}: ({coord[0]:.3f}, {coord[1]:.3f})")

    # Show result
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Pose Detected")
    plt.imshow(annotated)
    plt.axis('off')

    plt.tight_layout()
    plt.savefig("pose_test_result.png")
    plt.show()
    print("\nResult saved as pose_test_result.png")
else:
    print("No pose detected in test image")
    print("Try with a clearer cricket photo")