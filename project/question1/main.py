import re
import xml.etree.ElementTree as ET

import jieba
from udicOpenData.dictionary import *


def q1(path:str="news.rss") -> None:
    tree = ET.parse(path)
    with open("description.txt", "w") as df, open("output.txt", "w") as of:
        for elem in tree.iter(tag="description"):
            elem_text = re.sub(r"<.+?>", "", elem.text)
            news_story = []
            text = elem_text.replace("&nbsp", "")
            if text:
                of.write(text + "\n")
                news_story += jieba.lcut(text)
            df.write(" ".join(news_story) + "\n")
