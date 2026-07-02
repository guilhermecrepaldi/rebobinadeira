"""Serviço de detecção de defeitos usando OpenCV."""
import cv2
import numpy as np
from app.models import TipoDefeito


class DetectorDefeitos:
    """Detecta defeitos em imagens de tecido usando visão computacional."""

    def __init__(self, confidence_threshold: float = 0.7):
        self.threshold = confidence_threshold

    def detectar(self, frame: np.ndarray) -> list[dict]:
        """
        Processa um frame da câmera e retorna defeitos encontrados.
        Args:
            frame: Imagem numpy array (BGR)
        Returns:
            Lista de dicts com tipo, posição, severidade
        """
        defeitos = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 1. Detecção de variações bruscas (falhas, vincos)
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 50:  # Ignora ruído pequeno
                x, y, w, h = cv2.boundingRect(cnt)
                defeitos.append({
                    "tipo": self._classificar(frame, x, y, w, h),
                    "posicao_x": x,
                    "posicao_y": y,
                    "largura": w,
                    "altura": h,
                    "severidade": min(area / 1000, 1.0),
                    "area_px": int(area),
                })

        return defeitos

    def _classificar(self, frame, x, y, w, h) -> TipoDefeito:
        """Classifica o tipo de defeito baseado na região."""
        regiao = frame[y:y+h, x:x+w]
        mean_intensity = np.mean(cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY))

        if mean_intensity < 30:
            return TipoDefeito.FURO
        elif np.std(regiao) > 60:
            return TipoDefeito.IRREGULARIDADE
        elif w > h * 5:
            return TipoDefeito.VINCO
        elif mean_intensity < 80:
            return TipoDefeito.MANCHA
        else:
            return TipoDefeito.FALHA_MALHA
