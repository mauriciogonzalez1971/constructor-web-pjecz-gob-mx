import csv
from datetime import datetime
from comun.base import Base
from comun.seccion import Seccion


class Conocenos(Base):
    """ Coordina la rama de Conócenos """

    def __init__(self, arg):
        super().__init__(insumos_ruta, 'Conócenos')
        self.arg = arg

    def alimentar(self):
        pass

    def contenido(self):
        pass

    def __repr__(self):
        super().__repr__()