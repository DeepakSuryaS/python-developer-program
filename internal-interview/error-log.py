import re

tp = open('../internal-interview/parsed_lines.log', 'a+')
fp = open('../internal-interview/sample-log-file.log', 'r', encoding='utf-8')
rows = fp.readlines()

j = []
for i in rows:
    if('error' in i):
        # print(i)
        j.append(i)
        # print(j)
for x in j:
    print(x)
    tp.write(x)
