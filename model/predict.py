import os

# Temporary prediction function for Render deployment
# This prevents crash when model file is not available.

MODEL_PATH = 'plant_disease_model.pth'

def predict(image_path):
    # If model file is missing, return a default prediction
    if not os.path.exists(MODEL_PATH):
        print('Model file not found. Returning default prediction.')
        return 'Tomato_healthy'

    # Later we can load the real model here
    return 'Tomato_healthy'