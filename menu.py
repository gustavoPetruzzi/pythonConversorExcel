class Menu(object):
    
    def __init__(self, *opciones):
        self.opciones = opciones
        
    

    def mostrarMenu(self):
        nroOpcion = 1
        for option in self.opciones:
            print '{0}. {1}'.format(nroOpcion,option)
            nroOpcion = nroOpcion +1
        
        print '{0}. Salir'.format(nroOpcion, option)
        return raw_input("Ingrese opcion: ")
    
    if __name__ == '__main__':
        print 'Hello World'
            
        
    
