import socket
import subprocess
import threading
import cv2


class ADBVideoCapture(cv2.VideoCapture):
    def __init__(self,open=True):
        cv2.VideoCapture.__init__(self)
        self.t=None
        self.port=None
        if open:
            self.open()
    def open(self,resolution=[800,600],buffersize=1600000):
        ev=threading.Event()
        def service():
            PORT=0
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(("localhost", PORT))
            self.port = server_socket.getsockname()[1]
            # print(f"In ascolto sulla porta {self.port}")
            server_socket.listen(1)
            ev.set()
            client_socket, addr = server_socket.accept()
            # print(f"Connessione accettata da {addr}")
            w,h=resolution
            command=f"adb shell screenrecord --bit-rate={buffersize} --output-format=h264 --size {w}x{h} -"
            # print(command)
            while True:
                process = subprocess.Popen(command, stdout=client_socket.fileno(), stderr=subprocess.STDOUT, shell=True)
                process.wait()
        self.t=threading.Thread(target=service)
        self.t.start()
        ev.wait()
        # print("go",f"tcp://localhost:{self.port}")
        return super().open(f"tcp://localhost:{self.port}")


