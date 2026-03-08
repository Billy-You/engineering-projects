Claro. Te dejo un **resumen limpio, técnico y listo para Obsidian** centrado en el proyecto, la lógica de medida y la validación del canal analógico, **sin entrar todavía en las matemáticas internas del sensor**.

````markdown
# Proyecto: Sensor de temperatura con Arduino — base de adquisición y validación

## Objetivo del proyecto

Desarrollar un prototipo de ingeniería capaz de:

- simular un sistema de medida de temperatura
- construir un montaje físico en casa
- adquirir datos experimentales
- guardar resultados en archivos reutilizables
- comparar en el futuro simulación y realidad

En esta fase del proyecto, el foco principal no ha sido todavía validar el sensor térmico definitivo, sino **validar correctamente la cadena de adquisición de datos analógicos** del sistema.

---

## Estado actual del proyecto

En esta etapa se ha trabajado sobre:

- estructura del proyecto en el workspace
- entorno Python y scripts de simulación
- documentación técnica en Obsidian
- validación del canal analógico del Arduino
- comprensión del funcionamiento del ADC
- preparación para exportar datos a CSV

La parte de sensórica térmica física ha quedado condicionada por la fiabilidad del sensor utilizado.

---

## Fundamento de la adquisición analógica

Arduino no “entiende” directamente una tensión analógica como un número físico continuo.  
Lo que hace es usar un bloque interno llamado **ADC**.

## ¿Qué es el ADC?

ADC significa:

**Analog to Digital Converter**

Es decir:

**convertidor analógico-digital**

Su función es transformar una tensión continua de entrada en un número entero que el microcontrolador pueda procesar.

---

## ADC de 10 bits

En placas como Arduino Uno, el ADC trabaja con una resolución de **10 bits**.

Eso significa que puede representar la tensión de entrada con:

$$
2^{10} = 1024
$$

niveles posibles.

Como empieza en 0, los valores posibles son:

$$
0, 1, 2, \dots, 1023
$$

Por tanto:

- el valor mínimo digital es `0`
- el valor máximo digital es `1023`

---

## Relación entre tensión y lectura digital

Si la referencia analógica es de 5 V, entonces el ADC convierte el rango:

$$
0 \text{ V} \rightarrow 5 \text{ V}
$$

en el rango digital:

$$
0 \rightarrow 1023
$$

### Casos extremos

#### Si la entrada es 0 V

$$
ADC = 0
$$

#### Si la entrada es 5 V

$$
ADC = 1023
$$

Esto fue precisamente una de las pruebas más importantes del proyecto.

---

## Por qué fue importante probar A0 con 0 V y 5 V

Antes de confiar en cualquier sensor, había que demostrar que:

- la placa funciona
- el pin analógico funciona
- la lectura analógica no está rota
- el problema no está en el software base

Para eso se hizo una validación muy simple y muy potente.

### Prueba 1: A0 conectado a GND

Se conectó el pin analógico A0 directamente a tierra.

Eso equivale a aplicar:

$$
V_{in} = 0 \text{ V}
$$

y el resultado esperado era:

$$
ADC \approx 0
$$

### Prueba 2: A0 conectado a 5V

Se conectó A0 directamente a 5 V.

Eso equivale a aplicar:

$$
V_{in} = 5 \text{ V}
$$

y el resultado esperado era:

$$
ADC \approx 1023
$$

### Conclusión de esta prueba

Si ambas pruebas dan el resultado esperado, entonces queda validado que:

- el conversor analógico-digital está operativo
- el pin A0 responde correctamente
- la lectura por `analogRead()` es coherente
- el sistema base de adquisición es válido

Esta comprobación es muy valiosa porque aísla fallos.  
Permite separar:

- problemas de placa
- problemas de software
- problemas de sensor
- problemas de cableado

---

## ¿Qué es A0?

`A0` es uno de los **pines analógicos** del Arduino.

No representa una lectura, sino una **ubicación física de entrada**.

