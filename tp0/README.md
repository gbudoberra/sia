
# TP0 SIA - Análisis de Datos

## Introducción

Trabajo práctico orientativo para la materia Sistemas de Inteligencia Artificial con el
objetivo de evaluar la función de captura de un Pokemon.

[Enunciado](docs/SIA_TP0.pdf)

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Parado en la carpeta del tp0 ejecutar

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual

## Ejecución

```
pipenv run python main.py [config_file]
```

# TP0
## 1A
Ejecutando la función 100 veces, para cada Pokemon en condiciones ideales(HP:100 %, LVL 100) ¿Cuál es la probabilidad de captura promedio para cada pokebola?
```
python 1a.py
```
## 1B
¿Es cierto que algunas pokebolas son más o menos efectivas dependiendo de propiedades intrínsecas de cada Pokemon? Justificar.
```
python 1b.py
```
## 2A
¿Las condiciones de salud tienen algún efecto sobre la efectividad de la captura? Si es así, ¿Cuál es más o menos efectiva?
```
python 2a.py
```
## 2B
¿Cómo afectan los puntos de vida a la efectividad de la captura?
```
python 2b.py
```
## 2C
¿Qué parámetros son los que más afectan la probabilidad de captura?
```
python 2c.py
```
## 2D
Teniendo en cuenta uno o dos pokemones distintos: ¿Qué combinación de condiciones(propiedades mutables) y pokebola conviene utilizar para capturarlos?

Se generarán 4 gráficos sobre el pokemon ingresado en los parámetros:
- Probabilidad de captura por pokebola
- Probabilidad de captura por nivel
- Probabilidad de captura por StatusEffect
- Probabilidad de captura por HP %

Se guardan como imágenes en la carpeta graphs.
```
python 2d.py POKEMON_NAME
```
## 2E
A partir del punto anterior, ¿sería efectiva otra combinación de parámetros teniendo en cuenta un nivel del pokemon más bajo (o más alto)?

Se generarán 3 gráficos sobre el pokemon ingresado en los parámetros:
- Probabilidad de captura por pokebola
- Probabilidad de captura por StatusEffect
- Probabilidad de captura por HP %

Se guardan como imágenes en la carpeta graphs.

Además, imprime: "nombre, nivel, pokebola con más probabilidad, status con más probabilidad, HP% con más probabilidad".
```
python 2e.py POKEMON_NAME POKEMON_LEVEL
```
