"""Write strings from three files to sqlite db to remove duplicates."""
import os
import sqlite3

DATA = 'data'
EN_SRC = 'UNv1.0.en-ru.en'  # head -100000 UNv1.0.en-ru.en > data/test_en.txt
RU_SRC = 'UNv1.0.en-ru.ru'  # head -100000 UNv1.0.en-ru.ru > data/test_ru.txt
IDX_SRC = 'UNv1.0.en-ru.ids'  # head -100000 UNv1.0.en-ru.ids > data/test_ids.txt
DB = os.path.join(DATA, 'db.sqlite')

con = sqlite3.connect(DB)
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS uncorpus')
cur.execute('''CREATE TABLE uncorpus
    (en TEXT, ru TEXT, idx TEXT, UNIQUE(en, ru)
    );
    ''')

insert_query = '''
INSERT OR IGNORE INTO uncorpus (en, ru, idx) VALUES(?,?,?);
'''

en_f = open(EN_SRC, 'r', encoding='utf-8')
ru_f = open(RU_SRC, 'r', encoding='utf-8')
idx_f = open(IDX_SRC, 'r', encoding='utf-8')

count_equals = 0
count_missing = 0
try:
    for en, ru, idx in zip(en_f, ru_f, idx_f):
        if en and ru and idx:
            if en.casefold() != ru.casefold():
                en = en.strip()
                ru = ru.strip()
                idx = idx.strip()
                cur.execute(insert_query, [en, ru, idx])
            else:
                count_equals += 1
        else:
            count_missing += 1
    con.commit()
    con.close()
except Exception as e:
    print(e)
finally:
    en_f.close()
    ru_f.close()
    idx_f.close()

print(f'Number of en==ru: {count_equals}')
print(f'Number of missing: {count_missing}')
