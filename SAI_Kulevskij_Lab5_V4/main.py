import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('C:/Users/user/Desktop/CSV/titanic.csv')


print("====================/Загальна інформація про список/====================")
print(df.info())
print("\n")

print("====================/Статистичні дані про список/====================")
print(df.describe())
print("\n")

print("============================================================/Виведення перших п'ять пассажирів списку/============================================================")
print(df.head(5))
print("\n")

print("============================================================/Виведення останніх десять пассажирів списку/============================================================")
print(df.tail(10))
print("\n")

print("============================================================/Виведення всіх пассажирів, старше 30-ти, які вижили/============================================================")
new_df = df[(df['Age'] > 30) & (df['Survived'] == 1)].copy()
print(f"Кількість знайдених пасажирів: {len(new_df)}")
print(new_df.head())

print("\n")

print("============================================================/Виведення всіх пассажирів, які мали хоча б одного брата(сестру)/============================================================")
for item in df.index:
    if df.loc[item]['SibSp'] == 1 and df.loc[item]['Survived'] == 1:
        print(df.loc[item])
        print("\n")
print("\n")

print("============================================================/Побудова графіків/============================================================")

bins = [0, 12, 18, 35, 60, 120]
labels = ['Діти', 'Підлітки', 'Молодь', 'Працездатний вік', 'Пенсіонери']

survivors = df[(df['Survived'] == 1) & (df['Age'].notna())].copy()

survivors['AgeCategory'] = pd.cut(survivors['Age'], bins=bins, labels=labels)
age_counts = survivors['AgeCategory'].value_counts().reindex(labels)

plt.figure(figsize=(10, 6))
age_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Кількість врятованих за віковими категоріями', fontsize=14)
plt.xlabel('Вікова категорія', fontsize=12)
plt.ylabel('Кількість людей', fontsize=12)

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(age_counts):
    plt.text(i, v + 1, str(int(v)), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()