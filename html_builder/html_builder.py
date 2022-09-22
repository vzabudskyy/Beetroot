from selenium import webdriver as w
from time import sleep
import os
from datetime import datetime, timedelta


class HmtlDisplayer:
    webdrivers_info = {"firefox": {"driver": w.Firefox, "path": "\\browser_drivers\\geckodriver.exe"},
                       "chrome": {"driver": w.Chrome, "path": "\\browser_drivers\\chromedriver.exe"}
                       }

    def __init__(self, bw_name):
        self.bw_name = bw_name
        os.environ["PATH"] += os.pathsep + os.getcwd() + self.webdrivers_info[bw_name]["path"]
        self.driver = self.webdrivers_info[bw_name]["driver"](executable_path=self.webdrivers_info[bw_name]["path"][1:])

    def open(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()


class Tag:
    _tag_name = "tag"
    _type = "Double"

    def __init__(self, content=None, attr=None):
        self.content = content
        self.attr = attr

    def save(self, name):
        with open(f"{name}", "w") as file:
            file.write(self.__str__())

    def __str__(self):
        if type(self.content) == list:
            content = '\n'
            for i in self.content:
                content += str(i) + '\n'
        else:
            content = self.content

        if type(self.attr) == dict:
            attr = " ".join([f"{key}={value}" for key, value in self.attr.items()])
        else:
            attr = ""
        content = str(content).replace('\n', '\n\t')
        if self._type == "Double":
            return f"<{self._tag_name} {attr}>\n\t{content}\n</{self._tag_name}>"
        else:
            return f"<{self._tag_name} {attr}>"


class Div(Tag):
    _tag_name = "div"


class P(Tag):
    _tag_name = "p"


class H1(Tag):
    _tag_name = "h1"


class Link(Tag):
    _type = "Once"
    _tag_name = "link"


class Html(Tag):
    _tag_name = "html"

    def __str__(self):
        return f"<!DOCTYPE html>\n{Tag.__str__(self)}"


class Head(Tag):
    _tag_name = "head"


class Body(Tag):
    _tag_name = "body"


class Timer:
    def __init__(self, time):
        self.anchor_time = None
        self.time = datetime.strptime(time, "%H:%M:%S")

    def __call__(self):
        delta = self.time - (datetime.now() - self.anchor_time) + timedelta(microseconds=100000)
        return delta.strftime("%H:%M:%S")

    def start(self):
        self.anchor_time = datetime.now() + timedelta(microseconds=30000)


if __name__ == "__main__":
    t = Timer("00:00:20")
    screen = HmtlDisplayer("chrome")
    page = Html([
                Head(
                        Link(attr={"rel": "stylesheet", "href": "\"mystyle.css\""})
                    ),
                Body([
                        Div("TIMER"),
                        H1("########")
                    ])
                ])
    page.save("index.html")
    screen.open("C:\\Users\\Vladislav\\PycharmProjects\\BeetrootAcademy\\html_builder\\index.html")
    t.start()
    while t() != "00:00:00":
        sleep(1)
        t_time = t()
        page = Html([
            Head(
                Link(attr={"rel": "stylesheet", "href": "\"mystyle.css\""})
            ),
            Body([
                Div("TIMER"),
                H1(t_time)
            ])
        ])
        page.save("index.html")
        screen.refresh()

