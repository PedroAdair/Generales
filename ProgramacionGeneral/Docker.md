# Docker ![Docker](03-dark-blue-docker-logo.png)

Supongamos que nos encontramos desarrrollando un proyecto de Software que requiere de la colaboracion entre cientificos de datos, backend, frontend; los cuales han usado diferentes tecnologias para gesiotar el proyecto (ejemplo MongoDB para base de datos no estrucuradas, NextJs para el desarrollo de interfaces, Python y Spark para los trabajos de ciencia de datos y BigData) y que necesitamos realizar un cambio a una parte del proyecto. 

**¿Que opciones tenemos?**. Una primera idea es realizar el cambio directamente en los servidores de producción y esperaramos que todo saliera bien, o que copiaramos todo el proyecto en nuestro portatil y que una vez finalizada nuestra tarea copiaramos los cambios y realizaramos dichos cambios. Sin embargo, estas ideas conllevan grandes riesgos como el manejo de versiones (no nos gustaria trabajar con python 3.9.11 y que al final el  codigo de produccion esta en 3.7 donde tal vez una funcion que usamos no existia en esa versión haciendo inservible nuestro aporte). 

Devido a esto han surgido multiples estrategias para poder realizar despliegues exitosos, ademas del manejo de plataformas que nos permitan trabajar de forma eficiente aprovechando al máximo los recursos computaciones que disponemos en el proyecto, Una de estas opciones es el manejo de contenedores y para ello la plataforma más famosa es Docker.

## 1. Que es Docker?
Docker es una plataforma de software que permite tener un manejo optimo de nuestras aplicaciones en Contenedores, una estrategia para empaquetar y mantener un co

## 2. Instalacion 

### 2.1 Windows
Para poder realizar la instalacion de Docker en una computadora con sistema operativo Windows es necesario reviar que nuestro pc tiene habilidada la Opcion de virtualziación, para ello en el administrador de tareas/Rendimiento revisamos que la opcion de virtualización se encuentre activa, en caso negativo sera necesario entrar a la BIOS  para habilitar dicho proceso. La manera en la que se realiza dicho proceso varia de la marca del coputador. A continuacion se anexa el link para  [Habilitar la virtualización en equipos Windows 11](https://support.microsoft.com/es-es/windows/habilitar-la-virtualizaci%C3%B3n-en-equipos-windows-11-c5578302-6e43-4b4b-a449-8ced115f58e1).  En esta pagina se describe detalladamente el procedimiento necesario par realizar nuestra configuracion. 

## Imagenes y contenedores

En vez de nosotros instalar en nuestro pc una version especidifica de algun programa, 

## Comandos importantes para Docker.


## Ejemplo (Instalacion de imagen para Mongo DB)