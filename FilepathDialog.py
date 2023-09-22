from tkinter import filedialog
import glob
import os

class Interface:
    def OpenDialog():
        target = filedialog.askdirectory()
        files = glob.glob(os.path.join(target,'*.dat'))
        return target,files