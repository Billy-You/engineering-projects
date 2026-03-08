# Desarrollo matemático — Servo Position Control

## Conversión analógica-digital

Si la tensión de entrada es $$V_{in}$$ y la referencia del ADC es $$V_{ref}$$, entonces:

$$
\text{ADC} = \frac{V_{in}}{V_{ref}} \cdot 1023
$$

Para $$V_{ref} = 5 V$$:

$$
\text{ADC} = \frac{V_{in}}{5} \cdot 1023
$$

## Conversión ADC a ángulo de referencia

Suponiendo un rango angular de $$0^\circ$$ a $$180^\circ$$:

$$
\theta_{ref} = \frac{180}{1023} \cdot \text{ADC}
$$

## Modelo dinámico simplificado del servo

Se adopta un modelo de primer orden:

$$
\tau \frac{d\theta(t)}{dt} + \theta(t) = \theta_{ref}(t)
$$

donde:

$$
\theta(t)
$$

es la posición angular del servo, y

$$
\theta_{ref}(t)
$$

es la referencia angular.

## Error de seguimiento

$$
e(t) = \theta_{ref}(t) - \theta(t)
$$

## Interpretación

Un valor pequeño de $$\tau$$ implica respuesta rápida. Un valor mayor implica una respuesta más lenta y mayor retardo frente a la referencia.