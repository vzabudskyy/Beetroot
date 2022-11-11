"""
Task 2

Requests using asyncio and aiohttp

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump them to a file.
For this task use asyncio and aiohttp libraries for making requests to Reddit API.
"""
import asyncio
import aiohttp
import time
import json


async def save_json(file_name, data):
    with open(f"{file_name}.json", "w") as file:
        json.dump(data, file)


async def download_site(session, url, file_name):
    async with session.get(url) as response:
        await save_json(file_name, await response.json())


async def download_all_sites(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(asyncio.create_task(download_site(session, url[1], url[0])))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    requests = (
        ("request1", "https://api.pushshift.io/reddit/comment/search/?q=Ford+F350+1977&sort=asc&sort_type=created_utc"),
        ("request2", "https://api.pushshift.io/reddit/comment/search/?q=Canada+Weather&sort=asc&sort_type=created_utc"),
        ("request3", "https://api.pushshift.io/reddit/comment/search/?q=New+Year+Story&sort=asc&sort_type=created_utc")
    )
    asyncio.get_event_loop().run_until_complete(download_all_sites(requests))
    print(time.process_time())

