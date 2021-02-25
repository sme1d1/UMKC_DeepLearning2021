# Scott McElfresh sme1d1 ICP6-2
import pandas as pd
from kneed import KneeLocator
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

data = pd.read_csv('CC.csv')  # load dataframe

# Replace null values with mean values

data['CREDIT_LIMIT'].fillna((data['CREDIT_LIMIT'].mean()),
                            inplace=True)  # replace credit limit nulls with mean for credit limit
data['MINIMUM_PAYMENTS'].fillna((data['MINIMUM_PAYMENTS'].mean()),
                                inplace=True)  # replace min payments nulls with mean for minimum payments+

x = data.drop(['CUST_ID'], axis=1)  # Drop customer ID categorical data;

plot3 = plt.figure(3)  # create plot # 3
plt.hist(x['BALANCE'], bins=30)  # define plot - a histogram of the balance feature
# Data is not normally distributed

# print(x.describe()) - check data ranges
scaler = StandardScaler()  # Use Standard Scaler because we don't have data with normal distribution

# Tried StandardScaler and MinMax - (Standard Scaler returns 4 clusters and MinMax 3) Data set contains outliers so
# features won't be fully balanced, but data doesn't have a normal distribution so using Standard Scaler over MinMax

scaler.fit(x)  # fit our data to Standard Scaler function
x_scaled = scaler.transform(x)  # # perform standardization by centering and scaling
x_scaled = pd.DataFrame(x_scaled, columns=x.columns)  # create our data frame with same columns as x dataframe

ssd = []  # sum of squared distances array
sc = []  # silhouette scores array
ninit = 10
ninitplus = ninit + 1
# create a dictionary of key word arguments for kmeans
kmeans_kwargs = {"init": "random", "n_init": ninit, "max_iter": 300, "random_state": 0}

for k in range(1, ninitplus):  # for loop ninitplus times
    km = KMeans(n_clusters=k, **kmeans_kwargs)  # try 1 to 10 cluster sizes for kmeans
    km.fit(x_scaled)  # fit data to model
    ssd.append(km.inertia_)  # append sse array with lowest sse value

for k in range(2, ninitplus):
    km = KMeans(n_clusters=k, **kmeans_kwargs)  # iterate through dictionary and create model
    km.fit(x_scaled)  # fit data to model
    score = silhouette_score(x_scaled, km.labels_)  # create a silhouette score for each amount of cluster group
    sc.append(score)  # append to silhouette score array

    # Silhouette score ranges from -1 to 1.
    # individual sample scores show how close data points are to other points in the cluster

# plot Sum of squared error to find elbow
plot1 = plt.figure(1)
plt.style.use("bmh")
plt.plot(range(1, ninitplus), ssd)
plt.xticks(range(1, ninitplus))
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")

# plot Silhouette Scores
plot2 = plt.figure(2)
plt.style.use("ggplot")
plt.plot(range(2, ninitplus), sc)
plt.xticks(range(2, ninitplus))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")

# use knee-locator to help find optimal cluster amount with elbow method
kl = KneeLocator(range(1, ninitplus), ssd, curve="convex", direction="decreasing")
print("Elbow method determines number of clusters to be: {}".format(kl.elbow))
# elbow is at 4

# get silhouette score for 4 clusters
km = KMeans(n_clusters=kl.elbow, **kmeans_kwargs)  # create kmeans model with 4 clusters
km.fit(x_scaled)  # fit scaled data to model
score = silhouette_score(x_scaled, km.labels_)  # calculate silhouette score of data with labels. (average of all samples)
print("Silhouette score for {} clusters: {}".format(kl.elbow, score))

plt.show()  # display our plot

# feature scaling doesn't improve the Silhouette score but our model
# is more representative because the weight of our features is more balanced.
# Before features were scaled, weight was not even between features.
