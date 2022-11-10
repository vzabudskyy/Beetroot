"""
Task 3

Requests using multiprocessing

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.
"""
import requests
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from functools import wraps


def check_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        delta = end - start
        print(f"{func.__name__} was executed in {delta}")
        return result
    return wrapper


def get_json(request, file_name):
    response = requests.get(request).json()
    with open(f"{file_name}.json", "w") as file:
        json.dump(response, file)


@check_execution_time
def one_by_one_version(req1, req2, req3):
    get_json(req1, "request_json_1")
    get_json(req2, "request_json_2")
    get_json(req3, "request_json_3")


@check_execution_time
def threading_version(req1, req2, req3):
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(get_json, req1, "request_json_1")
        executor.submit(get_json, req2, "request_json_2")
        executor.submit(get_json, req3, "request_json_3")


if __name__ == "__main__":
    request1 = "https://api.pushshift.io/reddit/comment/search/?q=Ford+F350+1977&sort=asc&sort_type=created_utc"
    request2 = "https://api.pushshift.io/reddit/comment/search/?q=Canada+Weather&sort=asc&sort_type=created_utc"
    request3 = "https://api.pushshift.io/reddit/comment/search/?q=New+Year+Story&sort=asc&sort_type=created_utc"

    one_by_one_version(request1, request2, request3)
    threading_version(request1, request2, request3)
