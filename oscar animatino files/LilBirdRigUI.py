import bpy

class LilBirdRigUI(bpy.types.Panel):
    bl_label = "Lil Birdo Rig Layers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=3, toggle = True, text = "Face Viz")
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=4, toggle = True, text = "Upper Body Viz")
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=5, toggle = True, text = "Tail Viz")
        row = col.row()
        layout.prop(context.active_object.data)
        

bpy.utils.register_class(LilBirdRigUI)