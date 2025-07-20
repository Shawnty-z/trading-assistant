import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
c = conn.cursor()

# Table for storing user trades/preferences
c.execute("""
CREATE TABLE IF NOT EXISTS user_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    type TEXT,            -- e.g. "trade", "preference"
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def add_memory(user_id: str, mem_type: str, content: str):
    c.execute(
        "INSERT INTO user_memory (user_id,type,content) VALUES (?,?,?)",
        (user_id, mem_type, content)
    )
    conn.commit()

def get_trading_memory(user_id: str, limit: int = 10):
    c.execute(
        "SELECT content FROM user_memory WHERE user_id = ? AND type='trade' ORDER BY created_at DESC LIMIT ?",
        (user_id, limit)
    )
    return [row[0] for row in c.fetchall()]
