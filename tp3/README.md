# Perceptrón Simple y Multicapa
## [Presentación del proyecto](https://docs.google.com/presentation/d/1K7EQ9cbz-ziHh36JeA4BRDA0cQq3TYcE63AE4JNWVsk/edit#slide=id.g22e6deed11b_1_56)
## Contenido
 - [Introducción](#introduccion)
 - [Pre-requisitos](#pre-requisitos-)
 - [Estructura del proyecto](#estructura-del-proyecto-)
 - [Instalación](#instalacion-)
 - [Configuración](#configuracion-)
 - [Ejecución](#ejecucion-)
 - [Análisis de resultados](#analisis-de-resultados-)
 - [Autores](#autores-)

## Introduccion
Este proyecto es una implementación del algoritmo de perceptrón simple lineal y no lineal y del algoritmo de perceptrón multicapa.
El proyecto está desarrollado en Python 3.6.5 y utiliza la libreria plotlib para la representación de gráficos.

Implementamos las funciones de activación sigmoidea,  la tanh y la identidad.  Para la actualización de los pesos utilizamos el gradiente descendiente y también implementamos Adam. 
## Pre-requisitos ⌚
Para poder ejecutar el proyecto es necesario tener instalado Python 3.6.5 o superior. También es necesario tener 
instalado las librerías matplotlib, numpy y pandas para poder visualizar los gráficos. Para instalarlas se debe ejecutar 
el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Estructura del proyecto 🧱
El proyecto está compuesto por los siguientes archivos:


## Instalacion 🛠️
Para instalar el proyecto se debe clonar el repositorio en la carpeta deseada:
```bash
git clone https://github.com/gbudoberra/sia
```
Luego se debe ingresar a la carpeta del proyecto:
```bash
cd tp3
```
Por último se deben instalar las librerías necesarias para poder ejecutar el proyecto. Para instalarlas se debe ejecutar el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Configuracion ⚙️


## Ejecucion 🚀
Para ejecutar el proyecto y resolver un tablero aleatorio se debe ejecutar el siguiente comando en la terminal:
```bash
pipenv run python ej1.py
```
## Analisis de resultados 📊
Para realizar el analisis de los resultados, es necesario pararse en el directorio análisis, mediante el comando:
```bash
cd analysis
```
Para ejecutar la comparación de los métodos y comparar los métodos de selección y mutación, se debe ejecutar el siguiente comando en la terminal:
```bash
pipenv run python ./best_combination/ej1.py
```
Para ejecutar la comparación de tamaño de población y cantidad de hijos generados, se debe ejecutar el siguiente comando en la terminal:
```bash
pipenv run python ./alter_parameters/ej1.py
```
Para ejecutar la comparación de distintas probabilidades de mutación, se debe ejecutar el siguiente comando en la terminal:
```bash
pipenv run python ./alter_mutation_probability/ej1.py
```

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
