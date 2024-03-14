# **Tercera Pre-Entrega del Proyecto Final - Coderhouse**
## Alumno: Franco Cazal

superuser: Franco
contraseña: hola123

# Objetivo

- Simular un sistema de almacenamiento de datos interno de una clínica veterinaria

# Modelos Usados (atributos): 
- Doctor: nombre, apellido, nro_registro
- Funcionario: nombre, apellido, funcion, sueldo
- Cliente: nombre, apellido, nro_documento
- Mascota: nombre, especie, raza

# **Indicaciones Generales:**

## **Nombre del proyecto:** 'tercerapreentrega'

## **Nombre de la aplicación:** 'aplicacion'

## **Tema de la aplicación:** Sistema administrativo para una clínica veterinaria.

# **Funcionamiento de la aplicación:**

### Al levantar el alojamiento de la página, la principal es 'home' (url vacío), la cual ofrece una visualización general de información sobre la misma.

### La página cuenta con una barra de navegación mediante la cual, por medio de botones ubicados en la zona superior derecha de la misma, se puede acceder a las distintas funcionalidades que ofrece la aplicación.

### Cada botón da acceso a la visualización de una página, inicialmente para realizar una busqueda en la base de datos se tiene el ícono de la lupa, seguidamente se tienen los demás botones que redirigen a páginas que contienen una lista de datos según los modelos estableci0os pertinentes al tema escogido, los cuales son: Doctor, Funcionario, Cliente, Mascota. Las páginas correspondientes a cada uno son accesibles por medio de la barra de navegación, en el orden descrito.

## - Función de Búsqueda:

### Al apretar el botón de la lupa se redirige a una página que realiza la función; se pide ingresar una cadena al usuario, luego de realizar la petición se redirige a otra página en la que se devuelven en forma de lista todos los objetos de todas las clases que contengan en el atributo 'nombre' una coincidencia con dicha cadena indiferentemente de su posición en la misma.

## - Función de visualización de datos:

### Cada página que contiene la lista de objetos pertenecientes a sus respectivas clases es accesible por medio de su botón correspondiente en la barra de navegación de la página. Dentro de cada página se pueden visualizar los objetos almacenados en la base de datos conjuntamente con sus atributos, el orden elegido para su visualización fue del tipo alfabético respecto al nombre.

## - Función de insertar datos:

### Dentro de cada página en la cual son visualizables los datos de cada clase existe la opción 'añadir *objeto*' por medio de un botón con forma de cruz o 'más' que al presionarlo, redirige a un formulario por medio del cual es posible insertar datos en la base de datos de la aplicación. Luego de insertar un dato se redirige a la página correspondiente a la clase del dato insertado, donde se verifica que la lista fue actualizada.

## - Volver al inicio

### Para volver al inicio de la aplicación simplemente hay que apretar en el título de la barra de navegación, que se encuentra en la zona izquierda de la misma.

#### Si por alguna razón se desea acceder a la lista de objetos por medio de los urls en vez de los botones, se pueden consultar los mismos en el archivo de 'urls' en el código del proyecto.

# **Código de la aplicación**

## - views

### Cada función encargada de resolver las peticiones realizadas está clasificada por comentarios correspondientes a cada clase y organizados de manera que primero se encuentra la función visualización y luego la función create (formulario) de cada una.

## - urls

### Clasificados y ordenados de la misma forma que las funciones en views.

## - templates

### Cada función posee un template correspondiente, son excepciones los templates 'datos.html' y 'pagina.html'; 'pagina.html' es utilizado para mostrar los datos de cada página por medio de herencia y 'datos.html' sirve como lista general en la cual realizar la búsqueda por medio de la función búsqueda.
