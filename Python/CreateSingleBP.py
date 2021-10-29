import unreal

blueprintName = "MyEpicBPActorClass"

#define path
blueprintPath = "/Game/AutoCreated"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Actor)

# AseetToolsHelper  Create

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
myFancyNewAssetFile = assetTools.create_asset(blueprintName, blueprintPath, None, factory)

#EditorAssetLibrary  Save & loaded
unreal.EditorAssetLibrary.save_loaded_asset(myFancyNewAssetFile)