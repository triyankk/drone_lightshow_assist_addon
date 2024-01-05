import bpy
import math
sce = bpy.context.scene
number_of_emps = 50 #emp_last

#d_treshold = 2.51

for i in range(1, number_of_emps+1):
    ob = bpy.data.objects['Snake - ' + str(i)]
    ob.location.x=0
    ob.location.y=0
    ob.location.z=0
    constraint = ob.constraints.new('FOLLOW_PATH')
    constraint.target = bpy.data.objects['snake']
    constraint.offset = i*3 
      
#    for k in range(i, number_of_emps+1):
#       if (k != i+1):
#            ob2 = bpy.data.objects['Takeoff grid - ' + str(k)]
#            constraint = ob2.constraints.new('LIMIT_DISTANCE')
#            constraint.target = ob
#            constraint.distance = d_treshold
#            constraint.limit_mode = 'LIMITDIST_OUTSIDE'
  
          
constraint.show_expanded = False
constraint.mute = False