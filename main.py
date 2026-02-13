import sys
import cv2
import os
import numpy as np
from collections import deque
from datetime import datetime

from ultralytics import YOLO

from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QTimer, Qt, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMessageBox

from sayisal_ui import Ui_Dialog
from prompt_engine import PromptEngine
from image_generator import ImageGenerator  

MODEL_PATH = "AI/models/sd15/v1-5-pruned-emaonly.safetensors"

# ==================== THREAD (UI DONMASIN) ====================
class ImageGenerationThread(QThread):
    finished = Signal(bool, str)
    
    def __init__(self, generator, prompt, save_path, emotion):
        super().__init__()
        self.generator = generator
        self.prompt = prompt
        self.save_path = save_path
        self.emotion = emotion
    
    def run(self):
        success = self.generator.generate(
            prompt=self.prompt,
            save_path=self.save_path,
            emotion=self.emotion,
            width=512,
            height=512
        )
        self.finished.emit(success, self.save_path)


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.prev_mouth = None
        self.prev_eye = None
        self.prev_brow = None
        
        # -- ENGINES --
        self.prompt_engine = PromptEngine()
        self.worker = None
        self.gen_thread = None

        self.dominant_buffer = deque(maxlen=15)
        # ================= IMAGE INFO STORAGE =================
        self.image_infos = []

        # ================= FACE DETECTION MODEL =================
        self.face_model = YOLO("models/yolov8n-face-lindevs.pt")
        print("✅ YOLOv8 Face model yüklendi")
    
        # ================= IMAGE GENERATOR =================
        self.image_generator = ImageGenerator(MODEL_PATH)
        print("✅ Image Generator hazır!")

        # ================= UI DEFAULTS =================
        self.ui.radioButton.setChecked(True)
        self.ui.pushButton_3.clicked.connect(self.on_generate_image_clicked)
        self.ui.pushButton.clicked.connect(self.show_previous_image)
        self.ui.pushButton_2.clicked.connect(self.show_next_image)
        self.ui.pushButton_5.clicked.connect(self.reset_all)

        # ================= IMAGE STORAGE =================
        self.image_dir = "generated_images"
        os.makedirs(self.image_dir, exist_ok=True)
        self.generated_images = []
        self.current_image_index = -1
        
        # Generation thread
        self.gen_thread = None
        self.is_generating = False

        # ================= CAMERA =================
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        

        if not self.cap.isOpened():
            print("Kamera açılamadı")
            sys.exit(1)

        # ================= EMOTION MODEL =================
        self.emotion_model = YOLO("runs/classify/train3/weights/best.pt")

        self.class_names = [
            "angry", "fear", "happy",
            "neutral", "sad", "surprise"
        ]

        self.emoji_map = {
            "happy": "😊", "angry": "😡", "sad": "😢",
            "neutral": "😐", "fear": "😱", "surprise": "😲"
        }

        self.color_map = {
            "happy": (0, 255, 255),
            "angry": (0, 0, 255),
            "sad": (255, 0, 0),
            "neutral": (200, 200, 200),
            "fear": (128, 0, 128),
            "surprise": (0, 165, 255)
        }

        # ================= SMOOTHING =================
        self.buffers = {k: deque(maxlen=10) for k in self.class_names}

        self.last_dominant = "neutral"
        self.show_face_box = True
        self.face_detected = False
        self.last_text = ""

        # ================= TIMER =================
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # ================= CAMERA FREEZE STATE =================
        self.freeze_camera = False
        self.frozen_frame = None

        # ================= AUTO MODE =================
        self.auto_timer = QTimer()
        self.auto_timer.timeout.connect(self.auto_generate_tick)

        self.auto_paused = False
        self.auto_running = False

        self.ui.radioButton_2.toggled.connect(self.on_auto_mode_toggled)
        self.ui.pushButton_4.clicked.connect(self.toggle_auto_pause)

    # =====================================================
    # PROMPT BUILD
    # =====================================================
    def build_prompt(self):
        emotions = {
            "happy": self.ui.progressBar.value(),
            "angry": self.ui.progressBar_2.value(),
            "sad": self.ui.progressBar_3.value(),
            "neutral": self.ui.progressBar_4.value(),
            "fear": self.ui.progressBar_5.value(),
            "surprise": self.ui.progressBar_6.value()
        }
        style = self.ui.comboBox.currentText()
        return self.prompt_engine.generate(emotions, style)

    # =====================================================
    # GENERATE BUTTON
    # =====================================================
    def on_generate_image_clicked(self):
        if not self.ui.radioButton.isChecked():
            return
        
        if self.is_generating:
            print("⚠️ Zaten bir resim üretiliyor!")
            return

        # ================= FREEZE CAMERA =================
        self.freeze_camera = True

        if hasattr(self, "last_frame") and self.last_frame is not None:
            self.frozen_frame = self.last_frame.copy()

        prompt = self.build_prompt()
        
        # Prompt'u göster
        self.ui.textEdit_2.setPlainText(
            "🧠 GÖRÜNTÜ OLUŞTURULUYOR...\n"
            + "=" * 40 + "\n\n"
            + prompt + "\n\n"
            + "⏳ Lütfen bekleyin (5-20 saniye)..."
        )
        
        # Dosya adı
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = os.path.join(self.image_dir, f"emotion_{timestamp}.png")
        
        # Thread'de üret
        self.is_generating = True
        self.ui.pushButton_3.setEnabled(False)
        
        dominant_emotion = self.last_dominant

        self.gen_thread = ImageGenerationThread(
            self.image_generator, prompt, save_path, dominant_emotion
        )
        self.gen_thread.finished.connect(self.on_generation_finished)
        self.gen_thread.start()

    def on_auto_mode_toggled(self, checked):
        if checked:
            interval_sec = self.ui.spinBox.value()
            self.auto_timer.start(interval_sec * 1000)
            self.auto_running = True
            self.auto_paused = False
            print(f"▶️ Otomatik mod başladı ({interval_sec}s)")
        else:
            self.auto_timer.stop()
            self.auto_running = False
            print("⏹️ Otomatik mod kapandı")

    def auto_generate_tick(self):
        if self.auto_paused or self.is_generating:
            return

        if not self.face_detected:
            print("❌ Yüz yok → otomatik üretim atlandı")
            return

        stable_emotion = self.get_stable_emotion()
        if stable_emotion is None:
            print("⏳ Duygu stabil değil → bekleniyor")
            return

        # ===== FREEZE CAMERA =====
        self.freeze_camera = True
        if hasattr(self, "last_frame"):
            self.frozen_frame = self.last_frame.copy()

        prompt = self.build_prompt()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = os.path.join(self.image_dir, f"auto_{timestamp}.png")

        self.is_generating = True

        self.gen_thread = ImageGenerationThread(
            self.image_generator,
            prompt,
            save_path,
            stable_emotion
        )
        self.gen_thread.finished.connect(self.on_generation_finished)
        self.gen_thread.start()

        self.ui.textEdit_2.setPlainText(
            "🤖 OTOMATİK MOD\n"
            f"Duygu (stabil): {stable_emotion.upper()}\n"
            f"Sonraki üretim: {self.ui.spinBox.value()}s"
        )

    def showEvent(self, event):
        super().showEvent(event)

        # sadece ilk açılışta çalışsın
        if not hasattr(self, "_welcome_shown"):
            self._welcome_shown = True

            # layout kesin otursun diye küçük gecikme
            QTimer.singleShot(50, self.show_welcome_screen)

    def toggle_auto_pause(self):
        if not self.auto_running:
            return

        self.auto_paused = not self.auto_paused

        if self.auto_paused:
            self.ui.textEdit_2.setPlainText("⏸️ OTOMATİK MOD DURAKLATILDI")
            self.ui.pushButton_4.setText("▶ Devam Et")
        else:
            self.ui.textEdit_2.setPlainText("▶️ OTOMATİK MOD DEVAM EDİYOR")
            self.ui.pushButton_4.setText("⏸ Duraklat")


    def on_generation_finished(self, success, path):
        # ================= UNFREEZE CAMERA =================
        self.freeze_camera = False
        self.frozen_frame = None
        
        self.is_generating = False
        self.ui.pushButton_3.setEnabled(True)
        
        if success:
            self.generated_images.append(path)
            # ===== RESME AİT BİLGİYİ KAYDET =====
            info = {
                "emotion": self.last_dominant,
                "confidence": max(
                    self.ui.progressBar.value(),
                    self.ui.progressBar_2.value(),
                    self.ui.progressBar_3.value(),
                    self.ui.progressBar_4.value(),
                    self.ui.progressBar_5.value(),
                    self.ui.progressBar_6.value()
                ),
                "style": self.ui.comboBox.currentText()
            }

            self.image_infos.append(info)
            self.current_image_index = len(self.generated_images) - 1
            self.display_current_image()
            
            self.ui.textEdit_2.setPlainText(
                "✅ GÖRÜNTÜ OLUŞTURULDU!\n"
                + "=" * 40 + "\n\n"
                + f"Kaydedildi: {os.path.basename(path)}\n"
                + f"Toplam: {len(self.generated_images)} görsel"
            )
        else:
            self.ui.textEdit_2.setPlainText(
                "❌ GÖRÜNTÜ OLUŞTURULAMADI\n"
                + "=" * 40 + "\n\n"
                + "Model yüklenemedi veya RAM yetersiz."
            )

    # =====================================================
    # IMAGE NAVIGATION
    # =====================================================
    def display_current_image(self):
        self.ui.label_3.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 150);
                padding: 6px 12px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        
        if not self.generated_images:
            self.ui.label_3.setText("🖼️ 0 / 0")
            self.ui.label_3.repaint()
            return

        path = self.generated_images[self.current_image_index]

        if not os.path.exists(path):
            return

        pixmap = QPixmap(path).scaled(
            self.ui.label_2.width(),
            self.ui.label_2.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.ui.label_2.setPixmap(pixmap)

        current = self.current_image_index + 1
        total = len(self.generated_images)

        info = self.image_infos[self.current_image_index]

        emoji = self.emoji_map.get(info["emotion"], "")
        emotion_text = info["emotion"].capitalize()

        self.ui.label_3.setText(
            f"🖼️ {current} / {total}\n"
            f"{emoji} {emotion_text} %{info['confidence']}\n"
            f"🎨 Stil: {info['style']}"
        )

        self.ui.label_3.repaint()

    def show_previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.display_current_image()

    def show_next_image(self):
        if self.current_image_index < len(self.generated_images) - 1:
            self.current_image_index += 1
            self.display_current_image()

    def show_welcome_screen(self):
        w = self.ui.label_2.width()
        h = self.ui.label_2.height()

        pixmap = QPixmap(w, h)
        pixmap.fill(Qt.black)

        painter = QPainter(pixmap)
        painter.setPen(Qt.white)
        painter.setFont(QFont("Arial", 16, QFont.Bold))

        text = (
            "DUYGU TABANLI GÖRSEL ÜRETİM\n\n"
            "🎭 Yüz ifadeni algılar\n"
            "🎨 Ortama uygun görsel üretir\n\n"
            "▶ Başlamak için 'Resim Oluştur'a tıkla\n"
            "🤖 Otomatik mod için üstten seç"
        )

        painter.drawText(
            pixmap.rect(),
            Qt.AlignCenter,
            text
        )
        painter.end()

        self.ui.label_2.setPixmap(pixmap)
        self.ui.label_3.setText("🖼️ 0 / 0")

    def update_frame(self):
        # ================= FRAME SOURCE =================
        if self.freeze_camera and self.frozen_frame is not None:
            frame = self.frozen_frame.copy()
        else:
            ret, frame = self.cap.read()
            if not ret:
                return
            frame = cv2.flip(frame, 1)
            self.last_frame = frame.copy()

        emotions = {k: 0 for k in self.class_names}

        # ================= CLEAN FREEZE UI =================
        if self.freeze_camera:
            overlay = frame.copy()

            # çok hafif karartma
            cv2.rectangle(
                overlay,
                (0, 0),
                (frame.shape[1], frame.shape[0]),
                (0, 0, 0),
                -1
            )

            frame = cv2.addWeighted(overlay, 0.18, frame, 0.82, 0)

            # üst status bar
            cv2.rectangle(
                frame,
                (0, 0),
                (frame.shape[1], 70),
                (20, 20, 20),
                -1
            )

            # sol ince vurgu çizgisi
            cv2.rectangle(
                frame,
                (0, 0),
                (6, 70),
                (90, 180, 255),  # soft blue accent
                -1
            )

            cv2.putText(
                frame,
                "Ifade yakalandi",
                (20, 34),
                cv2.FONT_HERSHEY_TRIPLEX,
                0.9,
                (245, 245, 245),
                1,
                cv2.LINE_AA
            )

            cv2.putText(
                frame,
                "Resim olusturuluyor...",
                (20, 58),
                cv2.FONT_HERSHEY_TRIPLEX,
                0.6,
                (180, 180, 180),
                1,
                cv2.LINE_AA
            )

        # ================= FACE DETECTION =================
        results = self.face_model(frame, conf=0.4, verbose=False)[0]
        self.face_detected = False

        if results.boxes is not None and len(results.boxes) > 0:
            self.face_detected = True

            boxes = results.boxes.xyxy.cpu().numpy()

            # en büyük yüz
            areas = [(x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in boxes]
            i = int(np.argmax(areas))

            x1, y1, x2, y2 = map(int, boxes[i])

            # frame sınırlarını koru
            h, w, _ = frame.shape
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)

            face_crop = frame[y1:y2, x1:x2]

            if face_crop.size > 0:
                fh, fw, _ = face_crop.shape

                upper_face  = face_crop[0:int(fh * 0.35), :]
                middle_face = face_crop[int(fh * 0.35):int(fh * 0.65), :]
                lower_face  = face_crop[int(fh * 0.65):fh, :]

                # ================= ENERGY FEATURES =================
                mouth_energy = cv2.Laplacian(
                    cv2.cvtColor(lower_face, cv2.COLOR_BGR2GRAY),
                    cv2.CV_64F
                ).var()

                eye_energy = cv2.Laplacian(
                    cv2.cvtColor(middle_face, cv2.COLOR_BGR2GRAY),
                    cv2.CV_64F
                ).var()

                brow_energy = cv2.Laplacian(
                    cv2.cvtColor(upper_face, cv2.COLOR_BGR2GRAY),
                    cv2.CV_64F
                ).var()

                mouth_delta = abs(mouth_energy - self.prev_mouth) if self.prev_mouth else 0
                eye_delta   = abs(eye_energy - self.prev_eye) if self.prev_eye else 0
                brow_delta  = abs(brow_energy - self.prev_brow) if self.prev_brow else 0

                self.prev_mouth = mouth_energy
                self.prev_eye   = eye_energy
                self.prev_brow  = brow_energy

                # ================= EMOTION MODEL =================
                result = self.emotion_model(face_crop, verbose=False)[0]
                probs = result.probs.data.cpu().numpy()

                for i, p in enumerate(probs):
                    self.buffers[self.class_names[i]].append(p * 100)

                for k in emotions:
                    if self.buffers[k]:
                        emotions[k] = int(np.mean(self.buffers[k]))

                # ================= HEURISTIC BOOST =================
                if brow_energy > 120 and brow_delta > 15:
                    emotions["angry"] += 10

                if mouth_energy < 40 and mouth_delta < 5:
                    emotions["sad"] += 8

                if eye_delta > 25 and mouth_delta > 25:
                    emotions["fear"] += 12

                if mouth_energy > 90 and eye_energy > 90:
                    emotions["surprise"] += 8

                self.last_dominant = max(emotions, key=emotions.get)
                self.dominant_buffer.append(self.last_dominant)

                if emotions[self.last_dominant] < 30:
                    emotions["neutral"] = max(emotions["neutral"], 30)

                # ================= DRAW FACE =================
                if self.show_face_box:
                    color = self.color_map[self.last_dominant]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(
                        frame,
                        f"{self.last_dominant.upper()} {emotions[self.last_dominant]}%",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2
                    )

        # ================= UI UPDATE =================
        self.ui.progressBar.setValue(emotions["happy"])
        self.ui.progressBar_2.setValue(emotions["angry"])
        self.ui.progressBar_3.setValue(emotions["sad"])
        self.ui.progressBar_4.setValue(emotions["neutral"])
        self.ui.progressBar_5.setValue(emotions["fear"])
        self.ui.progressBar_6.setValue(emotions["surprise"])

        status = "✓ Yüz algılandı" if self.face_detected else "✗ Yüz algılanmadı"

        text = (
            f"{status}\n{'='*30}\n"
            f"{self.emoji_map['happy']} Mutlu: {emotions['happy']}%\n"
            f"{self.emoji_map['angry']} Kızgın: {emotions['angry']}%\n"
            f"{self.emoji_map['sad']} üzgün: {emotions['sad']}%\n"
            f"{self.emoji_map['neutral']} Nötr: {emotions['neutral']}%\n"
            f"{self.emoji_map['fear']} Korku: {emotions['fear']}%\n"
            f"{self.emoji_map['surprise']} Şaşırma: {emotions['surprise']}%\n\n"
            f"🎯 Dominant: {self.last_dominant.upper()}"
        )

        if text != self.last_text:
            self.ui.textEdit.setPlainText(text)
            self.last_text = text

        # ================= CAMERA DISPLAY =================
        h, w, ch = frame.shape
        qt_img = QImage(frame.data, w, h, ch * w, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qt_img).scaled(
            self.ui.label.width(),
            self.ui.label.height(),
            Qt.KeepAspectRatioByExpanding
        )
        self.ui.label.setPixmap(pixmap)

    def get_stable_emotion(self):
        if len(self.dominant_buffer) < 10:
            return None

        most_common = max(
            set(self.dominant_buffer),
            key=self.dominant_buffer.count
        )

        if self.dominant_buffer.count(most_common) >= 8:
            return most_common

        return None

    def reset_all(self):
        # ================= IMAGE RESET =================
        self.generated_images.clear()
        self.current_image_index = -1

        self.ui.label_2.clear()
        self.image_infos.clear()

        # ================= UI RESET =================
        self.ui.radioButton.setChecked(True)
        self.ui.comboBox.setCurrentIndex(0)

        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_3.setValue(0)
        self.ui.progressBar_4.setValue(0)
        self.ui.progressBar_5.setValue(0)
        self.ui.progressBar_6.setValue(0)

        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

    # ================= STATE RESET =================
        self.last_dominant = "neutral"
        self.prev_mouth = None
        self.prev_eye = None
        self.prev_brow = None

        self.buffers = {k: deque(maxlen=10) for k in self.class_names}

        print("🔄 Sistem sıfırlandı")

        QMessageBox.information(
            self,
            "Sistem Sıfırlandı",
            "Uygulama başlangıç durumuna döndürüldü.\nYeni üretime hazır."
        )

        self.auto_timer.stop()
        self.auto_running = False
        self.auto_paused = False
        self.ui.pushButton_4.setText("⏸ Duraklat")

        self.show_welcome_screen()

    # =====================================================
    # KEYS
    # =====================================================
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.show_face_box = not self.show_face_box
        elif event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        if self.gen_thread and self.gen_thread.isRunning():
            self.gen_thread.wait()
        self.cap.release()
        cv2.destroyAllWindows()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())