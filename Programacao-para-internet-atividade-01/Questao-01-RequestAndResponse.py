import requests


class RequestAndResponse:
    def __init__(self, url):
        self.url = url

    def response(self):
        return requests.get(self.url)

    def status_code(self):
        return self.response().status_code

    def headers(self):
        return self.response().headers

    def content_length(self):
        return self.response().headers['Content-length']

    def content(self):
        return self.response().content.__str__()

    def request_and_response_atividade(self):
        print("Status Code: {}\n"
              "Cabeçalhos (Headers): {}\n"
              "Tamanho da resposta (Content Length): {}\n"
              "Corpo da resposta: {}".format(self.status_code(),
                                             self.headers(),
                                             self.content_length(),
                                             self.content()))


if __name__ == '__main__':
    RequestAndResponse("http://www.google.com/").request_and_response_atividade()
