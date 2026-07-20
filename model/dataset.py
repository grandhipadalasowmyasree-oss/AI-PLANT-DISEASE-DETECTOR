from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Image Preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def load_dataset(train_path, val_path):

    # Load training dataset
    train_dataset = datasets.ImageFolder(
        root=train_path,
        transform=transform
    )

    # Load validation dataset
    val_dataset = datasets.ImageFolder(
        root=val_path,
        transform=transform
    )

    # Create DataLoader
    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        shuffle=True
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=32,
        shuffle=False
    )

    return train_loader, val_loader, train_dataset