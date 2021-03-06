import unreal

@unreal.uclass()
class UEEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

EdUtil = UEEditorUtility()

selectedAssets = EdUtil.get_selected_assets()

for selectedAsset in selectedAssets:
    selectedAssets.set_editor_property("BlueprintDisplayName", "Same BP")
    selectedAssets.set_editor_property("BlueprintDescription", "This is a blueprint generated by Python or something")
    selectedAssets.set_editor_property("BlueprintCategory", "Collectable")

selectedActors = EdUtil.get_selection_set()
for actor in selectedActors:
    actor.set_editor_property("canRotate", True)
    actor.set_editor_property("bHidden", 1)
    actor.set_editor_property("SpriteScale", 2.5)