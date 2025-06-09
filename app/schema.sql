CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    summary TEXT,
    source TEXT,
    published_at TEXT,
    tags TEXT,
    relevannce_score INTEGER DEFAULT 0,
    is_seen INTEGER DEFAULT 0,
    notes TEXT DEFAULT ''
);


