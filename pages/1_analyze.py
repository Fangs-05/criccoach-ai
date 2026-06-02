import streamlit as st
import numpy as np
import io
import time
from PIL import Image
from datetime import datetime
import tempfile
import cv2
import requests
import json
from streamlit_lottie import st_lottie
from pdf_engine import generate_pdf_report
from pose_analyzer import analyze_pose
from angle_calculator import calculate_all_batting_angles, calculate_all_bowling_angles
from scorer import score_angles, get_performance_label, get_priority_feedback
from feedback_engine import generate_coaching_report, format_report_text
from database import save_session, get_all_sessions

def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# Load it instantly from your hard drive
lottie_scanning = load_lottiefile("loading.json")

st.markdown("""
<div class="hero">
    <div class="hero-tag">AI Powered · Free · Instant</div>
    <h1>AI-Powered Cricket<br>Form <span>Analyzer</span></h1>
    <p>Upload your photo or use the camera for instant, professional coaching feedback.</p>
</div>
""", unsafe_allow_html=True)

# Configurations
col_config1, col_config2, col_config3 = st.columns(3)
with col_config1:
    player_name = st.text_input("Player Name", value="Player")
with col_config2:
    if st.session_state.app_mode == "Batting 🏏":
        handedness = st.radio("Batting Hand", ["Right", "Left"], horizontal=True)
    else:
        st.write("") # Leaves the column blank to keep the layout perfectly aligned
with col_config3:
    app_mode = st.session_state.app_mode
    
    if app_mode == "Batting 🏏":
        categories = {
            "Fundamentals": ["Stance", "Forward Defense"],
            "Front Foot": ["Cover Drive", "Straight Drive", "On Drive"],
            "Back Foot": ["Pull Shot", "Square Cut", "Hook Shot"],
            "Spin/T20": ["Standard Sweep", "Slog Sweep", "Helicopter Shot"]
        }
        
        flat_list = []
        for category, actions in categories.items():
            flat_list.append(f"── {category.upper()} ──")
            flat_list.extend(actions)
            
        raw_selection = st.selectbox("Select Batting Profile", flat_list)
        if raw_selection.startswith("──"):
            st.warning("☝️ Please select a specific action.")
            st.stop()
        else:
            shot_type = raw_selection
            
    else:
       
        # BOWLING MODE UI UPDATE
        categories = {
            "Pace Variations": ["Pace - Stock Delivery", "Pace - Yorker", "Pace - Bouncer"],
            "Spin Bowling": ["Spin - Off-Spin", "Spin - Leg-Spin"],
            "Unorthodox": ["Pace - Sling Action"]
        }
        
        flat_list = []
        for category, actions in categories.items():
            flat_list.append(f"── {category.upper()} ──")
            flat_list.extend(actions)
            
        raw_selection = st.selectbox("Select Bowling Profile", flat_list)
        if raw_selection.startswith("──"):
            st.warning("☝️ Please select a specific delivery type.")
            st.stop()
        else:
            shot_type = raw_selection
        
        bowler_arm = st.radio("Bowler Handedness:", ["Right-Arm", "Left-Arm"], horizontal=True)
        st.session_state.bowler_arm = bowler_arm

col_upload, col_pose = st.columns(2, gap="large")

with col_upload:
    st.markdown('<div class="sec-title">Media Source</div>', unsafe_allow_html=True)
    input_method = st.radio("Choose Input:", ["Upload Photo", "Upload Video", "Live Camera"], horizontal=True, label_visibility="collapsed")
    
    image_input = None
    
    if input_method == "Upload Photo":
        uploaded = st.file_uploader("Batting stance photo (JPG/PNG)", type=['jpg','jpeg','png'])
        if uploaded:
            image_input = Image.open(uploaded).convert('RGB')
            st.image(image_input, use_container_width=True)
            
    elif input_method == "Upload Video":
        uploaded_video = st.file_uploader("Upload Batting Video (MP4/MOV)", type=['mp4', 'mov'])
        if uploaded_video:
            with st.spinner("Extracting video frames..."):
                # 1. Reset file pointer so Streamlit reruns (like using the slider) don't read empty bytes
                uploaded_video.seek(0)
                
                tfile = tempfile.NamedTemporaryFile(delete=False)
                tfile.write(uploaded_video.read())
                
                # 2. Force write to disk and close so OpenCV can safely open it without OS lock errors
                tfile.flush()
                tfile.close() 
                
                cap = cv2.VideoCapture(tfile.name)
                frames = []
                
                count = 0
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    if count % 3 == 0: 
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        # 3. Convert to a PIL Image so it perfectly matches the Photo Upload data format
                        frames.append(Image.fromarray(frame))
                    count += 1
                cap.release()
            
            if frames:
                st.success(f"Extracted {len(frames)} playable frames.")
                frame_idx = st.slider(
                    "Scrub to the exact point of impact:", 
                    min_value=0, 
                    max_value=len(frames)-1, 
                    value=len(frames)//2
                )
                image_input = frames[frame_idx]
                st.image(image_input, use_container_width=True, caption=f"Selected Frame: {frame_idx}")

    elif input_method == "Live Camera":
        camera_snap = st.camera_input("Take a photo of your stance")
        if camera_snap:
            image_input = Image.open(camera_snap).convert('RGB')

