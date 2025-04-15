from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the zero-shot classification model
classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-MiniLM2-L6-H768")

# Define categories
CATEGORIES = [
    "Politics",
    "Entertainment",
    "Sports",
    "Science",
    "Technology",
    "Crime",
    "Business",
    "World",
    "Environment",
    "Health",
    "Education",
    "Education",
    "Social",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def classify():
    data = request.form.get("article")
    if not data:
        return jsonify({"error": "No article provided"}), 400

    # Perform classification
    result = classifier(data, CATEGORIES)
    category = result["labels"][0]  # Best match
    scores = dict(zip(result["labels"], result["scores"]))

    return jsonify({"category": category, "scores": scores})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
