"""
Task 1

Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc.
"""
import requests


response = requests.get("https://en.wikipedia.org/robots.txt")
with open("robots.txt", "w", encoding="utf8") as file:
    file.write(response.text)
