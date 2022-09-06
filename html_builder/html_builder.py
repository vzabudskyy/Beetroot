"""
html = HTML(Head -> class, Body -> class)
body = Body(Div -> class)
HTML -> те що збирає теги(класи) до купи

"""


"""
html = HTML(Head -> class, Body -> class)
body = Body(Div -> class)
HTML -> те що збирає теги(класи) до купи

"""


class Tag:
    def __init__(self, tag_name, content=None, attr=None):
        self.tag_name = tag_name
        self.content = content
        self.attr = attr

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
        return f"<{self.tag_name} {attr}>\n\t{content}\n</{self.tag_name}>"


class Div(Tag):
    def __init__(self, content, attr=None):
        super().__init__("div", content, attr)


class P(Tag):
    def __init__(self, content, attr=None):
        super().__init__("p", content, attr)


class Html(Tag):
    def __init__(self, content, attr=None):
        super().__init__("html", content, attr)

    def __str__(self):
        return f"<!DOCTYPE html>\n{Tag.__str__(self)}"


if __name__ == "__main__":
    tag = Html(Div([Div(P("First")), P('Frtrtr'), P('Frtrtr')]))
    print(tag)
    tag = Html(
        [Div(['First', P('Paragraph')], {'class': 'jss5 jss6'}),
         P('Hello world')]
    )
    print(tag)
