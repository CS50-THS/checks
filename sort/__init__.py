import check50
from re import search
from re import findall

@check50.check()
def exists():
    """answers.txt exists"""
    check50.exists("answers.txt")

@check50.check(exists)
def answers():
    """answers all questions"""
    content = open("answers.txt", "r").read()
    if "TODO" in content:
        raise check50.Failure("Not all questions answered.")


