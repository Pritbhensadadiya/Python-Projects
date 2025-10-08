import pandas as pd
import matplotlib.pyplot as plt

# LOAD THE DATA
df = pd.read_csv('netflix_titles.csv')

# CLEAN THE DATA

df = df.dropna(subset=['type','release_year','rating','country','duration'])

# MOVIES VS TV SHOWS IN NETFLIX

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title("Number of Movies VS TV Shows on Netflix")
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

# CONTENT WATCHING IN PERCENTAGE

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage of Content Rating")
plt.tight_layout()
plt.savefig("content_rating_pie.png")
plt.show()

# MOVIE DURATION DISTRIBUTED

movie_df = df[df['type']=='Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title("Distribution Of Movie Duration")
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig("movie_duration_histogram.png")
plt.show()

# RELEASE YEAR VS NUMBER OF SHOWS 

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index,release_count.values,color='red')
plt.title("Release Year VS Number Of Shows")
plt.xlabel('Release Year')
plt.ylabel('Number OF Shows')
plt.tight_layout()
plt.savefig("release_year_scatter.png")
plt.show()

# TOP 10 COUNTRY AS PER THE NUMBER OF SHOWS 

country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='teal')
plt.title("Top 10 Country By Number Of Shows")
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig("top10_countries.png")
plt.show()

# MOVIES VS TV SHOWS BY YEAR 

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2,figsize=(12,5))

    # first subplot: movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title("Movies Released Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number Of Movies')
    # second subplot: tv shows
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color='orange')
ax[0].set_title("TV Show Released Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number Of Movies')

fig.suptitle('Comparision Between Movies & TV Shows Released Over Year')

plt.tight_layout()
plt.savefig('movies_tvshows_comparision.png')
plt.show()

