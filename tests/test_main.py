from pathlib import Path

import pytest

from project.question1.main import q1
from project.question2.main import q2


def test_q1() -> None:
    q1(path="project/question1/news.rss")
    if __debug__:
        if not Path("output.txt").exists():
            raise AssertionError("output.txt not found")
        if not Path("description.txt").exists():
            raise AssertionError("description.txt not found")


def test_q2() -> None:
    q2(path="project/question1/output.txt")
    if __debug__:
        if not Path("output2.txt").exists():
            raise AssertionError("output2.txt not found")
