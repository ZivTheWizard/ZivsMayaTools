# python script made by Robin "Ziv" Courtoise
# contact at robincourtoise@gmail.com
#            ------------------------
# This script helps in creating very simple interlocking gears/cogs.

import maya.cmds as cmds

class Gearificator:
    def __init__(self):
        self.ui()

    def ui(self):
        self.window = cmds.window( title="Gearificator", iconName='Gearificator', widthHeight=(200, 150) )
        cmds.columnLayout( adjustableColumn=True )

        self.teeth_number_label = cmds.text(label = 'Teeth Number', ann = 'Larger number of teeth leads to larger gears.')
        self.teeth_number_field = cmds.intField(min=3, max=50, value=10)

        self.teeth_size_label = cmds.text(label = 'Size', ann = 'All gears with the same size value will work together.')
        self.teeth_size_field = cmds.floatField(min=0.1, max=5, value=1)

        self.gear_thickness_label = cmds.text(label = 'Gear Thickness', ann = 'Thickness of the entire gear.')
        self.gear_thickness_field = cmds.floatField(min=0.1, max=5, value=1)


        cmds.button( label='Create', command = self.createGear)
        cmds.setParent( '..' )
        cmds.showWindow(self.window)    


    def createGear(self, *args):
        teeth_number = cmds.intField(self.teeth_number_field, q = True, v = True)
        teeth_size = cmds.floatField(self.teeth_size_field, q = True, v = True)
        gear_thickness = cmds.floatField(self.gear_thickness_field, q = True, v = True)

        s = 2*teeth_number if teeth_number > 2 else 6
        r = (teeth_size*teeth_number)*0.1

        gear = cmds.polyDisc(sides = s, subdivisionMode = 2, subdivisions = 1, radius = r)
        
        poly = gear[0]
        edgenum = 3
        cmds.select(cl = True)

        for n in range(teeth_number):
            cmds.select(f'{poly}.e[{edgenum}]',add = True)    
            edgenum += 4
        
        cmds.polyExtrudeEdge(offset = 0.25*teeth_size)
        cmds.select(gear)
        cmds.polySmooth(mth = 1,ro = 0.5)
        cmds.polyExtrudeFacet(thickness = 0.2*gear_thickness)
        cmds.select(gear)

create_gear = Gearificator()