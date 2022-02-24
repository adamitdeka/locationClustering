from sklearn.metrics import silhouette_score
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
features = df[['Latitude', 'Longitude']]

sil = []
kmax = 10

# dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
for k in range(2, kmax+1):
  kmeans = KMeans(n_clusters = k).fit(features)
  labels = kmeans.labels_
  sil.append(silhouette_score(features, labels, metric = 'euclidean'))
  #print(k,silhouette_score(features, labels, metric = 'euclidean'))

# Visualize
plt.plot(range(2, kmax+1), sil)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Silhouette Curve')
plt.show()