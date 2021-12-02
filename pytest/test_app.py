import requests


def add(x, y):
    return x + y

def test_add():
    assert add(5, 6) == 1111

def test_app():
    #r = requests.get("http://shay.freeddns.org:8888")
    r = requests.get("http://web:5000")
    assert r.status_code == 200
    assert "Hello World I have been seen" in r.text

