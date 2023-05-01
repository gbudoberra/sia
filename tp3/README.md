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
El proyecto está compuesto por los siguientes archivos y directorios:
 - [README.md](README.md): Contiene la información del proyecto.
 - [configurations](configurations): JSON Parser
 - [singelayer](singlelayer): Implementación del perceptrón simple.
 - [multilayer](multilayer): Implementación del perceptrón multicapa.
 - [ej1](ej1): Ejercicio 1
 - [ej2](ej2): Ejercicio 2
 - [ej3](ej3): Ejercicio 3


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
En cada carpeta de ejercicio, donde corresponda, se encuentra un JSON que contiene los parámetros necesarios para correr el algoritmo. 

## Ejecucion 🚀
Para ejecutar el proyecto se debe correr el siguiente comando:
```bash
pipenv run python ejX.py
```
## Analisis de resultados 📊
Para realizar el analisis de los resultados, en cada carpeta de ejercicio se encuentran los gráficos relacionados al mismo.

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
