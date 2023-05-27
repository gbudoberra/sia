# Perceptrón Simple y Multicapa
## [Presentación del proyecto](https://docs.google.com/presentation/d/1ZlrDNgn6AtfRS_UDxdhYqKeqCKgcF5QQdqiMt8qSc-k/edit#slide=id.g6c52a2e8d8_0_177)
## Contenido
 - [Introducción](#introduccion)
 - [Pre-requisitos](#pre-requisitos-)
 - [Estructura del proyecto](#estructura-del-proyecto-)
 - [Instalación](#instalacion-)
 - [Configuración](#configuracion-)
 - [Ejecución](#ejecucion-)
 - [Autores](#autores-)

## Introduccion
Este proyecto es una implementación de los modelos de Kohonen, Hopfield y PCA para el aprendizaje no supervisado.
El proyecto está desarrollado en Python 3.6.5 y utiliza la libreria plotlib para la representación de gráficos.

## Pre-requisitos ⌚
Para poder ejecutar el proyecto es necesario tener instalado Python 3.6.5 o superior. También es necesario tener 
instalado las librerías matplotlib, numpy y pandas para poder visualizar los gráficos. Para instalarlas se debe ejecutar 
el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Estructura del proyecto 🧱
El proyecto está compuesto por los siguientes archivos:
- [Kohonen](kohonen): Directorio con todos los archivos de Hopfield.
  - [main.py](kohonen/main.py): Archivo que contiene el código principal del ejercicio 1.
  - [Som.py](kohonen/Som.py): Archivo que contiene la clase Som que se encarga de entrenar una red de Kohonen y generar
  el mapa auto-organizado.
  - [neuron.py](kohonen/neuron.py): Archivo que contiene la clase Neuron que se encarga de representar una neurona de
    la red de Kohonen.
  - [graph_generators.py](kohonen/graph_generators.py): Archivo que contiene las funciones que se encargan de generar
    los gráficos.
  - [europe.csv](kohonen/europe.csv): Datos de los países de Europa que se utilizaran como Input.
- [Hopfield](hopfield): Directorio con todos los archivos de Hopfield.
  - [conf.json](hopfield/conf.json): Archivo de configuración del ejercicio 2.
  - [config.py](hopfield/config.py): Archivo que contiene la clase Config que se encarga de leer el archivo de
  configuración.
  - [Hopfield.py](hopfield/hopfield.py): Este archivo contiene la clase Hopfield que se encarga de entrenar una red
  de Hopfield y de generar los gráficos.
  - [main.py](hopfield/main.py): Archivo que contiene el código principal del ejercicio 2.
  - [ortogonal_main.py](hopfield/ortogonal_main.py): Archivo que contiene la clase Orthogonal que se encarga de generar los
     patrones ortogonales.
- [pca](pca): Directorio con todos los archivos de PCA.
  - [main.py](pca/main.py): Archivo que contiene el código principal del ejercicio 3.
  - [pca.py](pca/pca.py): Archivo que contiene la clase PCA que se encarga de entrenar una red de PCA y de generar los
  gráficos.

 
## Instalacion 🛠️
Para instalar el proyecto se debe clonar el repositorio en la carpeta deseada:
```bash
git clone https://github.com/gbudoberra/sia
```
Luego se debe ingresar a la carpeta del proyecto:
```bash
cd tp4
```
Por último se deben instalar las librerías necesarias para poder ejecutar el proyecto. Para instalarlas se debe ejecutar 
el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Configuracion ⚙️
Para configurar el ejercicio de Hopfield puede modificarse el archivo [conf.json](hopfield/conf.json). El mismo contiene
los siguientes parámetros:
```json
{
  "characters": ["a", "k", "p", "h" ],
  "noises": [5]
}
```
De esta forma puede modificarse el nivel de ruido y los caracteres a analizar.

## Ejecucion 🚀
Cada directorio corresponde a un ejercicio o una forma de resolver el mismo. Para ejecutar un ejercicio se debe ingresar a su directorio y ejecutar el 
comando:
```bash
pipenv run python main.py
```

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
