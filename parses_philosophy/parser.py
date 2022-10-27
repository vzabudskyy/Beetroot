import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


pages = []


class Page:
    @staticmethod
    def get_links(page, path):
        req = Request("https://en.wikipedia.org" + page)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        links = set()
        for link in soup.findAll('a'):
            text = str(link.get('href'))
            if text.startswith("/wiki") and ":" not in text and text not in path:
                links.add(text)
        links = list(links)
        links.sort()
        return links

    def __init__(self, page, path):
        self.page = page
        self.links = self.get_links(page, path)
        self.path = path




def bfs(start, end):
    """Breadth First Search"""
    path_to_end = None
    page_queue = [start]
    while page_queue:
        current_page = page_queue.pop(0)
        print(f"{current_page.page}")
        for link in current_page.links:
            print(f"\t\t\t\t{link}")
            if link == end:
                path_to_end = current_page.path+[link]
                return path_to_end
            next_page = Page(link, current_page.path)
            if link not in current_page.path:
                page_queue.append(next_page)

"""
Алгоритм:
    1. Приходимо на сторінку, якщо вона не є шуканою, додаємо в шлях.
    2. Беремо всі посилання, що підходять нам.
    3. Вибираємо посилання, які не повторюються у інших вершинах.
    4. Заходимо в кожну з них, повторюємо алгоритм.
    
    queue
    
    current_page.links побити на 10 однакових частин.
    thread(10 links) -> 1 next pages in queue \
                                                } ?
    thread(10 links) -> 1 next pages in queue /
    
    thread(10 links) -> [10 next pages] -> queue = queue + [10 next pages]
"""

if __name__ == "__main__":
    #start = Page("/wiki/Evaluation", [])
    #bfs(start, "/wiki/Environment_(systems)")

    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    start = 0
    step = len(arr) // 5
    end = None
    for i in range(5):
        if i == 4:
            end = len(arr)
        else:
            end = start + step
        print(arr[start:end])
        start = end
