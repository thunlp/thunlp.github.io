metafile = open('meta.csv')
data = []
for line in metafile:
    attr = line.rstrip().split('\t')
    assert(len(attr) == 9)
    name, paper, code, inst, date, p1, p2, p3, p4 = attr
    score = float(p1) + float(p2) + float(p3) + float(p4)
    item = {'meta': [name, paper, code, inst, date, p1, p2, p3, p4], 'score': score}
    data.append(item)
data.sort(key=lambda x: x['score'], reverse=True)
from bs4 import BeautifulSoup

rank = 0
s = ''
for item in data:
    name, paper, code, inst, date, p1, p2, p3, p4 = item['meta']
    rank += 1
    s += '<tr>'
    s += '<th scope="row">'
    s += '<p>{}</p>'.format(rank)
    s += '</th>'
    s += '<td style="word-break:break-word;">'
    s += name
    if len(paper) > 0:
        s += '<a href="{}">[paper]</a>'.format(paper)
    if len(code) > 0:
        s += '<a href="{}">[code]</a>'.format(code)
    s += '<br>'
    s += '<strong>{}</strong>'.format(inst)
    s += '<br>'
    s += date
    s += '</td>'
    s += '<td>{}</td>'.format(p1)
    s += '<td>{}</td>'.format(p2)
    s += '<td>{}</td>'.format(p3)
    s += '<td>{}</td>'.format(p4)
    s += '</tr>'
    #print(BeautifulSoup(s).prettify())
    #htmlfile.write(s)

print(s)
