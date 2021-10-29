import unreal

info = dir(unreal)
for i in info:
    unreal.log("unreal" + str(i))
