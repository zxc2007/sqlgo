import os
import sys
sys.path.append(os.getcwd())
from lib.core.parser.cmdline import install_dep

def install_dependent():
    if install_dep:
        try:
            os.system("pip install -r requirements.txt")
        
        except os.error:
            try:
                
                os.system("pip3 install -r requirements.txt")
            
            except os.error:
                try:
                    os.system("python -m install -r requirements.txt")
                
                except:
                    os.system("python3 -m install -r requirements.txt")