with col_pose:
    st.markdown('<div class="sec-title">Pose Detection</div>', unsafe_allow_html=True)
    if image_input is not None:
        
        st.info("👆 Media loaded! Configure your settings above, then click Analyze.")
        
        # 1. THE GATEKEEPER BUTTON
        if st.button("⚡ Run AI Analysis", type="primary", use_container_width=True):
            loading_placeholder = st.empty()
            
            with loading_placeholder.container():
                if lottie_scanning:
                    st_lottie(lottie_scanning, height=250, key="loading")
                else:
                    st.spinner("Running pose detection...")
                    
            time.sleep(0.5) 
            
            # Force the image into a strict, C-contiguous 8-bit matrix for MediaPipe's C++ backend
            image_matrix = np.ascontiguousarray(np.array(image_input.convert('RGB'), dtype=np.uint8))
            
            # Run the heavy machine learning task on the safe matrix
            annotated, coords, success = analyze_pose(image_matrix)
            
            loading_placeholder.empty()
            
            if success:
                st.success("Pose detected successfully.")
                
                # 2. RUN THE MATH
                if st.session_state.app_mode == "Batting 🏏":
                    angles = calculate_all_batting_angles(coords, handedness)
                else:
                    angles = calculate_all_bowling_angles(coords, st.session_state.bowler_arm)
                    
                scores, feedback, overall = score_angles(angles, shot_type)
                label, color = get_performance_label(overall)
                tips   = get_priority_feedback(feedback, scores)
                report = generate_coaching_report(tips, overall, player_name)

                # 3. SAVE TO DATABASE (Only happens ONCE when button is clicked!)
                save_session(player_name, shot_type, overall, report, st.session_state.app_mode)
                
                # 4. SAVE TO SESSION STATE (Protects data from Streamlit reruns)
                st.session_state.analysis_results = {
                    'annotated': annotated,
                    'scores': scores,
                    'overall': overall,
                    'label': label,
                    'color': color,
                    'report': report,
                    'player_name': player_name,
                    'shot_type': shot_type
                }
            else:
                st.error("Could not detect a pose. Please ensure full body is visible.")
                st.session_state.analysis_results = None
    else:
        st.markdown("""
        <div class="upload-placeholder">
            <div class="up-icon">+</div>
            <h4>No media provided</h4>
            <p>Upload a video or photo to begin analysis</p>
        </div>
        """, unsafe_allow_html=True)
      
