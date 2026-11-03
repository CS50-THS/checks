import check50
import check50.c


@check50.check()
def exists():
    """roster.c exists"""
    check50.exists("roster.c")


@check50.check(exists)
def compiles():
    """roster.c compiles without errors"""
    check50.c.compile("roster.c", lcs50=True)


@check50.check(compiles)
def test_no_args():
    """handles lack of command-line arguments with usage message (exit code 1)"""
    check50.run("./roster").stdout("Usage: ./roster [Name:Score ...]\n").exit(1)


@check50.check(compiles)
def test_single_student():
    """correctly formats and prints a single student"""
    check50.run("./roster Alice:92").stdout("^1\\. Alice - 92\n?$", regex=True).exit(0)


@check50.check(compiles)
def test_sorting_descending():
    """sorts multiple students in descending order by score"""
    check50.run("./roster Bob:72 Charlie:95 Alice:88").stdout(
        "^1\\. Charlie - 95\n2\\. Alice - 88\n3\\. Bob - 72\n?$", regex=True
    ).exit(0)


@check50.check(compiles)
def test_equal_scores():
    """handles students with tied scores without crashing"""
    output = check50.run("./roster Alice:85 Bob:85").stdout()
    if "85" not in output or "1." not in output or "2." not in output:
        raise check50.Failure("Expected tied scores to both appear in output rankings")


@check50.check(compiles)
def test_valgrind_clean():
    """valgrind reports zero memory leaks and zero errors"""
    check50.c.valgrind("./roster", "Alice:90", "Bob:75", "Charlie:85").stdout(
        "^1\\. Alice - 90\n2\\. Charlie - 85\n3\\. Bob - 75\n?$", regex=True
    ).exit(0)
