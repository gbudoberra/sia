# Metodos de Busqueda Informados
## [Presentacion del proyecto](https://docs.google.com/presentation/d/1VXF63ETAOX4ev6w4Jyit8GFcDkQkWFuVxa9E8vRSutc/edit#slide=id.g22223e87909_2_23)
## Contenido
 - [Introduccion](#introduccion)
 - [Pre-requisitos](#pre-requisitos)
 - [Estructura del proyecto](#estructura-del-proyecto)
 - [Instalacion](#instalacion)
 - [Configuracion](#configuracion)
 - [Ejecucion](#ejecucion)
 - [Autores](#autores)

## Introduccion
Este proyecto es una implementacion de los algoritmos de busqueda informada BFS, DFS, A* y Greedy para resolver el problema de buscar la solucion al juego conocido como [FillZone](http://www.mygamesworld.com/game/7682/Fill_Zone.html). El proyecto esta desarrollado en Python 3.6.5 y utiliza la libreria plotlib para la representacion de graficos.

## Pre-requisitos ⌚
Para poder ejecutar el proyecto es necesario tener instalado Python 3.6.5 o superior. También es necesario tener instalado la libreria matplotlib para poder visualizar los graficos. Para instalar matplotlib se debe ejecutar el siguiente comando en la terminal:
```
pip install matplotlib
```

## Estructura del proyecto 🧱
El proyecto está compuesto por los siguientes archivos:
 - [README.md](README.md): Archivo que contiene la información del proyecto.
 - [main.py](main.py): Archivo que contiene el codigo principal del proyecto.
 - [main_with_metrics.py](main_with_metrics.py): Archivo que contiene el codigo principal del proyecto con la opcion de mostrar las metricas y generar los graficos necesarios.
 - [compare_heuristics.py](compare_heuristics.py): Archivo que contiene la comparacion de las heuristicas planteadas para el problema.
 - [utils.py](utils.py): Archivo que contiene las funciones auxiliares del proyecto.
 - [ColorGridStatus.py](ColorGridStatus.py): Archivo que contiene la clase ColorGridStatus que representa el estado del juego.
 - [conf.json](conf.json): Archivo que contiene la configuracion del juego.
 - [Graphs](Graphs): Carpeta que contiene los graficos generados por el proyecto. Muestran los pasos realizados para llegar a la solucion.
 - [Methods](Methods): Carpeta que contiene los archivos con los algoritmos de busqueda informada implementados.

## Instalacion 🛠️
Para instalar el proyecto se debe clonar el repositorio en la carpeta deseada:
```
git clone https://github.com/gbudoberra/sia
```
Luego se debe ingresar a la carpeta del proyecto:
```
cd tp1
```
Por último se deben instalar las librerias necesarias para poder ejecutar el proyecto. Para instalar matplotlib se debe ejecutar el siguiente comando en la terminal:
```
pip install matplotlib
```

## Configuracion ⚙️
Para configurar el proyecto se debe editar el archivo [conf.json](conf.json). En este archivo se puede configurar el tamaño del tablero, la cantidad de colores y el metodo a utilizar para resolver el tablero. 

## Ejecucion 🚀
Para ejecutar el proyecto y resolver un tablero aleatorio se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python main.py
```
Para ejecutar el proyecto con la opcion de mostrar las metricas y generar los graficos necesarios se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python main_with_metrics.py
```
Para ejecutar la comparacion de las heuristicas planteadas para el problema se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python compare_heuristics.py
```

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
