bl_info = {
    "name": "3D-Maker",
    "blender": (4, 2, 3),
    "category": "3D View",
    "author": "Austin Cabler",
    "version": (0, 2, 5),
    "description": "A plugin for Blender that uses Meshy's API to create models",
    "support": "COMMUNITY",
    "url": "https://github.com/austincabler13/3D-Maker/",
}

import bpy
import webbrowser

# Import your plugin module here
from .plugin import MeshyAPI

class MeshyOperator(bpy.types.Operator):
    bl_idname = "mesh.generate_3d_model"
    bl_label = "Generate 3D Model"

    api_key: bpy.props.StringProperty(name="API Key")
    input_data: bpy.props.StringProperty(name="Input Data")

    def execute(self, context):
        meshy_api = MeshyAPI(self.api_key)
        result = meshy_api.generate_3d_model({"input": self.input_data})

        if result.get("status") == "error":
            self.report({'ERROR'}, result["message"])
        else:
            self.report({'INFO'}, "3D model generated successfully")

        return {'FINISHED'}

class MeshyPanel(bpy.types.Panel):
    bl_label = "Meshy API 3D Model Generator"
    bl_idname = "PANEL_PT_meshy_api"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Meshy"

    # Properties for the API Key and Input Data
    api_key: bpy.props.StringProperty(name="API Key")
    input_data: bpy.props.StringProperty(name="Input Data")

    def draw(self, context):
        layout = self.layout

        # Use the panel's properties
        layout.prop(self, "api_key")
        layout.prop(self, "input_data")

        # Add a button to generate the model
        layout.operator(MeshyOperator.bl_idname, text="Generate 3D Model").api_key = self.api_key
        layout.operator(MeshyOperator.bl_idname, text="Generate 3D Model").input_data = self.input_data

        # Add a label with a link to the pricing
        layout.label(text="Note: You need an API key for usage.")
        layout.operator("wm.open_url", text="Meshy API Pricing").url = "https://docs.meshy.ai/api-introduction#pricing"

class WM_OT_OpenURL(bpy.types.Operator):
    """Open a URL in the default web browser"""
    bl_idname = "wm.open_url"
    bl_label = "Open URL"

    url: bpy.props.StringProperty()

    def execute(self, context):
        webbrowser.open(self.url)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MeshyOperator)
    bpy.utils.register_class(MeshyPanel)
    bpy.utils.register_class(WM_OT_OpenURL)  # Registering the URL operator

def unregister():
    bpy.utils.unregister_class(MeshyPanel)
    bpy.utils.unregister_class(MeshyOperator)
    bpy.utils.unregister_class(WM_OT_OpenURL)  # Unregistering the URL operator

if __name__ == "__main__":
    register()
