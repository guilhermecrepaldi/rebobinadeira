"""Interface para câmera industrial."""
import cv2
import asyncio
from threading import Thread
from app.services.detector import DetectorDefeitos


class CameraService:
    """Gerencia captura de frames da câmera industrial."""

    def __init__(self, source: str = "0", detector: DetectorDefeitos = None):
        self.source = source
        self.cap = None
        self.detector = detector or DetectorDefeitos()
        self.running = False
        self.on_defect_detected = None  # Callback

    def start(self):
        self.cap = cv2.VideoCapture(int(self.source) if self.source.isdigit() else self.source)
        if not self.cap.isOpened():
            raise RuntimeError(f"Não foi possível abrir câmera: {self.source}")

        self.running = True
        Thread(target=self._loop, daemon=True).start()

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()

    def _loop(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            defeitos = self.detector.detectar(frame)
            if defeitos and self.on_defect_detected:
                asyncio.run(self.on_defect_detected(defeitos, frame))
