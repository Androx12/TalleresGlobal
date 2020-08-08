import msvcrt

class vistasMenu:

    def __init__ (self): #Menús de vistas que se utilizan en el flujo como menús
        self.SaltoLinea =   ""

    def mInicio_Programa(self):
        print( self.SaltoLinea + "\n" + "\n" +"Taller número 5 Programación Avanzada")

    def mFin_Programa(self):
        print("************************************")
        print( "\n" + self.SaltoLinea + "Se ha completado el taller número 5")
        print("\n")
        print("************************************")


    def mOpcionesMenu(self):
        print("")
        print("*----*----*----*----*----*----*----*")
        print("| 1. Ingresar al Menú.             |")
        print("| 2. Salir del programa.           |")
        print("*----*----*----*----*----*----*----*")
        print("")

    def mOpcionesMenuInterno(self):
        print("")
        print("*----*----*----*----*----*----*----*")
        print("| 1. Ingresar credenciales (LOGIN).|")
        print("| 2. Nuevo jugador.                |")
        print("| 3. Ver los jugadores existentes. |")
        print("*----*----*----*----*----*----*----*")
        print("")
    
    def mConfirmar(self):
        print("")
        print("*------*------*------*-----*-----*------*------*")
        print("| Si está seguro presione 1 de lo contrario 2  |")
        print("|                                              |")
        print("| 1. Confirmar.                                |")
        print("| 2. Volver.                                   |")
        print("*------*------*------*-----*-----*------*------*")
        print("")

    def mDiezLineas(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

    def mExiste(self):
        print("----------------------------------------------")
        print("")
        print("")
        print("")
        print("            OOOOPS!")
        print("")
        print("         ¯\\_(ツ)_/¯")
        print("")
        print("Lo sentimos ese nombre de usuario está en uso")
        print("Intenta nuevamente con otro nombre")

    def mCreado(self):
        print("----------------------------------------------")
        print("")
        print("")
        print("")
        print("            EXITO!")
        print("")
        print("            (っ▀¯▀)つ  ")
        print("")
        print("Su usuario se ha creado satisfactoriamente")


    def mRegistroNuevo(self):
        print("♪    Registro de nuevo jugaodr    ♪")
        print("")
        print("")

    
    def mContinuar(self):
        print("")
        print("")
        print("Presiones 'C' para volver al menú del sistema.")
        key = None
        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
            key = msvcrt.getwch()   #como un HANDLE de .Net

    