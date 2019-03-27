import json
import requests


class DownloadImageAndSaveContent:
    def __init__(self, url):
        self.url = url

    def response(self):
        return requests.get(self.url)

    def download_image(self):
        download = self.response()
        filename = self.url.split('/')[-1]
        with open("./image/" + filename, 'wb') as image:
            for item in download:
                image.write(item)

    def content(self):
        return self.response().content.__str__()

    def saving_content(self):
        filename = self.url.split('/')[-1][:-4] + ".txt"
        with open('./content/' + filename, 'w') as content:
            json.dump(self.content(), content)

    def download_image_and_save_content_atividade(self):
        self.download_image()
        self.saving_content()


if __name__ == "__main__":
    DownloadImageAndSaveContent("https://livewallpaper.info/wp-content/uploads/2017/08/Caracal-gato-grande-%C2%BB-Caracal-gato-semejante-a-un-lince-de-patas-largas-con-orejas-con-me-wallpaper-wp8001777.jpg").download_image_and_save_content_atividade()