Cuando en el código se escribe algo como:

```cpp
const int sensorPin = A0;
````

eso significa:

* el sensor está conectado físicamente al pin analógico A0
* el programa leerá la tensión presente en ese punto

Después, al usar:

```cpp
analogRead(sensorPin);
```

el microcontrolador mide la tensión en ese pin y la convierte en un valor digital entre 0 y 1023.

---

## Resolución del ADC

Si la referencia es 5 V y el ADC tiene 1024 niveles, cada paso representa aproximadamente:

$$
\frac{5}{1023} \approx 0.00489 \text{ V}
$$

o lo que es lo mismo:

$$
4.89 \text{ mV por cuenta}
$$

Esto significa que el sistema no distingue infinitos valores, sino saltos discretos de unos pocos milivoltios.

Ese detalle es clave porque explica por qué toda medida real tiene una resolución limitada.

---

## Qué se ha aprendido con esta fase

La gran lección de esta etapa es que **no se debe empezar confiando ciegamente en el sensor**.

Primero hay que verificar la cadena de medida por bloques:

1. alimentación de la placa
2. comunicación serie
3. lectura del pin analógico
4. respuesta del ADC
5. coherencia del software
6. calidad del sensor

Este enfoque es mucho más ingenieril que conectar un sensor y asumir que todo lo que salga es correcto.

---

## Por qué queremos guardar datos en CSV

A medida que el proyecto evoluciona, no basta con mirar números en el monitor serie.
Hace falta almacenar resultados de forma ordenada y reutilizable.

Ahí entra el formato **CSV**.

## ¿Qué es un CSV?

CSV significa:

**Comma-Separated Values**

Es un archivo de texto donde los datos se guardan en forma de tabla.

Ejemplo simple:

```csv
temperatura_c,voltaje_v,adc
20.0,0.20,40.92
25.0,0.25,51.15
30.0,0.30,61.38
```

Cada fila representa una observación, y cada columna una variable.

---

## Por qué el CSV es importante

### 1. Permite guardar datos experimentales

No dependes solo de lo que se ve en pantalla en tiempo real.

### 2. Permite procesar datos en Python

Puedes usar:

* pandas
* matplotlib
* numpy

para analizar resultados.

### 3. Permite comparar simulación y experimento

Puedes guardar:

* datos simulados
* datos medidos
* errores
* calibraciones

y luego cruzarlos.

### 4. Permite trazabilidad

El experimento deja rastro.
Eso hace el proyecto más serio y reproducible.

### 5. Permite escalar el trabajo

Más adelante podrás:

* filtrar ruido
* calcular medias
* ajustar modelos
* comparar sensores
* generar figuras automáticamente

---

## Por qué no basta con el monitor serie

El monitor serie es útil para depuración rápida, pero tiene limitaciones:

* los datos desaparecen si no se guardan
* cuesta analizar muchas muestras
* no sirve bien para comparar series largas
* no es cómodo para postproceso

Por eso el CSV es un paso natural hacia una metodología más profesional.

---

## Separación conceptual del proyecto

## Parte de simulación

Generar datos teóricos del sistema en Python.

## Parte experimental

Montar físicamente el circuito y el sensor.

## Parte de medición

Leer señales reales y convertirlas a datos utilizables.

## Parte de validación

Comparar resultados esperados con resultados medidos.

---

## Resultado técnico de la fase actual

Aunque el sensor térmico probado no resultó fiable, la fase no ha sido un fracaso.
Al contrario, ha servido para validar algo fundamental:

### La base de adquisición analógica funciona correctamente.

Eso incluye:

* placa operativa
* A0 operativo
* ADC operativo
* lectura digital coherente en extremos
* metodología de comprobación correcta

---

## Valor didáctico de esta fase

Esta parte del proyecto ha sido especialmente útil para aprender:

* qué es un ADC
* qué significa 10 bits
* cómo se convierte una tensión en un número
* qué representa realmente `A0`
* cómo validar una entrada analógica
* por qué guardar datos en CSV
* por qué un proyecto de sensórica debe depurarse por bloques

---

## Conclusión

La fase actual ha permitido construir una base sólida para el proyecto de temperatura.

Antes de validar el sensor final, ya se ha demostrado que:

* el sistema de adquisición de Arduino responde correctamente
* la lectura analógica tiene sentido físico
* los extremos de 0 V y 5 V se traducen correctamente a 0 y 1023
* la exportación futura a CSV será esencial para el análisis experimental

La siguiente etapa consistirá en retomar la parte sensórica con un componente fiable y continuar con adquisición, almacenamiento y validación de datos.

```

