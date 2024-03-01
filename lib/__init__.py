import sqlite3

CONN = sqlite3.connect('./travels.db')
CURSOR = CONN.cursor()