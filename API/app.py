from flask import Flask, request, jsonify
#from recommender import recommend_books
import numpy as np
import pickle

app = Flask(__name__)


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

@app.route('/welcome')
def home():
    return "📚 Welcome to the Book Recommendation api!"

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    if not title:
        return jsonify({'error': 'Missing "title" parameter'}), 400
    recommendations = recommend_books(title)
    if not recommendations:
        return jsonify({'message': 'No recommendations found.'})
    return jsonify({'recommendations': recommendations})

@app.route('/liveness')
def liveness_check():
    return "Book recommendation system is live!"

# 👇 REMOVE this block for Vercel deployment
# if __name__ == '__main__':
#     app.run(debug=True)
