#Importamos el módulo datetime de la librería estándar para trabajar con fechas y horas.

import datetime

#La clase mensaje representa un correo electrónico con su remitente, asunto, cuerpo, fecha y estado de lectura.
class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        #  Inicializa una nueva instancia de Mensaje.
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._fecha = datetime.datetime.now()
        self._leido = False

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

   --- ENTREGA 2 ---
       --- CLASE USUARIO (MODIFICADA PARA EL ÁRBOL) ---
       class Carpeta:
    def __init__(self, nombre, padre=None):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas: list['Carpeta'] = [] # Lista de nodos hijos
        self._padre: 'Carpeta' | None = padre
    
    # Métodos de Gestión de Jerarquía
    def agregar_subcarpeta(self, nombre_subcarpeta):
        """Agrega una nueva subcarpeta a la lista de hijos."""
        nueva_carpeta = Carpeta(nombre_subcarpeta, padre=self)
        self._subcarpetas.append(nueva_carpeta)
        return nueva_carpeta

    def buscar_carpeta_recursivo(self, nombre_buscado: str) -> 'Carpeta' | None:
        """Busca una carpeta por nombre en la jerarquía (Pre-orden)."""
        if self._nombre == nombre_buscado:
            return self
        
        for sub in self._subcarpetas:
            resultado = sub.buscar_carpeta_recursivo(nombre_buscado)
            if resultado:
                return resultado
        return None

    # Método de Mover Mensajes (Implica búsqueda y modificación)
    def mover_mensaje(self, mensaje: Mensaje, destino: 'Carpeta') -> bool:
        """Mueve un mensaje de esta carpeta a una carpeta destino."""
        if self.eliminar_mensaje(mensaje):
            destino.agregar_mensaje(mensaje)
            return True
        return False # El mensaje no estaba en esta carpeta

    # Búsqueda Recursiva de Mensajes
    def buscar_mensajes_recursivo(self, criterio: str, valor: str) -> list[Mensaje]:
        """
        Busca mensajes en esta carpeta y sus subcarpetas por Asunto o Remitente.
        Retorna la lista de Mensajes encontrados (DFS/Pre-orden).
        """
        mensajes_encontrados = []
        
        # 1. Buscar en la carpeta actual
        for msg in self._mensajes:
            cumple_criterio = False
            if criterio.lower() == "asunto" and valor.lower() in msg.asunto.lower():
                cumple_criterio = True
            elif criterio.lower() == "remitente" and valor.lower() in msg.remitente.lower():
                cumple_criterio = True
            
            if cumple_criterio:
                mensajes_encontrados.append(msg)
                
        # 2. Buscar recursivamente en subcarpetas
        for sub in self._subcarpetas:
            mensajes_encontrados.extend(
                sub.buscar_mensajes_recursivo(criterio, valor)
            )
            
        return mensajes_encontrados
    
    # Métodos base
    def agregar_mensaje(self, mensaje: Mensaje):
        self._mensajes.append(mensaje)
        
    def eliminar_mensaje(self, mensaje: Mensaje):
        try:
            self._mensajes.remove(mensaje)
            return True
        except ValueError:
            return False

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
        return self._nombre

# --- CLASE USUARIO (MODIFICADA PARA EL ÁRBOL) ---
class Usuario: 
    def __init__(self, email, nombre, contrasena):
        self._email = email
        self._nombre = nombre
        self._contrasena = contrasena 
        # Bandeja de Entrada es la raíz del árbol de carpetas del usuario
        self._bandeja_entrada = Carpeta("Bandeja de Entrada") 
        self._bandeja_salida = Carpeta("Enviados")
        self._bandeja_entrada.agregar_subcarpeta("Importante")
        self._bandeja_entrada.agregar_subcarpeta("Trabajo")
        
        # Agregamos una subcarpeta anidada para la simulación
        self._bandeja_entrada.buscar_carpeta_recursivo("Trabajo").agregar_subcarpeta("Proyectos")
        
    # ... (Resto de métodos) ...
    # Requerimos un método para acceder a la raíz del árbol de carpetas.
    def get_bandeja_entrada(self):
        return self._bandeja_entrada
    
    # ... (Resto de métodos, ServidorCorreo, etc., se asume que funcionan igual) ...
    # El resto de las clases y el setup inicial del código del usuario se mantiene igual
    
    # --- SETUP INICIAL (Proporcionado por el usuario) ---
