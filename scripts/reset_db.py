import sqlite3

conn = sqlite3.connect("leads.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS articles;")

cursor.execute("""
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    summary TEXT,
    source TEXT,
    published_at TEXT,
    tags TEXT,
    is_seen INTEGER DEFAULT 0,
    notes TEXT DEFAULT '',
    relevance_score INTEGER DEFAULT 0
);
""")

conn.commit()
conn.close()

print("✅ articles table dropped and recreated.")
