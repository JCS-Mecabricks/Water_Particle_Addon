bl_info = {
    "name": "Snow/Water Particles Addon",
    "author": "JCS",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Water Droplet/Snow Addon",
    "description": "Adds Rain/Snow To Your Model",
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
            ico_sphere = bpy.context.active_object
            color = (0.0154895, 0.397459, 0.800505, 1) 
            material = bpy.data.materials.new("Color")
            material.diffuse_color = color
            mat = bpy.data.materials.new(name='Material')
            mat.use_nodes=True
            mat_nodes = mat.node_tree.nodes
            mat_links = mat.node_tree.links
            ico_sphere.data.materials.append(mat)        
            mat_nodes["Principled BSDF"].inputs['Metallic'].default_value = 1
            bpy.ops.object.shade_smooth()


        return {'FINISHED'}
class CustomPanel(bpy.types.Panel):
    bl_label = "Water Droplet/Snow Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Water Droplet/Snow Addon"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Add Rain/Snow", icon='SHADING_SOLID')

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
