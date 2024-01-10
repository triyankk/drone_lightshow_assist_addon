# Import Blender Python module
import bpy

# Property Group to store user input
class MyProperties(bpy.types.PropertyGroup):
    drone_count: bpy.props.IntProperty(name="Drone Count", default=25, min=1)
    distance_threshold: bpy.props.FloatProperty(name="Distance Threshold", default=2.51, min=0.01)

# Panel class for the UI in the 3D View
class OBJECT_PT_distance_constraint_panel(bpy.types.Panel):
    bl_label = "Distance Constraint Panel"
    bl_idname = "PT_DistanceConstraintPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My New Category'  # Change this to the desired category name

    # Draw function for the UI layout
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        my_properties = scene.my_properties

        # Display properties and operator in the UI
        layout.prop(my_properties, "drone_count")
        layout.prop(my_properties, "distance_threshold")
        layout.operator("object.apply_distance_constraints", text="Apply Distance Constraints")
        
class OBJECT_PT_additional_panel(bpy.types.Panel):
    bl_label = "Additional Panel"
    bl_idname = "PT_AdditionalPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My New Category'  # Use the same category as the previous panel

    # Draw function for the UI layout
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        my_properties = scene.my_properties

        # Display properties and operator in the UI
        layout.prop(my_properties, "drone_count")
        layout.prop(my_properties, "distance_threshold")
        layout.operator("object.apply_distance_constraints", text="Apply Distance Constraints")        

# Operator class to apply distance constraints
class OBJECT_OT_apply_distance_constraints(bpy.types.Operator):
    bl_label = "Apply Distance Constraints"
    bl_idname = "object.apply_distance_constraints"
    bl_options = {'REGISTER', 'UNDO'}

    # Execute function for the operator
    def execute(self, context):
        my_properties = context.scene.my_properties
        number_of_uavs = my_properties.drone_count
        d_threshold = my_properties.distance_threshold

        # Apply distance constraints between drones
        for i in range(1, number_of_uavs + 1):
            ob = bpy.data.objects.get('Drone ' + str(i))
            if ob:
                for k in range(1, number_of_uavs + 1):
                    if i != k:
                        ob2 = bpy.data.objects.get('Drone ' + str(k))
                        if ob2:
                            constraint = ob2.constraints.new('LIMIT_DISTANCE')
                            constraint.target = ob
                            constraint.distance = d_threshold
                            constraint.limit_mode = 'LIMITDIST_OUTSIDE'
                            constraint.show_expanded = False
                            constraint.mute = False

        return {'FINISHED'}

# Function to add the operator to the mesh add menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_apply_distance_constraints.bl_idname)

# Registration function
def register():
    bpy.utils.register_class(MyProperties)
    bpy.utils.register_class(OBJECT_PT_distance_constraint_panel)
    bpy.utils.register_class(OBJECT_PT_additional_panel)
    bpy.utils.register_class(OBJECT_OT_apply_distance_constraints)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.types.Scene.my_properties = bpy.props.PointerProperty(type=MyProperties)

# Unregistration function
def unregister():
    bpy.utils.unregister_class(MyProperties)
    bpy.utils.unregister_class(OBJECT_PT_distance_constraint_panel)
    bpy.utils.unregister_class(OBJECT_PT_additional_panel)
    bpy.utils.unregister_class(OBJECT_OT_apply_distance_constraints)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    del bpy.types.Scene.my_properties

# Entry point for the script
if __name__ == "__main__":
    register()
