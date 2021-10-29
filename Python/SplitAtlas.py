#from pyautogui import*
#import pyautogui
import time
#import keyboard
import random
#import wid32api, win32con
import unreal


# get_selected_assets
@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

#pockets
selectedAssets = MyEditorUtility().get_selected_assets()

for asset in range(selectedAssets):
    unreal.log("type() : " + asset.get_class())
