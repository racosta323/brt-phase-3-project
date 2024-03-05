import sqlite3

CONN = sqlite3.connect('lib/travels.db')
CURSOR = CONN.cursor()