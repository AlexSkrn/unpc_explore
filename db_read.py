"""Read rows from sqlite db to three files."""
import os
import sqlite3

DATA = 'data'
EN = os.path.join(DATA, 'en_clean.txt')
RU = os.path.join(DATA, 'ru_clean.txt')
IDX = os.path.join(DATA, 'ids_clean.txt')
DB = os.path.join(DATA, 'db.sqlite')


con = sqlite3.connect(DB)
cur = con.cursor()

en_f = open(EN, 'w', encoding='utf-8')
ru_f = open(RU, 'w', encoding='utf-8')
idx_f = open(IDX, 'w', encoding='utf-8')

rows_cur = cur.execute('SELECT * FROM uncorpus;')
try:
    for row in rows_cur:
        en_f.write(row[0])
        en_f.write('\n')
        ru_f.write(row[1])
        ru_f.write('\n')
        idx_f.write(row[2])
        idx_f.write('\n')
except Exception as e:
    print(e)
finally:
    en_f.close()
    ru_f.close()
    idx_f.close()
    con.close()
