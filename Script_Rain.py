bl_info = {
    "name": "Water Particles Addon",
    "author": "JCS",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Water Droplet Addon",
    "description": "Adds Rain To Your Model",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from random import randint
from bpy.types import Operator

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"


    def execute(self, context):
        for i in range(130):
            x = randint (-40, 70)
            y = randint (-40, 70)
            z = randint (20, 70)
            bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
            sphere = bpy.context.active_object
            color = (0.0154895, 0.397459, 0.800505, 1)
            material = bpy.data.materials.new("material")
            material.diffuse_color = color
            sphere.data.materials.append(material)
            bpy.ops.object.shade_smooth()


        return {'FINISHED'}
class CustomPanel(bpy.types.Panel):
    bl_label = "Water Droplet Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Water Droplet Addon"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Add Rain", icon='KEYTYPE_BREAKDOWN_VEC')

from bpy.utils import register_class, unregister_class

_classes = [
    ButtonOperator,
    CustomPanel
]
def register():
        for cls in _classes:
            register_class(cls)
   
def unregister():
        for cls in _classes:
            unregister_class(cls)

if __name__ == "__main__":
    register()
