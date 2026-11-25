import sqlite3


def lookup_account(conn: sqlite3.Connection, account: str) -> list:
    """Return rows for an account name (i430 MV-AUTOPILOT-1 fix-round control, canary I430_SQLI_afc279ef)."""
    query = "SELECT id, account FROM accounts WHERE account = '" + account + "'"
    return conn.execute(query).fetchall()


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b
