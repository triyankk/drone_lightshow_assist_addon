import bpy

mats = 100
light_efs = 4
frame_gap = 1

def button_1_function(self, context):
 for i in range(1,mats+1):
  obj = bpy.data.objects['Drone '+str(i)]    
  node = obj.active_material.node_tree.nodes['Emission']
 
 # bpy.context.scene.frame_set(bpy.context.scene.frame_current - 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
  bpy.context.scene.frame_set(bpy.context.scene.frame_current + 1)
     
  bpy.data.materials["LED color of Drone "+str(i)].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0, 0, 1)
  obj = bpy.data.objects['Drone '+str(i)]
  node.inputs[0].keyframe_insert(data_path="default_value")
 
  bpy.context.scene.frame_set(bpy.context.scene.frame_current + frame_gap )
 
  bpy.data.materials["LED color of Drone "+str(i)].node_tree.nodes["Emission"].inputs[0].default_value = (0, 0, 1, 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
 
  bpy.context.scene.frame_set(bpy.context.scene.frame_current + frame_gap)
 
  bpy.data.materials["LED color of Drone "+str(i)].node_tree.nodes["Emission"].inputs[0].default_value = (0, 1, 0, 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
 
  bpy.context.scene.frame_set(bpy.context.scene.frame_current + frame_gap)
 
  bpy.data.materials["LED color of Drone "+str(i)].node_tree.nodes["Emission"].inputs[0].default_value = (1, 1, 1, 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
 
  bpy.context.scene.frame_set(bpy.context.scene.frame_current + frame_gap)
 
  bpy.data.materials["LED color of Drone "+str(i)].node_tree.nodes["Emission"].inputs[0].default_value = (0, 0, 0, 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
 
  bpy.context.scene.frame_set(bpy.context.scene.frame_current - light_efs * frame_gap)

def button_2_function(self, context):
    print("Button 2 pressed!")

def button_3_function(self, context):
    print("Button 3 pressed!")

class MyPanel(bpy.types.Panel):
    bl_label = "My Panel"
    bl_idname = "OBJECT_PT_my_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Category"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.button_1", text="Button 1")
        row.operator("object.button_2", text="Button 2")
        row.operator("object.button_3", text="Button 3")

class Button1Operator(bpy.types.Operator):
    bl_idname = "object.button_1"
    bl_label = "Button 1"

    def execute(self, context):
        button_1_function(self, context)
        return {'FINISHED'}

class Button2Operator(bpy.types.Operator):
    bl_idname = "object.button_2"
    bl_label = "Button 2"

    def execute(self, context):
        button_2_function(self, context)
        return {'FINISHED'}

class Button3Operator(bpy.types.Operator):
    bl_idname = "object.button_3"
    bl_label = "Button 3"

    def execute(self, context):
        button_3_function(self, context)
        return {'FINISHED'}

classes = (MyPanel, Button1Operator, Button2Operator, Button3Operator)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
