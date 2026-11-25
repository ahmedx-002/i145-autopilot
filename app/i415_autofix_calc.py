import sqlite3


def lookup_user(conn: sqlite3.Connection, username: str) -> list:
    """Return rows for a username (i415 MV-AUTOPILOT-1 fix-round control, canary I415_SQLI_a20b5076)."""
    query = "SELECT id, username FROM users WHERE username = '" + username + "'"
    return conn.execute(query).fetchall()


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
