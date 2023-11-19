# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import functions_framework

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# mock POST request = {  "user_message": "how to code a binary search tree" }
# mock_response = {"etag":"eQ8JJeOb48ipqZ0cfIkrBtJL8Ng","items":[{"etag":"V87f7fL8gAi8jZlBwuc_XdWiATg","id":{"kind":"youtube#video","videoId":"COZK7NATh4k"},"kind":"youtube#searchResult","snippet":{"channelId":"UClEEsT7DkdVO_fkrBw0OTrA","channelTitle":"mycodeschool","description":"See complete series on data structures here: http://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P ...","liveBroadcastContent":"none","publishTime":"2014-02-04T11:40:40Z","publishedAt":"2014-02-04T11:40:40Z","thumbnails":{"default":{"height":90,"url":"https://i.ytimg.com/vi/COZK7NATh4k/default.jpg","width":120},"high":{"height":360,"url":"https://i.ytimg.com/vi/COZK7NATh4k/hqdefault.jpg","width":480},"medium":{"height":180,"url":"https://i.ytimg.com/vi/COZK7NATh4k/mqdefault.jpg","width":320}},"title":"Binary search tree - Implementation in C/C++"}},{"etag":"XneGPa7Kw4MwSyUUbHYPsOq0H_s","id":{"kind":"youtube#video","videoId":"FvdPo8PBQtc"},"kind":"youtube#searchResult","snippet":{"channelId":"UCgGf1eq52dPTVuf1Njb57Hw","channelTitle":"edutechional","description":"In this algorithm tutorial, I walk through how to construct a binary search tree given an unordered array, and then how to find ...","liveBroadcastContent":"none","publishTime":"2014-05-04T02:12:21Z","publishedAt":"2014-05-04T02:12:21Z","thumbnails":{"default":{"height":90,"url":"https://i.ytimg.com/vi/FvdPo8PBQtc/default.jpg","width":120},"high":{"height":360,"url":"https://i.ytimg.com/vi/FvdPo8PBQtc/hqdefault.jpg","width":480},"medium":{"height":180,"url":"https://i.ytimg.com/vi/FvdPo8PBQtc/mqdefault.jpg","width":320}},"title":"How to Construct a Binary Search Tree"}},{"etag":"v0NoccQfrbXjyztEIu1nuUQb3R0","id":{"kind":"youtube#video","videoId":"DlWxqU3LLpY"},"kind":"youtube#searchResult","snippet":{"channelId":"UC8wZnXYK_CGKlBcZp-GxYPA","channelTitle":"NeuralNine","description":"Today we learn how to implement binary search trees in Python. \u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe\u25fe Programming Books ...","liveBroadcastContent":"none","publishTime":"2022-02-10T16:54:28Z","publishedAt":"2022-02-10T16:54:28Z","thumbnails":{"default":{"height":90,"url":"https://i.ytimg.com/vi/DlWxqU3LLpY/default.jpg","width":120},"high":{"height":360,"url":"https://i.ytimg.com/vi/DlWxqU3LLpY/hqdefault.jpg","width":480},"medium":{"height":180,"url":"https://i.ytimg.com/vi/DlWxqU3LLpY/mqdefault.jpg","width":320}},"title":"Binary Search Tree in Python"}},{"etag":"zMbBFlek9tSgSKPQqJyt4BW1DYw","id":{"kind":"youtube#video","videoId":"Gt2yBZAhsGM"},"kind":"youtube#searchResult","snippet":{"channelId":"UC4SVo0Ue36XCfOyb5Lh1viQ","channelTitle":"Bro Code","description":"Binary search tree data structures and algorithms java #binary #search #tree.","liveBroadcastContent":"none","publishTime":"2021-11-10T15:22:47Z","publishedAt":"2021-11-10T15:22:47Z","thumbnails":{"default":{"height":90,"url":"https://i.ytimg.com/vi/Gt2yBZAhsGM/default.jpg","width":120},"high":{"height":360,"url":"https://i.ytimg.com/vi/Gt2yBZAhsGM/hqdefault.jpg","width":480},"medium":{"height":180,"url":"https://i.ytimg.com/vi/Gt2yBZAhsGM/mqdefault.jpg","width":320}},"title":"Learn Binary search trees in 20 minutes \ud83d\udd0d"}},{"etag":"GsKN3VtFU8zyGd2WCpg755Arkn0","id":{"kind":"youtube#video","videoId":"NFhOrxtXXcM"},"kind":"youtube#searchResult","snippet":{"channelId":"UC42pOSNg804f1wCcj7qL0mA","channelTitle":"Coding with John","description":"Full tutorial on Binary Search in Java! \u2615 Complete Java course: https://codingwithjohn.thinkific.com/courses/java-for-beginners ...","liveBroadcastContent":"none","publishTime":"2023-02-13T15:00:14Z","publishedAt":"2023-02-13T15:00:14Z","thumbnails":{"default":{"height":90,"url":"https://i.ytimg.com/vi/NFhOrxtXXcM/default.jpg","width":120},"high":{"height":360,"url":"https://i.ytimg.com/vi/NFhOrxtXXcM/hqdefault.jpg","width":480},"medium":{"height":180,"url":"https://i.ytimg.com/vi/NFhOrxtXXcM/mqdefault.jpg","width":320}},"title":"Binary Search in Java - Full Simple Coding Tutorial"}}],"kind":"youtube#searchListResponse","nextPageToken":"CAUQAA","pageInfo":{"resultsPerPage":5,"totalResults":1000000},"regionCode":"US"}

@functions_framework.http
def submit(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    video_context = "null"

    if request_json and "user_message" in request_json:
        video_context = youtube_search(request_json["user_message"])
        # video_context = mock_response

    return video_context


def youtube_search(query):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "FIXME"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)


    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=query,
        type="video",
        videoEmbeddable="true",
    )
    response = request.execute()

    return response
