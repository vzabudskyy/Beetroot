"""
Написати функцію, яка вираховує глибину словника.
"""

glossary_dict = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
"""
1. якщо словник пустий або у ньому немає інших словників, додаємо branch у checked
2. якщо досягнуто передостаннього елементу минулої гілки, наступний елемент поточному рівні, якщо можливо
3. якщо неможливо виконати попередній пункт, повернутися на минулий рівень вкладеності
"""

empty_dict = {}
dict_1 = {"key": "value"}
d = {"key": {"key":0}}

def dict_depth(dictionary, depth,counter = 0):
    for i in dictionary.values():
        depth.append(counter + 1)
        if type(i) == dict:
            return dict_depth(i, depth, counter + 1)
    if depth:
        return max(depth)
    return 0


if __name__ == "__main__":
    assert dict_depth(glossary_dict, []) == 6
    assert dict_depth(empty_dict, []) == 0
    assert dict_depth(dict_1, []) == 1
    assert dict_depth(d, []) == 2
