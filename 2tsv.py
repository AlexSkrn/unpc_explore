"""Transform UN parallel txt corpus to multiple tsv files."""
import os


DATA = 'data'
TSV = 'tsv'
EN = 'en_clean.txt'
RU = 'ru_clean.txt'
IDS = 'ids_clean.txt'
# EN = 'en_test_5000.txt'
# RU = 'ru_test_5000.txt'
# IDS = 'ids_test_5000.txt'


def gen_filename(idx):
    """Generate filenames from UN corpus per-line index.

    sample input: '2014/unw/2015/l_2 en:58:1 ru:58:1'
    sample output:'2014_unw_2015_l_2'
    """
    return '_'.join(idx.split()[0].split('/'))


en_f = open(os.path.join(DATA, EN), 'r', encoding='utf-8')
ru_f = open(os.path.join(DATA, RU), 'r', encoding='utf-8')
idx_f = open(os.path.join(DATA, IDS), 'r', encoding='utf-8')

# put ['en \t ru',] into a dict, where keys are filenames
contents_dict = dict()
counter = 0
try:
    for en, ru, idx in zip(en_f, ru_f, idx_f):
        counter += 1
        filename = gen_filename(idx.strip())
        try:
            contents_dict[filename].append(f'{en.strip()}\t{ru.strip()}')
        except KeyError:
            contents_dict[filename] = []
            contents_dict[filename].append(f'{en.strip()}\t{ru.strip()}')
except Exception as e:
    print(e)
finally:
    en_f.close()
    ru_f.close()
    idx_f.close()

ttl_lines = 0
for k, v in contents_dict.items():
    lines_num = len(v)
    # comment out next line in final version
    # print(f'doc_idx: {k}; lines: {lines_num}')
    ttl_lines += lines_num
    with open(os.path.join(DATA, TSV, k+'.tsv'), 'w', encoding='utf-8') as to_f:
        for line in v:
            to_f.write(line)
            to_f.write('\n')

print(f'Dictionary length is {len(contents_dict)}')
print(f'Total lines read from original files: {counter}')
print(f'Total lines written to all files: {ttl_lines}')
