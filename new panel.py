bl_info = {
    "name": "Simple Addon",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

# Property to store user input
class MyProperties(bpy.types.PropertyGroup):
    text_input: bpy.props.StringProperty(name="Text Input", default="1.0") 
# Panel class for the UI in the 3D View
class OBJECT_PT_simple_panel(bpy.types.Panel):
    bl_label = "Simple Panel"
    bl_idname = "PT_SimplePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Trial panel'

    # Draw function for the UI layout
    def draw(self, context):
        layout = self.layout

        # Add Cube button
        layout.operator("mesh.add_cube", text="Add Cube")

        # Add Sphere button
        layout.operator("mesh.add_sphere", text="Add Sphere")

        # Add Path button
        layout.operator("curve.add_path", text="Add Circular Path")
        
        # Row for input field (text input for cube size)
        row = layout.row()    
        row.prop(context.scene.my_properties, "text_input", text="")

# Operator class for adding a cube
class OBJECT_OT_add_cube(bpy.types.Operator):
    bl_label = "Add Cube"
    bl_idname = "mesh.add_cube"
    bl_options = {'REGISTER', 'UNDO'}

    # Execute function for the cube operator
    def execute(self, context):
        try:
            cube_size = float(context.scene.my_properties.text_input)
        except ValueError:
            self.report({'ERROR'}, "Invalid input. Please enter a numerical value.")
            return {'CANCELLED'}

        bpy.ops.mesh.primitive_cube_add(size=cube_size)
        return {'FINISHED'}

# Operator class for adding a sphere
class OBJECT_OT_add_sphere(bpy.types.Operator):
    bl_label = "Add Sphere"
    bl_idname = "mesh.add_sphere"
    bl_options = {'REGISTER', 'UNDO'}

    # Execute function for the sphere operator
    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
        return {'FINISHED'}

# Operator class for adding a path curve
class OBJECT_OT_add_path(bpy.types.Operator):
    bl_label = "Add Path"
    bl_idname = "curve.add_path"
    bl_options = {'REGISTER', 'UNDO'}

    # Execute function for the path operator
    def execute(self, context):
        bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        return {'FINISHED'}

# Function to add the operators to the mesh add menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_add_cube.bl_idname)
    self.layout.operator(OBJECT_OT_add_sphere.bl_idname)
    self.layout.operator(OBJECT_OT_add_path.bl_idname)

# Registration function
def register():
    bpy.utils.register_class(MyProperties)
    bpy.utils.register_class(OBJECT_PT_simple_panel)
    bpy.utils.register_class(OBJECT_OT_add_cube)
    bpy.utils.register_class(OBJECT_OT_add_sphere)
    bpy.utils.register_class(OBJECT_OT_add_path)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.types.Scene.my_properties = bpy.props.PointerProperty(type=MyProperties)

# Unregistration function
def unregister():
    bpy.utils.unregister_class(MyProperties)
    bpy.utils.unregister_class(OBJECT_PT_simple_panel)
    bpy.utils.unregister_class(OBJECT_OT_add_cube)
    bpy.utils.unregister_class(OBJECT_OT_add_sphere)
    bpy.utils.unregister_class(OBJECT_OT_add_path)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    del bpy.types.Scene.my_properties

# Entry point for the script
if __name__ == "__main__":
    register()
