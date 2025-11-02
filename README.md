Título del Trabajo: Cliente de Correo Electrónico (Email Client)

Grupo: 30

Integrantes: Daniela Gonzalez, Micaela Cafardo.

Fecha de Entrega: 20/9/25, 00:00hs (primera entrega)
                  11/10/25 22:50 (segunda entrega)
                  1/11/25 00:00 (tercera entrega)

Enlace al Repositorio de GitHub: (https://github.com/micaelacafardo/GRUPO-30-ESTR-DATOS)

Entrega 1: Modelado de Clases y Encapsulamiento

1. Introducción
   
El presente documento detalla el diseño y la implementación inicial de un sistema de cliente de correo electrónico, desarrollado en Python utilizando POO. Esta primera entrega se centra en el modelado de las clases fundamentales del sistema (Usuario, Mensaje, Carpeta, ServidorCorreo), asegurando el encapsulamiento de sus atributos y la implementación de interfaces básicas para la gestión de mensajes.

2. Diagrama de Clases (UML)
A continuación, se presenta un diagrama de clases UML que ilustra la estructura de las clases principales, sus atributos, métodos y las relaciones entre ellas.

[diagrama de clases UML que ilustra la estructura de las clases principales](DiagramaUML.png)

3. Justificación de Decisiones de Diseño
En esta sección, se explican las principales decisiones tomadas durante el modelado de las clases y la implementación del encapsulamiento, así como el uso de estructuras de datos específicas.


3. a. Clases Principales y su Responsabilidad

Usuario:
Responsabilidad: Representa a un usuario del sistema de correo electrónico. Es responsable de gestionar sus propias bandejas de entrada y salida, así como de iniciar el envío de mensajes.
Justificación: Centraliza toda la información y operaciones relativas a un individuo que interactúa con el cliente de correo.

Mensaje:
Responsabilidad: Modela la unidad básica de comunicación: un correo electrónico. Contiene toda la información relevante de un mensaje (remitente, asunto, cuerpo, fecha, estado).
Justificación: Permite encapsular la información del mensaje de manera coherente, facilitando su manejo, almacenamiento y visualización.

Carpeta:
Responsabilidad: Contiene y organiza una colección de objetos Mensaje. Provee métodos para agregar, eliminar y listar mensajes.
Justificación: Abstrae el concepto de una colección de correos, lo que es fundamental en un cliente de email (bandeja de entrada, enviados, borradores, etc.).

ServidorCorreo:
Responsabilidad: Actúa como el intermediario central para el registro de usuarios y la gestión del flujo de mensajes entre ellos. Simula la funcionalidad de un servidor real, encargándose de la entrega de mensajes.
Justificación: Desacopla la lógica de envío y recepción directa entre usuarios, centralizando el enrutamiento y la administración de usuarios, similar a cómo funciona un sistema de correo real.


3.b. Encapsulamiento y Propiedades


Uso de Atributos Privados (_atributo):
Decisión: Todos los atributos de las clases (ej. _remitente en Mensaje, _mensajes en Carpeta, _usuarios en ServidorCorreo) se han definido como privados (precedidos por un guion bajo).
Justificación: Esto refuerza el principio de encapsulamiento, impidiendo el acceso y la modificación directa de los datos internos desde fuera de la clase. Protege la integridad del estado del objeto y permite que la lógica interna de la clase gestione sus propios datos.


Uso de Propiedades (@property):
Decisión: Se han implementado propiedades de solo lectura para acceder a los atributos privados cuando se necesita exponerlos, pero sin permitir su modificación directa (ej. remitente, asunto en Mensaje, email en Usuario).
Justificación: Las propiedades ofrecen una interfaz pública "getter" que parece un atributo, pero bajo el capó permite controlar el acceso, validar datos o realizar operaciones adicionales si fuera necesario en el futuro, manteniendo la simplicidad para el usuario de la clase.


3.c. Implementación de Interfaces (Métodos de Acceso y Mutación)


Métodos para Enviar/Recibir/Listar Mensajes:
Decisión: Cada clase que interactúa con mensajes (Usuario, Carpeta, ServidorCorreo) expone métodos públicos específicos para estas operaciones (ej. enviar_mensaje, recibir_mensaje, listar_mensajes).
Justificación: Estos métodos definen la "interfaz" de las clases, es decir, cómo otras partes del sistema pueden interactuar con ellas para realizar las operaciones fundamentales de un cliente de correo. Están diseñados para ser intuitivos y reflejar las acciones del mundo real.


__str__ y __len__:
Decisión: Se han implementado los métodos  __str__ (para Mensaje y Usuario) y __len__ (para Carpeta).
Justificación: __str__ proporciona una representación de cadena legible y útil para la depuración o visualización del objeto. __len__ permite que la función len() se use de forma natural con objetos Carpeta, devolviendo la cantidad de mensajes que contiene, lo que mejora la usabilidad y la adherencia a las convenciones de Python.


3.d. Estructuras de Datos Utilizadas

list para _mensajes en Carpeta:
Justificación: Una lista es una estructura simple y eficiente para almacenar colecciones ordenadas de objetos, adecuada para representar los mensajes en una carpeta. Permite iteración, adición (append) y eliminación (remove) fácilmente.


dict para _usuarios en ServidorCorreo:
Justificación: Un diccionario (dict) mapea direcciones de correo electrónico (str) a objetos Usuario. Esto permite una búsqueda y acceso muy rápido a los usuarios por su email.


list de tuplas para _mensajes_pendientes en ServidorCorreo:
Justificación: Una lista de tuplas (destinatario, mensaje) es una forma de mantener un registro de los mensajes que esperan ser entregados.


4. Conclusión
El diseño presentado en esta primera entrega sienta una base sólida para el desarrollo completo del cliente de correo electrónico. El uso del encapsulamiento, las propiedades y una clara definición de responsabilidades para cada clase aseguran un código mantenible y extensible, preparando el terreno para las funcionalidades futuras.




Entrega 2: Estructuras de Datos y Recursividad

1. Introducción

En esta segunda entrega del sistema de cliente de correo electrónico, se implementó una estructura jerárquica de carpetas (carpetas y subcarpetas) como árbol general, y se habilitaron operaciones recursivas para mover mensajes entre carpetas y hacer búsquedas profundas. El propósito es demostrar el uso de recursividad y estructuras de datos jerárquicas en un contexto práctico.

2. Funcionalidades implementadas

a. Árbol de carpetas

La clase Carpeta representa un nodo del árbol que puede contener mensajes y varias subcarpetas (hijos). Se implementaron los siguientes métodos clave:

agregar_subcarpeta(nombre_subcarpeta): crea una nueva subcarpeta dentro de la carpeta actual.

buscar_carpeta_recursivo(nombre_buscado): recorre todo el árbol de carpetas (la carpeta actual y sus descendientes) para encontrar una carpeta con el nombre dado.

mover_mensaje(mensaje, carpeta_destino): permite mover un mensaje de cualquier nivel de la jerarquía a una carpeta de destino, explorando recursivamente para localizar el mensaje.

buscar_mensajes_recursivo(criterio, valor): busca mensajes en todas las carpetas de la jerarquía (criterio “asunto” o “remitente”), devolviendo los mensajes que coincidan.

b. Uso de recursividad

El recorrido del árbol de carpetas se implementa mediante llamadas recursivas para explorar todas las subcarpetas. Esto permite que la funcionalidad no quede limitada sólo al primer nivel de carpetas, sino que abarque profundidades arbitrarias.


3. Análisis de eficiencia 

la recursión implica una pila de llamadas que puede crecer proporcional al nivel de profundidad del árbol 
Conclusión de eficiencia: Las operaciones recursivas permiten cubrir toda la jerarquía de carpetas correctamente, pero presentan complejidad lineal en relación al número de carpetas o mensajes en el peor caso. Esto es aceptable para un sistema de cliente de correo de tamaño moderado. 

4. Casos límite considerados

Si se busca una carpeta que no existe, buscar_carpeta_recursivo devuelve None y el sistema lo maneja sin excepción.

Si se intenta mover un mensaje que no está presente en ninguna carpeta, mover_mensaje devuelve False, y no ocurre eliminación ni corrupción de datos.

Si se realiza una búsqueda (buscar_mensajes_recursivo) y no encuentra coincidencias, devuelve una lista vacía.

En estructuras de carpetas muy profundas, la recursión podría alcanzar gran profundidad.

5. Infografía 

Como material adicional, se ha elaborado una infografía que ilustra el árbol de carpetas (nodos, subcarpetas, carpetas raíz) y el flujo de una búsqueda/movimiento recursivo de un mensaje:

[Infografía](infografía.png)

6. Conclusión

La Entrega 2 cumple con los requisitos de manejar estructuras de datos jerárquicas (árbol de carpetas) y ejecutar operaciones recursivas fundamentales (mover y buscar mensajes). 




Entrega 3: Algoritmos y Funcionalidades Avanzadas


1. Introducción

En esta tercera entrega se amplía la funcionalidad del cliente de correo electrónico mediante la incorporación de estructuras de datos y algoritmos avanzados.
El objetivo es mejorar la organización, automatización y simulación de la red de correo, aplicando listas, diccionarios, colas de prioridad y grafos, junto con técnicas de recursividad y búsqueda.

2. Funcionalidades implementadas
a. Filtros automáticos (Listas y Diccionarios)

Los filtros permiten que el usuario organice sus mensajes entrantes de forma automática según reglas definidas.
Cada filtro asocia una palabra clave con una carpeta destino.

Ejemplo:

self._filtros = {"Factura": carpeta_finanzas, "Trabajo": carpeta_proyectos}


Cuando llega un mensaje, el sistema busca si el asunto contiene alguna de las palabras clave. Si la encuentra, el mensaje se mueve automáticamente a la carpeta asignada.

Estructura usada: Diccionario
Complejidad: O(f), donde f es la cantidad de filtros definidos.

b. Cola de prioridad (Heapq)

Para gestionar mensajes urgentes, se implementó una cola de prioridad utilizando el módulo heapq de Python.
Cada mensaje incluye un atributo prioridad, donde 1 representa mensajes urgentes.
Esto permite procesar primero los mensajes más importantes con eficiencia logarítmica.

Estructura usada: Heap (cola de prioridad)
Complejidad: Inserción y extracción O(log n)

c. Red de servidores de correo (Grafo + BFS)

La red de servidores se modela como un grafo no dirigido, donde cada servidor es un nodo y las conexiones entre ellos son aristas.

Para simular el envío de mensajes entre servidores, se implementa el algoritmo BFS, que encuentra la ruta más corta entre el servidor de origen y el de destino.


d. Recursividad en carpetas

Se mantuvo e integró la estructura de árbol general desarrollada en la entrega 2.
La recursividad se utiliza para:

Buscar mensajes (buscar_mensajes_recursivo)

Mover mensajes (mover_mensaje)

Localizar carpetas (buscar_carpeta_recursivo)

Estos métodos recorren el árbol completo sin importar la profundidad, implementando un recorrido en profundidad 

Complejidad: O(n), donde n es el número total de carpetas o mensajes explorados.

3. Análisis de eficiencia

El sistema combina distintas estructuras (diccionarios, heaps, grafos y árboles) para lograr un funcionamiento ágil y ordenado.
Todas las operaciones tienen tiempos de ejecución lineales o logarítmicos, lo que asegura buen rendimiento y escalabilidad para el tamaño del proyecto.

4. Casos límite considerados

Situaciones y sus comportamientos esperados:

Carpeta destino inexistente->	El método devuelve None sin error.
Mensaje no encontrado->	El método mover_mensaje retorna False.
Cola de prioridad vacía-> No se lanza excepción; no se procesan mensajes.
Envío entre servidores no conectados -> BFS devuelve None.
Filtro sin coincidencia-> El mensaje se mantiene en la bandeja de entrada.

5. Síntesis explicando los algoritmos aplicados:

Diccionarios: organización y acceso directo a filtros.
Heap (cola de prioridad): obtención eficiente del mensaje más urgente.
BFS en grafos: simulación del envío entre servidores con la ruta más corta.
Recursividad en árboles: búsqueda y movimiento en profundidad de mensajes.

6. Conclusión

La Entrega 3 cumple con los requisitos de aplicar estructuras y algoritmos avanzados:
Filtros automáticos (diccionarios y listas).
Cola de prioridad (heapq).
Red de servidores modelada como grafo (BFS).
Recursividad consolidada en el manejo de carpetas.

Estas implementaciones mejoran la eficiencia, automatización y escalabilidad del cliente de correo, integrando conceptos de POO y Estructuras de Datos.