# ... (Clases Mensaje, Usuario, ServidorCorreo) ...

servidor = []
usuario1 = Usuario("ana@correo.com", "Ana García", "pass123") 
usuario2 = Usuario("juan@correo.com", "Juan Pérez", "pass456")
servidor.registrar_usuario(usuario1) 
servidor.registrar_usuario(usuario2)

# Ana envía 3 mensajes
usuario1.enviar_mensaje(servidor, "juan@correo.com", "Urgente: reunión de las 10am", "No te olvides de la reunión.")
usuario1.enviar_mensaje(servidor, "juan@correo.com", "Re: Proyecto X - Reporte", "Aquí está el informe final.")
usuario1.enviar_mensaje(servidor, "juan@correo.com", "Oferta especial de vacaciones", "No te pierdas este descuento.")

servidor.entregar_mensajes_pendientes()

# Juan tiene 3 mensajes en su Bandeja de Entrada
bandeja_juan = usuario2.get_bandeja_entrada()
mensajes_juan = bandeja_juan.listar_mensajes()
msg_trabajo = mensajes_juan[1] # "Re: Proyecto X - Reporte"
msg_spam = mensajes_juan[2] # "Oferta especial de vacaciones"

print("\n--- Estado Inicial de la Bandeja de Juan ---")
for i, msg in enumerate(mensajes_juan):
    print(f"[{i+1}] {msg.asunto}")
print(f"Subcarpetas: {[s.nombre for s in bandeja_juan.subcarpetas]}")
print("="*60)

# --- 1. Mover Mensaje (Usa búsqueda y eliminación) ---
print("1. MOVER MENSAJE")
carpeta_destino = bandeja_juan.buscar_carpeta_recursivo("Trabajo")

if carpeta_destino:
    # Mover el mensaje del Reporte de la Bandeja de Entrada a /Trabajo
    if bandeja_juan.mover_mensaje(msg_trabajo, carpeta_destino):
        print(f"Moviendo: '{msg_trabajo.asunto}'")
        print(f"  -> DE: Bandeja de Entrada ({len(bandeja_juan)} msgs)")
        print(f"  -> A: {carpeta_destino.nombre} ({len(carpeta_destino)} msgs)")
        
print("="*60)

# --- 2. Búsqueda Recursiva por Asunto ---
print("2. BÚSQUEDA RECURSIVA (Criterio: Asunto='Reunión')")
# Movemos un mensaje de la bandeja de entrada a una carpeta más profunda
carpeta_proyectos = bandeja_juan.buscar_carpeta_recursivo("Proyectos")
carpeta_proyectos.agregar_mensaje(msg_spam) # Agregamos el spam a /Trabajo/Proyectos

resultados_busqueda = bandeja_juan.buscar_mensajes_recursivo("asunto", "reunión")

print(f"  Resultados encontrados en la jerarquía: {len(resultados_busqueda)}")
for msg in resultados_busqueda:
    print(f"  [ENCONTRADO] Asunto: {msg.asunto}")

print("="*60)

# --- 3. Búsqueda Recursiva por Remitente ---
print("3. BÚSQUEDA RECURSIVA (Criterio: Remitente='ana')")
resultados_remitente = bandeja_juan.buscar_mensajes_recursivo("remitente", "ana@")

print(f"  Resultados encontrados en la jerarquía: {len(resultados_remitente)}")
for msg in resultados_remitente:
    print(f"  [ENCONTRADO] De: {msg.remitente}, Asunto: {msg.asunto}")

print("="*60)


    @property
    def fecha(self):
        return self._fecha

    @property
    def leido(self):
        return self._leido

    def __str__(self):
        return f"De: {self._remitente}\nAsunto: {self._asunto}\nFecha: {self._fecha.strftime('%Y-%m-%d %H:%M:%S')}"


