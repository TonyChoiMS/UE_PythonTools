import unreal

actorsCount = 50
slowTaskDisplayText = "Spawning actors in the level..."

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedAsset = MyEditorUtility().get_selected_assets()

with unreal.ScopedSlowTask(actorsCount, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range (actorsCount):
        if ST.should_cancel():
            break

        unreal.EditorLevelLibrary.spawn_actor_from_object(selectedAsset[0], unreal.Vector(1.0+x*100, 1.0, 30.0), unreal.Rotator(0.0, 90.0, 0.0))
        unreal.log("Just added an actor to the level")
        ST.enter_progress_frame(1)