# SI_Tarea3_ICF222

Prediccion de retencion de clientes

---

Enunciado
---------

La base de datos consiste en 10000 clientes con 14 variables originales donde la variable de
salida es binaria e indica si la persona se retuvo o no como cliente dentro de un plazo
prefijado. El código base consistió en aplicar redes neuronales densas a este problema. En
esta tarea la idea es que profundicen un poco más.

---

Condiciones del trabajo
-----------------------

* Considerando la eliminación de variables espúreas, divida la base de datos en los
  conjuntos de entrenamiento y testeo considerando 75% para entrenamiento. Use una
  semilla con un numero entre 1 y 100. Reporte los primeros 5 registros del set de
  entrenamiento y testeo.
* Utilizando una regresión logística indique el resultado en el set de testeo. Reporte el
  resultado de precisión obtenida (accuracy en inglés). Recuerde que una regresión
  logística es equivalente a una red neuronal sin capas ocultas.
* Considere sólo una capa oculta. ¿Cómo evoluciona la precisión en el set de testeo si
  varía el número de neuronas en la capa oculta?. Considere los valores en lista
  [1,3,5,10,15,20,25,30,35]. Indique los valores en una tabla. ¿Qué puede concluir de
  los resultados?
* Considere 2 capas. Considere la combinación de neuronas consideran el set [5,10,15]
  para el numero de neuronas para ambas capas. En este caso hay 9 combinaciones.
  Indique los valores de precisión en sets de testeo en una tabla. ¿Qué puede concluir
  de los resultados?.
* Considere 3 capas. En este caso elija 10 combinaciones considerando todo lo que ha
  analizado hasta el momento. Considere las mismas preguntas del punto anterior.
* Considerando todos los experimentos, ¿que puede concluir de forma general?.
  Indique 4 maneras realistas en las que usted cree que podría mejorar el resultado.
  Puede usar su imaginación en este punto.

---

## Utilizando el repositorio

---

Una vez descargado el repositorio, crearemos un ambiente de trabajo en donde se instalaran las dependencias

```bash
  $python -m venv env
```

Se creara el ambiente de trabajo, ingresas a la direccion env/Scripts/ y seleccionas el archivo  activate.bat

```bash
  $/env/Scripts/activate.bat
```

Ahora activado el ambiente de trabajo, instalaremos las dependencias

```bash
  $pip install -r requirements.txt
```

---

Todo listo para utilizar el codigo!

```bash
  $cod/main.py
```