class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)
        
    def eliminar_mensaje(self, mensaje):
        try:
            self._mensajes.remove(mensaje)
            return True
        except ValueError:
            return False

    def listar_mensajes(self):
        return self._mensajes

    @property
    def nombre(self):
        return self._nombre

    def __len__(self):
        return len(self._mensajes)


class Usuario:
    def __init__(self, email, nombre, contrasena):
        self._email = email
        self._nombre = nombre
        self._contrasena = contrasena # Idealmente, se usaría un hash para la contraseña
        self._bandeja_entrada = Carpeta("Bandeja de Entrada")
        self._bandeja_salida = Carpeta("Enviados")

    def enviar_mensaje(self, servidor, destinatario_email, asunto, cuerpo):
        if servidor.enviar_mensaje(self, destinatario_email, asunto, cuerpo):
            print(f"Mensaje enviado a {destinatario_email} correctamente.")
            return True
        else:
            print(f"Error: no se pudo enviar el mensaje a {destinatario_email}.")
            return False

    def recibir_mensaje(self, mensaje):
        self._bandeja_entrada.agregar_mensaje(mensaje)

    def listar_bandeja_entrada(self):
        return self._bandeja_entrada.listar_mensajes()
    
    def listar_bandeja_salida(self):
        return self._bandeja_salida.listar_mensajes()

    def get_bandeja_entrada(self):
        return self._bandeja_entrada

    def get_bandeja_salida(self):
        return self._bandeja_salida
        
    @property
    def email(self):
        return self._email

    def __str__(self):
        return f"Usuario: {self._nombre} <{self._email}>"


class ServidorCorreo:
    def __init__(self):
        self._usuarios = {}
        self._mensajes_pendientes = []

    def registrar_usuario(self, usuario):
        if usuario.email in self._usuarios:
            print(f"Error: El usuario {usuario.email} ya existe.")
            return False
        self._usuarios[usuario.email] = usuario
        print(f"Usuario {usuario.email} registrado con éxito.")
        return True

    def enviar_mensaje(self, remitente, destinatario_email, asunto, cuerpo):
        destinatario = self._usuarios.get(destinatario_email)
        if not destinatario:
            print(f"Error: Destinatario {destinatario_email} no encontrado.")
            return False

        mensaje = Mensaje(remitente.email, destinatario_email, asunto, cuerpo)
        self._mensajes_pendientes.append((destinatario, mensaje))
        remitente.get_bandeja_salida().agregar_mensaje(mensaje)
        return True

    def entregar_mensajes_pendientes(self):
        if not self._mensajes_pendientes:
            print("No hay mensajes pendientes para entregar.")
            return

        print(f"Entregando {len(self._mensajes_pendientes)} mensajes pendientes...")
        for destinatario, mensaje in self._mensajes_pendientes:
            destinatario.recibir_mensaje(mensaje)
        
        self._mensajes_pendientes = []
        print("Entrega de mensajes completada.")


# 1. Crear el servidor
servidor = ServidorCorreo()

# 2. Crear y registrar usuarios
usuario1 = Usuario("ana@correo.com", "Ana García", "pass123")
usuario2 = Usuario("juan@correo.com", "Juan Pérez", "pass456")

servidor.registrar_usuario(usuario1)
servidor.registrar_usuario(usuario2)

# 3. Ana envía un mensaje a Juan
usuario1.enviar_mensaje(servidor, "juan@correo.com", "Hola, Juan", "Este es mi primer correo en el nuevo sistema.")

# 4. El servidor entrega los mensajes
servidor.entregar_mensajes_pendientes()

# 5. Juan revisa su bandeja de entrada
mensajes_juan = usuario2.listar_bandeja_entrada()
print("\n--- Mensajes en la bandeja de entrada de Juan ---")
for msg in mensajes_juan:
    print(msg)

# 6. Ana revisa su bandeja de salida
mensajes_ana = usuario1.listar_bandeja_salida()
print("\n--- Mensajes en la bandeja de enviados de Ana ---")
for msg in mensajes_ana:
        print(msg)
