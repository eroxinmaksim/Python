import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import  make_blobs
from sklearn.cluster import KMeans

# dataset = make_blobs(n_samples= 200,
#                      centers= 4,
#                      n_features= 2,
#                      cluster_std=1.6,
#                      random_state= 50)
# print(dataset[0])
# print(type(dataset[0]))
# # [[-1.06705283e+00  9.24306355e+00]
#  # [ 1.08654318e+00 -6.94815805e+00]]
# points = dataset[0]
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(points)
# plt.scatter(dataset[0][:,0],dataset[0][:,1])
# plt.show()
# clsters = kmeans.cluster_centers_
# print("---")
# print(clsters)

points = []
x = []
y = []
amount = 4

txt = open("s1.txt", "r")
lines = txt.readlines()
for i in lines:
    tmp = i.split()
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    points.append(tmp)

# #обычный массив "х" и "у"
# for item in points:
#     x.append(item[0])
#     y.append(item[1])



def createCentroids():
    arr = []
    for i in range(amount):
        arr.append([])
        for j in range(2):
            arr[i].append(np.random.randint(0, max(max(x),max(y))))
    arr = np.array(arr)
    return arr

points = np.array(points)

# clusters = np.array(createCentroids())


# kmeans = KMeans(n_clusters = amount)
# kmeans.fit(points)
# clusters = kmeans.cluster_centers_
# plt.scatter(points[:,0],points[:,1])
# plt.show()
#
# y_km = kmeans.fit_predict(points)
# plt.scatter(points[y_km == 0,0], points[y_km == 0,1], s=50, color ='r')
# plt.scatter(points[y_km == 1,0], points[y_km == 1,1], s=50, color ='g')
# plt.scatter(points[y_km == 2,0], points[y_km == 2,1], s=50, color ='y')
# plt.scatter(points[y_km == 3,0], points[y_km == 3,1], s=50, color ='c')
#
# plt.scatter(clusters[0][0],clusters[0][1],marker='*', s=100,color = 'b')
# plt.scatter(clusters[1][0],clusters[1][1],marker='*', s=100,color = 'b')
# plt.scatter(clusters[2][0],clusters[2][1],marker='*', s=100,color = 'b')
# plt.scatter(clusters[3][0],clusters[3][1],marker='*', s=100,color = 'b')
# plt.show()








# print(x)
# print(y)
# clusters = 5
# def createCentroids():
#     arr = []
#     for i in range(clusters):
#         arr.append([])
#         for j in range(2):
#             arr[i].append(np.random.randint(0, max(x)))
#     return arr
#
# kmeans = KMeans(n_clusters=clusters)
# kmeans.fit(points)
# plt.scatter(x,y)
# plt.show()
# clusters = createCentroids()
# print(clusters)






