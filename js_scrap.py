import logging


class JsScrap:

    logging.basicConfig(filename="log/js_scrap.log",
                        format='%(asctime)s - %(name)s -%(levelname)s - %(message)s', datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        logging.info('instanciation jsScrap class et get data')
        try:
            return [
                ('<iframe  src = "https://www.youtube.com/embed/bd0fwri-0No" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >',
                 'ECMAScript 6 - 1 - Introduction(Tutoriel Français)', 'les teachers du net', '6m04', 9008, 'javascript'),
                ('<iframe  src = "https://www.youtube.com/embed/1ODCRIsktWE" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >',
                 'ECMAScript 6 - 2 - Compatibilité au niveau des différents navigateurs(Tutoriel Français)', 'les teachers du net', '1m43', 2723, 'javascript'),
                ('<iframe  src="https://www.youtube.com/embed/63s2BNrL0IQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'ECMAScript 6 - 3 - Le transcompilateur Babel', 'les teachers du net', '1m19', 2375, 'javascript')
            ]
        except Exception as e:
            logging.error("error lors de l'insertion")


my_js = JsScrap()
my_js.get_data()