import bpy
from .meshy_api import MeshyAPI  # Relative import for Blender add-on compatibility

class MeshyPluginOperator(bpy.types.Operator):
    bl_idname = "meshy.plugin_operator"
    bl_label = "Generate 3D Model with Meshy"
    bl_description = "Generate a 3D model using the Meshy API"

    def execute(self, context):
        # Retrieve API key and inputs from Blender properties
        api_key = context.scene.meshy_api_key
        input_data = {
            "model_type": context.scene.model_type,
            "detail_level": context.scene.detail_level
        }

        # Initialize and call Meshy API
        meshy_api = MeshyAPI(api_key)
        response = meshy_api.generate_3d_model(input_data)

        # Process response (assuming it returns mesh data)
        print(response)  # Print response for debugging purposes
        if response.get("status") == "success":
            self.report({'INFO'}, "Model generated successfully!")
        else:
            self.report({'ERROR'}, "Failed to generate model.")
        
        return {'FINISHED'}

class MeshyPluginPanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_meshy_plugin"
    bl_label = "Meshy 3D Model Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Meshy Plugin'

    def draw(self, context):
        layout = self.layout

        # Input fields for API Key and model generation parameters
        layout.prop(context.scene, "meshy_api_key", text="API Key")
        layout.prop(context.scene, "model_type", text="Model Type")
        layout.prop(context.scene, "detail_level", text="Detail Level")

        # Button to execute the Meshy API call
        layout.operator("meshy.plugin_operator", text="Generate 3D Model")

def register():
    bpy.utils.register_class(MeshyPluginOperator)
    bpy.utils.register_class(MeshyPluginPanel)
    
    # Define custom properties for user input
    bpy.types.Scene.meshy_api_key = bpy.props.StringProperty(name="API Key", description="Meshy API Key")
    bpy.types.Scene.model_type = bpy.props.StringProperty(name="Model Type", description="Type of model to generate")
    bpy.types.Scene.detail_level = bpy.props.IntProperty(name="Detail Level", description="Level of detail", default=1, min=1, max=5)

def unregister():
    bpy.utils.unregister_class(MeshyPluginOperator)
    bpy.utils.unregister_class(MeshyPluginPanel)
    
    # Remove custom properties
    del bpy.types.Scene.meshy_api_key
    del bpy.types.Scene.model_type
    del bpy.types.Scene.detail_level

if __name__ == "__main__":
    register()
