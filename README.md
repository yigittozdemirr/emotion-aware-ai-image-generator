# 🎭 Emotion-Aware AI Image Generator

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLOv8%20/%20YOLO11-Ultralytics-orange)

An advanced AI-powered desktop application that analyzes real-time facial expressions via a live camera feed and automatically generates contextual images based on the user's detected emotional state. 

This project seamlessly integrates **Computer Vision (CV)** for facial analysis and **Generative AI** for automated, emotion-driven digital art creation.

---

## 🚀 Key Features

- **🎥 Real-Time Face Detection:** High-performance detection powered by YOLO models.
- **😊 Emotion Classification:** Accurately classifies 6 basic emotional states:
  - Happy | Sad | Angry | Fear | Surprise | Neutral
- **🎨 Emotion-to-Image Generation:** Dynamic translation of detected emotions into text prompts for automated AI image synthesis.
- **🔁 Auto-Generation Mode:** Continuous analysis and image generation loop.
- **🖥️ Native Desktop GUI:** Built with PySide6 for a responsive and intuitive user experience.
- **⚡ GPU Acceleration:** Full CUDA support for real-time inference and generation.

## 🧠 Tech Stack & Datasets

- **Core:** Python 3.10
- **Computer Vision:** OpenCV, NumPy
- **Deep Learning:** PyTorch, Ultralytics (YOLOv8 / YOLO11)
- **Generative AI:** Stable Diffusion v1.5 (Latent Diffusion Architecture)
- **GUI:** PySide6
- **Dataset:** FER-2013 (Facial Expression Recognition Dataset)

## 🏗️ System Architecture

The pipeline operates in 5 continuous stages:
1. **Face Detection:** YOLO Face Model extracts facial bounding boxes from the live feed.
2. **Emotion Classification:** YOLO Classification Model evaluates the cropped face.
3. **Prompt Engine:** The detected emotion is dynamically mapped to a text-to-image prompt.
4. **AI Generation:** The generative model synthesizes a new image based on the prompt.
5. **UI Display:** Results (emotion state, bounding boxes, and generated image) are rendered on the PySide6 dashboard.

## 📈 Model Performance

### Emotion Classification
| Model | Top-1 Accuracy | Top-5 Accuracy |
|:---:|:---:|:---:|
| YOLOv8s | 65.12% | 99.35% |
| YOLOv8n | 67.30% | 99.43% |
| YOLO11n | 67.30% | 99.43% |

### Face Detection
| Model | mAP50 | mAP50-95 |
|:---:|:---:|:---:|
| YOLOv8n-face | 37.5 | 78.2 |
| YOLOv8s-face | 40.6 | 82.5 |
| YOLOv8m-face | 41.7 | 84.8 |
> *Detection metrics are referenced from the official model documentation.*

## ⚙️ Installation & Setup

### 1. Clone the Repository
git clone [https://github.com/yigittozdemirr/emotion-aware-ai-image-generator.git](https://github.com/yigittozdemirr/emotion-aware-ai-image-generator.git)
cd emotion-aware-ai-image-generator


### 2. Create a Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Model Weights Configuration (Important)
Due to GitHub file size limits, the pre-trained weights are not included in this repository. You must download and place the required models in the models/ directory:
Emotion classification model (.pt)
Face detection model (.pt)
Generative model (.safetensors - Stable Diffusion v1.5 architecture)

Note: If you are using Ultralytics pre-trained models, running pip install ultralytics will automatically download the required YOLO weights upon first run.

▶️ Usage
Start the application by running the main entry point:

python main.py
The camera feed will initialize, and real-time emotion analysis will begin immediately.

📁 Project Structure
.
├── models/                  # Pre-trained weights (.pt, .safetensors)
├── main.py                  # Application entry point
├── image_generator.py       # AI generation module (Stable Diffusion)
├── prompt_engine.py         # Emotion-to-text mapping logic
├── sayisal_ui.py            # Compiled PySide6 UI logic
├── sayisal.ui               # Qt Designer UI file
├── requirements.txt         
└── README.md

🔮 Future Roadmap
[ ] Multi-Face Support: Analyze and generate responses for multiple users in frame.

[ ] Temporal Emotion Tracking: Analyze emotional transitions over time rather than isolated frames.

[ ] Cloud Deployment: Migrate inference to scalable cloud instances.

[ ] Multimodal Inputs: Integrate audio and vocal tone analysis with facial expressions.

[ ] Web Version: Port the interface to a web architecture (FastAPI backend + React frontend).

👤 Author
Yiğit Özdemir
Software Engineering Student | AI & Computer Vision Enthusiast

GitHub: @yigittozdemirr

Project Link: [emotion-aware-ai-image-generator](https://github.com/yigittozdemirr/emotion-aware-ai-image-generator)
