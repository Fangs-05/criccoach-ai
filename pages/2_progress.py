import streamlit as st
import plotly.express as px
from database import get_all_sessions

st.markdown("""
<div class="hero">
    <div class="hero-tag">Performance Tracking</div>
    <h1>Personal <span>Progress</span></h1>
    <p>Track your form and efficiency scores over time.</p>
</div>
""", unsafe_allow_html=True)

# 1. Pull the master database
df = get_all_sessions()

# 2. FILTER: Only show data for the currently selected discipline!
if not df.empty and 'discipline' in df.columns:
    df = df[df['discipline'] == st.session_state.app_mode]

if df.empty:
    st.markdown("""
    <div class="prog-empty">
        <div style="font-size:2.5rem">—</div>
        <h3>No session data found</h3>
        <p>Run a pose analysis to generate your first progress report.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # 2. Extract a list of unique player names for our dropdown
    unique_players = df['player_name'].unique().tolist()
    
    # 3. Create the dropdown menu
    selected_player = st.selectbox("Select Player Profile:", options=unique_players)
    
    # 4. THE FILTER: Tell Pandas to drop everyone except the selected player
    player_df = df[df['player_name'] == selected_player]
    
    # Check if the player has enough sessions to draw a chart
    if len(player_df) < 2:
        st.info(f"{selected_player} only has one session recorded. Complete another analysis to see the progress chart!")
        # FIX: Changed to 'date_time'
        st.dataframe(player_df[['date_time', 'shot_type', 'score']], use_container_width=True, hide_index=True)
    else:
        # 5. Draw the chart using ONLY the filtered data
        st.markdown('<div class="sec-title">Score History</div>', unsafe_allow_html=True)
        
        # Sort by date so the line graph flows left to right
        player_df = player_df.sort_values(by='id') 
        
        fig = px.line(
            player_df, 
            # FIX: Changed to 'date_time'
            x='date_time', 
            y='score', 
            markers=True,
            color_discrete_sequence=['#F26522'],
            hover_data=['shot_type']
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', 
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, title="Session Date"),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Form Efficiency Score", range=[0, 100]),
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed Session History Table
        st.markdown('<div class="sec-title">Session History</div>', unsafe_allow_html=True)
        # FIX: Changed to 'date_time'
        display_df = player_df[['date_time', 'shot_type', 'score']].rename(columns={
            'date_time': 'Date', 'shot_type': 'Shot Analyzed', 'score': 'Score'
        })
        st.dataframe(display_df, use_container_width=True, hide_index=True)