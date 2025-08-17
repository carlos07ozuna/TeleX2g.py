
# 📦 Importación de librerías
import pandas as pd
import requests
import json
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE

# 🔄 Función para desanidar columnas con diccionarios (recursiva)
def desanidar_columnas(df):
    while True:
        dict_cols = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, dict)).any()]
        if not dict_cols:
            break
        for col in dict_cols:
            print(f"Desanidando columna: {col}")
            nested_df = df[col].apply(pd.Series)
            nested_df.columns = [f"{col}_{subcol}" for subcol in nested_df.columns]
            df = pd.concat([df.drop(columns=[col]), nested_df], axis=1)
    return df

# 🟢 1. Cargar datos desde JSON
url = "https://raw.githubusercontent.com/alura-cursos/challenge2-data-science-LATAM/main/TelecomX_Data.json"
response = requests.get(url)
data = json.loads(response.text)
df_raw = pd.DataFrame(data)

# 🟢 2. Desanidar columnas
df_flat = desanidar_columnas(df_raw.copy())

# 🟢 3. Eliminar columnas innecesarias
if "customerID" in df_flat.columns:
    df_flat.drop(columns=["customerID"], inplace=True)

# 🟢 4. Codificación One-Hot
df_encoded = pd.get_dummies(df_flat, drop_first=True)

# 🟢 5. Proporción de cancelación
print("\nProporción de cancelación:")
print(df_flat["Churn"].value_counts(normalize=True))

# 🟢 6. Separar variables
X = df_encoded.drop("Churn_Yes", axis=1)
y = df_encoded["Churn_Yes"]

# 🟢 7. Balanceo con SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# 🟢 8. Normalización
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_resampled)

# 🟢 9. Separación de datos
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_resampled, test_size=0.3, random_state=42
)

# 🟢 10. Modelos
model_lr = LogisticRegression()
model_rf = RandomForestClassifier()

model_lr.fit(X_train, y_train)
model_rf.fit(X_train, y_train)

# 🟢 11. Evaluación
def evaluar_modelo(modelo, X_test, y_test, nombre):
    print(f"\n🔍 Evaluación del modelo: {nombre}")
    y_pred = modelo.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

evaluar_modelo(model_lr, X_test, y_test, "Regresión Logística")
evaluar_modelo(model_rf, X_test, y_test, "Random Forest")

# 🟢 12. Importancia de variables (Random Forest)
importances = model_rf.feature_importances_
features = X.columns
importancia_df = pd.DataFrame({"Feature": features, "Importance": importances})
print("\n🔝 Variables más importantes según Random Forest:")
print(importancia_df.sort_values(by="Importance", ascending=False).head(10))



## 📊 Visualizaciones Recomendadas

### 1. 🔥 Matriz de Correlación
#Para identificar relaciones entre variables numéricas y su vínculo con la cancelación.


#import seaborn as sns
#import matplotlib.pyplot as plt

# Solo variables numéricas
corr_matrix = df_encoded.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, cmap="coolwarm", annot=False, fmt=".2f")
plt.title("🔍 Matriz de Correlación")
plt.show()

### 2. 📦 Boxplot: Tenencia vs Cancelación
#Visualiza cómo varía la tenencia (`customer_tenure`) entre clientes que cancelaron y los que no.


sns.boxplot(x=df_flat["Churn"], y=df_flat["customer_tenure"])
plt.title("📦 Tenencia del Cliente vs Cancelación")
plt.xlabel("¿Canceló?")
plt.ylabel("Meses como cliente")
plt.show()


### 3. 💰 Boxplot: Cargos Mensuales vs Cancelación
#Explora si los cargos mensuales influyen en la decisión de cancelar.


sns.boxplot(x=df_flat["Churn"], y=df_flat["account_Charges"]["Monthly"])
plt.title("💰 Cargos Mensuales vs Cancelación")
plt.xlabel("¿Canceló?")
plt.ylabel("Monto mensual")
plt.show()


### 4. 📉 Gráfico de Barras: Tipo de Contrato vs Cancelación
#Muestra cómo el tipo de contrato afecta la tasa de cancelación.


sns.countplot(x="account_Contract", hue="Churn", data=df_flat)
plt.title("📉 Tipo de Contrato vs Cancelación")
plt.xlabel("Tipo de contrato")
plt.ylabel("Cantidad de clientes")
plt.legend(title="¿Canceló?")
plt.xticks(rotation=45)
plt.show()