from mensaje import Mensaje

class Carpeta:
    """Estructura recursiva tipo árbol para carpetas de correo."""

    def __init__(self, nombre, padre=None):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []
        self._padre = padre

    def agregar_subcarpeta(self, nombre_subcarpeta):
        nueva = Carpeta(nombre_subcarpeta, padre=self)
        self._subcarpetas.append(nueva)
        return nueva

    def buscar_carpeta_recursivo(self, nombre_buscado):
        if self._nombre == nombre_buscado:
            return self
        for sub in self._subcarpetas:
            resultado = sub.buscar_carpeta_recursivo(nombre_buscado)
            if resultado:
                return resultado
        return None

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):
        try:
            self._mensajes.remove(mensaje)
            return True
        except ValueError:
            return False

    def mover_mensaje(self, mensaje, carpeta_destino):
        if self.eliminar_mensaje(mensaje):
            carpeta_destino.agregar_mensaje(mensaje)
            return True
        for sub in self._subcarpetas:
            if sub.mover_mensaje(mensaje, carpeta_destino):
                return True
        return False

    def buscar_mensajes_recursivo(self, criterio, valor):
        resultados = []
        for m in self._mensajes:
            if criterio == "asunto" and valor.lower() in m.asunto.lower():
                resultados.append(m)
            elif criterio == "remitente" and valor.lower() in m.remitente.lower():
                resultados.append(m)
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensajes_recursivo(criterio, valor))
        return resultados

    def listar_mensajes(self):
        return self._mensajes

    @property
    def nombre(self):
        return self._nombre

    @property
    def subcarpetas(self):
        return self._subcarpetas

    def __len__(self):
        return len(self._mensajes)

    def __str__(self):
        return f"Carpeta: {self._nombre}"