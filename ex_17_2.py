from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Создание вызова API и сохранение ответа..
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Построение словаря для каждой статьи.
    try:
        submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
        }
    except:
        print(f"В статье с id {submission_id} нет комментариев")

    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

comment_count_list = []
comment_title_list= []
hover_texts_list = []

for submission_dict in submission_dicts:
    comment_title_list.append(submission_dict['title'])
    hover_texts_list.append(submission_dict['hn_link'])
    comment_count_list.append(submission_dict['comments'])

# Построение визуализации.
data = [{
    'type': 'bar',
    'x': comment_title_list,
    'y': comment_count_list,
    'hovertext': hover_texts_list,
    'marker': {
        'color': 'aquamarine',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.5,
}]

my_layout = {
    'title': 'Most-comment Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'count_comment',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='most_comment.html')

