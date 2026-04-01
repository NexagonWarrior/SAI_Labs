import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv('C:/Users/user/Desktop/CSV/insurance.csv', sep="\t")
df['charges'] = df['charges'].astype(str).str.rstrip('.').astype(float)


data = df[['age', 'region', 'smoker', 'charges']].copy()
data_encoded = pd.get_dummies(data, columns=['region', 'smoker'], drop_first=True)

X = data_encoded.drop('charges', axis=1)
y = data_encoded['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

comparison_df = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})

comparison_df['Absolute_Error'] = abs(comparison_df['Actual'] - comparison_df['Predicted'])
comparison_df['Error_Percentage'] = (comparison_df['Absolute_Error'] / comparison_df['Actual']) * 100

print(comparison_df.head())

plt.figure(figsize=(10, 6))
plt.hist(comparison_df['Error_Percentage'], bins=30, color='skyblue', edgecolor='black')
plt.title('Гістограма відсоткових значень похибки')
plt.xlabel('Відсоток похибки (%)')
plt.ylabel('Кількість випадків')
plt.grid(axis='y', alpha=0.3)
plt.show()

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mean_error_pct = comparison_df['Error_Percentage'].mean()

print(f"\n--- ВИСНОВОК ---")
print(f"Коефіцієнт детермінації (R2): {r2:.4f}")
print(f"Середня абсолютна похибка (MAE): {mae:.2f}")
print(f"Середній відсоток похибки: {mean_error_pct:.2f}%")