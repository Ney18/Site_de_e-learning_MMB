# coding=utf-8

import logging


class VideoDocker():

    logging.basicConfig(filename="log/docker_scrap.log",
                        level=logging.DEBUG,
                        format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

    def __init__(self):
        self.docker_list_link = []
        self.docker_list_title = []
        self.docker_list_youtuber = []
        self.docker_list_duration = []
        self.docker_list_vue = []
        self.docker_list_theme = []
        self.docker_zip_list = []

        # try:
        #     self.response = requests.get('https://www.youtube.com/results?search_query=docker')
        # except Exception as e:
        # #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
        #     logging.error("[SCRAP DOCKER] ERROR !! failed to access url" + str(e))

        #self.docker_html = self.response.text
        #self.soup = BeautifulSoup(self.docker_html,"html.parser")
        # print(self.data.prettify())

    def docker_link(self):

        logging.info("[DOCKER] accessing docker video link -- Start")

        try:
            self.docker_list_link = ["""<iframe width="560" height="315" src="https://www.youtube.com/embed/fqMOX6JJhGo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""",
                                     """<iframe width="560" height="315" src="https://www.youtube.com/embed/X48VuDVv0do" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""", """<iframe width="560" height="315" src="https://www.youtube.com/embed/m3cKkYXl-8o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""]
        except Exception as e:
            logging.error("[DOCKER] Error in docker link list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker video link -- End")
        return self.docker_list_link

    def docker_title(self):

        logging.info("[DOCKER] accessing docker video title -- Start")

        try:
            self.docker_list_title = ["""Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers""",
                                      "Kubernetes Tutorial for Beginners", "Terraform Tutorial | Terraform Course Overview"]
        except Exception as e:
            logging.error("[DOCKER] Error in docker title list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker video title -- End")

        return self.docker_list_title

    def docker_youtuber(self):

        logging.info("[DOCKER] accessing docker video youtuber -- Start")

        try:
            self.docker_list_youtuber = [
                "freeCodeCamp.org", "TechWorld with Nana", "TechWorld with Nana"]
        except Exception as e:
            logging.error(
                "[DOCKER] Error in docker youtuber list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker video youtuber -- End")

        return self.docker_list_youtuber

    def docker_duration(self):

        logging.info("[DOCKER] accessing docker video duration -- Start")

        try:
            self.docker_list_duration = ["2:10:18", "3:36:54", "5:40"]
        except Exception as e:
            logging.error(
                "[DOCKER] Error in docker duration list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker video duration -- End")

        return self.docker_list_duration

    def docker_vue(self):

        logging.info("[DOCKER] accessing docker video vues -- Start")

        try:
            self.docker_list_vue = ["1043959", "610423", "19786"]
        except Exception as e:
            logging.error("[DOCKER] Error in docker vues list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker video vues -- End")

        return self.docker_list_vue

    def docker_theme(self):

        logging.info("[DOCKER] accessing docker video theme -- Start")

        try:
            self.docker_list_theme = ["Docker", "Kubernetes", "Terraform"]
        except Exception as e:
            logging.error("[DOCKER] Error in docker theme list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker video theme -- End")

        return self.docker_list_theme

    def docker_zip(self):
        logging.info("[DOCKER] accessing docker zip list -- Start")

        try:
            self.docker_zip_list = list(zip(self.docker_list_link, self.docker_list_title, self.docker_list_youtuber,
                                            self.docker_list_duration, self.docker_list_vue, self.docker_list_theme))
        except Exception as e:
            logging.error("[DOCKER] Error in docker zip list !!!! " + str(e))

        logging.info("[DOCKER] accessing docker zip list -- End")

        return self.docker_zip_list
