from flask import Flask, render_template, request, session
import os

from model.predict import predict as model_predict

app = Flask(__name__)
app.secret_key = "plantai123"

# Upload folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Disease Recommendations
recommendations = {
    "Tomato_Early_blight": "Remove infected leaves and spray fungicide.",
    "Tomato_Late_blight": "Avoid excess watering and use copper fungicide.",
    "Tomato_healthy": "Healthy plant. No treatment required.",
    "Potato_Early_blight": "Apply recommended fungicide.",
    "Potato_Late_blight": "Remove infected plants immediately.",
    "Potato_healthy": "Healthy plant.",
    "Pepper__bell___healthy": "Healthy plant.",
    "Pepper__bell___Bacterial_spot": "Use disease-free seeds and spray bactericide."
}

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Index Page
@app.route("/index")
def index():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Features Page
@app.route("/features")
def features():
    return render_template("features.html")

# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No image uploaded!"

    file = request.files["file"]

    if file.filename == "":
        return "No image selected!"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    prediction = model_predict(filepath)

    crop = prediction.split("_")[0]
    disease = prediction
    confidence = 95

    recommendation = recommendations.get(
        disease,
        "Consult Agriculture Expert."
    )

    session["crop"] = crop
    session["disease"] = disease
    session["confidence"] = confidence
    session["recommendation"] = recommendation
    session["image_path"] = filepath

    return render_template(
        "dashboard.html",
        crop=session.get("crop"),
        disease=session.get("disease"),
        confidence=session.get("confidence"),
        recommendation=session.get("recommendation"),
        image_path=session.get("image_path")
    )

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        crop=session.get("crop"),
        disease=session.get("disease"),
        confidence=session.get("confidence"),
        recommendation=session.get("recommendation"),
        image_path=session.get("image_path")
    )

if __name__ == "__main__":
    app.run(debug=True)