import json

news_list = []
news = []
top_list = []
with open('files/newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)
    for items in json_data["rss"]["channel"]["items"]:
        news_list.append(items['description'].split())
    for i in news_list:
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

