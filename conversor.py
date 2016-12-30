
import xlrd
import xlwt
from xlutils.copy import copy
class banco:
    Cmf,Finansur = range(1,3)

class excelConversor(object):

    def __init__(self, archivoOriginal, template):
        self.archivoOriginal = archivoOriginal
        self.template = template

    def copiarDatos(self, Banco):
        """Copia los datos del del template y el original en uno nuevo.
        Devuelve un booleano"""

        if(Banco == 1):
            # print '***Sin implementar CMF***'
            self.__copiarColumna(1,2,3,4,5)
        elif(Banco == 2):
            original = xlrd.open_workbook(self.archivoOriginal)
            template = xlrd.open_workbook(self.template)
            nuevo = copy(template)

            nuevo.save('Impreso.xls')

            # print '***Sin implementar FINANSUR***'
        else:
            print 'nou implementation'


    def __copiarColumna(self,excelOriginal, hojaNueva, nroColumnaNueva, nroColumnaOriginal, nroFila):
        print '*** Sin implementar***'




if __name__ == '__main__':
    print 'algo'
