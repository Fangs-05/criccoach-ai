# CricCoach: AI-Powered Cricket Biomechanics Analyzer 🏏⚾

CricCoach is a full-stack, dual-engine computer vision application designed to analyze and score cricket batting and bowling mechanics. Built as an end-to-end machine learning capstone project, it uses local 2D pose estimation to provide professional-grade biomechanical feedback without the need for expensive motion-capture equipment.

## Live Demo
*(Insert your Streamlit Community Cloud link here once deployed)*

## Core Architecture & Features

### 1. Dual-Engine Analytics
The app dynamically routes state management and mathematical logic based on a Master Discipline Toggle, allowing it to process entirely different skeletal geometries without crashing:
* **Batting Engine:** Evaluates stance, footwork, and bat path across 11 different shot profiles (e.g., Cover Drive, Slog Sweep, Helicopter Shot).
* **Bowling Engine:** Maps release points, braced front legs, and trunk lean for pace variations (Stock, Yorker, Bouncer).

### 2. Solving 2D Spatial Limitations (The Spin Engine)
Standard 2D smartphone cameras cannot track Z-axis depth, making it difficult to measure the hip-to-shoulder rotation required for spin bowling. CricCoach circumvents this physical limitation by calculating a **visible shoulder-width ratio** against torso length, creating an artificial rotational index. This allows the AI to accurately grade side-on Leg-Spinners vs. front-on Off-Spinners from a flat, umpire-view camera angle.

### 3. Unorthodox Action Support
Includes custom data dictionaries for non-traditional mechanics, such as the horizontal arm paths and extreme lateral body bends of "Sling Action" fast bowlers.

### 4. Role-Based Dashboards & Data Management
* **Personal Progress:** A micro-view for individual players to track their mechanics over time.
* **Academy Dashboard:** A macro-view for coaches to filter top performers by discipline.
* **Backend:** Custom SQLite database with automated schema migrations to tag and separate batting and bowling sessions cleanly.

## 🛠️ Tech Stack
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Computer Vision:** OpenCV (Headless), Google MediaPipe Pose
* **Data Processing & Math:** Pandas, NumPy
* **Database:** SQLite3
* **Reporting:** FPDF (Dynamic PDF Generation)

##  Scope & Hardware Limitations
To maintain accuracy on consumer hardware (mobile phones/laptops), this V1 release focuses strictly on **macro-mechanics**:
*  Posture, arm elevation, knee bracing, and trunk momentum.
*  **Out of Scope:** Seam presentation, wrist micro-movements, and finger placement. MediaPipe tracks 33 macro body landmarks; sub-centimeter wrist physics require high-speed cameras and custom-trained YOLO models, which are slated for future iterations.

##  Local Setup (For Developers)

1. Clone the repository:
   bash
   git clone [https://github.com/yourusername/CricCoach-AI.git](https://github.com/yourusername/CricCoach-AI.git)
   cd CricCoach-AI

2.Create and activate a virtual environment:
  bash
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  
3.Install dependencies:
  bash
  pip install -r requirements.txt

4.Run the application:
  bash
  streamlit run app.py
