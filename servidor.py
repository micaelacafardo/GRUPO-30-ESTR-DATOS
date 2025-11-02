from mensaje import Mensaje

class ServidorCorreo:
    """Administra usuarios y flujo de mensajes."""

    def __init__(self, nombre):
        self._nombre = nombre
        self._usuarios = {}

    def registrar_usuario(self, usuario):
        if usuario.email in self._usuarios:
            print(f"Error: {usuario.email} ya registrado.")
            return False
        self._usuarios[usuario.email] = usuario
        print(f"Usuario {usuario.email} registrado en {self._nombre}.")
        return True

    def enviar_mensaje(self, remitente, destinatario_email, asunto, cuerpo, prioridad=0):
        destinatario = self._usuarios.get(destinatario_email)
        if not destinatario:
            print("Error: destinatario no encontrado.")
            return
        msg = Mensaje(remitente.email, destinatario_email, asunto, cuerpo, prioridad)
        destinatario.recibir_mensaje(msg)
        remitente.get_bandeja_salida().agregar_mensaje(msg)