import requests

# Spider code
class XianyuSpider:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

if __name__ == '__main__':
    spider = XianyuSpider('https://example.com/api')
    data = spider.fetch_data()
    print(data)