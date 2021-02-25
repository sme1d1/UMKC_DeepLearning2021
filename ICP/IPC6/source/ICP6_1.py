# Scott McElfresh sme1d1 ICP6-1

# import libraries
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from kneed import KneeLocator

data = pd.read_csv('CC.csv')  # load dataframe
# print(data.head())  # debug

# Check for nulls
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
# from class slides - detect sums of null values for all features in dataset and add them
# to nulls dataframe
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls.head())

# found 313 nulls in minimum_payments and 1 credit_limit - replace with mean values

data['CREDIT_LIMIT'].fillna((data['CREDIT_LIMIT'].mean()),
                            inplace=True)  # replace credit limit nulls with mean for credit limit
data['MINIMUM_PAYMENTS'].fillna((data['MINIMUM_PAYMENTS'].mean()),
                                inplace=True)  # replace min payments nulls with mean for minimum payments+

X = data.drop(['CUST_ID'], axis=1)  # Drop customer ID categorical data;
# print(x.shape)

ssd = []  # define sum of squared distance array for elbow method
sc = []  # define silhouette scores array
ninit = 10  # number of randomly chosen centroids
ninitplus = ninit + 1
# create a dictionary of key word arguments for kmeans - avoid typing out all the parameters each time we use kmeans.
kmeans_kwargs = {"init": "random", "n_init": ninit, "max_iter": 300, "random_state": 42}

for k in range(1, ninitplus):  # for loop 10 times
    km = KMeans(n_clusters=k, **kmeans_kwargs)  # try 1 to ninitplus cluster sizes for kmeans
    km.fit(X)  # fit data to model
    ssd.append(km.inertia_)  # append sse array with lowest sse value

for k in range(2, ninitplus):
    km = KMeans(n_clusters=k, **kmeans_kwargs)  # iterate through dictionary and create model
    km.fit(X)  # fit data to model
    score = silhouette_score(X, km.labels_)  # create a silhouette score for each amount of cluster group
    sc.append(score)  # append to silhouette score array

    # Silhouette score ranges from -1 to 1.
    # individual sample scores show how close data points are to other points in the cluster

# plot Sum of squared error to find elbow
plot1 = plt.figure(1)  # create figure 1
plt.style.use("bmh")  # set style
plt.plot(range(1, ninitplus), ssd)  # define what we're plotting (sum of square distances)
plt.xticks(range(1, ninitplus))  # set x-ticks values
plt.xlabel("Number of Clusters")  # label x axis
plt.ylabel("SSD")  # label Y axis

# plot Silhouette Scores
plot2 = plt.figure(2)  # create figure 2
plt.style.use("ggplot")  # set style
plt.plot(range(2, ninitplus), sc)  # define what we're plotting (silhouette scores)
plt.xticks(range(2, ninitplus))  # set x-ticks values
plt.xlabel("Number of Clusters")  # label x axis
plt.ylabel("Silhouette Coefficient")  # label Y axis

# use Kneed library to find elbow from kaggle - help determine optimal numbers of cluster with elbow method
kl = KneeLocator(range(1, ninitplus), ssd, curve="convex", direction="decreasing")
print("\nElbow method determines number of clusters to be: {}".format(kl.elbow))


# get silhouette score for 3 clusters
km = KMeans(n_clusters=kl.elbow, **kmeans_kwargs)  # create kmeans model
km.fit(X)  # fit data to model
score = silhouette_score(X, km.labels_)  # calculate silhouette score of data with labels. (average of all samples)
print("Silhouette score for {} clusters: {}".format(kl.elbow, score))

plt.show()  # display our plots
