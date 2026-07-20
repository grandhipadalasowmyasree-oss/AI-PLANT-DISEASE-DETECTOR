import os
import torch

from dataset import load_dataset
from cnn_model import PlantDiseaseCNN

# Dataset paths
base_path = os.getcwd()
print("========== NEW TRAIN.PY IS RUNNING ==========")
train_path = os.path.join(base_path, "train")
val_path = os.path.join(base_path, "val")

# Load dataset
train_loader, val_loader, train_dataset = load_dataset(train_path, val_path)
print("Training Images:", len(train_dataset))
print("Training Batches:", len(train_loader))

print("Dataset Loaded Successfully!")
print("Number of Classes:", len(train_dataset.classes))
print("Classes:", train_dataset.classes)

# Create CNN model
model = PlantDiseaseCNN(len(train_dataset.classes))
import torch.nn as nn

# Loss Function
criterion = nn.CrossEntropyLoss()
import torch.optim as optim

# Optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)
# Number of epochs
epochs = 10

for epoch in range(epochs):

    print(f"\n===== Epoch {epoch+1} Started =====")

    running_loss = 0.0

    for batch_idx, (images, labels) in enumerate(train_loader):

        print(f"Processing Batch {batch_idx+1}/{len(train_loader)}")

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        # Print only the first 3 batches
        if batch_idx == 2:
            break

    print(f"Epoch [{epoch+1}/{epochs}] Loss: {running_loss:.4f}")








print("\nCNN Model Created Successfully!")
print(model)
print(f"Epoch [{epoch+1}/{epochs}] Loss: {running_loss:.4f}")
# Save the trained model
torch.save(model.state_dict(), "plant_disease_model.pth")

print("\nModel Saved Successfully!")