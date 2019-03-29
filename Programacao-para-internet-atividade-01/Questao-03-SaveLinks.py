import requests
import re
import json


class SaveLinks:
    def __init__(self, url):
        self.url = url.__str__()

    def response(self):
        return requests.get(self.url)

    def content(self):
        return self.response().content.__str__()

    def page_links(self):
        return re.findall('(?<=href=["\'])https?://.+?(?=["\'])', self.content())

    def save_links(self):
        links = self.page_links()[0]
        filename = "links.txt"
        for link in self.page_links()[1:]:
            links += '  ' + link

        with open("./links/" + filename, 'w') as page_links:
            json.dump(links, page_links)


if __name__ == "__main__":
    SaveLinks("http://www.google.com/").save_links()
