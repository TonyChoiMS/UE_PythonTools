import unreal

totalRequiredBluprints = 70
newAssetName = "BP_pythonMade_%d"
createdAssetsPath = "/Game/TestStuff"
slowTaskDisplayText = "Creating new Assets..."

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Pawn)

assetTools = unreal.AssetToolsHelpers.get_asset_tools()

with unreal.ScopedSlowTask(totalRequiredBluprints, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range(totalRequiredBluprints):
        if ST.should_cancel():
            break
        newAsset = assetTools.create_asset(newAssetName%(x), createdAssetsPath, None, factory)
        unreal.EditorAssetLibrary.save_loaded_asset(newAsset)
        unreal.log("Just created an asset BP_PythonMade_%d via Python API" %(x))
        ST.enter_progress_frame(1)