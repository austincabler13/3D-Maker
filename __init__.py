bl_info = {
    "name": "3D-Maker",
    "blender": (4, 2, 3),
    "category": "3D View",
    "author": "Austin Cabler",
    "version": (0, 1, 4),
    "description": "A plugin for Blender that uses Meshy's API to create models",
    "support": "COMMUNITY",
    "url": "https://github.com/austincabler13/3D-Maker/",
}

# Import the plugin module
from . import plugin

def register():
    plugin.register()  # Register the classes from plugin.py

def unregister():
    plugin.unregister()  # Unregister the classes from plugin.py

if __name__ == "__main__":
    register()
