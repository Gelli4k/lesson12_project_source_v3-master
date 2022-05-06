import json
from exceptions import *


def load_json_data(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(substring, path):
    posts = load_json_data(path)
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded

# print(load_json_data('../lesson12_project_source_v3-master/posts.json'))
# print(search_post_by_substring('Ага', '../lesson12_project_source_v3-master/posts.json'))
