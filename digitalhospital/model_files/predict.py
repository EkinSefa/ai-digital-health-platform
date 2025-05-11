import joblib
import numpy as np
import re
import string
import torch
import torch.nn as nn
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

# 🧠 PyTorch model sınıfı
class DeepModel(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(DeepModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, 512)
        self.dropout1 = nn.Dropout(0.4)
        self.fc2 = nn.Linear(512, 256)
        self.dropout2 = nn.Dropout(0.3)
        self.fc3 = nn.Linear(256, 128)
        self.out = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = F.relu(self.fc3(x))
        return self.out(x)

# 🔄 Gereksiz karakterleri temizleme
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return re.sub(r'\s+', ' ', text).strip()

# 🔃 Modelleri yükle (bir kere)
mpnet = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# PCA ve LabelEncoder'ı yükleyin
pca = joblib.load('model_files/pca_model.pkl')
label_encoder = joblib.load('model_files/label_encoder.pkl')

# 🔢 Girdi boyutu PCA'dan alınır
input_dim = pca.components_.shape[0]  # PCA komponentlerinin boyutunu alıyoruz
num_classes = len(label_encoder.classes_)  # sınıf sayısını alıyoruz

# 📦 PyTorch modelini yükle
model = DeepModel(input_dim=input_dim, num_classes=num_classes)
model.load_state_dict(torch.load('model_files/deep_model.pt'))
model.eval()  # modeli değerlendirme moduna alıyoruz

# 🧪 Tahmin fonksiyonu
from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    try:
        translated = translator.translate(text, src='tr', dest='en')
        return translated.text
    except Exception as e:
        print("Çeviri hatası:", e)
        return text  # çeviri başarısızsa orijinal metni kullan

def predict_text(text):
    # Metni İngilizceye çevir
    translated_text = translate_to_english(text)

    # Temizleme
    text_clean = clean_text(translated_text)

    # MPNet ile vektöre dönüştür
    vector = mpnet.encode([text_clean])

    # PCA uygula
    vector_pca = pca.transform(vector)
    x_tensor = torch.tensor(vector_pca, dtype=torch.float32)

    # Tahmin
    with torch.no_grad():
        logits = model(x_tensor)
        probabilities = torch.softmax(logits, dim=1).numpy().flatten()

    # Yüzdelikler
    class_probs = {
        label: round(prob * 100, 2)
        for label, prob in zip(label_encoder.classes_, probabilities)
    }

    # En yüksek olasılık
    predicted_label = max(class_probs, key=class_probs.get)

    return predicted_label, class_probs

