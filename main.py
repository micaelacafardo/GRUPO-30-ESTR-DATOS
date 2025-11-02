from usuario import Usuario
from servidor import ServidorCorreo
from red_servidores import RedServidores

# Simulación
servidor = ServidorCorreo("Servidor-A")
ana = Usuario("ana@correo.com", "Ana")
juan = Usuario("juan@correo.com", "Juan")

servidor.registrar_usuario(ana)
servidor.registrar_usuario(juan)

# Crear filtros y carpetas
finanzas = juan.get_bandeja_entrada().agregar_subcarpeta("Finanzas")
juan.definir_filtro("Factura", finanzas)

# Enviar mensajes
servidor.enviar_mensaje(ana, "juan@correo.com", "Factura de luz", "Monto $12000", prioridad=0)
servidor.enviar_mensaje(ana, "juan@correo.com", "Reunión urgente", "Nos vemos a las 10", prioridad=1)

# Procesar mensajes urgentes
juan.procesar_urgentes()

# Red de servidores
red = RedServidores()
for s in ["A", "B", "C", "D"]:
    red.agregar_servidor(s)
red.conectar("A", "B")
red.conectar("B", "C")
red.conectar("C", "D")

camino = red.bfs("A", "D")
print("\nRuta entre servidores:", " -> ".join(camino))