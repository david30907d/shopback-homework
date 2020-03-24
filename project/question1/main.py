import re

import jieba
from defusedxml.ElementTree import parse
from udicOpenData.dictionary import *


def q1(path: str = "news.rss") -> None:
    tree = parse(path)
    with open("description.txt", "w") as df, open("output.txt", "w") as of:
        for elem in tree.iter(tag="description"):
            elem_text = re.sub(r"<.+?>", "", elem.text)
            news_story = []
            text = elem_text.replace("&nbsp", "")
            if text:
                df.write(text + "\n")
                news_story += jieba.lcut(text)
            of.write(" ".join(news_story) + "\n")
