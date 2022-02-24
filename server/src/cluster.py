import pdb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def create_cluster():
	df = pd.read_csv('data.csv')
	features = df[['Latitude', 'Longitude']]
	# Remove the comments of to see actual plot of the given dataset

	# plt.scatter(df['Latitude'],df['Longitude'], s=50, cmap='viridis')
	# plt.show()
	# pdb.set_trace()

	kmeans = KMeans(n_clusters = 4, init ='k-means++')
	kmeans.fit(features) # Compute k-means clustering.

	centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
	##print("Centers",centers[:,1])

	labels = kmeans.predict(features) # Labels of each point
	
	cluster_group = {}
	for idx,cluster_id in enumerate(labels.tolist()):
		if cluster_group.get(cluster_id,False):
			cluster_group[cluster_id].append(features.values[idx].tolist()) 
		else:
			cluster_group[cluster_id] = [features.values[idx].tolist()]

	# features.plot.scatter(x = 'Latitude', y = 'Longitude', c=labels, s=50, cmap='viridis')
	# plt.grid()
	# plt.show()
	return cluster_group
create_cluster()