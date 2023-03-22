# Métodos de Búsqueda Informados
## [Presentación del proyecto](https://docs.google.com/presentation/d/1VXF63ETAOX4ev6w4Jyit8GFcDkQkWFuVxa9E8vRSutc/edit#slide=id.g22223e87909_2_23)
## Contenido
 - [Introducción](#introduccion)
 - [Pre-requisitos](#pre-requisitos-)
 - [Estructura del proyecto](#estructura-del-proyecto-)
 - [Instalación](#instalacion-%EF%B8%8F)
 - [Configuración](#configuracion-%EF%B8%8F)
 - [Ejecución](#ejecucion-)
 - [Autores](#autores-)

## Introducción
Este proyecto es una implementación de los algoritmos de búsqueda informada BFS, DFS, A* y Greedy para resolver el problema de buscar la solución al juego conocido como [FillZone](http://www.mygamesworld.com/game/7682/Fill_Zone.html). El proyecto está desarrollado en Python 3.6.5 y utiliza la libreria plotlib para la representación de gráficos.

## Pre-requisitos ⌚
Para poder ejecutar el proyecto es necesario tener instalado Python 3.6.5 o superior. También es necesario tener instalado las librerías matplotlib, numpy y pandas para poder visualizar los gráficos. Para instalarlas se debe ejecutar el siguiente comando en la terminal:
```
pip install matplotlib && pip install pandas && pip install numpy
```

## Estructura del proyecto 🧱
El proyecto está compuesto por los siguientes archivos:
 - [README.md](README.md): Archivo que contiene la información del proyecto.
 - [main.py](main.py): Archivo que contiene el código principal del proyecto.
 - [main_with_metrics.py](main_with_metrics.py): Archivo que contiene el código principal del proyecto con la opción de mostrar las métricas y generar los gráficos necesarios.
 - [compare_heuristics.py](compare_heuristics.py): Archivo que contiene la comparación de las heurísticas planteadas para el problema.
 - [utils.py](utils.py): Archivo que contiene las funciones auxiliares del proyecto.
 - [ColorGridStatus.py](ColorGridStatus.py): Archivo que contiene la clase ColorGridStatus que representa el estado del juego.
 - [conf.json](conf.json): Archivo que contiene la configuración del juego.
 - [Graphs](Graphs): Carpeta que contiene los gráficos generados por el proyecto. Muestran los pasos realizados para llegar a la solución.
 - [Methods](Methods): Carpeta que contiene los archivos con los algoritmos de búsqueda informada implementados.
 - Otras carpetas y archivos como [CompareHeuristics](CompareHeuristics), [CompareMethods](CompareMethods) y [graph.py](graph.py)

## Instalacion 🛠️
Para instalar el proyecto se debe clonar el repositorio en la carpeta deseada:
```
git clone https://github.com/gbudoberra/sia
```
Luego se debe ingresar a la carpeta del proyecto:
```
cd tp1
```
Por último se deben instalar las librerías necesarias para poder ejecutar el proyecto. Para instalarlas se debe ejecutar el siguiente comando en la terminal:
```
pip install matplotlib && pip install pandas && pip install numpy
```

## Configuracion ⚙️
Para configurar el proyecto se debe editar el archivo [conf.json](conf.json). En este archivo se puede configurar el tamaño del tablero, la cantidad de colores y el método a utilizar para resolver el tablero. 

## Ejecucion 🚀
Para ejecutar el proyecto y resolver un tablero aleatorio se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python main.py
```
Para ejecutar el proyecto con la opción de mostrar las metricas y generar los graficos necesarios se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python main_with_metrics.py
```
Para ejecutar la comparación de las heurísticas planteadas para el problema, se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python compare_heuristics.py
```
Para ejecutar la comparación de las heurísticas planteadas para el problema, con diferentes matrices,  se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python /CompareHeuristics/compare_with_different_matrix.py
```
Para ejecutar la comparación de los métodos, con diferentes matrices,  se debe ejecutar el siguiente comando en la terminal:
```
pipenv run python /CompareMethods/compare_with_different_matrix.py
```

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
