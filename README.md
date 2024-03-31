### ADBVideoCapture

ADBVideoCapture is a Python module that allows you to open a video stream from an Android device using ADB (Android Debug Bridge) without the need to install any server application on the mobile device. It relies solely on OpenCV as its dependency.

### How It Works

The ADBVideoCapture module provides a class named `ADBVideoCapture`, which extends OpenCV's `VideoCapture` class. It establishes a connection with the Android device through ADB and streams the video content directly to your Python application.

### Example Usage

```python
import cv2
from ADBVideoCapture import ADBVideoCapture

def main():
    # Create an instance of ADBVideoCapture, specify whether to automatically open the connection
    cap = ADBVideoCapture(False)
    cap.open()

    # Check if the video stream was opened successfully
    if not cap.isOpened():
        print("Unable to open the video stream")
        return

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Unable to read the frame")
            break

        # Display the frame
        cv2.imshow('Video', frame)

        # Wait for ESC key press to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

### Dependencies
- OpenCV

### Installation
This module does not require installation from a repository like pip. Simply download the ADBVideoCapture.py file and include it in your project directory.

### Notes
- Make sure your environment is set up to use ADB and that your Android device is properly connected.
- You may adjust parameters such as resolution and buffer size according to your needs.
- Check for exceptions and connection issues carefully during execution.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.

### Author
Alessandro Roat