import torch
import torchvision.transforms as transforms
from PIL import Image
import os

# Dummy model simulasi (tanpa training)
# Untuk proyek nyata, model harus dilatih dengan dataset luka
class DummyLukaClassifier(torch.nn.Module):
    def __init__(self):
        super(DummyLukaClassifier, self).__init__()

    def forward(self, x):
        # Simulasi: selalu hasilkan prediksi acak dari 3 kelas
        return torch.tensor([[0.2, 0.5, 0.3]])  # [Ringan, Sedang, Parah]

model = DummyLukaClassifier()
LABELS = ['Ringan', 'Sedang', 'Parah']

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_luka(img_path):
    try:
        img = Image.open(img_path).convert('RGB')
        img_tensor = transform(img).unsqueeze(0)  # Tambah batch dimensi

        with torch.no_grad():
            outputs = model(img_tensor)
            probs = torch.nn.functional.softmax(outputs[0], dim=0)
            predicted_idx = torch.argmax(probs).item()
            confidence = probs[predicted_idx].item()

        return LABELS[predicted_idx], confidence
    except Exception as e:
        print(f"[ERROR] Gagal prediksi gambar: {e}")
        return "Gagal memproses gambar", 0.0