Si quieres, en el siguiente mensaje te lo convierto en una **versión más corta y más visual**, estilo nota de estudio para Obsidian.
```

////////////////////////////////////////////////////////////////////////////////////////////


# Fundamento general

El LM35 no “mide temperatura” como lo haría un termómetro clásico con mercurio.  
Lo que hace es aprovechar que en los **semiconductores** ciertas magnitudes eléctricas cambian con la temperatura de forma predecible.

La idea central es esta:

## La temperatura altera el comportamiento electrónico del material

Cuando cambia la temperatura:

- cambia la energía térmica de los portadores
    
- cambia la población de electrones y huecos
    
- cambian corrientes internas
    
- cambian tensiones en uniones PN o transistores
    

Y esas variaciones pueden transformarse en una señal eléctrica utilizable.

---

# 1. Física del fenómeno

## Temperatura como energía térmica

A nivel microscópico, la temperatura está relacionada con la agitación térmica media de las partículas.

En física estadística, la escala energética típica asociada a la temperatura viene dada por:

$$  
E \sim kT  
$$

donde:

- $k$ es la constante de Boltzmann
    
- $T$ es la temperatura absoluta en kelvin
    

Esto significa que al subir la temperatura aumenta la energía térmica disponible en el material.

---

## Qué pasa en un semiconductor

Un semiconductor tiene una estructura de bandas:

- **banda de valencia**
    
- **banda de conducción**
    
- una **brecha energética** o bandgap entre ambas
    

En materiales como el silicio, la conductividad depende de cuántos electrones consiguen pasar a la banda de conducción.

Cuando aumenta la temperatura:

- más electrones adquieren energía suficiente
    
- aumenta la concentración efectiva de portadores
    
- cambian las corrientes y tensiones internas del dispositivo
    

---

# 2. Química / ciencia de materiales detrás

Aquí “química” se entiende más como **estructura material y dopado** que como reacción química.

## Silicio dopado

Los sensores integrados como el LM35 están fabricados sobre silicio dopado.

### Dopado tipo n

Se introducen impurezas donadoras que aportan electrones.

### Dopado tipo p

Se introducen impurezas aceptoras que favorecen huecos.

Esto permite crear:

- uniones PN
    
- diodos
    
- transistores bipolares
    
- estructuras integradas de referencia y amplificación
    

---

## Importancia del dopado

El dopado controla:

- concentración de portadores
    
- corrientes de saturación
    
- tensión de unión
    
- sensibilidad térmica
    

O sea: la respuesta térmica del sensor no sale “por magia”, sino del diseño material del chip.

---

# 3. El núcleo físico real: unión PN y transistor bipolar

El LM35 se basa en principios muy cercanos a los de la unión PN y, más concretamente, en el comportamiento térmico de transistores bipolares integrados.

## Ecuación de un transistor bipolar

La corriente de colector de un BJT ideal puede escribirse como:

$$  
I_C = I_S e^{\frac{V_{BE}}{V_T}}  
$$

donde:

- $I_C$ es la corriente de colector
    
- $I_S$ es la corriente de saturación
    
- $V_{BE}$ es la tensión base-emisor
    
- $V_T$ es la tensión térmica
    

---

## Tensión térmica

La tensión térmica es:

$$  
V_T = \frac{kT}{q}  
$$

donde:

- $k$ es la constante de Boltzmann
    
- $T$ es la temperatura absoluta
    
- $q$ es la carga del electrón
    

A temperatura ambiente:

$$  
V_T \approx 25.8 \text{ mV}  
$$

Este término es fundamental porque muestra que el propio semiconductor ya lleva la temperatura “embebida” en sus ecuaciones.

---

# 4. De dónde sale una magnitud proporcional a la temperatura

Si despejamos $V_{BE}$:

$$  
V_{BE} = V_T \ln\left(\frac{I_C}{I_S}\right)  
$$

Sustituyendo $V_T$:

$$  
V_{BE} = \frac{kT}{q} \ln\left(\frac{I_C}{I_S}\right)  
$$

Aquí aparece una dependencia con $T$, pero hay un problema:

## Problema

$V_{BE}$ por sí sola **no es lineal y además suele disminuir con la temperatura**.

Eso no es ideal para un sensor limpio y cómodo como el LM35.

---

# 5. Truco de ingeniería: generar una señal PTAT

Los sensores integrados usan una magnitud llamada:

## PTAT = Proportional To Absolute Temperature

es decir:

**proporcional a la temperatura absoluta**

La forma clásica de obtenerla es usando **dos transistores bipolares** que trabajan a distinta densidad de corriente.

---

## Diferencia de tensiones base-emisor

Si tienes dos transistores con distinta densidad de corriente, la diferencia entre sus tensiones base-emisor vale aproximadamente:

$$  
\Delta V_{BE} = \frac{kT}{q} \ln(N)  
$$

donde:

- $N$ es la razón de áreas efectivas o densidades de corriente
    

Esto es importantísimo porque:

## Ahora sí

$\Delta V_{BE}$ es directamente proporcional a $T$.

Es decir:

$$  
\Delta V_{BE} \propto T  
$$

Y esa es la base elegante de muchos sensores integrados de temperatura.

---

# 6. Por qué esto es tan útil

Porque permite fabricar dentro del chip una señal que:

- depende de la temperatura
    
- es predecible
    
- puede amplificarse
    
- puede calibrarse
    
- puede convertirse en una salida lineal útil
    

---

# 7. Qué hace internamente un sensor como LM35

El LM35 no saca directamente una unión PN al exterior. Internamente hace bastante más:

1. genera una señal PTAT usando estructuras bipolares
    
2. la acondiciona con circuitería analógica integrada
    
3. la amplifica
    
4. la calibra en fábrica
    
5. entrega una salida lineal cómoda para el usuario
    

El resultado es una relación ideal del tipo:

$$  
V_{out} = 10 \text{ mV/}^\circ\text{C} \cdot T_C  
$$

donde $T_C$ es la temperatura en grados Celsius.

---

# 8. Paso de temperatura absoluta a Celsius

La física del semiconductor trabaja naturalmente mejor con temperatura absoluta:

$$  
T_K = T_C + 273.15  
$$

Muchos bloques internos generan una señal proporcional a:

$$  
T_K  
$$

Pero el usuario normalmente quiere grados Celsius.

Así que el circuito del sensor incorpora compensaciones para darte una salida referida a Celsius, no a Kelvin.

Por eso en el LM35 ideal:

- a $0^\circ$C → salida cercana a 0 V
    
- a $25^\circ$C → salida cercana a 0.25 V
    
- a $100^\circ$C → salida cercana a 1.00 V
    

---

# 9. Interpretación física de la linealidad

La linealidad no nace sola del material puro.  
Nace de combinar:

- física del semiconductor
    
- diseño analógico
    
- compensación interna
    
- calibración de fábrica
    

El ingeniero de circuito busca que el comportamiento final sea aproximadamente:

$$  
V_{out} = aT + b  
$$

En el LM35 ideal:

$$  
a = 10 \text{ mV/}^\circ\text{C}  
$$

y aproximadamente:

$$  
b \approx 0  
$$

---

# 10. Matemática de tu modelo externo

Una vez que el chip ya te entrega un voltaje analógico, desde fuera el modelo se simplifica muchísimo.

## Modelo ideal del sensor

$$  
V_{out} = 0.01 \cdot T  
$$

con:

- $V_{out}$ en voltios
    
- $T$ en grados Celsius
    

Despejando:

$$  
T = 100 \cdot V_{out}  
$$

Este modelo ya no muestra toda la física interna, pero es la versión ingenieril práctica para usar el sensor.

---

# 11. Relación con el ADC

Cuando conectas ese voltaje a Arduino, el ADC hace:

$$  
ADC = \frac{V_{out}}{V_{ref}} \cdot 1023  
$$

Si $V_{ref} = 5$ V:

$$  
ADC = \frac{V_{out}}{5} \cdot 1023  
$$

Sustituyendo el modelo del LM35:

$$  
ADC = \frac{0.01T}{5} \cdot 1023  
$$

$$  
ADC = \frac{10.23}{5} \cdot T  
$$

$$  
ADC \approx 2.046 \cdot T  
$$

Y despejando temperatura:

$$  
T \approx \frac{ADC}{2.046}  
$$

o equivalentemente:

$$  
T = \frac{500}{1023} \cdot ADC  
$$

---

# 12. Limitaciones físicas reales

El modelo ideal es útil, pero el comportamiento real incluye varios efectos.

## a) Tolerancias de fabricación

No todos los chips salen exactamente iguales.

## b) Offset

Puede haber una pequeña desviación fija.

## c) Error de ganancia

La pendiente real puede no ser exactamente 10 mV/°C.

## d) Ruido electrónico

Tanto el sensor como el ADC y la alimentación añaden ruido.

## e) Autocalentamiento

El propio sensor puede calentarse ligeramente por su disipación interna.

## f) Inercia térmica

El encapsulado no cambia de temperatura instantáneamente.

---

# 13. Modelo dinámico térmico

Además del modelo estático, hay un modelo dinámico interesante.

El sensor no responde de forma instantánea, sino con cierta constante de tiempo térmica. Una aproximación típica es de primer orden:

$$  
\tau \frac{dT_s}{dt} + T_s = T_{amb}  
$$

donde:

- $T_s$ es la temperatura del sensor
    
- $T_{amb}$ es la temperatura del entorno
    
- $\tau$ es la constante de tiempo térmica
    

Eso explica por qué cuando lo tocas o lo acercas a una fuente caliente la salida no salta instantáneamente al valor final.

---

# 14. Resumen físico en una frase

El LM35 funciona porque la **temperatura modifica de forma predecible el comportamiento eléctrico de estructuras semiconductor-bipolares integradas**, y el chip transforma esa dependencia en una **salida analógica lineal en voltaje**.

---

# 15. Resumen por capas

## Física

La temperatura cambia la energía térmica de los portadores y afecta las tensiones/corrientes internas del semiconductor.

## Química / materiales

El silicio dopado permite construir uniones PN y transistores cuya respuesta depende de la temperatura.

## Electrónica interna

El chip genera una señal PTAT, la amplifica, la compensa y la calibra.

## Matemática interna

Aparecen relaciones exponenciales y logarítmicas derivadas del transistor:

$$  
I_C = I_S e^{\frac{V_{BE}}{V_T}}  
$$

y señales PTAT del tipo:

$$  
\Delta V_{BE} = \frac{kT}{q} \ln(N)  
$$

## Matemática externa útil

El usuario ve un modelo lineal simple:

$$  
V_{out} = 0.01 \cdot T  
$$

---

# 16. Lo más importante que debes quedarte

Hay dos niveles de entender el sensor:

## Nivel 1 — usuario/ingeniería aplicada

“El sensor entrega 10 mV por cada grado Celsius.”

## Nivel 2 — ingeniería física/electrónica

“Ese voltaje sale de explotar la dependencia térmica de tensiones y corrientes en estructuras semiconductor-bipolares integradas, especialmente señales PTAT.”

---
