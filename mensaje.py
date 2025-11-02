import datetime

class Mensaje:
    """Representa un correo electrónico."""

    def __init__(self, remitente, destinatario, asunto, cuerpo, prioridad=0):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._fecha = datetime.datetime.now()
        self._leido = False
        self._prioridad = prioridad  # 0 = normal, 1 = urgente

    def marcar_como_leido(self):
        self._leido = True

    @property
    def remitente(self):
        return self._remitente

    @property
    def asunto(self):
        return self._asunto

    @property
    def cuerpo(self):
        return self._cuerpo

    @property
    def prioridad(self):
        return self._prioridad

    def __str__(self):
        prioridad_txt = "URGENTE" if self._prioridad == 1 else "Normal"
        return f"[{prioridad_txt}] De: {self._remitente} | Asunto: {self._asunto} | Fecha: {self._fecha.strftime('%d/%m %H:%M')}"
