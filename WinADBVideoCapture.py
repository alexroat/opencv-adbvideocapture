import socket
import subprocess
import threading
import cv2
import signal



class ADBVideoCapture(cv2.VideoCapture):
    def __init__(self,open=True):
        cv2.VideoCapture.__init__(self)
        self.t=None
        self.port=None
        if open:
            self.open()
    def open(self,resolution=[800,600],buffersize=1600000):
        import win32pipe
        import win32file
        import pywintypes
        ev=threading.Event()
        pipe_name=r'\\.\pipe\MyNamedPipe'
        def service():
            pipe = win32pipe.CreateNamedPipe(
                pipe_name,
                win32pipe.PIPE_ACCESS_DUPLEX,
                win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
                1, 65536, 65536,
                0,
                None)
            ev.set()
            win32pipe.ConnectNamedPipe(pipe, None)
            # print(f"Connessione accettata da {addr}")
            w,h=resolution
            command=f"adb exec-out screenrecord --bit-rate={buffersize} --output-format=h264 --size {w}x{h} -"
            # print(command)
            print("starting process")
            while True:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                print("starting copy")
                while True:
                    data=process.stdout.read(10000)
                    win32file.WriteFile(pipe, data)
                    if not data:
                        break
                print("ending")
        self.t=threading.Thread(target=service)
        self.t.daemon=True
        self.t.start()
        ev.wait()
        # print("go",f"tcp://localhost:{self.port}")
        return super().open(pipe_name)
