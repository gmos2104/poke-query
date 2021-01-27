class MockRequests:
    def __init__(self, ok=True, json_data=None):
        self.ok = ok
        self.json_data = json_data
        self.get_method_called = False

    def __call__(self, *args, **kwargs):
        self.get_method_called = True
        self.response = MockResponse(json_data=self.json_data)
        return self.response


class MockResponse:
    def __init__(self, ok=True, json_data=None):
        self.ok = ok
        self.json_method_called = False
        self.json_data = json_data

    def json(self):
        self.json_method_called = True
        return self.json_data


class MockRedis:
    def __init__(self, get_data=None):
        self.get_data = get_data
        self.get_method_called = False
        self.set_method_called = False

    def get(self, *args, **kwargs):
        self.get_method_called = True
        return self.get_data

    def set(self, *args, **kwargs):
        self.set_method_called = True

    def __call__(self, *args, **kwargs):
        return self
