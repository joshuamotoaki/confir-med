import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# Define the list of medicines for mapping predictions
medicines = [
    'Alaxan',
    'Bactidol',
    'Bioflu',
    'Biogesic',
    'DayZinc',
    'Fish Oil',
    'Kremil S',
    'Medicol',
    'Neozep',
]

# Define the CNN model architecture (the same as the training code)
class CNN(nn.Module):
    def __init__(self, num_classes=9):
        super().__init__()
        self.feature_extractor = nn.Sequential(
            nn.Conv2d(3, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 2)),
            nn.Conv2d(256, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 2)),
            nn.Conv2d(128, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 2))
        )
        # Adjust dummy input to match image size (100x100)
        dummy_input = torch.zeros(1, 3, 100, 100)
        in_features = self.feature_extractor(dummy_input).view(1, -1).size(1)
        self.classifier = nn.Sequential(
            nn.Linear(in_features, 128),
            nn.Dropout(0.2),
            nn.ReLU(inplace=True),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.feature_extractor(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

# Initialize and load the model weights
model = CNN(num_classes=9)
model.load_state_dict(torch.load(r'apps\api\pretrained-models\cnn2.pth'))
model.eval()  # Set to evaluation mode

# Preprocessing for the input image
test_transform = transforms.Compose([
    transforms.Resize((100, 100)),  # Ensure this matches the model input size
    transforms.ToTensor()
])

def predict(image_path, model):
    # Load and preprocess the image
    image = Image.open(image_path)
    image = test_transform(image).unsqueeze(0)  # Add batch dimension

    # Run the model on the input image
    with torch.no_grad():
        output = model(image)
        # Apply softmax to get probabilities
        probabilities = torch.softmax(output, dim=1)
        # Get the top probability and the corresponding class
        confidence, predicted = torch.max(probabilities, dim=1)

    # Map prediction to medicine name
    predicted_medicine = medicines[predicted.item()]
    return predicted_medicine, confidence.item()

def plot_prediction(image_path, predicted_medicine, confidence, fig_width=5, fig_height=5, dpi=100):
    # Load the original image
    image = Image.open(image_path)

    # Plot the image with the prediction label
    plt.figure(figsize=(fig_width, fig_height), dpi=dpi)  # Define figure size and DPI
    plt.imshow(image)
    plt.axis('off')  # Hide axes
    plt.title(f"Predicted: {predicted_medicine} ({confidence * 100:.2f}%)")
    plt.show()

# Run the prediction and plot the result with specific resolution
predicted_medicine, confidence = predict(r"apps\api\medicine-pics\fish_sample.jpg", model)
print(f"Predicted medicine: {predicted_medicine}, Confidence: {100*confidence:.2f}%")
plot_prediction(r"apps\api\medicine-pics\fish_sample.jpg", predicted_medicine, confidence, fig_width=6, fig_height=6, dpi=100)