import requests


def add(x, y):
    return x + y

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(15, 16) == 31

def test_add3():
    assert add(151, 161) == 312

def test_true():
    assert True == True

def test_app():
    r = requests.get("http://web:5000")
    assert r.status_code == 200
    assert "Hello World I have been seen" in r.text
    pattern = "^[a-zA-Z ]{1,}[0-9]{1,}$"
    assert re.match(pattern, r.text)
