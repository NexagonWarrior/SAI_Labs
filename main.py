import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, classification_report

df = pd.read_csv('C:/Users/user/Desktop/CSV/diabetes_data.csv')

print("--- СТРУКТУРА ДАНИХ ---")
print(f"Розмірність: {df.shape}")
print(df.info())
print("\nРозподіл цільової змінної (WaterQuality):")
print(df['WaterQuality'].value_counts())


X = df.drop(columns=['PatientID', 'DoctorInCharge', 'WaterQuality'])
y = df['WaterQuality']

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Розподіл прогнозів моделі:")
print(pd.Series(y_pred).value_counts())

print("\n--- ХАРАКТЕРИСТИКИ ЕФЕКТИВНОСТІ МОДЕЛІ ---")
print(f"Загальна точність (Accuracy): {accuracy_score(y_test, y_pred):.4f}")
print(f"Повнота (Recall): {recall_score(y_test, y_pred):.4f}")
print("\nДетальний звіт класифікації:")
print(classification_report(y_test, y_pred, zero_division=0))

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', 
            xticklabels=['Непридатна', 'Придатна'], 
            yticklabels=['Непридатна', 'Придатна'])
plt.title('Матриця помилок (Water Quality Classification)')
plt.xlabel('Прогноз')
plt.ylabel('Реальність')
plt.show()

accuracy = accuracy_score(y_test, y_pred)
print(f"\n--- ВИСНОВОК ---")
if accuracy > 0.8:
    print(f"Модель продемонструвала високу ефективність з точністю {accuracy*100:.2f}%.")
else:
    print(f"Модель потребує доопрацювання, оскільки точність становить лише {accuracy*100:.2f}%.")