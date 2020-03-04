class Naves():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Plateado"
    motores = 4
    activada = False
    compuerta_principal = False
    sistema_defensa = True
    autodestruccion = False

    def encender(self):
        self.activada = True

    def apagar(self):
        self.activada = False

    def abrir_compuerta(self):
        self.compuerta_principal = True

    def cerrar_compuerta(self):
        self.compuerta_principal = False

    def desactivar_defensas(self):
        self.sistema_defensa = False

    def activar_defensas(self):
        self.sistema_defensa = True

    def activar_autodestrucion(self):
        self.autodestruccion = True
        mensaje = "Protocolo de autodestrucción activado..."
        print(mensaje)

    def estado_motores(self):
        if (self.activada):
            return "Motores trabajando al 100%."
        else:
            return "Motores apagados."

    def estado_compuerta(self):
        if (self.compuerta_principal):
            return "La compuerta está abierta."
        else:
            return "La compuerta está cerrada."

    def estado_defensa(self):
        if (self.sistema_defensa):            
            return "El sistema de defensa está activado."
        else:
            return "¡Peligro! El sistema de defensa está desactivado."
    
#Se crea el objeto nave1 perteneciente a la clase Naves.
    
nave1=Naves()

print("\n\n\n\n")































print(nave1.estado_compuerta())











print("\n\n\n\n")