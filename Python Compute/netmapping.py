import re
import urllib.request

kegg = []
kegg_hsa = []
with open('R_e.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        kegg.append(line.split('\t')[1].strip())
        kegg_hsa.append(line.split('\t')[0].strip())

dict = {}
final_db = []
final_kegg = []
count = 0
for id in kegg:
    # count += 1
    url = 'https://www.kegg.jp/entry/' + id
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    data = resp.read().decode('utf-8')

    if re.search(r'DB\d\d\d\d\d', data):
        m = re.search(r'DB\d\d\d\d\d', data).group(0)
        dict.update({id: m})
        final_db.append(m)
        final_kegg.append(id)

    # if count > 50:
    #     break

print(dict)
print(len(dict))

with open('kegg.txt', 'w') as f:
    for kegg_id in final_kegg:
        f.write(kegg_id+'\n')

with open('db.txt', 'w') as f:
    for db_id in final_db:
        f.write(db_id+'\n')
