"""Read rows from sqlite db to create a csv file with simple stats.

Desired columns:
    en_word_count INT
    en_char_count INT
    ru_word_count INT
    ru_char_count INT
    year INT
    body STR
"""
import os
import sqlite3

DATA = 'data'
UNSIMPLE = os.path.join(DATA, 'unsimple.csv')  # to be created
DB = os.path.join(DATA, 'db.sqlite')  # existing db


con = sqlite3.connect(DB)
cur = con.cursor()

f = open(UNSIMPLE, 'w', encoding='utf-8')

rows_cur = cur.execute('SELECT * FROM uncorpus;')
try:
    f.write('en_words,en_chars,ru_words,ru_chars,year,body\n')
    for row in rows_cur:
        en_words, en_chars = len(row[0].split()), len(row[0])
        ru_words, ru_chars = len(row[1].split()), len(row[1])
        year, body = row[2].split('/')[0], row[2].split('/')[1].split()[0]
        f.write(f'{en_words},{en_chars},{ru_words},{ru_chars},{year},{body}')
        f.write('\n')
except Exception as e:
    print(e)
finally:
    f.close()
    con.close()
