from flask import Flask, request, jsonify
from recommender import recommend_books

app = Flask(__name__)

@app.route('/welcome')
def home():
    return "📚 Welcome to the Book Recommendation API!"

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
