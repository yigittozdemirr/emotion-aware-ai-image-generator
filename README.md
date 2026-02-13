\# 🎭 Gerçek Zamanlı Duygu Tabanlı Yapay Zekâ Görsel Üretim Sistemi



Bu proje, canlı kamera görüntüsünden yüz tespiti yaparak kullanıcının duygu durumunu analiz eden ve tespit edilen duyguya göre otomatik olarak görsel üreten bir yapay zekâ uygulamasıdır.



Projede \*\*Bilgisayarla Görme (Computer Vision)\*\* ve \*\*Üretken Yapay Zekâ (Generative AI)\*\* sistemleri entegre edilmiştir.



---



\## 🚀 Özellikler



\- 🎥 Gerçek zamanlı yüz tespiti (YOLO tabanlı)

\- 😊 6 temel duygu sınıflandırması:

&nbsp; - Mutlu

&nbsp; - Üzgün

&nbsp; - Kızgın

&nbsp; - Korku

&nbsp; - Şaşkın

&nbsp; - Nötr

\- 🎨 Duyguya bağlı otomatik görsel üretimi

\- 🔁 Otomatik üretim modu

\- 🖥️ PySide6 ile geliştirilmiş masaüstü arayüz

\- ⚡ GPU (CUDA) destekli çalışma



---



\## 🧠 Kullanılan Teknolojiler



\- Python 3.10

\- OpenCV

\- PyTorch

\- Ultralytics YOLOv8 / YOLO11

\- NumPy

\- PySide6



\### 📊 Veri Seti



\- FER-2013 (Facial Expression Recognition Dataset)



---



\## 🏗️ Sistem Mimarisi



1️⃣ Yüz Tespiti (YOLO Face Model)  

2️⃣ Duygu Sınıflandırma (YOLO Classification Model)  

3️⃣ Prompt Motoru (Duygu → Metin Prompt Dönüşümü)  

4️⃣ Yapay Zekâ Görsel Üretimi  

5️⃣ Arayüz Üzerinde Sonuç Gösterimi  



---



\## 📈 Model Performansı



\### Duygu Sınıflandırma



| Model      | Top-1 Accuracy | Top-5 Accuracy |

|------------|----------------|----------------|

| YOLOv8s    | 65.12%         | 99.35%         |

| YOLOv8n    | 67.30%         | 99.43%         |

| YOLO11n    | 67.30%         | 99.43%         |



\### Yüz Tespiti



| Model         | mAP50 | mAP50-95 |

|--------------|-------|----------|

| YOLOv8n-face | 37.5  | 78.2     |

| YOLOv8s-face | 40.6  | 82.5     |

| YOLOv8m-face | 41.7  | 84.8     |



> Yüz tespiti metrikleri ilgili model dokümantasyonlarından alınmıştır.



---



\## ⚙️ Kurulum



\### 1️⃣ Depoyu klonlayın



```bash

git clone https://github.com/yigittozdemirr/real-time-emotion-ai-generator

cd real-time-emotion-ai-generator

2️⃣ Sanal ortam oluşturun

Kodu kopyala

python -m venv venv

venv\\Scripts\\activate

3️⃣ Gerekli kütüphaneleri yükleyin

Kodu kopyala

pip install -r requirements.txt

📦 Model Kurulumu (Önemli)

Model dosyaları büyük boyutlu olduğu için GitHub reposuna dahil edilmemiştir.



Gerekli model dosyaları:



Duygu sınıflandırma modeli (.pt)



Yüz tespit modeli (.pt)



Görsel üretim modeli (.safetensors)



İndirilen model dosyalarını aşağıdaki klasöre yerleştiriniz:



Kodu kopyala

models/

Eğer Ultralytics YOLO ön-eğitimli modelleri kullanıyorsanız:



Kodu kopyala

pip install ultralytics

YOLO gerekli ağırlıkları otomatik olarak indirecektir.



▶️ Uygulamayı Çalıştırma

Kodu kopyala

python main.py

Kamera açılacak ve gerçek zamanlı duygu analizi başlayacaktır.



📁 Proje Yapısı

Kodu kopyala

├── main.py

├── image\_generator.py

├── prompt\_engine.py

├── sayisal\_ui.py

├── sayisal.ui

├── models/

├── requirements.txt

└── README.md

🔮 Gelecek Geliştirmeler

Çoklu yüz desteği



Zamansal duygu geçiş analizi



Bulut tabanlı dağıtım



Ses + mimik entegre duygu analizi



Web tabanlı versiyon (FastAPI + React)



🎯 Projenin Amacı

Bu proje aşağıdaki alanların entegrasyonunu deneyimlemek amacıyla geliştirilmiştir:



Gerçek zamanlı bilgisayarla görme sistemleri



Derin öğrenme tabanlı sınıflandırma modelleri



Duygu farkındalıklı üretken yapay zekâ sistemleri



Etkileşimli masaüstü uygulama geliştirme



👤 Geliştirici

Yiğit Özdemir

Yazılım Mühendisliği Öğrencisi

Yapay Zekâ \& Bilgisayarla Görme Çalışmaları

