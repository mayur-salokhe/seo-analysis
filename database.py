import sqlite3
import datetime

DB_NAME = "seo_rankings.db"

def create_tables():
    """
    Creates necessary tables for tracking keyword rankings and search quota.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Table for storing keyword rankings
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rankings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL,
            rank INTEGER NOT NULL,
            previous_rank INTEGER,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            domain TEXT NOT NULL,
            snippet INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table for tracking API search quota
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_quota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            remaining_searches INTEGER DEFAULT 100,
            last_updated_month INTEGER,
            last_updated_year INTEGER
        )
    """)

    # Initialize search quota if not exists
    cursor.execute("SELECT COUNT(*) FROM search_quota")
    if cursor.fetchone()[0] == 0:
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        cursor.execute("INSERT INTO search_quota (remaining_searches, last_updated_month, last_updated_year) VALUES (100, ?, ?)", 
                       (current_month, current_year))

    conn.commit()
    conn.close()

def reset_search_quota_if_needed():
    """
    Resets the monthly search quota if a new month has started.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT last_updated_month, last_updated_year FROM search_quota WHERE id=1")
    result = cursor.fetchone()

    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    if result:
        last_month, last_year = result
        if last_month != current_month or last_year != current_year:
            cursor.execute("UPDATE search_quota SET remaining_searches = 100, last_updated_month = ?, last_updated_year = ? WHERE id=1", 
                           (current_month, current_year))

    conn.commit()
    conn.close()

def check_search_quota():
    """
    Returns the remaining searches for the current month.
    """
    reset_search_quota_if_needed()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT remaining_searches FROM search_quota WHERE id=1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def update_search_quota():
    """
    Decreases the remaining search quota by 1 after each API call.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE search_quota SET remaining_searches = remaining_searches - 1 WHERE id=1")
    conn.commit()
    conn.close()

def insert_ranking(keyword, rank, title, url, snippet):
    """
    Inserts a new keyword ranking into the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    domain = url.split("/")[2]  # Extract domain from URL

    # Get previous rank
    cursor.execute("SELECT rank FROM rankings WHERE keyword=? ORDER BY date DESC LIMIT 1", (keyword,))
    prev_rank = cursor.fetchone()
    previous_rank = prev_rank[0] if prev_rank else None

    cursor.execute("""
        INSERT INTO rankings (keyword, rank, previous_rank, title, url, domain, snippet) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (keyword, rank, previous_rank, title, url, domain, snippet))

    conn.commit()
    conn.close()

def fetch_rankings():
    """
    Fetches all keyword rankings from the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rankings ORDER BY date DESC")
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_top_competitors():
    """
    Fetches competitor rankings (counts how many times each domain appears).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT domain, COUNT(*) AS count FROM rankings GROUP BY domain ORDER BY count DESC")
    data = cursor.fetchall()
    conn.close()
    return data

# Initialize database tables
create_tables()
