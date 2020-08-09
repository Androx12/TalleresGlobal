from Vistas import vistasMenu
from controllers import Controller
import msvcrt

class ejecucionSistemaControl:

    obj_Controller = Controller()
    obj_VistaMenu = vistasMenu()

    def __init__(self):
        self.obj_VistaMenu.mInicio_Programa()
        self.correo = ''
        self.usuario = ''
        self.contrasena = ''
        self.banderaRegistro = None
        self.banderaLogin = None

    def CorrerPrograma(self):
        
        BanderaPrograma = True

        while BanderaPrograma == True:  #Se crea un ciclo para mantener el flujo validando con (BanderaPrograma)

            try:
                print('Trabajo con archivos JSON')
                self.obj_VistaMenu.mOpcionesMenu() #Se trae la vista de el Menú
                sEntrada_Usuario = input("Seleccione una opción de Menú --> ")
                
                if (sEntrada_Usuario == '1'): #Flujo en 1

                    self.obj_VistaMenu.mDiezLineas()
                    self.obj_VistaMenu.mOpcionesMenuInterno() #Se trae la vista de el Menú interno

                    sEntrada_Interna = input("Seleccione una opción de Menú --> ")

                    if sEntrada_Interna == '1':
                        
                        self.obj_VistaMenu.mDiezLineas()
                        self.obj_VistaMenu.mLoginUsuario()
                        self.banderaLogin = True
                        while(self.banderaLogin):

                            self.usuario = input("Digite su usuario --> ")
                            print("")
                            self.contrasena = input("Digite su contraseña --> ")
                            print("")

                            if(self.obj_Controller.mVerificarLogin(self.usuario,self.contrasena)):
                                self.banderaLogin = False
                            else:
                                self.banderaLogin = True
                        self.obj_VistaMenu.mContinuar()
                    else:
                        if sEntrada_Interna == '2':
                            
                            self.obj_VistaMenu.mDiezLineas()
                            self.obj_VistaMenu.mRegistroNuevo()
                            
                            self.banderaRegistro = True
                            while(self.banderaRegistro): 
                                print("")
                                self.correo = input("Por favor ingrese su correo --> ")
                                if(self.obj_Controller.mVerificarFormatos(self.correo,"correo")):
                                    self.banderaRegistro = False
                                else:
                                    self.banderaRegistro = True

                            self.banderaRegistro = True
                            while(self.banderaRegistro): 
                                print("")
                                self.usuario = input("Por favor cree un usuario --> ")
                                print("")
                                self.contrasena = input("Por favor cree una contraseña --> ")
                                nuevo = {'username': self.usuario, 'password': self.contrasena}

                                if(self.obj_Controller.mVerificarFormatos(nuevo,"pass")):

                                    if(self.obj_Controller.mVerificarFormatos(nuevo,"usuario")):
                                        self.banderaRegistro = False
                                        print('Nuevo usuario: {}'.format(nuevo['username']))
                                    else:
                                        self.banderaRegistro = True
                                else:
                                    self.banderaRegistro = True
                            
                            self.obj_VistaMenu.mContinuar()
                        else:
                            if sEntrada_Interna == '3':

                                print('')
                                print('Lista de Jugadores.')
                                print('')
                                self.obj_Controller.mCargarJugadores()
                                self.obj_VistaMenu.mContinuar()

                            else:
                                self.obj_VistaMenu.mDiezLineas()
                                print('Entrada invalida.')
                                print("Las opciones del Menú interno son '1', '2' o '3'.")
                                print("Presione 'C' para voler al Menú Principal")
                                key = None
                                while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
                                    key = msvcrt.getwch()   #como un HANDLE de .Net
                                self.obj_VistaMenu.mDiezLineas()
                else:
                    if sEntrada_Usuario == '2':  #Flujo en S
                        self.obj_VistaMenu.mDiezLineas()
                        self.obj_VistaMenu.mFin_Programa() #Vista de Salida
                        BanderaPrograma = False
                    else:                       #Otra entrada genera un flujo de error para obligar al usuario
                        BanderaPrograma = True  #a ingresar los datos dentro del menú
                        self.obj_VistaMenu.mDiezLineas()
                        print('Entrada invalida.')
                        print("Las opciones del Menú son '1' y '2'.")
                        print("Presione 'C' para voler al Menú")
                        key = None
                        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
                            key = msvcrt.getwch()   #como un HANDLE de .Net
                        self.obj_VistaMenu.mDiezLineas()
            except:
                pass