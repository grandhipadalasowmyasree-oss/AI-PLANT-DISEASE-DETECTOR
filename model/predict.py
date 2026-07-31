import torch
from torchvision import transforms
from PIL import Image

from cnn_model import PlantDiseaseCNN

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])
classes = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]
# Create the CNN model
model = PlantDiseaseCNN(len(classes))

# Load the trained weights
model.load_state_dict(torch.load("plant_disease_model.pth"))

# Set the model to evaluation mode
model.eval()
def predict(image_path):

    # Open the image
    image = Image.open(image_path).convert("RGB")

    # Resize and convert to tensor
    image = transform(image)

    # Add batch dimension
    image = image.unsqueeze(0)

    # Disable gradient calculation
    with torch.no_grad():

        # Predict
        output = model(image)

        # Get predicted class
        _, predicted = torch.max(output, 1)

    return classes[predicted.item()]

if __name__ == "__main__":

    image_path = r"C:\Users\grand\Downloads\AI Plant Disease Detector\YOUR_IMAGE_PATH.JPG"

    prediction = predict(image_path)

    print("Predicted Disease:", prediction)
if __name__ == "__main__":

    image_path = r"C:\Users\grand\Downloads\AI Plant Disease Detector\test\Tomato_healthy\image1.JPG"

    prediction = predict(image_path)

    print("Predicted Disease:", prediction)