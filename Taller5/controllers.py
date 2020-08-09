from Vistas import vistasMenu
from collections import Counter
import json

class Controller:

    obj_VistaMenu = vistasMenu() #En todos los metodos se hacen llamados a las vistas según corresponda

    def __init__(self):
        self.usuariosJson = 'Taller5/existing_users.json'
        self.registrationJson = 'Taller5/registration.json'
        self.loginJson = 'Taller5/login.json'
        self.banderaExistencia = None
        self.bandNumeros = None
        self.banderaCaract = None


    def mCargarJugadores(self):
        with open (self.usuariosJson) as contJugadores: #Abre el json y guarda los datos en un contenedor
            jugadores = json.load(contJugadores)        #Luego los recorre en un for para obtener los datos
            contador = 0                                # con un 'get'
            for jugador in jugadores:
                contador = contador + 1
                print ("El jugador número {} es {}".format(contador, jugador.get('username')))


    def mRegistrarJugador (self, nuevo):
        with open (self.usuariosJson, "w") as contJugadores:            #Se abre el json para poder sobreecribir
            json.dump(self.mAgregar(nuevo), contJugadores, indent=4)    #los datos de el nuevo registro
    

    def mAgregar(self, nuevo):
        with open (self.usuariosJson) as contJugadores: #Se abre el json y se extraen los datos
            jugadores = json.load(contJugadores)        #luego de agregamos el valor nuevo con un 'append'
            jugadores.append(nuevo)
        with open (self.usuariosJson, "w") as contJugadores: 
            json.dump(jugadores, contJugadores, indent=4)
        self.obj_VistaMenu.mCreado()
        return True


    def mVerificarExitencia(self, nuevo):   

        nuevoRegistro = nuevo['username']                   #Se abre el json y se extraen datos

        with open (self.usuariosJson) as contJugadores:
            jugadores = json.load(contJugadores)

            for jugador in jugadores:
                if(nuevoRegistro == jugador.get('username')):   #Hacemos un for para recorrer todos los jugadores
                    self.banderaExistencia = True               # de el json y buscando la similitud con el dato
                    break                                       #dependiendo del resultado devuelve (True/False)
                else:
                    self.banderaExistencia = False
            
            if(self.banderaExistencia):
                self.obj_VistaMenu.mExiste()
                return False
            else:
                if(self.mAgregar(nuevo)):
                    return True


    def mVerificarFormatos(self, nuevo, caso):  #Este metodo funciona por parametros, dependiendo del valor de caso
                                                #que reciba va a ser el proceso que ejecute
        
        if(caso == "usuario"):                              #1. Caso usuario, se eliminan espacios
            nuevoRegistro = nuevo['username']
            nuevoRegistro = nuevoRegistro.replace(' ','')
            nuevo['username'] = nuevoRegistro
            if(self.mVerificarExitencia(nuevo)):            #Se llama al metodo que verifica existencia
                return True                                 #dependiendo del resultado devuelve (True/False)
            else:
                return False

        if (caso == "pass"):                                #2. Caso pass, se eliminan espacios

            nuevoRegistro = nuevo['password']
            nuevoRegistro = nuevoRegistro.replace(' ','')
            nuevo['password'] = nuevoRegistro

            contador = Counter(nuevoRegistro)               #Implementamos un algoritmo para contar las repeticiones
            Repeticiones = len([tupla[1] for tupla in list(contador.items()) if tupla[1]>1])

            if(len(nuevoRegistro) >= 8):                    #Verificamos que sea de almenos 8 caracteres
                if(Repeticiones == 0):                      #Verificamos que las repeticiones sean 0

                    self.bandNumeros = None
                    self.banderaCaract = None
                    for item in nuevoRegistro:

                        try:                                #Se implementa algoritmo que nos indique que existen 
                            if(float(item)):                #números y tambien letras
                                self.bandNumeros = True
                        except:
                            self.banderaCaract = True
                            
                    if((self.bandNumeros == True) and (self.banderaCaract == True)):
                        print("Contraseña admitida: {}".format(nuevoRegistro))
                        return True                         #dependiendo del resultado devuelve (True/False)
                    else:
                        print("Contraseña NO admitida, debe contener letras y numeros: {}".format(nuevoRegistro))
                        return False
                else:
                    
                    print("Contraseña NO admitida, no puede repetir caracteres: {}".format(nuevoRegistro))
                    return False
            else:
                print("Contraseña NO admitida, debe contener mínimo 8 caracteres: {}".format(nuevoRegistro))
                return False
            
        if(caso == "correo"):                               #3. Caso correo, se eliminan espacios y mayusculas
            nuevoRegistro = nuevo.lower()                   
            nuevoRegistro = nuevoRegistro.replace(' ','')

            nuevo = nuevoRegistro

            if "@" in nuevo:                    #Se verifica que contenga el @
                print("")
                print("Correo admitido: {}".format(nuevo))   #dependiendo del resultado devuelve (True/False)
                return True
            else:
                print("")
                print("Correo NO admitido, es necesario ingresar '@': {}".format(nuevo))
                return False

    
    def mVerificarLogin(self, usuario, contrasena):

        with open (self.usuariosJson) as contJugadores: #Primero traemos los datos del json
            jugadores = json.load(contJugadores)

            for jugador in jugadores:                   #Los recorremos buscando que el usuario exista dentro del
                if(usuario == jugador.get('username')): #registro
                    self.banderaExistencia = True 
                    break
                else:
                    self.banderaExistencia = False
            
            if(self.banderaExistencia):                 #Basandonos en esa previa revision seguimos a la contraseña
                
                self.banderaExistencia = None           #Realizamos la misma logica pero ahora no solo vamos a buscar
                for jugador in jugadores:               #Que exista el usuario si no que la contraseña sea la misma
                                                        #De esta forma verifiamos la credencial
                    if(usuario == jugador.get('username') and contrasena== jugador.get('password')):
                        self.banderaExistencia = True 
                        break
                    else:
                        self.banderaExistencia = False  #dependiendo del resultado devuelve (True/False)

                if(self.banderaExistencia):
                    self.obj_VistaMenu.mLoginCorrecto()
                    return True
                else:
                    self.obj_VistaMenu.mLoginIncorrecto()
                    return False
            else:
                self.obj_VistaMenu.mNoExiste()
                return False