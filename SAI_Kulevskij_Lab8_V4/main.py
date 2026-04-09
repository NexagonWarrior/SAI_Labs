import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_csv('C:/Users/user/Desktop/CSV/Lab_08_Var_04 - Lab_08_Var_04.csv')

X = df[['x', 'y']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = 4
kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

cluster_dfs = {}
for i in range(k):
    cluster_dfs[f'cluster_{i}'] = df[df['cluster'] == i].copy()
    cluster_dfs[f'cluster_{i}'].to_csv(f'cluster_{i}.csv', index=False)
    print(f"Кластер {i} збережено. Кількість точок: {len(cluster_dfs[f'cluster_{i}'])}")

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='x', y='y', hue='cluster', palette='viridis', s=100)

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Центроїди')

plt.title(f'Кластеризація методом k-means (k={k})', fontsize=14)
plt.legend(title='Кластери')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

sil_score = silhouette_score(X_scaled, df['cluster'])
print(f"Коефіцієнт силуету (Silhouette Score): {sil_score:.4f}")
print(f"Інерція (Inertia): {kmeans.inertia_:.2f}")