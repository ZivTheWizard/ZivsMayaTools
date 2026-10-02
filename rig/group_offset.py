# python script made by Robin "Ziv" Courtoise
# contact at robincourtoise@gmail.com
#            ------------------------
# Yet another group offset script.

import maya.cmds as cmds

sel = cmds.ls(selection = True)

cmds.select(cl = True)

for s in sel:
    prt = cmds.listRelatives(s, parent = True)
    gr = cmds.createNode('transform', n=f'{s}_groupOffset',)
    cmds.matchTransform(gr, s)
    cmds.parent(s,gr)
    cmds.parent(gr,prt)