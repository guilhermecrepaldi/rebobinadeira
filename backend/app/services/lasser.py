"""Interface para sensor laser."""
import serial
import asyncio
import re
from threading import Thread


class LaserService:
    """Gerencia leitura do sensor laser para medição de metragem."""

    def __init__(self, port: str = "/dev/ttyUSB0", baud: int = 9600):
        self.port = port
        self.baud = baud
        self.ser = None
        self.running = False
        self.metragem_atual = 0.0
        self.on_distance_update = None  # Callback

    def start(self):
        try:
            self.ser = serial.Serial(self.port, self.baud, timeout=1)
            self.running = True
            Thread(target=self._loop, daemon=True).start()
        except serial.SerialException as e:
            print(f"Laser não disponível (modo simulação): {e}")
            self.running = False

    def stop(self):
        self.running = False
        if self.ser:
            self.ser.close()

    def _loop(self):
        while self.running:
            try:
                line = self.ser.readline().decode().strip()
                match = re.search(r"(\d+\.?\d*)", line)
                if match:
                    self.metragem_atual = float(match.group(1))
                    if self.on_distance_update:
                        asyncio.run(self.on_distance_update(self.metragem_atual))
            except Exception:
                pass
