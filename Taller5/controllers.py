from Vistas import vistasMenu
from collections import Counter
import json

class Controller:

    obj_VistaMenu = vistasMenu()

    def __init__(self):
        self.usuariosJson = 'Taller5/existing_users.json'
        self.registrationJson = 'Taller5/registration.json'
        self.loginJson = 'Taller5/login.json'
        self.banderaExistencia = None
        self.bandNumeros = None
        self.banderaCaract = None


    def mCargarJugadores(self):
        with open (self.usuariosJson) as contJugadores:
            jugadores = json.load(contJugadores)
            contador = 0
            for jugador in jugadores:
                contador = contador + 1
                print ("El jugador número {} es {}".format(contador, jugador.get('username')))


    def mRegistrarJugador (self, nuevo):
        with open (self.usuariosJson, "w") as contJugadores:
            json.dump(self.mAgregar(nuevo), contJugadores, indent=4)
    

    def mAgregar(self, nuevo):
        with open (self.usuariosJson) as contJugadores:
            jugadores = json.load(contJugadores)
            jugadores.append(nuevo)
        with open (self.usuariosJson, "w") as contJugadores:
            json.dump(jugadores, contJugadores, indent=4)
        self.obj_VistaMenu.mCreado()
        return True


    def mVerificarExitencia(self, nuevo):

        nuevoRegistro = nuevo['username']

        with open (self.usuariosJson) as contJugadores:
            jugadores = json.load(contJugadores)

            for jugador in jugadores:
                if(nuevoRegistro == jugador.get('username')):
                    self.banderaExistencia = True 
                    break
                else:
                    self.banderaExistencia = False
            
            if(self.banderaExistencia):
                self.obj_VistaMenu.mExiste()
                return False
            else:
                if(self.mAgregar(nuevo)):
                    return True


    def mVerificarFormatos(self, nuevo, caso):

        if(caso == "usuario"):
            nuevoRegistro = nuevo['username']
            nuevoRegistro = nuevoRegistro.replace(' ','')
            nuevo['username'] = nuevoRegistro
            if(self.mVerificarExitencia(nuevo)):
                return True
            else:
                return False

        if (caso == "pass"):

            nuevoRegistro = nuevo['password']
            nuevoRegistro = nuevoRegistro.replace(' ','')
            nuevo['password'] = nuevoRegistro

            contador = Counter(nuevoRegistro)
            Repeticiones = len([tupla[1] for tupla in list(contador.items()) if tupla[1]>1])

            if(len(nuevoRegistro) >= 8):
                if(Repeticiones == 0):

                    self.bandNumeros = None
                    self.banderaCaract = None
                    for item in nuevoRegistro:

                        try:
                            if(float(item)):
                                self.bandNumeros = True
                        except:
                            self.banderaCaract = True
                            
                    if((self.bandNumeros == True) and (self.banderaCaract == True)):
                        print("Contraseña admitida: {}".format(nuevoRegistro))
                        return True
                    else:
                        print("Contraseña NO admitida, debe contener letras y numeros: {}".format(nuevoRegistro))
                        return False
                else:
                    
                    print("Contraseña NO admitida, no puede repetir caracteres: {}".format(nuevoRegistro))
                    return False
            else:
                print("Contraseña NO admitida, debe contener mínimo 8 caracteres: {}".format(nuevoRegistro))
                return False
            
        if(caso == "correo"):
            nuevoRegistro = nuevo.lower()
            nuevoRegistro = nuevoRegistro.replace(' ','')

            nuevo = nuevoRegistro

            if "@" in nuevo:
                print("")
                print("Correo admitido: {}".format(nuevo))
                return True
            else:
                print("")
                print("Correo NO admitido, es necesario ingresar '@': {}".format(nuevo))
                return False

    
    def mVerificarLogin(self, usuario, contrasena):

        with open (self.usuariosJson) as contJugadores:
            jugadores = json.load(contJugadores)

            for jugador in jugadores:
                if(usuario == jugador.get('username')):
                    self.banderaExistencia = True 
                    break
                else:
                    self.banderaExistencia = False
            
            if(self.banderaExistencia):
                
                self.banderaExistencia = None
                for jugador in jugadores:

                    if(usuario == jugador.get('username') and contrasena== jugador.get('password')):
                        self.banderaExistencia = True 
                        break
                    else:
                        self.banderaExistencia = False

                if(self.banderaExistencia):
                    self.obj_VistaMenu.mLoginCorrecto()
                    return True
                else:
                    self.obj_VistaMenu.mLoginIncorrecto()
                    return False
            else:
                self.obj_VistaMenu.mNoExiste()
                return False