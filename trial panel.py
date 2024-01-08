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
    bl_category = 'cube trial'

    # Draw function for the UI layout
    def draw(self, context):
        layout = self.layout

        # Row for input field and button
        row = layout.row(align=True)
        row.operator("object.color_transition", text="Apply Effect")
        row.prop(context.scene.my_properties, "text_input", text="")
        

# Operator class for adding light effect
class OBJECT_OT_color_transition(bpy.types.Operator):
    bl_label = "Add Cube"
    bl_idname = "object.color_transition"
    bl_options = {'REGISTER', 'UNDO'}

    # Execute function for the light effect operator
    def execute(self, context):
        try:
            frame_size = float(context.scene.my_properties.text_input)
        except ValueError:
            self.report({'ERROR'}, "Invalid input. Please enter a numerical value.")
            return {'CANCELLED'}
        
        selected_objs = bpy.context.selected_objects
        for i, obj in enumerate(selected_objs):   
            name_suf = obj.name.split(' ')[-1]
            obj = bpy.data.objects.get('Drone '+str(name_suf))
            if obj:
                node = obj.active_material.node_tree.nodes.get('Emission')
                if node:
                    current_frame = context.scene.frame_current
                    start_frame = current_frame + 1
                    end_frame = current_frame + frame_size

                    # Insert keyframes
                    node.inputs[0].default_value = (0, 0, 0, 1)
                    node.inputs[0].keyframe_insert(data_path="default_value", frame=start_frame)
                    
                    node.inputs[0].default_value = (0, 0, 1, 1)
                    node.inputs[0].keyframe_insert(data_path="default_value", frame=end_frame)
        
        return {'FINISHED'}

# Function to add the operators to the mesh add menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_color_transition.bl_idname)

# Registration function
def register():
    bpy.utils.register_class(MyProperties)
    bpy.utils.register_class(OBJECT_PT_simple_panel)
    bpy.utils.register_class(OBJECT_OT_color_transition)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.types.Scene.my_properties = bpy.props.PointerProperty(type=MyProperties)

# Unregistration function
def unregister():
    bpy.utils.unregister_class(MyProperties)
    bpy.utils.unregister_class(OBJECT_PT_simple_panel)
    bpy.utils.unregister_class(OBJECT_OT_color_transition)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    del bpy.types.Scene.my_properties

# Entry point for the script
if __name__ == "__main__":
    register()
