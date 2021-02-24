from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import geckodriver_autoinstaller
import lxml
import os
from pprint import pprint
import time


class JsScrap:

    def __init__(self, theme_query):
        self.theme = theme_query.lower()
        self.url_site = f"https://www.youtube.com/results?search_query=tuto+{self.theme}"
        self.base_url = self.url_site.split('/results')[0]
        geckodriver_autoinstaller.install()
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('-no-sandbox')
        self.options.add_argument('-disable-dev-shm-usage')
        self.driver = webdriver.Firefox(
            service_log_path='log/geckodriver.log', options=self.options)
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
        # listData = self.driver.find_elements_by_xpath(
        #     '//*[@id = "dismissable"]')
        print(len(listData))
        all_data = []
        for key, value in enumerate(listData):
            time.sleep(5)
            data = []
            try:
                # titre
                data.append(listData[key].find('yt-formatted-string',
                                               {'class': 'style-scope ytd-video-renderer'}).get_text())
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@id = "video-title"]')[key].text)
            except:
                data.append('')
            try:
                # nb de vues
                data.append(listData[key].find('span',
                                               {'class': 'style-scope ytd-video-meta-block'}).get_text().replace('\xa0', ' ').replace('\xa0', ' '))
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@class="style-scope ytd-video-meta-block"]')[key].text)

            except:
                data.append('')
            try:
                # auteur
                data.append(listData[key].find('a',
                                               {'class': 'yt-simple-endpoint style-scope yt-formatted-string'}).get_text())
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@class="yt-simple-endpoint style-scope yt-formatted-string"]')[key].text)

            except:
                data.append('')
            try:
                # description
                data.append(listData[key].find('yt-formatted-string',
                                               {'id': 'description-text'}).get_text(strip=True).replace('\xa0', ''))
                time.sleep(5)
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@id="description-text"]')[key].text)
            except:
                data.append('')
            try:
                # durée
                data.append(listData[key].find('span', {
                    'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).get_text(strip=True))
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@id="overlays"]/span[1]')[key].text)

            except:
                data.append('')
            try:
                # lien de la video
                data.append(
                    self.base_url + listData[key].find('a', {'id': 'video-title'})['href'])
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@id="thumbnail"]')[key].get_attribute('href'))

            except:
                data.append('')
            try:
                # image
                # data.append(listData[key].find('img',
                #                                {'class': 'style-scope yt-img-shadow'})['src'])
                data.append(listData[key].find('img',
                                               {'id': 'img'})['src'])
                # data.append(self.driver.find_elements_by_xpath(
                #     '//*[@id="img"]')[key].get_attribute('src'))

            except:
                data.append('')
            # clé étrangère
            data.append(self.id_theme[self.theme])
            all_data.append(tuple(data))

        return all_data


scrap_test = JsScrap('javascript')
pprint(scrap_test.get_data())
# scrap_test.driver.quit()


# url_site = f"https://www.youtube.com/results?search_query=tuto+javascript"
# geckodriver_autoinstaller.install()
# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
# options.add_argument('-no-sandbox')
# options.add_argument('-disable-dev-shm-usage')
# driver = webdriver.Firefox(
#     service_log_path='log/geckodriver.log', options=options)
# driver.get(url_site)
# chaine_titre = driver.find_elements_by_xpath('//*[@id = "video-title"]')
# titres = []
# for i in range(len(chaine_titre)):
#     titre = chaine_titre[i].text
#     titres.append(titre)

# print(titres)


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
