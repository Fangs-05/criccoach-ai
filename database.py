import sqlite3
from datetime import datetime
import json
import pandas as pd

DB_NAME = "criccoach.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  player_name TEXT,
                  date_time TEXT,
                  shot_type TEXT,
                  score INTEGER,
                  report TEXT)''')
    
    # --- MIGRATION: Add discipline column ---
    try:
        c.execute("ALTER TABLE sessions ADD COLUMN discipline TEXT DEFAULT 'Batting 🏏'")
    except sqlite3.OperationalError:
        pass # Column already exists
        
    conn.commit()
    conn.close()

def save_session(player_name, shot_type, score, report, discipline="Batting 🏏"):
    """Saves a new session with the app's current discipline."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Convert report to JSON string if it's a dictionary
    if isinstance(report, dict):
        report = json.dumps(report)
        
    c.execute('''INSERT INTO sessions (player_name, date_time, shot_type, score, report, discipline) 
                 VALUES (?, ?, ?, ?, ?, ?)''', 
              (player_name, date_time, shot_type, score, report, discipline))
    conn.commit()
    conn.close()

def get_all_sessions():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM sessions", conn)
    conn.close()
    return df

def clear_sessions():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM sessions')
    conn.commit()
    conn.close()

def delete_player(player_name):
    """Deletes all session records for a specific player."""
    conn = sqlite3.connect(DB_NAME) 
    c = conn.cursor()
    c.execute("DELETE FROM sessions WHERE player_name = ?", (player_name,))
    conn.commit()
    conn.close()