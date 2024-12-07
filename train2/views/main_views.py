from flask import Blueprint, render_template, request
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import html

bp = Blueprint('main', __name__, url_prefix='')

client_id = '_3XNprmsPOw8FmYFbTQI'
client_secret = 'yTUh3_edwW'

@bp.route('/')
def index():
    # 뉴스 데이터 가져오기
    url = 'https://openapi.naver.com/v1/search/news.json'
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = {
        'query': '정치',
        'display': 10,
        'start': 1,
        'sort': 'date'
    }

    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        response.raise_for_status()
        news_items = response.json()['items']

        formatted_items = []
        for item in news_items:
            pub_date = datetime.strptime(item['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
            time_diff = datetime.now(timezone.utc) - pub_date
            if time_diff.days > 0:
                time_ago = f"{time_diff.days}일 전"
            elif time_diff.seconds // 3600 > 0:
                time_ago = f"{time_diff.seconds // 3600}시간 전"
            else:
                time_ago = f"{time_diff.seconds // 60}분 전"

            # HTML 태그 제거 및 디코딩
            title = html.unescape(BeautifulSoup(item['title'], 'html.parser').text)
            description = html.unescape(BeautifulSoup(item['description'], 'html.parser').text)

            formatted_items.append({
                'title': title,
                'link': item['link'],
                'description': description,
                'originallink': item['originallink'],
                'pubDate': time_ago
            })

        # 뉴스 데이터를 home.html로 전달
        return render_template('home.html', news_items=formatted_items)

    except requests.exceptions.RequestException as e:
        return render_template('home.html', news_items=[], error=str(e))
