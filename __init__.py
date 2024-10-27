bl_info = {
    "name": "3D-Maker",
    "blender": (4, 2, 3),  # Change to your supported Blender version
    "category": "3D View",  # Change to the appropriate category
    "author": "Austin Cabler",
    "version": (0, 1, 4),
    "description": "A plugin for Blender that uses Meshy's API to create models",
    "support": "COMMUNITY",
    "url": "https://github.com/austincabler13/3D-Maker/"
    
}

def register():
    print("Add-on registered.")

def unregister():
    print("Add-on unregistered.")
