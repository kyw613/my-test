# init_note_db.py

import os
import mysql.connector
from datetime import datetime
import json

mydb = mysql.connector.connect(
    host=os.environ.get('MYSQL_HOST', 'mysql-svc'),
    user=os.environ.get('MYSQL_USER', 'root'),
    password=os.environ.get('MYSQL_PASSWORD', 'pass123#'),
    database=os.environ.get('MYSQL_DB', 'awswiki_db')
)

mycursor = mydb.cursor()

data = [
    {
        "reviews": [],
        "tag": "note",
        "title": "NetworkPolicy",
        "writer": "오현택",
        "content": "k8s에 들어오거나 나가는 트래픽 흐름 제어하는 규칙 정책",
        "date": "2024-05-03T17:38:50.405889Z",
        "image": "1714757926.78622.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "NetworkPolicy 세팅",
        "writer": "오현택",
        "content": "기본 세팅",
        "date": "2024-05-03T17:39:43.654295Z",
        "image": "1714757983.252861.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "NetworkPolicy 실행",
        "writer": "오현택",
        "content": "내부 pod에 접속",
        "date": "2024-05-03T17:40:58.326401Z",
        "image": "1714758057.961767.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "NetworkPolicy yaml",
        "writer": "오현택",
        "content": "yaml 파일 작성",
        "date": "2024-05-03T17:41:38.441772Z",
        "image": "1714758097.952024.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "NetworkPolicy 실행",
        "writer": "오현택",
        "content": "pod에 접속해서 networkpolicy가 정상 작동하는지 확인",
        "date": "2024-05-03T17:42:33.522940Z",
        "image": "1714758153.027812.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "netpol 정보 조회",
        "writer": "최선홍",
        "content": "yaml 파일로 작성한 netpol에 대한 정보 조회",
        "date": "2024-05-03T17:43:22.719329Z",
        "image": "1714758202.291818.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "다중 labeld을 통한 트래픽 제어",
        "writer": "최선홍",
        "content": "label을 사용하여 pod 생성",
        "date": "2024-05-03T17:44:24.694758Z",
        "image": "1714758263.237897.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "label을 사용한 netpol",
        "writer": "최선홍",
        "content": "label을 사용한 netpol yaml파일을 생성",
        "date": "2024-05-03T17:45:32.405247Z",
        "image": "1714758332.103811.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "label을 사용한 netpol 조회",
        "writer": "곽재헌",
        "content": "role=app 라벨을 가지고 있는 pod는 run=myblog 라벨을 가지고 있는 pod에 대해서 모든 port에서 접근 허용",
        "date": "2024-05-03T17:46:07.612887Z",
        "image": "1714758367.19696.jpg"
    },
    {
        "reviews": [],
        "tag": "note",
        "title": "적용한 netpol 확인",
        "writer": "정희빈",
        "content": "여러 label을 부여한 pod들을 통해 적용한 netpol을 확인",
        "date": "2024-05-03T17:47:11.046501Z",
        "image": "1714758430.338954.jpg"
    }
]

for item in data:
    sql = "INSERT INTO note_note (tag, title, writer, content, date, image) VALUES (%s, %s, %s, %s, %s, %s)"
    date_time_obj = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_date = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
    val = (item["tag"], item["title"], item["writer"], item["content"], formatted_date, item["image"])
    mycursor.execute(sql, val)

mydb.commit()

print("Note DB Insert completed successfully!")

mydb.close()
