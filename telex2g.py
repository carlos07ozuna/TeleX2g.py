
## 📊 Visualizaciones Recomendadas

### 1. 🔥 Matriz de Correlación
#Para identificar relaciones entre variables numéricas y su vínculo con la cancelación.


import seaborn as sns
import matplotlib.pyplot as plt

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
