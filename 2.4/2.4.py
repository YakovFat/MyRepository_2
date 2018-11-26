import json
news_list = []
news = []
with open('files/newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)
    for items in json_data["rss"]["channel"]["items"]:
        news_list.append(items['description'].split())
    for i in news_list:
        for n in i:
            if len(n) >= 6:
                news.append(n)
    news_d = {}.fromkeys(news, 0)
    for a in news:
        news_d[a] += 1
    top_list = []
    top_list.append(sorted(news_d, key=max, reverse=True))
    print("Топ 10 самых популярных слов:")
    for number, i in enumerate(top_list[0][0:10]):
        print(number+1, i)


