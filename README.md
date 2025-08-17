# TeleX2g.py
Challenge Telecom X: análisis de evasión de clientes - Parte 2
¡Claro! Aquí tienes un ejemplo de README en español para tu proyecto de análisis de cancelación de clientes en TelecomX:

---

# 📊 Análisis de Cancelación de Clientes — TelecomX

Este proyecto realiza un análisis completo del comportamiento de cancelación de clientes de una empresa de telecomunicaciones ficticia llamada **TelecomX**. Utiliza técnicas de preprocesamiento, balanceo de clases, entrenamiento de modelos de clasificación y visualización de datos para entender los factores que influyen en la cancelación.

## 🧰 Tecnologías Utilizadas

- Python
- Pandas
- Requests / JSON
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Seaborn / Matplotlib

## 📦 Estructura del Código

### 1. **Importación de Librerías**
Se cargan las librerías necesarias para manipulación de datos, visualización y modelado.

### 2. **Carga y Desanidado de Datos**
- Se obtiene el dataset en formato JSON desde un repositorio público.
- Se desanidan columnas que contienen diccionarios anidados mediante una función recursiva.

### 3. **Preprocesamiento**
- Se eliminan columnas irrelevantes (`customerID`).
- Se aplica codificación One-Hot para variables categóricas.
- Se calcula la proporción de cancelaciones.

### 4. **Preparación para Modelado**
- Separación de variables predictoras (`X`) y variable objetivo (`y`).
- Balanceo de clases con **SMOTE**.
- Normalización de variables numéricas.
- División en conjuntos de entrenamiento y prueba.

### 5. **Entrenamiento de Modelos**
Se entrenan dos modelos:
- Regresión Logística
- Random Forest

### 6. **Evaluación**
Se evalúan los modelos con:
- Matriz de confusión
- Reporte de clasificación (precisión, recall, F1-score)

### 7. **Importancia de Variables**
Se extraen las variables más influyentes según el modelo de Random Forest.

## 📊 Visualizaciones Incluidas

1. **🔍 Matriz de Correlación**  
   Para identificar relaciones entre variables numéricas.

2. **📦 Boxplot: Tenencia vs Cancelación**  
   Muestra cómo varía la duración como cliente entre quienes cancelaron y quienes no.

3. **💰 Boxplot: Cargos Mensuales vs Cancelación**  
   Analiza si los cargos mensuales influyen en la decisión de cancelar.

4. **📉 Gráfico de Barras: Tipo de Contrato vs Cancelación**  
   Examina la relación entre el tipo de contrato y la tasa de cancelación.

## 📁 Fuente de Datos

- [TelecomX_Data.json](https://raw.githubusercontent.com/alura-cursos/challenge2-data-science-LATAM/main/TelecomX_Data.json)

## 🚀 Cómo Ejecutar

1. Clona el repositorio o copia el código en tu entorno local.
2. Asegúrate de tener instaladas las librerías necesarias:
   ```bash
   pip install pandas requests seaborn matplotlib scikit-learn imbalanced-learn
   ```
3. Ejecuta el script en un entorno como Jupyter Notebook o VS Code.

## 📌 Objetivo

Este análisis busca entender los factores que influyen en la cancelación de clientes para ayudar a la empresa a tomar decisiones estratégicas que mejoren la retención.

---
#fin
