CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    summary TEXT,
    source TEXT,
    published_at TEXT,
    tags TEXT,
    is_seen INTEGER DEFAULT 0,
    notes TEXT DEFAULT ''
);


