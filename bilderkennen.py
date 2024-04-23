import cv2
import numpy as np
import pyautogui

def suchen(template_path, threshold):
    # Lade das Template-Bild
    template = cv2.imread(template_path)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # Erfasse einen Screenshot vom aktuellen Bildschirm
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Führe die Vorlagenübereinstimmung durch
    result = cv2.matchTemplate(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    # Überprüfe, ob die Übereinstimmung den Schwellenwert überschreitet
    if max_val >= threshold:
        top_left = max_loc
        bottom_right = (top_left[0] + template_gray.shape[1], top_left[1] + template_gray.shape[0])
        
        # Mittelpunkt des Rechtecks
        x_center = (top_left[0] + bottom_right[0]) // 2
        y_center = (top_left[1] + bottom_right[1]) // 2
        
        if __name__ == "__main__":
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            cv2.circle(frame, (x_center ,y_center), radius=5, color=(0, 0, 255), thickness=-1)
            cv2.imshow('Bildschirm mit markiertem Template', frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return x_center, y_center
    else:
        print("Das Template wurde nicht gefunden.")
        return None

if __name__ == "__main__":
    # Beispielaufruf der Funktion suchen()
    ergebnis = suchen("Image\leereLeiste.png",0.8)
    if ergebnis:
        print("Das Template wurde bei den Koordinaten", ergebnis, "gefunden.")

