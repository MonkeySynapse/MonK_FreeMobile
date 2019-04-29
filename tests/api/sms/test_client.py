from monkfreemobile.api.sms.client import Client


class TestClient(object):
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def tearDown_method(self, method):
        pass

    def test_send(self):
        client = Client("BadUser", "BadPassword")
        response = client.send("This is a test")
        assert response.status_code == 403
