EN_SRC = 'test_en.txt'  # head -200 UNv1.0.en-ru.en > test_en.txt
RU_SRC = 'test_ru.txt'  # head -200 UNv1.0.en-ru.ru > test_ru.txt
DUPES = 'dupes.txt'
EQUALS = 'equals.txt'

en_f = open(EN_SRC, 'r', encoding='utf-8')
ru_f = open(RU_SRC, 'r', encoding='utf-8')
duplicates_f = open(DUPES, 'w', encoding='utf-8')
equals_f = open(EQUALS, 'w', encoding='utf-8')

bitext_list = []
try:
    count = 0
    for en, ru in zip(en_f, ru_f):
        count += 1
        en = en.strip()
        ru = ru.strip()
        if en.casefold() == ru.casefold():
            equals_f.write(f'{en}\t{ru})')
        if (en, ru) in bitext_list:
            duplicates_f.write(en)
            duplicates_f.write('\t')
            duplicates_f.write(ru)
            duplicates_f.write('\n')
        bitext_list.append((en, ru))
    print(count)
except Exception as e:
    print(e)
    pass

en_f.close()
ru_f.close()
duplicates_f.close()
equals_f.close()
