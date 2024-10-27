import bpy
import requests
import webbrowser

class MeshyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.meshy.ai"

    def generate_3d_model(self, input_data):
        url = f"{self.base_url}/generate_3d_model"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.post(url, json=input_data, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "message": response.text}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": str(e)}

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

    def draw(self, context):
        layout = self.layout
        operator = layout.operator(MeshyOperator.bl_idname)
        layout.prop(operator, "api_key")
        layout.prop(operator, "input_data")

        # Add a label with a link to the pricing
        layout.label(text="Note: You need an API key for usage.")
        layout.operator("wm.open_url", text="Meshy API Pricing").url = "https://api.meshy.ai/pricing"
        
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

def unregister():
    bpy.utils.unregister_class(MeshyPanel)
    bpy.utils.unregister_class(MeshyOperator)

if __name__ == "__main__":
    register()
