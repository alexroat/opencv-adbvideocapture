import cv2
from ADBVideoCapture import ADBVideoCapture

def main():
    # Apertura del flusso video dalla webcam (0) o da un file video ("nomefile.mp4")
    cap = ADBVideoCapture(False)
    cap.open()

    # Controlla se il flusso video è stato aperto correttamente
    if not cap.isOpened():
        print("Impossibile aprire il flusso video")
        return

    while True:
        # Lettura di un frame dal flusso video
        ret, frame = cap.read()

        # Controlla se il frame è stato letto correttamente
        if not ret:
            print("Impossibile leggere il frame")
            break

        # Visualizzazione del frame
        cv2.imshow('Video', frame)

        # Attendere 1 millisecondo per la pressione del tasto ESC per uscire
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Rilascio delle risorse
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
