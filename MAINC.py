# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:31:17 2023

@author: dsdhr
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import ATTENDANCE
import webbrowser
kivy.require('1.11.1')  # Make sure to adjust the version based on your Kivy installation
import os
class MyGUI(App):
    def build(self):
        # Create a BoxLayout for the main layout
        layout = BoxLayout(orientation='vertical', size=(1000, 5000)) # Convert inches to millimeters

        # Create and add buttons with labels and event handlers
        button1 = Button(text='Scan Qr Codes for Attendance', on_release=self.on_button1_click, background_normal='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg1.png', background_down='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg5.png', font_name='C:/Users/dsdhr/OneDrive/Desktop/HTML/Comfortaa/static/Comfortaa-Regular.ttf') 
        button2 = Button(text='Open Viewing Website', on_release=self.on_button2_click, background_normal='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg2.png', background_down='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg6.png', font_name='C:/Users/dsdhr/OneDrive/Desktop/HTML/Comfortaa/static/Comfortaa-Regular.ttf')
        button3 = Button(text='View Spreadsheets', on_release=self.on_button3_click, background_normal='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg3.png', background_down='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg7.png', font_name='C:/Users/dsdhr/OneDrive/Desktop/HTML/Comfortaa/static/Comfortaa-Regular.ttf')
        button4 = Button(text='WDK FOR NOW', on_release=self.on_button4_click, background_normal='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg4.png', background_down='C:/Users/dsdhr/OneDrive/Desktop/picturesforclg/buttonbg8.png', font_name='C:/Users/dsdhr/OneDrive/Desktop/HTML/Comfortaa/static/Comfortaa-Regular.ttf')

        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        return layout

    


    def on_button1_click(self, instance):
        print("Button 1 clicked")
        ATTENDANCE.scan_qr_code()

    




















    def on_button2_click(self, instance):
        print("Button 2 clicked")
        html_file_path = 'C:/Users/dsdhr/OneDrive/Desktop/HTML/try1ggsn.html'
        webbrowser.open('file://' + html_file_path)
    
   
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def on_button3_click(self, instance):
        print("Button 3 clicked")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def on_button4_click(self, instance):
        print("Button 4 clicked")
        



















if __name__ == '__main__':
    MyGUI().run()
