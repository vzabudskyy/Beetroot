"""
ask 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

```

def stop_words(words: list):

    pass



@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"



assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

```
"""
import re


def stop_words(words: list):
    def inner(func):
        def wrapper(*args, **kwargs):
            s = func(*args, **kwargs)
            for i in words:
                s = s.replace(i, "*")
            return s
        return wrapper
    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
