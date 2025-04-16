# def recommend_books(title):
#     if title is not None:
#         return "Rites of Passage"


import numpy as np
import pickle

# Load Pickle
with open("recommender_model.pkl", "rb") as file:
    data = pickle.load(file)

#print(data)
pt = data.get('pt_data')
similarity_score = data.get('similarity_matrix')
books = data.get('books')
def recommend_books(book_name):
    index = np.where(pt.index==book_name)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1], reverse=True)[1:6]

    data = []

    for i in similar_books:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    return data