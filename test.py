import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image

print("OpenCV:", cv2.__version__)
print("MediaPipe:", mp.__version__)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Pillow:", Image.__version__)
print("")
print("All libraries imported successfully!")
print("Ready to build CricCoach AI")