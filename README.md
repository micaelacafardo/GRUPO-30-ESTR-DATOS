Título del Trabajo: Cliente de Correo Electrónico (Email Client)
Grupo: 30
Integrantes: Daniela Gonzalez, Micaela Cafardo.
Fecha de Entrega: 20/9/25, 00:00hs
Enlace al Repositorio de GitHub: https://github.com/DanielaMaiteGonzalez/TrabajoIntegradorparte1/tree/main

Entrega 1: Modelado de Clases y Encapsulamiento

1. Introducción
El presente documento detalla el diseño y la implementación inicial de un sistema de cliente de correo electrónico, desarrollado en Python utilizando POO. Esta primera entrega se centra en el modelado de las clases fundamentales del sistema (Usuario, Mensaje, Carpeta, ServidorCorreo), asegurando el encapsulamiento de sus atributos y la implementación de interfaces básicas para la gestión de mensajes.

2. Diagrama de Clases (UML)
A continuación, se presenta un diagrama de clases UML que ilustra la estructura de las clases principales, sus atributos, métodos y las relaciones entre ellas.

[presenta un diagrama de clases UML que ilustra la estructura de las clases principales](imagen.png)

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