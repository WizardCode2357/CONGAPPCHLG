# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:13:38 2023

@author: dsdhr
"""

import cv2
from pyzbar import pyzbar

def scan_qr_code():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Set to store scanned QR codes
    scanned_qr_codes = set()

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Flip the frame horizontally (mirror effect)
        flipped_frame = cv2.flip(frame, 1)

        # Display the flipped frame
        cv2.imshow('QR Code Scanner', flipped_frame)

        # Convert the frame to grayscale for QR code detection
        gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes
        qr_codes = pyzbar.decode(gray)

        # Process each detected QR code
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            
            # Check if the QR code has already been scanned
            if qr_data not in scanned_qr_codes:
                scanned_qr_codes.add(qr_data)
                print('QR Code data:', qr_data)

        # Check for user input to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()

def kivyv():
    import cv2
from pyzbar import pyzbar
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

class QRCodeScannerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cap = cv2.VideoCapture(0)
        self.scanned_qr_codes = set()
        self.capture = Image()

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.capture)

        # Create a button to close the scanner
        close_button = Button(text="Close Scanner")
        close_button.bind(on_press=self.close_scanner)
        layout.add_widget(close_button)

        # Schedule the function to update the image regularly
        Clock.schedule_interval(self.update, 1.0/30.0)

        return layout

    def update(self, dt):
        ret, frame = self.cap.read()
        if ret:
            # Flip the frame horizontally
            flipped_frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)
            qr_codes = pyzbar.decode(gray)

            for qr_code in qr_codes:
                qr_data = qr_code.data.decode('utf-8')
                if qr_data not in self.scanned_qr_codes:
                    self.scanned_qr_codes.add(qr_data)
                    print('QR Code data:', qr_data)

            # Convert the frame to RGB for display in Kivy
            flipped_frame_rgb = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)
            buf1 = cv2.flip(flipped_frame_rgb, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.capture.texture = texture

    def close_scanner(self, instance):
        # Release the webcam and close the app
        self.cap.release()
        App.get_running_app().stop()

if __name__ == '__main__':
    QRCodeScannerApp().run()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    