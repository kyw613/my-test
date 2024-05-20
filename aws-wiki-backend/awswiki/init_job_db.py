# init_job_db.py

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
        "tag": "job",
        "title": "슬링",
        "writer": "오현택",
        "content": "요즘 고등학생들이 아이패드(태블릿)와 애플펜슬(스마트펜)로 수능 공부를 한다는 걸 알고 계셨나요? 과거에 PMP를 통해 인터넷강의를 시청한 것처럼, 현재 고등학생들은 태블릿과 스마트펜을 활용해 스마트하게 공부하고 있습니다. ORZO는 2020년 11월 베타 출시 이후 6개월만에 앱스토어 1위를 달성하며 빠르게 성장하고 있는 서비스입니다. 태블릿 교육 킬러앱을 만드는 슬링의 여정에 동참해보면 어떨까요?",
        "date": "2024-05-03T16:47:50.674288Z",
        "image": "1714754868.3727.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "결제 SI JAVA 개발 (2년 이상)",
        "writer": "오현택",
        "content": "결제 SI JAVA 개발 (2년 이상) 경력직 모집 희망연봉 기재",
        "date": "2024-05-03T16:55:20.536101Z",
        "image": "1714755318.45375.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "백엔드 개발 (8년 이상)",
        "writer": "오현택",
        "content": "플랫폼팀은 업무용 AI 서비스에 필요한 백엔드 기능 개발 업무를 담당하고 있습니다. 고객에게 더 나은 서비스를 제공할 수 있도록 꾸준히 개선하고 안정적으로 운영합니다.",
        "date": "2024-05-03T16:57:19.073992Z",
        "image": "1714755436.639926.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "광고 플랫폼 개발자(팀 리더급)",
        "writer": "최선홍",
        "content": "10년간의 온라인 광고 팔랫폼 개발 경험을 통해 독보적인 기술과 노하우를 보유한 AD-Tech 기업의 Top ! 11시11분(NHN AD 자회사)에서 개발자를 모집합니다.  우리는 '같이'의 가치를 중요하게 생각합니다. 능동적이며 즐겁게 '같이' 도전 할 구성원을 기다리고 있습니다. 많은 지원바랍니다.",
        "date": "2024-05-03T16:58:37.141611Z",
        "image": "1714755515.515343.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "백엔드 엔지니어 (Nest.js / 5년 이상)",
        "writer": "최선홍",
        "content": "\"백엔드 엔지니어는 이런 업무를 하시게 됩니다\"  • 자사의 Wep Application 및 Mobile App에 필요한 API 및 Back-Office 설계 및 개발 • 효율적이고 안정적인 서비스 운영을 위한 인프라 구조 및 성능 개선 • 다양한 외부 서비스와의 API 개발 연동",
        "date": "2024-05-03T17:00:03.918754Z",
        "image": "1714755602.548041.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "개발 팀장(로봇 관제 시스템 분석 및 설계)",
        "writer": "곽재헌",
        "content": "2017년에 설립된 클로봇은 꾸준하고 지속적인 성장과 사업의 확대를 진행하고 있으며 현재 글로벌 사업/기술 트렌드인 무인화, 비대면, 자동화를 위하여 로봇, 인공지능, IOT, RPA 등 첨단 기술요소를 융합한 신사업 개발을 추진하고 있습니다. 로봇, AI 등을 융합한 기술로 디지털 전환이 가속화 되는 현 시점에 앞서서 시장을 선도해 나가는 길을 함께할 인재를 찾고 있습니다.",
        "date": "2024-05-03T17:01:59.580595Z",
        "image": "1714755717.851782.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "ITS파트 매니저(10년 이상)",
        "writer": "곽재헌",
        "content": "그린카는 언제 어디서나 최소 30분부터 10분 단위로 차량을 이용할 수 있는 카셰어링 브랜드입니다. 2015년 6월 롯데그룹의 손자회사로 편입되어 사업 확장 기반을 다졌습니다. 그린카는 국내 최초로 카셰어링 서비스를 개발 · 시스템 특허를 출원하였으며 2011년 10월 자동차 공유(카셰어링) 서비스 브랜드 '그린카'를 론칭하였습니다. 2020년 2월 기준 전국 88개 도시 3,200여개 거점에서 약 9,000여대의 차량으로 카셰어링 서비스를 제공하고 있습니다. 소형 · 승합 · SUV에 이르기까지 업계 최다 60종의 차종을 보유하고 있으며, 업계 유일 친환경차 풀 라인업(전기차, 하이브리드, 플러그인 하이브리드)을 구축하여 총 1,208대의 친환경 차량을 운영하고 있습니다. 특히 2018년 9월에는 대기환경 개선과 친환경 소비 산업 육성에 기여한 내용을 인정받아 업계 최초로 국무총리 표창을 수상하였습니다.",
        "date": "2024-05-03T17:03:09.339813Z",
        "image": "1714755786.766052.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "JAVA기반 인사관리 솔루션 개발(9년 이상)",
        "writer": "정희빈",
        "content": "주요업무 • JAVA기반 인사/급여 솔루션 구축 및 운영 개발   • 자사 솔루션 고도화 개발  • 외부 시스템 연동 개발",
        "date": "2024-05-03T17:04:31.820212Z",
        "image": "1714755870.417252.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "MLOps Engineer",
        "writer": "정희빈",
        "content": "영상 처리 인공지능 스타트업 메이아이(mAy-I)에서 MLOps Engineer를 모십니다! 본 포지션은 산업기능요원, 전문연구요원으로의 전직 및 편입이 가능합니다. ⦁ ’산업기능요원’ 보충역은 전직과 편입이 가능하며, 현역은 전직만 가능합니다. ⦁ ’전문연구요원’은 보충역, 현역 모두 전직과 편입이 가능합니다.",
        "date": "2024-05-03T17:05:34.194564Z",
        "image": "1714755932.637985.jpg"
    },
    {
        "reviews": [],
        "tag": "job",
        "title": "백엔드 개발자 (Node.js)",
        "writer": "정희빈",
        "content": "피지엠파트너스는 PC방 운영 및 가맹 사업을 기반으로 PC방 멤버십 플랫폼 서비스와 F&B 브랜드를 개발하고 운영합니다. 현재 업계 유일하게 20곳 이상의 옵티멈존 PC방 직영 사업장 및 가맹 사업장을 보유하고 있으며, 이를 기반으로 양질의 먹거리를 개발부터 유통까지 책임지는 식음료 유통전문 브랜드 푸드차지를 확장해 나가고 있습니다.",
        "date": "2024-05-03T17:06:56.341752Z",
        "image": "1714756014.551831.jpg"
    }
]

for item in data:
    sql = "INSERT INTO job_job (tag, title, writer, content, date, image) VALUES (%s, %s, %s, %s, %s, %s)"
    date_time_obj = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_date = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
    val = (item["tag"], item["title"], item["writer"], item["content"], formatted_date, item["image"])
    mycursor.execute(sql, val)

mydb.commit()

print("Job DB Insert completed successfully!")

mydb.close()
