import streamlit as st

st.markdown("""
<div class="hero">
    <div class="hero-tag">Documentation</div>
    <h1>How<br>CricCoach <span>Works</span></h1>
    <p>The technology and methodology behind your AI coach.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="sec-title">The Process</div>', unsafe_allow_html=True)
st.markdown("""
<div class="step-grid">
    <div class="step">
        <div class="step-num">1</div>
        <h4>Upload Photo</h4>
        <p>Upload a clear full-body batting stance photo or use the live camera. Head-to-feet visibility is required.</p>
    </div>
    <div class="step">
        <div class="step-num">2</div>
        <h4>Pose Detection</h4>
        <p>Google MediaPipe detects 33 body landmark coordinates, mapping your complete body skeleton.</p>
    </div>
    <div class="step">
        <div class="step-num">3</div>
        <h4>Angle Calculation</h4>
        <p>Seven critical batting angles are extracted based on handedness and specific shot requirements.</p>
    </div>
    <div class="step">
        <div class="step-num">4</div>
        <h4>Benchmark Scoring</h4>
        <p>Each angle is compared against professional batting benchmarks and scored out of 10.</p>
    </div>
    <div class="step">
        <div class="step-num">5</div>
        <h4>Coaching Feedback</h4>
        <p>An NLP feedback engine generates specific, actionable coaching tips and practice drills per weakness.</p>
    </div>
    <div class="step">
        <div class="step-num">6</div>
        <h4>Progress Tracking</h4>
        <p>Every session is saved in a local SQLite database, allowing you to track improvement over time.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="sec-title">Technology Stack</div>', unsafe_allow_html=True)
st.markdown("""
<div class="tech-row">
    <div class="tech-chip"><span>+</span>MediaPipe — Pose Detection</div>
    <div class="tech-chip"><span>+</span>OpenCV — Image Processing</div>
    <div class="tech-chip"><span>+</span>Scikit-learn — ML Scoring</div>
    <div class="tech-chip"><span>+</span>SQLite3 — Database</div>
    <div class="tech-chip"><span>+</span>Streamlit — Web Interface</div>
    <div class="tech-chip"><span>+</span>NumPy / Pandas — Data Layer</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="sec-title">About This Project</div>', unsafe_allow_html=True)
st.markdown("""
<div class="coach-banner">
    <strong>CricCoach AI</strong> is an internship project built by <strong>Shri Amarnath S</strong>,
    MCA student at St. Joseph's College (Autonomous), Tiruchirappalli.<br><br>
    Developed at <strong>Astonish Infotech, Tiruchirappalli</strong> as part of a full stack and
    machine learning internship programme — May 2026.<br><br>
    The system demonstrates practical integration of computer vision, machine learning,
    and natural language processing to solve a real-world sports coaching problem.
</div>
""", unsafe_allow_html=True)