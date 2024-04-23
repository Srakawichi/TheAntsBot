import pyautogui
import time
from bilderkennen import suchen

class MachenHelper:
    def __init__(self):
        self.is_machen_running = False

    def blattschneider(self, x, y):
        '''Blatschneider'''
        if self.is_machen_running:
            return  # Beende die Funktion, wenn sie bereits ausgeführt wird
        self.is_machen_running = True  # Setze den Status auf "ausgeführt"
        
        print("Funktion: blattschneider")
        pyautogui.moveTo(suchen("Image\leereLeiste.png", 0.8), duration=1)
        pyautogui.click()  
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\transportierenM.png", 0.7), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\transportierenButton.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(20)
        
        self.is_machen_running = False
        
    def armee1(self, x, y):
        '''Ausbilden'''
        if self.is_machen_running:
            return  # Beende die Funktion, wenn sie bereits ausgeführt wird
        
        self.is_machen_running = True  # Setze den Status auf "ausgeführt"
        print("Funktion: armee1")
            
        pyautogui.moveTo(suchen("Image\armee1.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\ausbilden.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\ausbildenStart.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\leave.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        self.is_machen_running = False
#------------------------        
    def armee2(self, x, y):
        '''Ausbilden'''
        if self.is_machen_running:
            return  # Beende die Funktion, wenn sie bereits ausgeführt wird
            
        self.is_machen_running = True  # Setze den Status auf "ausgeführt"
        print("Funktion: armee2")
        
        pyautogui.moveTo(suchen("Image\armee2.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\ausbilden.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\ausbildenStart.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\leave.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        self.is_machen_running = False
#-------------------------
        
    def armee3(self, x, y):
        '''Ausbilden'''
        if self.is_machen_running:
            return 
            
        self.is_machen_running = True  
        print("Funktion: armee3")
            
        pyautogui.moveTo(suchen("Image\armee3.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\ausbilden.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\ausbildenStart.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\leave.png", 0.8), duration=1)
        pyautogui.click()
        
        self.is_machen_running = False
        
    def machen3(self, x, y):
        '''Essbereich'''
        if self.is_machen_running:
            return  # Beende die Funktion, wenn sie bereits ausgeführt wird
        
        self.is_machen_running = True  # Setze den Status auf "ausgeführt"
        print("Funktion: Essbereich")
        pyautogui.moveTo(suchen("Image\essbereich.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\transportieren.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\transportierenButton.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        
        self.is_machen_running = False
        
    def machen4(self, x, y):
        '''Kämpfen'''
        if self.is_machen_running:
            return  
        
        self.is_machen_running = True  
        print("Funktion: machen4")
        pyautogui.moveTo(suchen("Image\kampf.png", 0.7), duration=1)
        pyautogui.click()
        time.sleep(2)  
        pyautogui.moveTo(suchen("Image\welt.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        if not suchen("Image\lupe.png", 0.8):
            print("lupe nicht gefunden")
            pyautogui.moveTo(suchen("Image\Einheit1.png", 0.8), duration=1)
            pyautogui.click()
            pyautogui.moveTo(suchen("Image\welt.png", 0.8), duration=1)
            pyautogui.click()
            time.sleep(2)
            
        pyautogui.moveTo(suchen("Image\lupe.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\gehen.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(suchen("Image\orchideenmantisA.png", 0.7), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\angreifen.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\marsch.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(5)
        
        self.is_machen_running = False
    
    def machen5(self, x, y):
        '''Ausgebildete Einheiten werden eingesammelt'''
        if self.is_machen_running:
            return  
        self.is_machen_running = True
        
        print("Funktion: Ausgebildete Einheiten werden eingesammelt")
        pyautogui.moveTo(suchen("Image\einheitenSammeln.png", 0.8), duration=1)
        while not suchen("Image\einheitenSammeln.png", 0.8):
            pyautogui.moveTo(suchen("Image\einheitenSammeln.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        self.is_machen_running = False
        
    def machen6(self, x, y):
        '''Sammelt VIP'''
        if self.is_machen_running:
            return  
        self.is_machen_running = True
        
        print("Funktion: machen6")
        pyautogui.moveTo(suchen("Image\VIP.png", 0.9), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\pruefen.png", 0.9), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\VIP_Sammeln.png", 0.9), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        pyautogui.moveTo(suchen("Image\leave.png", 0.9), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        self.is_machen_running = False
        
    def machen7(self, x, y):
        '''Popup entfernen'''
        if self.is_machen_running:
            return  
        self.is_machen_running = True
        
        print("Funktion: Popup entfernen")
        pyautogui.moveTo(suchen("Image/x.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        self.is_machen_running = False
        
    def machen8(self, x, y):
        '''Spezial Ameisen'''
        if self.is_machen_running:
            return  
        self.is_machen_running = True
        
        print("Funktion: Spezial Ameisen")
        pyautogui.moveTo(suchen("Image\spezialAmeisen.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\spezial_gratis.png", 0.6), duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(suchen("Image\spezial_back.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(suchen("Image\spezial_back.png", 0.8), duration=1)
        pyautogui.click()
        time.sleep(2)
        
        self.is_machen_running = False
        
    def test(self):
        '''Hier wird nur getestet'''
        if self.is_machen_running:
            return  
        self.is_machen_running = True
        print("Test_funktionen.test")
        pyautogui.moveTo(100, 100, duration=1)
        self.is_machen_running = False
        
        time.sleep(5)
            
    
        
if __name__ == "__main__":
    machen_helper = MachenHelper()
    machen_helper.test()
