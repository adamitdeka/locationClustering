from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
features = df[['Latitude', 'Longitude']]

# function returns WSS score for k values from 1 to kmax
def calculate_WSS(points, kmax):
  sse = []
  for k in range(1, kmax+1):
    kmeans = KMeans(n_clusters = k).fit(points)
    centroids = kmeans.cluster_centers_
    pred_clusters = kmeans.predict(points)
    curr_sse = 0
    # import pdb;pdb.set_trace()
    # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
    for i in range(len(points)):
      curr_center = centroids[pred_clusters[i]]
      curr_sse += (points.values.tolist()[i][0] - curr_center[0]) ** 2 + (points.values.tolist()[i][1] - curr_center[1]) ** 2
    sse.append(curr_sse)
  return sse

kmax = 10
sse = calculate_WSS(features,kmax)

# Visualize
plt.plot(range(1, kmax+1), sse)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()