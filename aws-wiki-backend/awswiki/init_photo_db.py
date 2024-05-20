# init_photo_db.py

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
        "tag": "photo",
        "date": "2024-05-03T17:49:34.174508Z",
        "image": "1714758573.529695.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:49:43.774032Z",
        "image": "1714758583.136279.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:49:51.012746Z",
        "image": "1714758590.427735.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:50:00.378329Z",
        "image": "1714758599.370335.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:50:07.376007Z",
        "image": "1714758606.194763.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:50:13.677018Z",
        "image": "1714758613.147397.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:50:21.066338Z",
        "image": "1714758620.380007.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:50:31.587405Z",
        "image": "1714758631.037513.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:50:51.325205Z",
        "image": "1714758650.778901.jpg"
    },
    {
        "tag": "photo",
        "date": "2024-05-03T17:51:06.288601Z",
        "image": "1714758665.679935.jpg"
    }
]

for item in data:
    sql = "INSERT INTO photo_photo (tag, date, image) VALUES (%s, %s, %s)"
    date_time_obj = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_date = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
    val = (item["tag"], formatted_date, item["image"])
    mycursor.execute(sql, val)

mydb.commit()

print("Photo DB Insert completed successfully!")

mydb.close()
