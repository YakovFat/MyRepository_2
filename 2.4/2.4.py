import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("files/newsafr.xml", parser=parser)
descriptions = []
news = []

root = tree.getroot()

xml_items = root.findall("channel/item")

for item in xml_items:
    description = item.find("description")
    descriptions.append(description.text.split())
for i in descriptions:
    for n in i:
        if len(n) >= 6:
            news.append(n.lower())
news_d = {}.fromkeys(news, 0)
for a in news:
    news_d[a] += 1

top_list = sorted(news_d.items(), key=lambda item: item[1], reverse=True)
print("Топ 10 самых популярных слов:")

for number, i in enumerate(top_list[0:10]):
    print(number + 1, i[0], '(кол-во повторений={})'.format(i[1]))
