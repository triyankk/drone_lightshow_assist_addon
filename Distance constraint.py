import bpy
import math
sce = bpy.context.scene
number_of_uavs = 19 #Drone Count
d_treshold = 2.51

for i in range(1, number_of_uavs+1):
    ob = bpy.data.objects['Drone ' + str(i)]    
    for k in range(1, number_of_uavs):
            ob2 = bpy.data.objects['Drone ' + str(k)]
            constraint = ob2.constraints.new('LIMIT_DISTANCE')
            constraint.target = ob
            constraint.distance = d_treshold
            constraint.limit_mode = 'LIMITDIST_OUTSIDE'
            constraint.show_expanded = False
            constraint.mute = False



