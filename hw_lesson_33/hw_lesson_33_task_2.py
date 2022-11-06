"""
Load data

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.


"""
import requests
import json


def task_3():
    request = "https://api.pushshift.io/reddit/comment/search/?q=Ford+F350+1977&sort=asc&sort_type=created_utc"
    response = requests.get(request).json()
    with open("Task2.json", "w") as file:
        json.dump(response, file)


if __name__ == "__main__":
    task_3()
