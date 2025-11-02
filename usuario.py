import heapq
from carpeta import Carpeta
from mensaje import Mensaje

class Usuario:
    """Representa un usuario del sistema de correo."""

    def __init__(self, email, nombre):
        self._email = email
        self._nombre = nombre
        self._bandeja_entrada = Carpeta("Bandeja de Entrada")
        self._bandeja_salida = Carpeta("Enviados")
        self._filtros = {}  # palabra -> carpeta destino
        self._cola_prioridad = []  # mensajes urgentes (heap)

    def definir_filtro(self, palabra, carpeta_destino):
        self._filtros[palabra] = carpeta_destino

    def recibir_mensaje(self, mensaje):
        for palabra, carpeta in self._filtros.items():
            if palabra.lower() in mensaje.asunto.lower():
                carpeta.agregar_mensaje(mensaje)
                return
        if mensaje.prioridad == 1:
            heapq.heappush(self._cola_prioridad, (-mensaje.prioridad, mensaje))
        else:
            self._bandeja_entrada.agregar_mensaje(mensaje)

    def procesar_urgentes(self):
        while self._cola_prioridad:
            _, mensaje = heapq.heappop(self._cola_prioridad)
            print("Procesando urgente:", mensaje)

    def get_bandeja_entrada(self):
        return self._bandeja_entrada

    def get_bandeja_salida(self):
        return self._bandeja_salida

    @property
    def email(self):
        return self._email

    def __str__(self):
        return f"Usuario: {self._nombre} <{self._email}>"