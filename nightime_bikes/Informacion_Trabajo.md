1. Detalles de las entidades

*Perfiles (clientes, empleados, admins)
-usuario (nombre del usuario)
-rol (por defecta sera empleado cuando se cree nueva cuenta, normalmente a los empleados o admins se les da una cuenta)
-cedula
-telefono
-direccion (para perfil cliente)
-estado (activo, descanso, deshabilitado. Esta parte es para empleados y admins)

*productos
-nombre_p
-descripcion
-precio
-imagen
-id_categoría
-stock
-estado_p

*categoría
-nombre_categoria

*horarios
-nombre_h
-tiempo

*pedidos (esta seria la informacion de la factura)
-id_usuario
-fecha_pedido
-total_pagado
-estado_pedido (pendiente, pagado, enviado)

*detalles_pedido (los productos que contiene la factura)
-id_pedido (a que factura estan relacionados los productos)
-id_productos (que productos compro)
-cantidad
-precio_unitario

______________________________________________________________________________

2. Detalles de las aplicaciones 

*catalog

-Manejo de productos
-Estructura modelos de biciclteas y accesorios
-información de modelos de productos

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
    -Cada usuario tiene un carrito 1=1. cada carrito puede almacenar varios productos y mas de un solo producto puede ir varias veces a un carrito

*Pedidos y detalles. 
    -1=muchos. Un usuario puede tener mcuhos pedidos, un pedido tiene muchos productos

______________________________________________________________________________

partes a trabajar cada miembro:

*Abraham:

-staff 
-catalog para las vistas de crear/editar productos
-Diagramas corregido (tomando como ejemplo los ya hechos en anteriores semestres y los que estan en el documento)

*Juan:

-catalog. Toda la parte de los productos
-cart. Toda la sesion del carrito 

*app compartida

-accounts. 
    -Juan: modelo perfil 
    -Abraham: vistas para que el admin vea los empleados usando el mismo modelo

______________________________________________________________________________

Librerias a utilizar

Nota importante, al abrir el repositorio y en la consola estar en el venv e ingresar el siguiente comando:
python -m pip install -r requirements.txt
Se instalara todo lo necesario, en caso de que algo no funcione y ponga un texto que diga algo similar a "no se a detactado django, sql, etc" hacer el install correspondiente

python -m pip install
    -django
    -mysqlclient
    -python-dotenv
    -Pillow (imagenes)

______________________________________________________________________________