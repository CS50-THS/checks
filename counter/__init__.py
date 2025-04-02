import check50

@check50.check()
def index_exists():
    """index.html exists"""
    check50.exists("index.html")

@check50.check()
def style_exists():
    """style.css exists"""
    check50.exists("styles.css")

@check50.check()
def script_exists():
    """script.js exists"""
    check50.exists("script.js")

   
