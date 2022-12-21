import base64
import codecs
import os
from datetime import datetime

class Deobfuscator:
    def __init__(self, magic:str, love:str, god:str,destiny:str) -> None:
        self.magic = magic
        self.love = love
        self.god = god
        self.destiny = destiny
        pass

    def run(self) -> str:
        joy = 'rot13'

        trust = self.magic + codecs.decode(self.love, joy) + self.god + codecs.decode(self.destiny, joy)

        code = (base64.b64decode(trust),'<string>','exec')
        full = code[0].decode("utf-8")
        
        # save the code into /results/currenttime/deobfuscated.py
        # first, create results folder if it doesn't exist
        
        if not os.path.exists("results"):
            os.mkdir("results")
            
        # second, create a folder with the current time (YYYY-MM-DD_HH;MM;SS) in the folder results
        current_time = datetime.now().strftime("%Y-%m-%d_%H;%M;%S")
        
        # Create the subdirectory with the current time
        os.mkdir(f"results/{current_time}")
        
        # Write the custom file
        with open(f"results/{current_time}/deobfuscated.py", "w", encoding="utf-8") as f:
            f.write(full)
