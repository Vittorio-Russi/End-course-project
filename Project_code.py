import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pylab as plt
import pickle as pk

# loading the dataset
df = pd.read_csv("videogames_sales.csv")

# searching correlation between reviews and sales:
plt.figure(figsize=(10,10))
corr_matrix = sns.heatmap(df.corr(), linewidth = 0.5, annot=True, cmap = 'coolwarm')
plt.show()
# by this matrix it can be deduced zero (or almost) correlation, so
# we are going to discard this idea. Then we will try to predict global 
# sales based on the sales of each country

# analyzing dataset for discovering the main videogames markets
n=(df['North America'].mean()*1000000)
e=(df['Europe'].mean()*1000000)
j=(df['Japan'].mean()*1000000)
r=(df['Rest of World'].mean()*1000000)
g=(df['Global'].mean()*1000000)
global_sales = [n,e,j,r,g]

# display results
print("The average sales in North America =", (f"${n:,.3f}")) #comma separated values till 3 decimal place and $ sign
print("The average sales in Europe =",(f"${e:,.3f}"))
print("The average sales in Japan =",(f"${j:,.3f}"))
print("The average sales in other regions =",(f"${r:,.3f}"))
print("The average sales globally =",(f"${g:,.3f}"))

# plot the results
marks=[n,e,j,r,g]
bars=('North America','Europe', 'Japan', 'Rest of World', 'Global')
y=np.arange(len(bars))
plt.bar(y,marks,color='g')
plt.legend(['Sales average in dollars'])
plt.xticks(y,bars)
plt.show()
    
# checking for missing values and dropping them (if belonging to useless features):
for i in range(df.shape[1]):
    nan = df.iloc[:,i].isnull().sum()
    print('> %d, Missing: %d' % (i, nan))
df = df.dropna()
df.reset_index(drop=True, inplace=True)

# defining useful variables and selecting the features for this problem:
platforms = df['Platform']
genres = df['Genre']
publishers = df['Publisher']

columns = ["Platform", "Genre", "Publisher", "North America", "Europe"]

# using labelEncoder convert categorical data into numerical data:
number = LabelEncoder()
df['Platform'] = number.fit_transform(df['Platform'].astype('str'))
df['Genre'] = number.fit_transform(df['Genre'].astype('str'))
df['Publisher'] = number.fit_transform(df['Publisher'].astype('str'))

labels = df["Global"].values
features = df[list(columns)].values

#end analyzing data

##############################################################
##############################################################
##############################################################


# learning phase (linear regression, static train/test division, accuracy)

def learn(labels, features):
    model = linear_model.LinearRegression()
    X = features
    y = labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model.fit(X_train, y_train)
    pk.dump(model, open('model.sav', 'wb'))
    return model

def assess(model):
    acc_train = model.score(X_train, y_train)
    print ("Accuracy in the training data: ", acc_train*100, "%")
    acc_test = model.score(X_test, y_test)
    print ("Accuracy in the test data", acc_test*100, "%")
    return acc_test

# prediction test with new data:
def predict(platform, genre, publisher, na_sales, e_sales, model):
    platform = search_num(platform, platforms, df.Platform)
    genre = search_num(genre, genres, df.Genre)
    publisher = search_num(publisher, publishers, df.Publisher)
    x_test = np.array([platform, genre, publisher, na_sales, e_sales])
    x_test = x_test.reshape(1, 5)
    y = model.predict(x_test)
    print('Predicted global sale: ',y)
    return y

# searching the numbers associated with string after label_encoder used:
def search_num (a,b,c):
    word = str()
    if any (b.isin([a])):
        i=-1
        while word!= a:
            i+=1
            word = b[i]
        a = c[i]
    else:
        print(f"{a} doesn't exist")
    return a
