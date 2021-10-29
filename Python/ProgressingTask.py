import unreal

totalFrames = 100000
textDisplay = "i love python, an i guess i'll be using this for a while!"

with unreal.ScopredSlowTask(totalFrames, textDisplay) as ST:
    ST.make_dialog(True)
    for i in range (totalFrames):
        if ST.should_cancel():
            break
        unreal.log("one step!!!")
        ST.enter_progress_frame(1)
