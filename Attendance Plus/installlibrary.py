# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:55:38 2023

@author: dsdhr
"""


import subprocess

def install_libraries(library_names):
    for library_name in library_names:
        try:
            # Use pip to install the current library in the iteration
            subprocess.run(["pip", "install", library_name])
            print(f"Successfully installed {library_name}")
        except Exception as e:
            print(f"An error occurred while installing {library_name}: {e}")

if __name__ == "__main__":
    libraries_to_install = ["pygame", "pyzbar", "playsound", "opencv-python", "webbrowser"]  # Add library names to install
    install_libraries(libraries_to_install)
    
'''def dhruvi():
    for i in range(1, 11, 1):
        print (i)'''