import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D'],
    'Movie': ['Inception', 'Avatar', 'Titanic', 'Avatar', 'Titanic', 'Inception', 'Titanic', 'Inception'],
    'Rating': [5, 3, 4, 5, 4, 2, 5, 4]
}

df = pd.DataFrame(data)
matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)
scaled = StandardScaler().fit_transform(matrix)
sim = cosine_similarity(scaled)
sim_df = pd.DataFrame(sim, index=matrix.index, columns=matrix.index)

def recommend(user, n=2):
    if user not in matrix.index:
        return None
    similar = sim_df[user].sort_values(ascending=False)[1:]
    rec = pd.Series()
    for other in similar.index:
        ratings = matrix.loc[other]
        unseen = matrix.loc[user] == 0
        rec = rec.add(ratings[unseen], fill_value=0)
    return rec.sort_values(ascending=False).head(n)

print(recommend('C'))
