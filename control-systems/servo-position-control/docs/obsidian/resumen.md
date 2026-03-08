# Resumen limpio para Obsidian

## `docs/obsidian/resumen.md`

```text
# Servo Position Control

## Descripción del problema

Se desea controlar la posición angular de un servomotor SG90 a partir de una referencia manual generada con un potenciómetro y leída por un Arduino UNO.

## Teoría física

El potenciómetro actúa como divisor de tensión variable. El Arduino convierte esa tensión en un valor digital mediante un ADC de 10 bits. Ese valor se transforma en una referencia angular para el servo.

## Variables principales

- Valor ADC
- Ángulo de referencia
- Ángulo real del servo
- Error de seguimiento

## Hipótesis

- Potenciómetro lineal
- ADC ideal
- Servo aproximable mediante dinámica de primer orden
- Sin carga mecánica significativa

## Diseño experimental

El potenciómetro genera la referencia. El Arduino procesa la señal y ordena la posición al servo. Se comparará la referencia con el movimiento real observado del eje.

## Validación

Se analizarán:
- seguimiento de posición
- error angular
- repetibilidad
- diferencias entre modelo y prototipo real