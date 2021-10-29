import ctypes

def Mbox(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 16)

Mbox("Error Message", "Please Select Texture Asset!!")