from flask import Flask, render_template, request, jsonify
import pickle
import requests

app = Flask(__name__)

# load models
similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pickle.load(open("movies.pkl", "rb"))
svd_model = pickle.load(open("svd_model.pkl", "rb"))

# ---------------- POSTER FUNCTION (SAFE) ----------------
API_KEY ="f0d4548a99dde1c53265d8eab7544cd7"

def fetch_poster(movie):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}"
        res = requests.get(url, timeout=5)
        data = res.json()

        if data.get("results") and data["results"][0].get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["results"][0]["poster_path"]
    except:
        pass

    return "https://via.placeholder.com/200x300?text=No+Image"

# ---------------- COSINE ----------------
def recommend_cosine(movie):
    similar = similarity[movie].sort_values(ascending=False)[1:6]

    results = []
    for m in similar.index:
        results.append({
            "title": m,
            "poster": fetch_poster(m)
        })
    return results

# ---------------- SVD ----------------
def recommend_svd(user_id):
    user_data = svd_model.loc[user_id].sort_values(ascending=False).head(5)

    results = []
    for m in user_data.index:
        results.append({
            "title": m,
            "poster": fetch_poster(m)
        })
    return results

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/movies")
def get_movies():
    return jsonify(movies)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json

    try:
        if data["type"] == "cosine":
            result = recommend_cosine(data["input"])
        else:
            result = recommend_svd(int(data["input"]))
    except:
        return jsonify([])

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)