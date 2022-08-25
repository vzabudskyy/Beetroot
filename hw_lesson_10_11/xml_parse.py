import xml.etree.ElementTree as ET
from pprint import pprint


def read_xml_by_tag(file):
    text = ""
    subject_state = None
    while True:
        buffer = file.read(128)
        text += buffer
        if "</SUBJECT>" in buffer and subject_state is False:
            break
        elif "<SUBJECT>" in buffer:
            subject_state = False

    begin = text.index("<SUBJECT>")
    end = text.index("</SUBJECT>") + 10
    text = text[begin:end]

    return text, buffer


def dict_tags(root):
    subject = {child.tag: child.text for child in root}
    return subject


def set_on_next_tag(file, buffer):
    file.seek(file.tell() - (128 - buffer.index("</SUBJECT>") - 10))


def search_by_tag(tag, root):
    answer = root.find(tag).text
    return answer


def get_user_input():
    user_inp = input("Enter code: ")
    return user_inp


def main():
    counter = 0
    user_data = get_user_input()
    with open("data/17.1-EX_XML_EDR_UO_FULL_24.01.2022.xml", "r", encoding="windows-1251") as file:
        while True:
            text, buffer = read_xml_by_tag(file)
            root = ET.fromstring(text)

            data = search_by_tag(root=root, tag="EDRPOU")
            if data == user_data:
                pprint(dict_tags(root))
                return
            else:
                set_on_next_tag(file, buffer)
            counter += 1
            if counter % 100 == 0:
                print(f"Processed {counter} records from file")


if __name__ == "__main__":
    main()
