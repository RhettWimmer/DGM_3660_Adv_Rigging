import maya.cmds as mc

sels = mc.ls(sl=True)

for sel in sels:
    if (mc.nodeType(sel) == 'joint'):
        if mc.getAttr('%s.displayLocalAxis' % sel) == False:
            mc.setAttr('%s.displayLocalAxis' % sel, k = True)
            mc.setAttr('%s.jointOrientX' % sel, k = True)
            mc.setAttr('%s.jointOrientY' % sel, k = True)
            mc.setAttr('%s.jointOrientZ' % sel, k = True)
            mc.setAttr('%s.displayLocalAxis' % sel, True)  
        else:
            mc.setAttr('%s.displayLocalAxis' % sel, k = False, cb = False)  
            mc.setAttr('%s.jointOrientX' % sel, k = False, cb = False)
            mc.setAttr('%s.jointOrientY' % sel, k = False, cb = False)
            mc.setAttr('%s.jointOrientZ' % sel, k = False, cb = False)
            mc.setAttr('%s.displayLocalAxis' % sel, False)        