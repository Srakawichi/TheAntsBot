import time
from bilderkennen import suchen
from funktionen import MachenHelper
funktion = MachenHelper()



class CaseDistinction:
    def __init__(self):
        self.is_machen_running = False
        
    def distinction(self):
        '''Fallunterscheidung'''
        if self.is_machen_running:
            return  
        self.is_machen_running = True
        
        print("case distinction in process")
        
        if suchen("Image/x.png",0.8):
            x, y = suchen("Image/x.png",0.8)
            funktion.machen7(x,y)
        elif suchen("Image\spezialAmeisen.png", 0.8):
            x, y = suchen("Image\spezialAmeisen.png", 0.8)
            funktion.machen8(x,y)
        elif suchen("Image\leereLeiste.png",0.8):
            x, y = suchen("Image\leereLeiste.png",0.8)
            funktion.blattschneider(x,y)
        elif suchen("Image\armee1.png",0.8) and not suchen("Image\armeeWarten.png",0.8):
            x, y = suchen("Image\armee1.png",0.8)
            funktion.armee1(x,y)
        elif suchen("Image\armee2.png",0.8) and not suchen("Image\armee2Warten.png",0.8):
            x, y = suchen("Image\armee2.png",0.8)
            funktion.armee2(x,y)
        elif suchen("Image\armee3.png",0.8) and not suchen("Image\armee3Warten.png",0.8):
            x, y = suchen("Image\armee3.png",0.8)
            funktion.armee3(x,y)
        elif suchen("Image\einheitenSammeln.png",0.8):
            x, y = suchen("Image\einheitenSammeln.png",0.8)
            funktion.machen5(x,y)
        elif suchen("Image\essbereich.png",0.8):
            x, y = suchen("Image\essbereich.png",0.8)
            funktion.machen3(x,y)
#         if suchen("Image\kampf.png",0.8) and not suchen("Image\2von2.png",0.8):
#              x, y = suchen("Image\kampf.png",0.8)
#              print(x,y)
#              funktion.machen4(x,y)
#         if suchen("Image\VIP.png",0.9):
#              '''Es gibt noch Problemen mit dem Roten Punkt, der nicht verschwindet
#              x, y = suchen("Image\kampf.png",0.8)
#              print(x,y)
#              funktion.machen6(x,y)
        else:
            print("Wartezeit")
            time.sleep(100)  # Führe eine 100-sekündige Pause durch

        self.is_machen_running = False
        
if __name__ == "__main__":
    cd = CaseDistinction()
    cd.distinction()
    
