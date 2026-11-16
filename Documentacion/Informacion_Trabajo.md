1. Detalles de las entidades

*Perfiles (clientes, admins, empleado)
-usuario (nombre del usuario)
-rol (por defecto sera cliente cuando se cree nueva cuenta, normalmente a los empleados o admins se les da una cuenta)
-cedula
-telefono
-direccion (para perfil cliente)
-estado (activo, descanso, deshabilitado. Esta parte es para empleados y admins)
-horario (para empleados)

*productos
-nombre_p
-descripcion
-precio
-imagen
-id_categoría
-stock
-estado

*categoría
-nombre_categoria
-Descripcion

*horarios
-nombre_h
-tiempo_inicio
-tiempo_fin

*Carrito 
-id_usuario
-fecha_pedido
-total_pagado
-estado_pedido (pendiente, pagado, enviado)

*item_carrito (los productos que contiene la factura)
-id_carrito 
-id_productos (que productos compro)
-cantidad
-precio_unitario

______________________________________________________________________________

2. Detalles de las aplicaciones 

*catalog

-Manejo de productos
-Estructura modelos de los productos (bicis, accesorios, indumentaria)
-información de modelos de productos
-Templates para mostrar los productos (todo perfil) y gestionarlos (solo administracion)

*accounts

-Manejo de cuentas de usuario (registro, ingreso y salida)
-Maneja Información de los clientes, empleados y admins  por medio de *Perfil

*cart

-Dedicada al uso del carrito de la cuenta de clientes
-relación entre los productos y el cliente
-en esta app se guarda la informacion temporal pre factura

*staff

-Gestion del personal para la parte administrativa
-parte lógica de recursos humanos
-Funciona para administrar al completo los empleados

______________________________________________________________________________

3. Detalle de los modelos 

*usuarios y perfil 
    -relación 1=1

*productos y categoría 
    -relación 1=muchos, una categoría puede tener varios productos. Un producto puede estar en una categoría a la vez

*Carrito, ítems y usuario. 
    -Cada usuario tiene un carrito al tiempo 1=1. cada carrito puede almacenar varios productos y mas de un solo producto puede ir varias veces a un carrito

*facturas y detalles. 
    -1=muchos. Un usuario puede tener muchos facturas, una factura puede tener muchos productos

______________________________________________________________________________

partes a trabajar cada miembro:

*Abraham:

-staff para la gestion de los empleados
-catalog para la gestion de productos
-Diagramas corregido (tomando como ejemplo los ya hechos en anteriores semestres y los que estan en el documento)

*Juan:

-catalog. Toda la parte de los productos
-cart. Toda la sesion del carrito 
-Proceso Debug
-Proceso de diseño

*app compartida

-accounts. 
    -Juan: modelo perfil y manejo de alertas
    -Abraham: modelado para que la parte administrativa pueda gestionar los elementos necesarios 

______________________________________________________________________________

Librerias a utilizar

Nota importante, al abrir el repositorio y en la consola estar en el venv e ingresar el siguiente comando:
python -m pip install -r requirements.txt
Se instalara todo lo necesario, en caso de que algo no funcione y ponga un texto que diga algo similar a "no se a detactado django, sql, etc" hacer el install correspondiente

python -m pip install
    (informacion del requirements)
    asgiref==3.13.0
    Django==6.1.2
    mysqlclient==2.3.0
    pillow==13.0.0
    python-dotenv==1.2.4
    sqlparse==0.6.0
    tzdata==2026.6

______________________________________________________________________________