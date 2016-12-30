import menu

miMenu = menu.Menu('Cmf','Finansur')
nroOpcion = -1
while not nroOpcion == 3:
    try:
        nroOpcion = int(miMenu.mostrarMenu())
    except ValueError:
        print 'Forro, un numero pone'
raw_input('Press Enter to exit')