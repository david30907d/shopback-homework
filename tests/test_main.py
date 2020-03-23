from pathlib import Path

import pytest

from project.question1.main import q1
from project.question2.main import q2


def test_q1():
    q1(path='project/question1/news.rss')
    assert Path('output.txt').exists() == True
    assert Path('description.txt').exists() == True

def test_q2():
    q2(path='project/question1/output.txt')
    assert Path('output.txt').exists() == True
