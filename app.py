from flask import Flask, render_template, request
import os

from predict import predict as model_predict

app = Flask(__name__)

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

# index Page
@app.route("/index")
def index():
    return render_template("index.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Features page
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

    # Predict Disease
    prediction = model_predict(filepath)

    crop = prediction.split("_")[0]
    disease = prediction

    # Temporary confidence
    confidence = 95

    recommendation = recommendations.get(
        disease,
        "Consult Agriculture Expert."
    )

    return render_template(
        "result.html",
        crop=crop,
        disease=disease,
        confidence=confidence,
        recommendation=recommendation,
        image_path=filepath
    )


if __name__ == "__main__":
    app.run(debug=True)
