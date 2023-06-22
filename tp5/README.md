# Perceptrón Simple y Multicapa
## [Presentación del proyecto](https://docs.google.com/presentation/d/1kDC5cKwpa_Tj5CTGadoiDxzBlGZ8nCj7wkJEtXdVdG8/edit#slide=id.g6c52a2e8d8_0_177)
## Contenido
 - [Introducción](#introduccion)
 - [Pre-requisitos](#pre-requisitos-)
 - [Estructura del proyecto](#estructura-del-proyecto-)
 - [Instalación](#instalacion-)
 - [Configuración](#configuracion-)
 - [Ejecución](#ejecucion-)
 - [Autores](#autores-)

## Introduccion
Este proyecto es una implementación de autoencoders, tanto de Denoising (DAE) como Variacionales (VAE).
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

- [perceptrons](perceptrons): Directorio con los archivos utilizados para modelar las redes neuronales.
- [update_methods](update_methods): Directorio con los archivos utilizados para actualizar los pesos de las redes.
- [utils](utils): Directorio con los archivos utilizados para manejar archivos.
- [font.py](font.py): Archivo que contiene la clase Font que se encarga de configurar los caracteres a utilizar
 y otras funciones sobre el manejo de los caracteres, incluida su graficacion.
- [encoder_conf.json](encoder_conf.json): Archivo de configuracion del encoder.
- [Variational_weitghts](variational_weights): Directorio con los archivos de pesos utilizados para el VAE. 
  - Idem para [denoising_weights_X.txt](denoising_weights_1.txt) y [weights.txt](weights_1.txt).
- [denoising_main.py](denoising_main.py): Archivo principal para ejecutar el DAE.
- [denoising_pre_trained_main.py](denoising_main_pre_trained.py): Archivo principal para ejecutar el DAE con pesos pre-entrenados.
- [variational_main.py](variational_main.py): Archivo principal para ejecutar el VAE.
- [variational_pre_trained_main.py](variational_pre_trained.py): Archivo principal para ejecutar el VAE con pesos pre-entrenados.
- [autoencoder_main.py](autoencoder_main.py): Archivo principal para ejecutar el autoencoder.
- [autoencoder_pre_trained_main.py](autoencoder_pre_trained_main.py): Archivo principal para ejecutar el autoencoder con pesos pre-entrenados.

## Instalacion 🛠️
Para instalar el proyecto se debe clonar el repositorio en la carpeta deseada:
```bash
git clone https://github.com/gbudoberra/sia
```
Luego se debe ingresar a la carpeta del proyecto:
```bash
cd tp5
```
Por último se deben instalar las librerías necesarias para poder ejecutar el proyecto. Para instalarlas se debe ejecutar 
el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Configuracion ⚙️
Para configurar el encoder puede modificarse el archivo [conf.json](encoder_conf.json). 
El mismo contiene los siguientes parámetros, por ejemplo:
```json
{
  "perceptron_by_layer": [35, 20, 10, 2 , 10 ,  20,  35],
  "activation_methods":[ "sigmoid","sigmoid","sigmoid","sigmoid","sigmoid","sigmoid","sigmoid"],
  "update_method": "adam",
  "learning_rate": 0.005,
  "epsilon": 1
}
```
De esta forma puede modificarse la arquitectura de la red, los metodos de activacion y actualizacion de pesos, la tasa de
aprendizaje y el epsilon a utilizar.

## Ejecucion 🚀
Cada directorio corresponde a un ejercicio o una forma de resolver el mismo. Para ejecutar un ejercicio se debe ingresar a su directorio y ejecutar el 
comando:
```bash
pipenv run python {X}_main.py
```
Remplazando {X} por el nombre del ejecutable deseado.

## Autores 💭
 - [Gaspar Budó Berra](https://github.com/gbudoberra)
 - [Marcos Dedeu](https://github.com/mdedeu)
 - [Santiago Hadad](https://github.com/shadad00)
 - [Bruno Squillari](https://github.com/bsquillari)
 - [Marcus Galea Jacobsen](https://github.com/MarcusGalea)
