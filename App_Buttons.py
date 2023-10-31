   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:08:06 2023

@author: DhruvSingh
"""
import cv2
from pyzbar import pyzbar
import subprocess
file_path = "Externalfiles/verified.mp3"
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import webbrowser
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import os
from kivy.uix.gridlayout import GridLayout
from datetime import date
today = date.today()
default_dir = "Attendence_Files/"
current_file = "x.csv"
import csv
import pkgutil
import platform
folder_path = 'Attendence_Files'  # Replace with the actual path to your folder

class HomeGUI(App):
    title = 'Attendance Plus' 
    

    def build(self):
        # Create a BoxLayout for the main layout
        print("Running Build\n")

        layout = BoxLayout(orientation='vertical', size=(1000, 5000)) # Convert inches to millimeters

        # Create and add buttons with labels and event handlers
        button1 = Button(text='Mark Attendance', on_release=self.on_button1_click, background_normal='Externalfiles/buttonbg1.png', background_down='Externalfiles/buttonbg5.png', font_name='Externalfiles/Comfortaa-Regular.ttf')
        button2 = Button(text='Open Viewing Website', on_release=self.on_button2_click, background_normal='Externalfiles/buttonbg2.png', background_down='Externalfiles/buttonbg6.png', font_name='Externalfiles/Comfortaa-Regular.ttf')
        button3 = Button(text='View All Spreadsheets', on_release=self.on_button3_click, background_normal='Externalfiles/buttonbg3.png', background_down='Externalfiles/buttonbg7.png', font_name='Externalfiles/Comfortaa-Regular.ttf')
        button4 = Button(text='Link to GitHub(for any instructions or issues)', on_release=self.on_button4_click, background_normal='Externalfiles/buttonbg4.png', background_down='Externalfiles/buttonbg8.png', font_name='Externalfiles/Comfortaa-Regular.ttf')

        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        return layout


    def on_button1_click(self, instance):
        print("Button 1 clicked")
        self.show_popup()
        
        

    def on_button2_click(self, instance):
        print("Button 2 clicked")
        html_file_path = 'Externalfiles/Java'
        webbrowser.open('file://' + html_file_path)


    def on_button3_click(self, instance):
        print("Button 3 clicked")
        if platform.system() == 'Linux':
            subprocess.Popen(['xdg-open', folder_path])
        if platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['open', folder_path])
        else:  # Linux
            os.system(f'explorer "{folder_path}"')

    
    
    def on_button4_click(self, instance):
        print("Button 4 clicked")
        webbrowser.open('https://github.com/WizardBoy2357/CONGAPPCHLG')
        
    def show_popup(self):
        self.text_popup = GridLayout(cols=1, padding=20)
        self.text_input2 = TextInput(hint_text="Enter Name of Class")
        self.text_input = TextInput(hint_text="Enter Room Number")
        self.text_input1 = TextInput(hint_text="Enter Period Number")
        self.ok_button = Button(text="OK", on_release=self.get_user_input,font_name='Externalfiles/Comfortaa-Regular.ttf')
        self.cancel_button = Button(text="Cancel", on_release=self.cancel_user_input,font_name='Externalfiles/Comfortaa-Regular.ttf')
        #self.ok_button.bind(on_press=lambda x: self.get_user_input())
        self.text_popup.add_widget(self.text_input2)
        self.text_popup.add_widget(self.text_input)
        self.text_popup.add_widget(self.text_input1)
        self.text_popup.add_widget(self.ok_button)
        self.text_popup.add_widget(self.cancel_button)
        
        self.input_popup = Popup(title="User Input Popup", content=self.text_popup, size_hint=(None, None), size=(600, 400))
        self.input_popup.open()
        
    def get_user_input(self, instance):
        self.user_input2 = self.text_input2.text
        self.user_input = self.text_input.text
        self.user_input1 = self.text_input1.text
        RMNUM = self.user_input1
        Period = self.user_input
        Classname = self.user_input2
        attendence_file = "{2}--{1}--{0}--{3}.csv".format(RMNUM, Period, Classname, today)
        #print(dhruv_file)
        self.current_file = default_dir + attendence_file
        #with open(self.current_file, mode='w', newline='') as file:
        #self.csv_file = open(self.current_file, 'a', newline='')
        #self.csv_writer = csv.writer(self.csv_file)
        #self.writer = csv.writer(self.csv_writer)  
        
        print("user_input is {0} {1} and {2}".format(self.user_input2, self.user_input, self.user_input1))
        self.input_popup.dismiss()
        #time.sleep(7)
        self.scan_qr_code()
    def cancel_user_input(self, instance):
        self.input_popup.dismiss()
    def install_libraries(self):
        self.t = ["pygame", "pyzbar", "playsound", "opencv-python"]  # Add library names to install
        self.x =0 #first item of list:t
        for i in range(0, 4, 1):
            if pkgutil.find_loader(self.t[self.x]) is not None:
                print("Package is installed")
                self.x = self.x+1

            else:
                print("Package is not installed")
                subprocess.run(["pip", "install", self.t[self.x]])
                self.x = self.x+1
    
    
    
    
    def play_sound(self):
        import pygame
        pygame.init()
        self.sound = pygame.mixer.Sound(file_path)
        self.sound.play()
        while pygame.mixer.get_busy():
            pass
        pygame.quit()
        

    
    
    def scan_qr_code(self):
        #self.install_libraries()
        self.cap = cv2.VideoCapture(0) #webcam
        self.scanned_qr_codes = set()  #mark QR CODES
        self.qr_code_count = 0 #start count for QR codes
    
        while True:
          
            ret, frame = self.cap.read()
            self.flipped_frame = cv2.flip(frame, 1)
            self.gray = cv2.cvtColor(self.flipped_frame, cv2.COLOR_BGR2GRAY)
            self.qr_codes = pyzbar.decode(self.gray) #looking for qr codes
            for self.qr_code in self.qr_codes:
                self.qr_data = self.qr_code.data.decode('utf-8')

                # Check if the QR code has already been scanned
                if self.qr_data not in self.scanned_qr_codes:
                    self.scanned_qr_codes.add(self.qr_data)
                    self.qr_code_count += 1
                    print(f'QR Code count: {self.qr_code_count}')
                    print('Last QR Code:', self.qr_data)
                    self.play_sound()
                    '''self.csv_file = open(self.current_file, 'a+', newline='')
                    self.csv_writer = csv.writer(self.csv_file)
                    x = 'Present'
                   
                    #while 1:   
                    self.csv_writer.writerow([self.qr_data, x])'''
                    with open(self.current_file, 'a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        x = 'Present'
                        csv_writer.writerow([self.qr_data, x])
                    
    
            # Overlay QR code count on the frame            
            cv2.putText(self.flipped_frame, f'QR Code count: {self.qr_code_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(self.flipped_frame, 'To close program, hit the Enter/Return key', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow('QR Code Scanner', self.flipped_frame)
            key = cv2.waitKey(1)
            if key == 13: # Enter key in ASCHII
                break
        self.cap.release() #close webcam and window
        cv2.destroyAllWindows()

