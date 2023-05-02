# Perceptrón Simple y Multicapa
## [Presentación del proyecto](https://docs.google.com/presentation/d/1K7EQ9cbz-ziHh36JeA4BRDA0cQq3TYcE63AE4JNWVsk/edit#slide=id.g22e6deed11b_1_56)
## Contenido
 - [Introducción](#introduccion)
 - [Pre-requisitos](#pre-requisitos-)
 - [Estructura del proyecto](#estructura-del-proyecto-)
 - [Instalación](#instalacion-)
 - [Configuración](#configuracion-)
 - [Ejecución](#ejecucion-)
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
 - [jsonReader.py](configurations/jsonReader.py): Este archivo contiene la clase JsonReader que se encarga de leer el archivo de configuración y parsearlo.
 - [SimplePerceptron.py](singlelayer/SimplePerceptron.py): Este archivo contiene la clase SimplePerceptron que se encarga de entrenar un perceptrón simple.
 - [MultilayerPerceptron.py](multilayer/multilayerperceptron.py): Este archivo contiene la clase MultilayerPerceptron que se encarga de entrenar un perceptrón multicapa.
 - [ej1](ej1): 
   - [ej1.py](ej1/ej1.py): Codigo fuente del ejercicio 1.
   - [conf_and.json](ej1/conf_and.json): Archivo de configuracion del operador AND para el ejercicio 1.
   - [conf_or.json](ej1/conf_or.json): Archivo de configuracion del operador OR para el ejercicio 1.
 - [ej2](ej2):
   - [ej2.py](ej2/ej2.py): Codigo fuente del ejercicio 2.
   - [TP3-ej2-conjunto.csv](ej2/TP3-ej2-conjunto.csv): Conjunto de datos para el ejercicio 2.
 - [ej3](ej3):
   - [ej.3a.py](ej3/ej3.a.py), [ej3.b.py](ej3/ej3.b.py), [ej3.c.py](ej3/ej3.c.py): Codigos fuente para la resolucion de cada enunciado
   - [configurations](ej3/configurations): Directorio que contiene los archivos de configuración para el problema de clasificación de dígitos.
   - [graphs](ej3/graphs): Directorio que contiene los gráficos generados por el programa.
   - [utils](ej3/utils): Directorio que contiene los archivos de utilidades para el problema de clasificación de dígitos.
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
Para configurar el proyecto cada ejercicio cuenta con un archivo .json de configuracion.
Por ejemplo, en el ejercicio 1 puede modificarse [conf_and.json](ej1/conf_and.json) para elegir diferentes metodos activacion o actualizacion:
```json
{
  "points": [[-1, 1], [1, -1], [-1, -1], [1, 1]],
  "expected": [[1], [1], [1], [-1]],
  "update_method": "adam",
  "activation_method": "step"
}
```

## Ejecucion 🚀
Para ejecutar el proyecto se puede ejecutar cada uno de los items del enunciado de forma individual. Para ello se debe ingresar a la carpeta del item y ejecutar el siguiente comando en la terminal
```bash
pipenv run python ejX/ejX.py
```
Donde X es el numero de ejercicio que se desea ejecutar.

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
