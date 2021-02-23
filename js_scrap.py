from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import geckodriver_autoinstaller
import lxml
import os
from pprint import pprint


class JsScrap:

    def __init__(self, theme_query):
        self.theme = theme_query.lower()
        self.url_site = f"https://www.youtube.com/results?search_query=tuto+{self.theme}"
        self.base_url = self.url_site.split('/results')[0]
        geckodriver_autoinstaller.install()
        self.driver = webdriver.Firefox(
            service_log_path='log/geckodriver.log')
        self.driver.get(self.url_site)
        self.page_source = self.driver.page_source
        self.soup = BeautifulSoup(self.page_source, 'lxml')
        self.id_theme = {
            'python': 1,
            'javascript': 2,
            'docker': 3,
            'cloud': 4
        }

    def get_data(self):
        listData = self.soup.find_all('div', {'id': 'dismissable'})
        print(len(listData))
        all_data = []
        for key, value in enumerate(listData):
            data = []
            try:
                data.append(listData[key].find('yt-formatted-string',
                                               {'class': 'style-scope ytd-video-renderer'}).get_text())
                # nb de vues
                data.append(listData[key].find('span',
                                               {'class': 'style-scope ytd-video-meta-block'}).get_text().replace('\xa0', ' ').replace('\xa0', ' '))
                # auteur
                data.append(listData[key].find('a',
                                               {'class': 'yt-simple-endpoint style-scope yt-formatted-string'}).get_text())
                # description
                data.append(listData[key].find('yt-formatted-string',
                                               {'id': 'description-text'}).get_text(strip=True).replace('\xa0', ''))
                # durée
                data.append(listData[key].find('span', {
                    'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).get_text(strip=True))

                # lien de la video
                data.append(
                    self.base_url + listData[key].find('a', {'id': 'video-title'})['href'])

                # image
                data.append(listData[key].find('img',
                                               {'class': 'style-scope yt-img-shadow'})['src'])

                # clé étrangère
                data.append(self.id_theme[self.theme])
                all_data.append(tuple(data))
            except:
                pass
        return all_data


scrap_test = JsScrap('javascript')

pprint(scrap_test.get_data())
# scrap_test.driver.quit()


# base_url = scrap_test.url_site.split('/results')[0]
# baseScrap = scrap_test.soup.find_all('div', {'id': 'dismissable'})
# try:
#     # titre
#     print(baseScrap[0].find('yt-formatted-string',
#                             {'class': 'style-scope ytd-video-renderer'}).get_text())
#     # nb de vues
#     print(baseScrap[0].find('span',
#                             {'class': 'style-scope ytd-video-meta-block'}).get_text(strip=True).split('vues')[0])
#     # auteur
#     print(baseScrap[0].find('a',
#                             {'class': 'yt-simple-endpoint style-scope yt-formatted-string'}).get_text())
#     # description
#     print(baseScrap[0].find('yt-formatted-string',
#                             {'id': 'description-text'}).get_text(strip=True))
#     # durée
#     print(baseScrap[0].find('span', {
#           'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).get_text(strip=True))

#     # lien de la video
#     print(base_url + baseScrap[0].find('a', {'id': 'video-title'})['href'])

#     # image
#     print(baseScrap[0].find('img',
#                             {'class': 'style-scope yt-img-shadow'})['src'])

#     # scrap_test.driver.quit()
# except:
#     pass
