import streamlit as st
import plotly.express as px
from database import get_all_sessions, delete_player

st.markdown("""
<div class="hero">
    <div class="hero-tag">Roster Management</div>
    <h1>Academy <span>Dashboard</span></h1>
    <p>Track performance averages and session counts across all registered players.</p>
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
        <h3>No players found</h3>
        <p>Run a pose analysis to register your first player.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Group data by player name to get academy stats
    roster_df = df.groupby('player_name').agg(
        Sessions=('id', 'count'),
        Avg_Score=('score', 'mean'),
        Best_Score=('score', 'max')
    ).reset_index()
    
    roster_df['Avg_Score'] = roster_df['Avg_Score'].round(1)
    
    # KPI Cards for the Team
    kpi_html = f"""
    <div class="kpi-wrap">
        <div class="kpi">
            <div class="kpi-value">{len(roster_df)}</div>
            <div class="kpi-label">Active Players</div>
        </div>
        <div class="kpi">
            <div class="kpi-value">{roster_df['Avg_Score'].mean():.1f}</div>
            <div class="kpi-label">Academy Average</div>
        </div>
        <div class="kpi">
            <div class="kpi-value">{len(df)}</div>
            <div class="kpi-label">Total Sessions</div>
        </div>
    </div>
    """
    st.markdown(kpi_html, unsafe_allow_html=True)

    # Leaderboard Chart
    st.markdown('<div class="sec-title">Player Leaderboard</div>', unsafe_allow_html=True)
    
    # Sort by highest average score
    roster_df = roster_df.sort_values(by='Avg_Score', ascending=False)
    
    fig = px.bar(roster_df, x='player_name', y='Avg_Score', 
                 text='Avg_Score',
                 color='Avg_Score',
                 color_continuous_scale=['#1A2634', '#F26522'],
                 labels={'player_name': 'Player Name', 'Avg_Score': 'Average Score'})
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=20, b=0)
    )
    fig.update_traces(textposition='outside', textfont=dict(color='#F8FAFC', family='Oswald'))
    
    st.plotly_chart(fig, use_container_width=True)

    # Detailed Roster Table
    st.markdown('<div class="sec-title">Detailed Roster</div>', unsafe_allow_html=True)
    display_df = roster_df.rename(columns={
        'player_name': 'Player', 'Sessions': 'Total Sessions', 'Avg_Score': 'Average Form', 'Best_Score': 'Personal Best'
    })
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # --- HEAD-TO-HEAD COMPARISON ---
    st.markdown('<div class="sec-title" style="margin-top: 40px;">Head-to-Head Comparison</div>', unsafe_allow_html=True)
    
    # Allow the user to select up to 2 players (e.g., yourself and M. Navin Kumar)
    compare_players = st.multiselect(
        "Select exactly two players to compare progress:", 
        options=roster_df['player_name'].tolist(),
        max_selections=2
    )

    if len(compare_players) == 2:
        # Filter the master database for only these two players
        comp_df = df[df['player_name'].isin(compare_players)].sort_values(by='id')
        
        fig_comp = px.line(
            comp_df, 
            x='date_time', 
            y='score', 
            color='player_name', # This automatically draws a different colored line for each player!
            markers=True,
            hover_data=['shot_type']
        )
        
        fig_comp.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', 
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, title="Session Date"),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Form Efficiency Score", range=[0, 100]),
            margin=dict(l=0, r=0, t=20, b=0),
            legend_title_text='Athlete'
        )
        
        st.plotly_chart(fig_comp, use_container_width=True)
    elif len(compare_players) == 1:
        st.info("Select one more player from the dropdown to generate the comparison chart.")

    # --- ADMIN ZONE: REMOVE PLAYERS ---
    st.markdown('<div class="sec-title" style="color:#ef4444; border-color:#ef4444">Admin Controls</div>', unsafe_allow_html=True)
    
    del_col1, del_col2 = st.columns([3, 1])
    with del_col1:
        # Create a dropdown menu containing all current player names
        player_to_delete = st.selectbox(
            "Select player to remove from academy:", 
            options=roster_df['player_name'].tolist(),
            key="delete_select"
        )
    with del_col2:
        st.write("") # Spacing to align button with dropdown
        st.write("")
        if st.button("Delete Player", type="primary", use_container_width=True):
            delete_player(player_to_delete)
            st.success(f"Deleted all records for {player_to_delete}.")
            st.rerun() # Instantly refresh the page to update the charts
# --- DATABASE ADMIN TOOLS ---
st.markdown('<div class="sec-title" style="margin-top: 50px;">🛠️ Developer Admin</div>', unsafe_allow_html=True)

with st.expander("View Raw Database & Controls"):
    # Show the raw spreadsheet so you can see exactly how things are tagged
    st.dataframe(df, use_container_width=True)
    
    # Wire up your clear_sessions function!
    if st.button("🚨 Wipe Entire Database (Hard Reset)", type="secondary"):
        from database import clear_sessions
        clear_sessions()
        st.success("Database wiped successfully. Refreshing...")
        st.rerun()