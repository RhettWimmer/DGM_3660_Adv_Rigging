'''rot 90 X for legs and torso, 90 Y for arms '''

import maya.cmds as mc

UserDefinedRadius = 10

class CC():
    def createControl(self, UserDefinedRadius):
    
        sels = mc.ls(sl = True)
        
        if len(sels):
            for sel in sels:
                selName1 = str(sel).replace("_Geo","")
                selName2 = selName1.replace("_Jnt","")
                pivCen = mc.xform(sel, q = True, ws = True, scalePivot = True)
                Rot = mc.xform(sel, q = True, ws = True, rotation = True)
                createC = mc.circle (name = selName2 + '_Ctrl ', radius = UserDefinedRadius)
                mc.move(pivCen[0], pivCen[1], pivCen[2], createC)
                mc.rotate(0, 90, 0, createC)
                
        if (len(sels) == 0):
            mc.circle(nr = [0, 0, 0], name = '_Ctrl',radius = UserDefinedRadius)      
        mc.warning('! ! ! Control placed sucessfully ! ! !')       
create = CC()
create.createControl(UserDefinedRadius)
