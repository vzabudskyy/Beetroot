"""
Task 2

Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use concurrent and multiprocessing libraries for making requests to Reddit API.
"""
from hw_lesson_34.hw_lesson_34_task_3 import check_execution_time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import json
import requests


def get_json(request, file_name):
    response = requests.get(request).json()
    with open(f"{file_name}.json", "w") as file:
        json.dump(response, file)


@check_execution_time
def threading_version(req1, req2, req3):
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(get_json, req1, "request_json_1t")
        executor.submit(get_json, req2, "request_json_2t")
        executor.submit(get_json, req3, "request_json_3t")


@check_execution_time
def processing_version(req1, req2, req3):
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.submit(get_json, req1, "request_json_1p")
        executor.submit(get_json, req2, "request_json_2p")
        executor.submit(get_json, req3, "request_json_3p")


if __name__ == "__main__":
    request1 = "https://api.pushshift.io/reddit/comment/search/?q=Ford+F350+1977&sort=asc&sort_type=created_utc"
    request2 = "https://api.pushshift.io/reddit/comment/search/?q=Canada+Weather&sort=asc&sort_type=created_utc"
    request3 = "https://api.pushshift.io/reddit/comment/search/?q=New+Year+Story&sort=asc&sort_type=created_utc"

    threading_version(request1, request2, request3)
    processing_version(request1, request2, request3)