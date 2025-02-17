from starlette.testclient import TestClient

from tutorial import _01_click_to_edit as module


def test_app():
    client = TestClient(module.app)

    def check(r):
        c = module.current
        assert r.status_code == 200
        assert c.name in r.text
        assert c.email in r.text

    r = client.get("/contact")
    check(r)

    r = client.get("/contact/edit")
    check(r)

    r = client.put("/contact", data={"name": "AAA", "email": "BB"})
    check(r)
    assert module.current.name == "AAA"
