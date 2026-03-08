# Servo Position Control

Proyecto básico de control de posición angular con Arduino UNO, potenciómetro y servomotor SG90.

## Objetivo

Leer una referencia analógica desde un potenciómetro, convertirla en una consigna angular y accionar un servomotor para seguir esa referencia.

## Sistema

- Entrada: potenciómetro
- Procesamiento: Arduino UNO
- Actuador: servo SG90
- Salida: posición angular del eje

## Parte de simulación

Se utiliza un modelo simplificado de primer orden para representar la dinámica del servo:

tau * d(theta)/dt + theta = theta_ref

## Estructura

- `src/`: modelo y simulación en Python
- `arduino/`: código de control para Arduino
- `docs/obsidian/`: documentación para estudio y portfolio
- `results/`: gráficas y resultados
- `data/`: datos experimentales futuros

## Ejecución

```bash
source .venv/bin/activate
python3 src/plots.py