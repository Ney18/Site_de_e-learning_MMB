import logging


class PythonScrap:

    logging.basicConfig(filename="log/Python_scrap.log",
                        format='%(asctime)s - %(name)s -%(levelname)s - %(message)s', datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        logging.info('instanciation PythonScrap class et get data')
        try:
            return [
                ('<iframe width = "560" height = "315" src = "https://www.youtube.com/watch?v=psaDHhZ0cPs" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >',
                 'APPRENDRE LE PYTHON #1 ? LES BASES & PREREQUIS', 'Graven - Développement', '9m26', 9008, 'Python'),
                ('<iframe width = "560" height = "315" src = "https://www.youtube.com/watch?v=rfscVS0vtbw" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >',
                 'Learn Python - Full Course for Beginners [Tutorial]', 'freeCodeCamp.org', '4h26m56', 2723, 'Python'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/watch?v=DPaUCvNcHiM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 '5 mini-projets python pour les débutants', 'FORMASYS', '1h13m08', 2375, 'Python')
            ]
        except Exception as e:
            logging.error("error lors de l'insertion")

toto = PythonScrap()
toto.data

