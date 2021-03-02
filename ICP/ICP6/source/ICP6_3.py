# Scott McElfresh sme1d1 ICP6-3
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import seaborn as sns
from kneed import KneeLocator

data = pd.read_csv('CC.csv')  # load dataframe

# Replace null values with mean values
data['CREDIT_LIMIT'].fillna((data['CREDIT_LIMIT'].mean()),
                            inplace=True)  # replace credit limit nulls with mean for credit limit
data['MINIMUM_PAYMENTS'].fillna((data['MINIMUM_PAYMENTS'].mean()),
                                inplace=True)  # replace min payments nulls with mean for minimum payments+
x = data.drop(['CUST_ID'], axis=1)  # Drop customer ID categorical data;

# print(x.describe()) - check data ranges
scaler = StandardScaler()  # use StandardScaler
scaler.fit(x)  # fit our data to scaler
x_scaled = scaler.transform(x)  # perform standardization by centering and scaling
x_scaled = pd.DataFrame(x_scaled, columns=x.columns)  # create dataframe from scaled data with same columns as x
pca = PCA(2)  # set Principal Component Analysis to determine 2 principal components
df = pca.fit_transform(x_scaled)  # create data frame from scaled data fit to PCA

ninit = 10
ninitplus = ninit + 1
# define our keyword arguments for kmeans
kmeans_kwargs = {"init": "random", "n_init": ninit, "max_iter": 300, "random_state": 0}

ssd = []
for k in range(1, ninitplus):  # for loop ninitplus times
    km = KMeans(n_clusters=k, **kmeans_kwargs)  # try 1 to 10 cluster sizes for kmeans
    km.fit(df)  # fit data to model
    ssd.append(km.inertia_)  # append sse array with lowest sse value

# use knee-locator to help find optimal cluster amount with elbow method
kl = KneeLocator(range(1, ninitplus), ssd, curve="convex", direction="decreasing")
print("Elbow method determines number of clusters to be: {}".format(kl.elbow))
# elbow is at 4

km = KMeans(n_clusters=kl.elbow, **kmeans_kwargs)  # create kmeans model
km.fit(df)  # fit data to model

# calculate silhouette score of data with labels. (average of all samples)
score = silhouette_score(df, km.labels_)
print("Silhouette score is: {}".format(score))

# silhouette score has gone up with PCA - because we're analyzing our data set based on the most correlated features
# with maximal amount of variance. We're looking at the most significant data so each object
# should be more similar to its own cluster aa compared to other clusters.

# scatter plot points
ulabels = np.unique(km.labels_)  # create unique labels by extracting unique elements in array [0 1 2 3]
for i in ulabels:
    plt.scatter(df[km.labels_ == i, 0], df[km.labels_ == i, 1], label=i)
    # iterate through our labels and scatter plot our
    # points with that label (our X and Y which is our 0 and 1 PCA components)
plot1 = plt.figure(1)
plt.legend()

# Scree plot - show variance of each principal component - check how many components we need
plot2 = plt.figure(2)
df3 = pd.DataFrame({'variance': pca.explained_variance_ratio_,
                    'Principal Components': ['PC1', 'PC2']})
sns.barplot(x='Principal Components', y="variance",
            data=df3, color="r")

plt.show()  # show our plot
