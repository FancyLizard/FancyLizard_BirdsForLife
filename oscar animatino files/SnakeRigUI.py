import bpy

###RIG CONTROLS

class RigUI(bpy.types.Panel):
    bl_label = "Snake Rig Controls"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"
    
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
        Head = "SnakeHead"
        Jaw = "snakeJaw"
        
        #Face region
        ForebrowL = "S_ForeBrowCTRL.l"
        ForebrowR = "S_ForeBrowCTRL.r"
        
        eyecornerL= "S_EyecornerCTRL.l"
        eyecornerR= "S_EyecornerCTRL.r"
        
        Upperlip = "S_MouthTopMid"
        UpperLLip = "S_UpperLipCTRL.l"
        UpperRLip = "S_UpperLipCTRL.r"
        
        Bottomlip = "S_MouthBotMid"
        BottomLLip = "S_LowerLipCTRL.l"
        BottomRLip = "S_LowerLipCTRL.r"
        
        
        #Tail/Body Region
        Neck_fk = "FKSnakeNeck1"
        TailBod2_fk = "FKTailBod6"
        TailBod1_fk = "FKTailBod3"
        TailBodEnd_fk = "FKTailBodEnd"
        
        #TailEnd Region
        TailStart_fk = "FKTailStart"
        TailB_fk = "FKTailb"
        TailC_fk = "FKTailC"
        TailD_fk = "FKTailD"

        
        NeckEnd_IK = "SnakeNeckEndIK"
        NeckVizIK = "S_IKFrontViz"
        NeckPole = "S_IKPole"
        
        Tail_IK = "IKTd3"
        Tail_Pole = "IK_TailPole"
          
        #Define what controls to show depending on the bones selected
        #IK Visibility
        if is_selected([Tail_Pole,  Tail_IK,  TailStart_fk, TailB_fk, TailC_fk, TailD_fk]):
            layout.prop(pose_bones["IKTd3"], '["FK/IK switch"]', slider=True)
        
        if is_selected([NeckEnd_IK , NeckPole , Neck_fk, TailBod2_fk, TailBod1_fk, TailBodEnd_fk]):
            layout.prop(pose_bones["S_IKPole"], '["FK/IK Switch"]', slider=True)
            
        #Head Controls Visability    
        if is_selected([Head]):
            layout.prop(pose_bones["SnakeHead"], '["ExtraCTRLs Viz"]', slider=True)
            
        if is_selected([Head]):
            layout.prop(pose_bones["SnakeHead"], '["EyeCTRL Viz"]', slider=True)
            
        if is_selected([Head]):
            layout.prop(pose_bones["SnakeHead"], '["Eyebrow CTRL Viz"]', slider=True)
            
        if is_selected([Head]):
            layout.prop(pose_bones["SnakeHead"], '["ForeBrow Viz CTRL"]', slider=True)
        
        if is_selected([Head]):
            layout.prop(pose_bones["SnakeHead"], '["Mouth Sides CTRL Viz"]', slider=True)

        #EyeBrow Control Visibility
        if is_selected([ForebrowL]):
            layout.prop(pose_bones["S_ForeBrowCTRL.l"], '["ForeBrow Tweak VIZ.l"]', slider=True)
        
        if is_selected([ForebrowR]):
            layout.prop(pose_bones["S_ForeBrowCTRL.r"], '["Forebrow Tweak VIZ.r"]', slider=True)
            
        #Eyes & Cheeks    
        if is_selected([eyecornerL]):
            layout.prop(pose_bones["S_EyecornerCTRL.l"], '["Cheek Control.l"]', slider=True)
        
        if is_selected([eyecornerL]):
            layout.prop(pose_bones["S_EyecornerCTRL.l"], '["Cheek Tweak Viz.l"]', slider=True)
        
        if is_selected([eyecornerL]):
            layout.prop(pose_bones["S_EyecornerCTRL.l"], '["Eye Tweak VIZ.l"]', slider=True)
            
        if is_selected([eyecornerR]):
            layout.prop(pose_bones["S_EyecornerCTRL.r"], '["Cheek Control.r"]', slider=True)
        
        if is_selected([eyecornerR]):
            layout.prop(pose_bones["S_EyecornerCTRL.r"], '["Cheek Tweak Viz.r"]', slider=True)
        
        if is_selected([eyecornerR]):
            layout.prop(pose_bones["S_EyecornerCTRL.r"], '["Eye Tweak Viz.r"]', slider=True)        
       
        #Mouth Control Visibility
        #Upper Lips Control 
        if is_selected([Upperlip]):
            layout.prop(pose_bones["S_MouthTopMid"], '["Extra Teeth CTRL Viz Top"]', slider=True)
        
        if is_selected([Upperlip]):
            layout.prop(pose_bones["S_MouthTopMid"], '["Extra Teeth Viz Top"]', slider=True)  
        
        if is_selected([Upperlip]):
            layout.prop(pose_bones["S_MouthTopMid"], '["Fang CTRL Viz"]', slider=True)
        
        if is_selected([Upperlip]):
            layout.prop(pose_bones["S_MouthTopMid"], '["Fangs Retract"]', slider=True)      
            
        if is_selected([UpperLLip]):
            layout.prop(pose_bones["S_UpperLipCTRL.l"], '["UpperLip Tweak VIZ.l"]', slider=True) 
        
        if is_selected([UpperRLip]):
            layout.prop(pose_bones["S_UpperLipCTRL.r"], '["Upperlip Tweak Viz.r"]', slider=True)       
       
       #Lower Lips Controls
        if is_selected([Bottomlip]):
            layout.prop(pose_bones["S_MouthBotMid"], '["Bot Fangs CTRL Viz"]', slider=True)
        
        if is_selected([Bottomlip]):
            layout.prop(pose_bones["S_MouthBotMid"], '["Extra Teeth CTRL Viz Bot"]', slider=True)
            
        if is_selected([Bottomlip]):
            layout.prop(pose_bones["S_MouthBotMid"], '["Extra Teeth Viz Bot"]', slider=True)
        
        if is_selected([Bottomlip]):
            layout.prop(pose_bones["S_MouthBotMid"], '["Retract/Adhere Bot Fangs"]', slider=True)
        
        if is_selected([Bottomlip]):
            layout.prop(pose_bones["S_MouthBotMid"], '["Retract/Adhere Tongue"]', slider=True)  
        
        if is_selected([BottomLLip]):
            layout.prop(pose_bones["S_LowerLipCTRL.l"], '["LowerLip Tweak VIZ.l"]', slider=True)
        
        if is_selected([BottomRLip]):
            layout.prop(pose_bones["S_LowerLipCTRL.r"], '["Lowerlip Tweak Viz.r"]', slider=True)                      
       
            
      
    
    
###RIG LAYERS    
    
class RigLayers(bpy.types.Panel):
    bl_label = "Rig Controls"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Snake Rig Layers"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        #Layers
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=0, toggle=True, text='head/face')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=6, toggle=True, text='FK Body')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=22, toggle=True, text='IK Body')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=7, toggle=True, text='FK Tail')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=23, toggle=True, text='IK Tail')
            
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=16, toggle=True, text='ROOT')
    
    
    
bpy.utils.register_class(RigUI)
bpy.utils.register_class(RigLayers)