import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedActors = MyEditorUtility().get_selection_set()

for actor in selectedActors:
    unreal.log(actor.get_name())
    if actor.actor_has_tag("tagOne"):
        unreal.log("[1]")
    if actor.actor_has_tag("tagTwo"):
        unreal.log("[2]")
    
    pass

unreal.log("Clear")