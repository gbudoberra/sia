# Métodos de Búsqueda Informados
## [Presentación del proyecto](https://docs.google.com/presentation/d/19SKlx6vl42VX2JnWaQeLwlgPUETAQvQkEmcCt38WnCE/edit#slide=id.g22e6deed11b_1_82)
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
Este proyecto es una implementación de los algoritmos genéticos para resolver el problema de encontrar la combinación de
colores RGB para llegar a un valor objetivo.
El proyecto está desarrollado en Python 3.6.5 y utiliza la libreria plotlib para la representación de gráficos.

Utilizamos los métodos de selección por ruleta, elite y por torneo (determinístico y probabilístico), y los métodos de 
mutación Multigen limitada, Multigen Uniforme y Mutación completa. Para la cruza utilizamos el método de cruza uniforme.
## Pre-requisitos ⌚
Para poder ejecutar el proyecto es necesario tener instalado Python 3.6.5 o superior. También es necesario tener 
instalado las librerías matplotlib, numpy y pandas para poder visualizar los gráficos. Para instalarlas se debe ejecutar 
el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Estructura del proyecto 🧱
El proyecto está compuesto por los siguientes archivos:
 - [README.md](README.md): Contiene la información del proyecto.
 - [main.py](main.py): Código principal del proyecto.
 - [mutation.py](mutation/mutation.py): AFunciones de mutación.
 - [methods](methods): Directorio que contiene los archivos de los métodos de selección
 - [genotype](genotype): Directorio con los archivos que representan el genotipo y todas sus funciones
 - [generic_genetic.py](genetics/generic_genetic.py): Clase abstracta de los algoritmos genéticos.
 - [configurations](configurations): Directorio con los archivos de configuración.
   - [model.json](configurations/model.json): Configuración del proyecto.
   - [model_colors.json](configurations/model_colors.json): Colores de los modelos.
   - [jsonReader.py](configurations/jsonReader.py): Clase que lee los archivos de configuración.
 - [color_crossover.py](color_crossover/rgb_crossover.py): Funciones de cruza.
 - [analysis](analysis): códigos de análisis de los resultados

## Instalacion 🛠️
Para instalar el proyecto se debe clonar el repositorio en la carpeta deseada:
```bash
git clone https://github.com/gbudoberra/sia
```
Luego se debe ingresar a la carpeta del proyecto:
```bash
cd tp2
```
Por último se deben instalar las librerías necesarias para poder ejecutar el proyecto. Para instalarlas se debe ejecutar el siguiente comando en la terminal:
```bash
pip install matplotlib && pip install pandas && pip install numpy
```

## Configuracion ⚙️
Para configurar el proyecto se debe editar el archivo [model.json](configurations/model.json). 
En este archivo se puede configurar el tamaño de la población, el método de selección (para padres y nuevas generaciones),
la función de mutación, la probabilidad de mutación, la cantidad de hijos generados, el epsilon para la solución.
```json
{
  "population_size": 120,
  "parent_selector": "ProbabilisticTournamentGenetic",
  "new_generation_selector": "ProbabilisticTournamentGenetic",
  "mutation_function": "mutation_uniform_gen",
  "mutation_delta": 100,
  "mutation_probability": 0.1,
  "k_generated_sons": 30,
  "deterministic_tournament_participant_number": 50,
  "solution_epsilon": 10
}
```
También se puede configurar la paleta de colores y el color objetivo en el archivo [model_colors.json](configurations/model_colors.json).
```json
{
  "color_palette": [
    {
      "r": 255,
      "g": 255,
      "b": 255
    },
    ...
  ],
  "goal_color": {
    "r": 120,
    "g": 120,
    "b": 120
  }
}

```

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
