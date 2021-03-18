#Vamos a crear una cajita con texto 
#aplicando decoradores en python
#Es decir vamos a modificar una funcion con otra funcion
def my_borde(func, texto):
    LINE = "━"
    TOP_LEFT = "┏"
    TOP_RIGHT = "┓"
    BOTTOM_LEFT = "┗"
    BOTTOM_RIGHT = "┛"

    def caja():
    	print(f"{TOP_LEFT}{LINE*(len(texto)+2)}{TOP_RIGHT}")
    	func(texto)
    	print(f"{BOTTOM_LEFT}{LINE*(len(texto)+2)}{BOTTOM_RIGHT}")
    return caja

def contenido(mensaje):
   vline = "|"
   titulo = mensaje.center(len(mensaje)+2, ' ')
   print(f"{vline}{titulo}{vline}")

txt = input("Ingresa tu texto: ")
decorador = my_borde(contenido, txt)
decorador()
