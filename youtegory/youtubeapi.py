
import requests
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import googleapiclient.discovery

def get_videos(categoryId):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBP7wo8LVQcNgdUo5BQKMzZZejqgMI5Rds"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        maxResults=10,
        regionCode="KR",
        videoCategoryId=categoryId
    )
    response = request.execute()
    items = response["items"]
    dics=[]
    for item in items:
        video_id = item["id"]
        title = item["snippet"]["title"]
        data={
            'category' : categoryId,
            'video_id' : video_id,
            'title': title
            }
        dics.append(data)
    return dics

        # data = requests.post('http://localhost:8000/categories/{}/videos'.format(categoryId), data=doc)