# 5. RENDER RESULTS FROM MEMORY
if 'analysis_results' in st.session_state and st.session_state.analysis_results is not None:
    # Grab the saved data
    res = st.session_state.analysis_results
    
    st.markdown('<div class="sec-title">Analysis Complete</div>', unsafe_allow_html=True)
    st.image(res['annotated'], use_container_width=True)
    
    total_sessions = len(get_all_sessions())
    good_c = sum(1 for s in res['scores'].values() if s['status'] == 'good')
    bad_c  = sum(1 for s in res['scores'].values() if s['status'] == 'needs_work')

    st.markdown('<div class="sec-title">Results</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="kpi-wrap">
        <div class="kpi">
            <div class="kpi-value" style="color:{res['color']}">{res['overall']}</div>
            <div class="kpi-label">Overall / 100</div>
            <div style="font-size:0.82rem;font-weight:600;color:{res['color']};margin-top:4px">{res['label']}</div>
        </div>
        <div class="kpi">
            <div class="kpi-value" style="color:#15803d">{good_c}</div>
            <div class="kpi-label">Good Areas</div>
        </div>
        <div class="kpi">
            <div class="kpi-value" style="color:#b91c1c">{bad_c}</div>
            <div class="kpi-label">To Improve</div>
        </div>
        <div class="kpi">
            <div class="kpi-value" style="color:#1d4ed8">{total_sessions}</div>
            <div class="kpi-label">Total Sessions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-title">Angle Breakdown</div>', unsafe_allow_html=True)
    a_col1, a_col2 = st.columns(2, gap="large")
    items = list(res['scores'].items())
    for i, (name, d) in enumerate(items):
        if d['status'] == 'obscured':
            bcolor = "#f59e0b"
            chip = '<span class="chip-bad" style="background:#fef3c7;color:#d97706">Obscured</span>'
            pct = 0
            val_display = "N/A"
        else:
            pct = int(d['score'] / 10 * 100)
            bcolor = "#22c55e" if d['status'] == 'good' else "#ef4444"
            chip = f'<span class="chip-good">Good</span>' if d['status'] == 'good' else f'<span class="chip-bad">Fix</span>'
            val_display = f"{d['value']}°"
            
        html = f"""
        <div class="angle-item">
            <div class="angle-top">
                <span class="angle-name">{d['description']}</span>
                <span>{chip} &nbsp;<span class="angle-score" style="color:{bcolor}">{d['score']}/10</span></span>
            </div>
            <div class="angle-meta">Measured: {val_display} &nbsp;&middot;&nbsp; Ideal: {d['ideal_min']}° &ndash; {d['ideal_max']}°</div>
            <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{bcolor}"></div></div>
        </div>"""
        with (a_col1 if i % 2 == 0 else a_col2):
            st.markdown(html, unsafe_allow_html=True)

    st.markdown('<div class="sec-title">Coaching Feedback</div>', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns(2, gap="large")

    with f_col1:
        st.markdown("**Corrections Required**")
        if res['report']['corrections']:
            for c in res['report']['corrections']:
                st.markdown(f"""
                <div class="fb-fix">
                    <div class="fb-title">Priority {c['priority']} &mdash; {c['area']}</div>
                    <div class="fb-meta">Measured {c['your_angle']}° &nbsp;&middot;&nbsp; Ideal {c['ideal']}</div>
                    <div class="fb-body">{c['problem']}</div>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="fb-good">
                <div class="fb-title">No corrections required</div>
                <div class="fb-body">Your form is excellent across all visible areas.</div>
            </div>""", unsafe_allow_html=True)

    with f_col2:
        st.markdown("**Strengths & Warnings**")
        for s in res['report']['strengths']:
            st.markdown(f"""
            <div class="fb-good">
                <div class="fb-title">{s['area']}</div>
                <div class="fb-body">{s['message']}</div>
            </div>""", unsafe_allow_html=True)
            
        for w in res['report'].get('warnings', []):
            st.markdown(f"""
            <div class="fb-fix" style="border-left-color:#f59e0b; background:#fffbeb; border-color:#fde68a">
                <div class="fb-title" style="color:#b45309">{w['area']}</div>
                <div class="fb-body" style="color:#78350f">{w['message']}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec-title">Practice Drills</div>', unsafe_allow_html=True)
    if res['report']['corrections']:
        d_col1, d_col2 = st.columns(2, gap="large")
        for i, c in enumerate(res['report']['corrections']):
            with (d_col1 if i % 2 == 0 else d_col2):
                st.markdown(f"""
                <div class="fb-drill">
                    <div class="fb-title">{c['area']} Drill</div>
                    <div class="fb-body">{c['drill']}</div>
                </div>""", unsafe_allow_html=True)
    else:
        st.info("No specific drills required. Maintain your current practice routine.")

    st.markdown(f"""
    <div class="coach-banner">
        <strong>Coach's Assessment</strong><br><br>
        {res['report']['opening']}<br><br>
        {res['report']['closing']}<br><br>
        <strong>Today's Focus:</strong> {res['report']['session_tip']}
    </div>
    """, unsafe_allow_html=True)

    # Generate PDF bytes using the saved state
    pdf_bytes = generate_pdf_report(res['player_name'], res['overall'], res['shot_type'], res['report'])

    st.download_button(
        label="Download PDF Coaching Report",
        data=bytes(pdf_bytes),
        file_name=f"{res['player_name'].replace(' ', '_')}_CricCoach_{datetime.now().strftime('%Y%m%d')}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
