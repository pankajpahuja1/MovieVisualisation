# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import os


# %%
movie=pd.read_csv("P4-Movie-Ratings.csv")


# %%
os.getcwd()


# %%
movie


# %%
movie.head()


# %%
movie.tail()


# %%
movie.columns


# %%
movie.columns=['Film', 'Genre', 'criticRatings', 'audienceRatings',
       'Budgetmillion', 'Yearrelease']


# %%
movie.columns


# %%
import matplotlib.pyplot as plt


# %%
plt.hist(movie.Budgetmillion)


# %%
movie.Genre=="action"


# %%
movie.head()


# %%
movie[movie.Genre=="Action"]


# %%
movie[movie.Genre=="Action"].Budgetmillion


# %%
plt.hist(movie[movie.Genre=="Action"].Budgetmillion)
plt.hist(movie[movie.Genre=="Comedy"].Budgetmillion)
plt.show()


# %%
movie.info()


# %%
movie.Film=movie.Film.astype('category')
movie.Genre=movie.Genre.astype('category')
movie.Yearrelease=movie.Yearrelease.astype('category')


# %%
movie.info()


# %%
movie.Yearrelease


# %%
movie.head()


# %%
movie.tail()


# %%
a=movie.Genre.cat.categories


# %%
for i in movie.Genre.cat.categories:
    plt.hist(movie[movie.Genre==i].Budgetmillion,stacked="True",bins=10,label=i)
plt.legend()
plt.show()


# %%
import seaborn as sns


# %%
for i in movie.Genre.cat.categories:
    sns.distplot(movie[movie.Genre==i].Budgetmillion,bins=10,label=i)


# %%



# %%


