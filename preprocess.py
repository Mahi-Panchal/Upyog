from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
])

def preprocess_image(image):

    image = image.convert("RGB")

    img = transform(image)

    img = img.unsqueeze(0)

    return img
