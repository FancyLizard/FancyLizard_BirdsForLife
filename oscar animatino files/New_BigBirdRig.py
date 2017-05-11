import bpy

class BigBirdRigUI(bpy.types.Panel):
    bl_label = "Big Bird Rig Controls" #name in the properties Panel
    bl_space_type = "VIEW_3D" # when you can see it
    bl_region_type = "UI" # so it appears in the properties panel (alternately you can type TOOLS to appear in toolbar instead)
    bl_context = "posemode" # so you will only see it in posemode
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        pose_bones = context.active_object.pose.bones
        try:
            selected_bones = [bone.name for bone in context.selected_pose_bones]
            selected_bones += [context.active_pose_bone.name]
        except (AttributeError, TypeError):
            return
        
        def is_selected(names):
        #Returns whether any of the named bones are selected
            if type(names) == list:
                for name in names:
                    if name in selected_bones:
                        return True
            elif names in selected_bones:
                return True
            return False
    
        #Define the names we'll use for bones
        #Head region
        Head = "BB_head"
        Jaw1 = "BB_Jaw.000"
        Jaw2 = "BB_Jaw.001"
        Beak = "BB_Beak.000"
        
        #Neck
            #FK
        Neck1 = "BB_NeckFK.000"
        Neck2 = "BB_NeckFK.004"
        Neck3 = "BB_NeckFK.008"
        Neck4 = "BB_NeckFK.012"
            #IK
        NeckPole = "BB_NeckPole"    
          
        #FK/IK Arm Region
        ###note to self: there was a syntax error and the issue was there were spaces there can't be spaces (ex. Arm FK 1 L <--- Wrong  Right---> ArmFK1L or Arm_FK_1_L)
            #FK
        ArmFK1L= "BB_FeatherArm1FK.l"
        ArmFK2L= "BB_FeatherArm5FK.l"
        ArmFK3L= "BB_FeatherArm9FK.l"
        ArmFK1R= "BB_FeatherArm1FK.r"
        ArmFK2R= "BB_FeatherArm5FK.r"
        ArmFK3R= "BB_FeatherArm9FK.r"
            #IK
        IKPoleL = "BB_IKPole2.l"
        IKPoleR = "BB_IKPole2.r"
        IKHDLL = "BB_FeatherArm9IK.l"
        IKHDLR = "BB_FeatherArm9IK.r"
        
       #FK/IK Leg Region
            #FK
        ThighLFK= "BB_BrokenThighFK.l"
        ShinLFK = "BB_Shin1FK.l"
        AnkleLFK= "BB_ankleFK.l"
        ThighRFK= "BB_BrokenThighFK.r"
        ShinRFK = "BB_Shin1FK.r"
        AnkleRFK= "BB_ankleFK.r"
            #IK
        IKLegPoleL = "BB_IKLegPole.l"
        IKLegPoleR = "BB_IKLegPole.r"
        IKLegHDLL = "BB_FootIK.l"
        IKLegHDLR = "BB_FootIK.r"
       
        #Head, Neck and face controls
        if is_selected([Head]):
            layout.prop(pose_bones["BB_head"], '["Beak_and_Jaw"]', slider=True)     
            layout.prop(pose_bones["BB_head"], '["Eye CTRL"]', slider=True)
            layout.prop(pose_bones["BB_head"], '["Eyebrows L"]', slider=True)
            layout.prop(pose_bones["BB_head"], '["Eyebrows R"]', slider=True)
            layout.prop(pose_bones["BB_head"], '["Head Feathers"]', slider=True)
            layout.prop(pose_bones["BB_head"], '["Blink"]', slider=True)
            
        if is_selected([Head,Beak, Jaw1]):
            layout.prop(pose_bones["BB_head"], '["Mouth Corner tweak"]', slider=True)
        
        if is_selected([Head, Neck1, Neck2, Neck3, Neck4, NeckPole]):
            layout.prop(pose_bones["BB_head"],'["FK/IK neck"]', slider=True)    
        
        if is_selected([Head,Beak]):
            layout.prop(pose_bones ["BB_head"],'["Cheeks L"]', slider=True)
            layout.prop(pose_bones ["BB_head"], '["Cheeks R"]', slider=True)
            
        if is_selected([Beak]):
            layout.prop(pose_bones["BB_Beak.000"], '["UpperMouthTweaks"]', slider=True)
            
        if is_selected([Jaw1]):
            layout.prop(pose_bones["BB_Jaw.000"],'["Extra Bend Jaw"]', slider=True)     
            layout.prop(pose_bones["BB_Jaw.000"],'["Lower Mouth Tweak"]', slider=True)
            layout.prop(pose_bones["BB_Jaw.000"],'["Tongue Viz & Follow"]', slider=True)
        #FK/IK Arm L Visibility
        if is_selected([ArmFK1L,  ArmFK2L,  ArmFK3L, IKPoleL, IKHDLL]):
            layout.prop(pose_bones["BB_FeatherArm9IK.l"], '["FK/IK Switch Arm L"]', slider=True)
        
        #Arm bones independence L
        if is_selected([ArmFK1L]):
            layout.prop(pose_bones["BB_FeatherArm1FK.l"],'["Bone 1 Independent L"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm1FK.l"],'["Bone 2 independent L"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm1FK.l"],'["Bone 3 independent L"]', slider=True)
            
        if is_selected([ArmFK2L]):
            layout.prop(pose_bones["BB_FeatherArm5FK.l"], '["Bone 4 independent L"]', slider=True)    
            layout.prop(pose_bones["BB_FeatherArm5FK.l"], '["Bone 5 independent L"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm5FK.l"], '["Bone 6 independent L"]', slider=True)
            
        if is_selected([ArmFK3L]):
            layout.prop(pose_bones["BB_FeatherArm9FK.l"], '["Bone 7 independent L"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm9FK.l"], '["Bone 8 independent L"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm9FK.l"], '["Bone 9 independent L"]', slider=True)
            
        #FK/IK Arm R Visibility
        if is_selected([ArmFK1R,  ArmFK2R,  ArmFK3R, IKPoleR, IKHDLR]):
            layout.prop(pose_bones["BB_FeatherArm9IK.r"],'["FK/IK Switch Arm R"]', slider=True)
            
        #Arm bones independence R
        if is_selected([ArmFK1R]):
            layout.prop(pose_bones["BB_FeatherArm1FK.r"],'["Bone 1 independent R"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm1FK.r"],'["Bone 2 independent R"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm1FK.r"],'["Bone 3 independent R"]', slider=True)
            
        if is_selected([ArmFK2R]):
            layout.prop(pose_bones["BB_FeatherArm5FK.r"], '["Bone 4 independent R"]', slider=True)    
            layout.prop(pose_bones["BB_FeatherArm5FK.r"], '["Bone 5 independent R"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm5FK.r"], '["Bone 6 independent R"]', slider=True)
            
        if is_selected([ArmFK3R]):
            layout.prop(pose_bones["BB_FeatherArm9FK.r"], '["Bone 7 independent R"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm9FK.r"], '["Bone 8 independent R"]', slider=True)
            layout.prop(pose_bones["BB_FeatherArm9FK.r"], '["Bone 9 independent R"]', slider=True)
            
        #Leg Controls
            #FK/IK Switch
        if is_selected([ThighLFK, ShinLFK, AnkleLFK, IKLegHDLL,  IKLegPoleL]):
            layout.prop(pose_bones["BB_IKLegPole.l"], '["FK/IK Switch Leg L"]', slider=True)
        
        if is_selected([ThighRFK, ShinRFK, AnkleRFK, IKLegHDLR, IKLegPoleR]):  
            layout.prop(pose_bones["BB_IKLegPole.r"], '["FK/IK Switch Leg R"]', slider=True)
            
            #BrokenBones
        if is_selected([ThighRFK, ShinRFK, AnkleRFK, ThighLFK, ShinLFK, AnkleLFK]):  
            layout.prop(pose_bones["BB_Shin1FK.l"],'["Broken bones L"]', slider=True)
            layout.prop(pose_bones["BB_Shin1FK.r"],'["Broken Bones R"]', slider=True)
            
###RIG Layers
class BigBirdRigLayers(bpy.types.Panel):
    bl_label = "Big Bird Rig Layers" #name in the properties Panel
    bl_space_type = "VIEW_3D" # when you can see it
    bl_region_type = "UI" # so it appears in the properties panel (alternately you can type TOOLS to appear in toolbar instead)
    bl_label = "Big Bird Rig Layers"   
    
    def draw(self, context):
        layout = self.layout    
        #creates a column  
        col = layout.column()
           
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=0, toggle=True, text='HEAD')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=1, toggle=True, text='NECK FK')
        row.prop(context.active_object.data, 'layers', index=17, toggle=True, text='NECK IK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=16, toggle=True, text='BODY')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=7, toggle=True, text='ARM FK L')
        row.prop(context.active_object.data, 'layers', index=6, toggle=True, text='ARM FK R')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=23, toggle=True, text='ARM IK L')
        row.prop(context.active_object.data, 'layers', index=22, toggle=True, text='ARM IK R')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=9, toggle=True, text='TAIL')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=4, toggle=True, text='LEG FK L')
        row.prop(context.active_object.data, 'layers', index=3, toggle=True, text='LEG FK R')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=20, toggle=True, text='LEG IK L')    
        row.prop(context.active_object.data, 'layers', index=19, toggle=True, text='LEG IK R')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=25, toggle=True, text='TOES')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=26, toggle=True, text='ROOT')
        
         
         #an ending to our python script
bpy.utils.register_class(BigBirdRigUI)
bpy.utils.register_class(BigBirdRigLayers) 