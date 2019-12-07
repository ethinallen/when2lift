import requests
from bs4 import BeautifulSoup
import time

class getter():

    def __init__(self):

        self.cookies = {
            'PHPSESSID': '44bbb1809a90f92d9c4a920b469e87e2',
            'CP5XKN6QLDFWUC': 'ff4f34e046678ae7eea4b822d62a70e6%7C%7C1575760342',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'http://www.clemson.edu/campus-life/campus-recreation/counts.html',
            'Upgrade-Insecure-Requests': '1',
        }

        self.params = (
            ('type', 'circle'),
            ('key', '92433390-628E-42FC-918F-9111CBAF9D63'),
            ('', ''),
        )
        self.responseContent = self.getContent()
        self.parseContent()
        self.writeContent()

    def getContent(self):
        responseContent = requests.get('https://connect2concepts.com/connect2/', headers=self.headers, params=self.params, cookies=self.cookies).content
        return responseContent

    def parseContent(self):
        soup = BeautifulSoup(self.responseContent, features = 'html.parser')
        self.data = soup.find_all('div', {'style':'text-align:center;'})

    def writeContent(self):
        with open('needToMakeDynamoDB.txt', 'a') as f:
            f.write(str(time.time()) + '\n')
            for d in self.data:
                f.write(d.text + '\n')
            f.write('\n\n')


if __name__ == '__main__':
    g = getter()
