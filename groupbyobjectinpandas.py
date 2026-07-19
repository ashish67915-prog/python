import numpy as np
import pandas as pd

movies = pd.read_csv("C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/imdb-top-1000.csv")
# genres = movies.groupby('Genre')
# print(genres)

#applying builtin aggregation fuction on groupby object
# print(genres.sum())


#find the top 3 genres by total earning
# genres = movies.groupby('Genre') ['Gross'].sum().sort_values(ascending=False).head(3)
# print(genres)



#find the genre with highest average IMDB rating
# genres = movies.groupby('Genre') ['IMDB_Rating'].mean().sort_values(ascending=False).head(1)
# print(genres)


#find the director with most  popularity
# genres = movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)
# print(genres)

#find the number of movies done by the each actor
# genres = movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False)
# print(genres)


#how to find the number of groups 
# genres = movies.groupby('Genre')
# print(len(genres))


#finding the first ,last ,and nth movies of each genre
# genres = movies.groupby('Genre').size().sort_values(ascending=False)
# print(genres)
# genres = movies.groupby('Genre')
# print(genres.first())
# print(genres.last())
# print(genres.nth(6))



#use of get_group ->for filtering the data
# print(genres.get_group('Horror'))



#use of agg
# genres = movies.groupby('Genre')
# new = genres.agg(
#     {
#         'Runtime':'mean',
#         'IMDB_Rating':'max',
#         'No_of_Votes':'sum',
#         'Gross':'sum',
#         'Metascore':'min'
#     }
# )

# print(new)


#using list
# genres = movies.groupby('Genre')
# new = genres.agg(
#     {
#         'Runtime':['mean','max'],
#         'IMDB_Rating':'max',
#         'No_of_Votes':['sum','max'],
#         'Gross':'sum',
#         'Metascore':'min'
#     }
# )

# print(new)

# genres = movies.groupby('Genre')
# new = genres.agg(['max','min'])
# print(new)


#looping
# for group,data in genres:
#     print(data)


#appy method
#number of movies starting with A in each genres 
# def foo(group):
#     return group['Series_Title'].str.startswith('A').sum()

# print(genres.apply(foo))


#find the ranking of each movie in group according to their IMDB rating
# def movie_ranking(group):
#     group['genre_ranking'] = group['IMDB_Rating'].rank(ascending=False)
#     return group

# print(genres.apply(movie_ranking))


#find normalised IMDB rating groupwise
# def normalise(group):
#     group['norm_rating'] = (group['IMDB_Rating']-group['IMDB_Rating'].min())/(group['IMDB_Rating'].max()-group['IMDB_Rating'].min())
#     return group

# print(genres.apply(normalise))



#groupby on multiple columns
duo = movies.groupby(['Director','Star1'])
#here we apply some operation
# print(duo.size())


# #find the most earning actor->director combo
# print(duo['Gross'].sum().sort_values(ascending=False).head(1))


#agg in multiple columns
print(duo.agg(['max','min']))