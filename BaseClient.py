class BaseClient:

    BASE_URL = "https://api.vk.com/method/"
    method = None
    http_method = None


    def generate_url(self):
        return '{0}{1}{2}{3}'.format(self.BASE_URL, self.method, self.http_method, self.username)

    def _get_data(self):
        response = None
        return response