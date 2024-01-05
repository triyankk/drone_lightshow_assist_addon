import bpy
import math

sce = bpy.context.scene
mats = 100 #emp_last
f_frame=1
l_frame=240
light_efs = 4
frame_gap = 10


selected_objs = bpy.context.selected_objects

# set the keyframe on each object
for i, obj in enumerate(selected_objs):   
  curr_frame= bpy.context.scene.frame_current


  name_suf = obj.name.split(' ')[-1]
  obj = bpy.data.objects['Drone '+str(name_suf)]    
  node = obj.active_material.node_tree.nodes['Emission']
 
 
  sce.frame_set(curr_frame+ 1)
     
  bpy.data.materials["LED color of Drone "+str(name_suf)].node_tree.nodes["Emission"].inputs[0].default_value = (0, 0, 0, 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
 
  sce.frame_set(curr_frame + frame_gap)
  
  bpy.data.materials["LED color of Drone "+str(name_suf)].node_tree.nodes["Emission"].inputs[0].default_value = (0, 0, 1, 1)
  node.inputs[0].keyframe_insert(data_path="default_value")
 
 
 
 
 

