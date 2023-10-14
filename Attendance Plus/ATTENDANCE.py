# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:13:38 2023

@author: dsdhr
"""
import cv2
from pyzbar import pyzbar
import subprocess



def install_libraries(library_names):
    for library_name in library_names:
        subprocess.run(["pip", "install", library_name])
        print(f"Successfully installed {library_name}")
if __name__ == "__main__":
    libraries_to_install = ["pygame", "pyzbar", "playsound", "opencv-python", "webbrowser"]  # Add library names to install
    install_libraries(libraries_to_install)

def play_sound(file_path):
    import pygame
    pygame.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    while pygame.mixer.get_busy():
        pass
    pygame.quit()
if __name__ == "__main__":
    file_path = "Externalfiles/verified.mp3"
    play_sound(file_path)

    


def scan_qr_code():
    cap = cv2.VideoCapture(0) #webcam
    scanned_qr_codes = set()  #mark QR CODES
    qr_code_count = 0 #start count for QR codes

    while True:
      
        ret, frame = cap.read()
        flipped_frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)
        qr_codes = pyzbar.decode(gray) #looking for qr codes
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            
            # Check if the QR code has already been scanned
            if qr_data not in scanned_qr_codes:
                scanned_qr_codes.add(qr_data)
                qr_code_count += 1
                print(f'QR Code count: {qr_code_count}')
                print('Last QR Code:', qr_data)
                play_sound(file_path)

        # Overlay QR code count on the frame
        cv2.putText(flipped_frame, f'QR Code count: {qr_code_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('QR Code Scanner', flipped_frame)
        key = cv2.waitKey(1)
        if key == 13: # Enter key in ASCHII
            break
    cap.release() #close webcam and window
    cv2.destroyAllWindows()
if __name__ == "__main__":
    scan_qr_code()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    