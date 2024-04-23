import cv2
import numpy as np
import pyautogui
import time
import threading
from bilderkennen import suchen
from funktionen import MachenHelper
from fallunterscheidung import CaseDistinction

funktion = MachenHelper()

class DesktopRecorder:
        # Initialisierung der Klasse
    def __init__(self, template_path, output_path='desktop_capture.avi', scale_factor=0.7, duration=86400):
        self.template = cv2.imread(template_path)
        self.template_gray = cv2.cvtColor(self.template, cv2.COLOR_BGR2GRAY)
        self.template_height, self.template_width = self.template_gray.shape[::-1]
        
        # Ermittelt die Bildschirmgroesse und skaliert
        self.screen_width, self.screen_height = pyautogui.size()
        self.scaled_width = int(self.screen_width * scale_factor)
        self.scaled_height = int(self.screen_height * scale_factor)
        
        self.out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (self.scaled_width, self.scaled_height))
        
        self.recording_duration = duration
        
        # Variable zur Verfolgung des Status der Funktion machen()
        self.is_machen_running = False     
        
    def record(self):
        counter = 0
        for _ in range(int(20 * self.recording_duration)):
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Vergleicht mit dem Bild
            result = cv2.matchTemplate(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), self.template_gray, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            x, y = max_loc
            
             # Definiere die Schwellenwert für die Ähnlichkeit
            threshold = 0.7
            
            # Finde alle Bereiche, die über dem Schwellenwert liegen
            loc = np.where(result >= threshold)
            
            # Iteriere über die gefundenen Bereiche und markiere sie
            for pt in zip(*loc[::-1]):
                top_left = pt  
                bottom_right = (top_left[0] + self.template_height, top_left[1] + self.template_width)
                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 1)
                # Pointer
                cv2.circle(frame, (x + 20,y + 20), radius=5, color=(0, 0, 255), thickness=-1)
                # Starte die Funktion machen() in einem separaten Thread
                if not self.is_machen_running:
                    CaseDistinction.distinction(self)
                    counter += 1
                    print(counter)
                    #threading.Thread(target=CaseDistinction.distinction(self)).start()

            # Bildschirm wird nach dem Vergleich skaliert
            scaled_frame = cv2.resize(frame, (self.scaled_width, self.scaled_height))
            self.out.write(scaled_frame)
            #cv2.imshow('Desktop Recording', scaled_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        #self.out.release()
        #cv2.destroyAllWindows()

# Beispielaufruf des DesktopRecorders
recorder = DesktopRecorder('Image\gameBar.png')
recorder.record()



