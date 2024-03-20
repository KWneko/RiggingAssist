
import maya.cmds
#import maya.cmds as cmds
import maya.mel as mm
import re
import time

RLHDummy = ['RigRightHandThumbDummy1','RigRightHandThumbDummy2','RigRightHandThumbDummy3','RigRightHandIndexDummy1','RigRightHandIndexDummy2','RigRightHandIndexDummy3','RigRightHandMiddleDummy1','RigRightHandMiddleDummy2','RigRightHandMiddleDummy3','RigRightHandRingDummy1','RigRightHandRingDummy2','RigRightHandRingDummy3','RigRightHandPinkyDummy1','RigRightHandPinkyDummy2','RigRightHandPinkyDummy3']

RLH = ['RigRightHandThumb1','RigRightHandThumb2','RigRightHandThumb3','RigRightHandIndex1','RigRightHandIndex2','RigRightHandIndex3','RigRightHandMiddle1','RigRightHandMiddle2','RigRightHandMiddle3','RigRightHandRing1','RigRightHandRing2','RigRightHandRing3','RigRightHandPinky1','RigRightHandPinky2','RigRightHandPinky3']

LH = ['RightHandThumb1','RightHandThumb2','RightHandThumb3','RightHandIndex1','RightHandIndex2','RightHandIndex3','RightHandMiddle1','RightHandMiddle2','RightHandMiddle3','RightHandRing1','RightHandRing2','RightHandRing3','RightHandPinky1','RightHandPinky2','RightHandPinky3']

Joint_Name_Right = 'Character2_Hips1|Character2_Spine|Character2_Spine1|Character2_Spine2|Character2_RightShoulder|Character2_RightShoulderExtra|Character2_RightArm|Character2_RightForeArm|Character2_RightHand|Character2_'


print(RLHDummy[0])
print(len(RLHDummy))#15
print(type(len(RLHDummy[0])))#<class 'int'>

Count = 1
Len_Count = 0

#for node in RLHDummy:
for node in RLH:
    print("node:",node)
    #print(repr(node))

    Re_node = re.sub(r"[0-9]+", "", node)
    print("Re_node:",Re_node)
    #print("Count:",Count)
    print("Len_Count:",Len_Count)


    #print("'" + node + 'Dummy' + "'" + Count + "'")
    ###print("'" + node + 'Dummy' + str(Count) + "'")
    #print("'" + Re_node + 'Dummy' + str(Count) + "'")
    ##Loc_name = "'" + Re_node + 'Dummy' + str(Count) + "'"
    ##Loc_name = "'" + Re_node + "'" + 'Dummy' + str(Count)

    Loc_name = Re_node + 'Dummy' + str(Count)
    print("Loc_name:", Loc_name)
    #time.sleep(1)

    ##maya.cmds.spaceLocator(name="'" + Re_node + 'Dummy' + str(Count) + "'")
    maya.cmds.spaceLocator(name = Loc_name)

    mm.eval('string $Loc_name = "%s";' % Loc_name)
    #mm.eval('select -r $Loc_name;')
    Rig_name = node
    mm.eval('string $Rig_name = "%s";' % Rig_name)


    if Count == 1:
        print("End_Count:",Count)

        LH_Joint = Joint_Name_Right + str(LH[Len_Count])

        print("LH_Joint:", LH_Joint)
        print("str(LH[Len_Count]):", str(LH[Len_Count]))#LeftHandThumb1

        mm.eval('string $LH_Joint = "%s";' % LH_Joint)
        #mm.eval('select -r $Loc_name;')
        #mm.eval('select -tgl $LH_Joint ;')

        maya.cmds.select(Loc_name, r=True )
        maya.cmds.select(LH_Joint, add=True )

        #mm.eval('matchTransform;')
        #maya.cmds.matchTransform("'" + Loc_name + "'", "'"+ LH_Joint + "'")
        maya.cmds.matchTransform(Loc_name, LH_Joint)


        #mm.eval('curve -d 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -n' +  $Rig_name + ';')
        maya.cmds.curve(name=Rig_name, d=1, p=[(1, 0, -1),(-1, 0, -1),(-1, 0, 1),(1, 0, 1),(1, 0, -1)], k=[0,1,2,3,4])

        #mm.eval('parent ' + $Rig_name + " " + $Loc_name +' ;')
        maya.cmds.parent(Rig_name, Loc_name) #child,parent

        #mm.eval('select -r $Rig_name ;')
        maya.cmds.select(Rig_name, r=True )

        maya.cmds.setAttr(Rig_name +'.translate', 0,0,0)
        maya.cmds.setAttr(Rig_name +'.rotate', 0,0,0)
        maya.cmds.setAttr(Rig_name +'.rotateZ', 90)
        #maya.cmds.makeIdentity(apply=True, jointOrient=True)

        #mm.eval('setAttr' + ' "' + $Rig_name + '.translateX"' + ' 0;')
        #mm.eval('setAttr' + ' "' + $Rig_name + '.translateY"' + ' 0;')
        #mm.eval('setAttr' + ' "' + $Rig_name + '.translateZ"' + ' 0;')
        #mm.eval('setAttr' + ' "' + $Rig_name + '.rotateX"' + ' 0;')
        #mm.eval('setAttr' + ' "' + $Rig_name + '.rotateY"' + ' 0;')
        #mm.eval('setAttr' + ' "' + $Rig_name + '.rotateZ"' + ' 0;')
        #mm.eval('setAttr' + ' "' + $Rig_name + '.rotateZ"' + ' 90;')
        mm.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1 -jointOrient;')



    if Count == 2:
        print("End_Count:",Count)

        #LH_Joint = Joint_Name_Left + str(LH[Len_Count-1])+ '|testmomo02dl02ae05a:Character2_' + str(LH[Len_Count])
        LH_Joint = Joint_Name_Right + str(LH[Len_Count-1])+ '|Character2_' + str(LH[Len_Count])

        print("LH_Joint:", LH_Joint)
        print("str(LH[Len_Count]):", str(LH[Len_Count]))#LeftHandThumb1

        mm.eval('string $LH_Joint = "%s";' % LH_Joint)

        maya.cmds.select(Loc_name, r=True )
        maya.cmds.select(LH_Joint, add=True )

        maya.cmds.matchTransform(Loc_name, LH_Joint)


        maya.cmds.curve(name=Rig_name, d=1, p=[(1, 0, -1),(-1, 0, -1),(-1, 0, 1),(1, 0, 1),(1, 0, -1)], k=[0,1,2,3,4])
        maya.cmds.parent(Rig_name, Loc_name) #child,parent
        maya.cmds.select(Rig_name, r=True )

        maya.cmds.setAttr(Rig_name +'.translate', 0,0,0)
        maya.cmds.setAttr(Rig_name +'.rotate', 0,0,0)
        maya.cmds.setAttr(Rig_name +'.rotateZ', 90)

        mm.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1 -jointOrient;')



    if Count == 3:
        print("End_Count:",Count)


        #LH_Joint = Joint_Name_Left + str(LH[Len_Count-2]) + '|testmomo02dl02ae05a:Character2_' + str(LH[Len_Count-1]) + '|testmomo02dl02ae05a:Character2_' + str(LH[Len_Count])
        LH_Joint = Joint_Name_Right + str(LH[Len_Count-2]) + '|Character2_' + str(LH[Len_Count-1]) + '|Character2_' + str(LH[Len_Count])

        print("LH_Joint:", LH_Joint)
        print("str(LH[Len_Count]):", str(LH[Len_Count]))#LeftHandThumb1

        mm.eval('string $LH_Joint = "%s";' % LH_Joint)

        maya.cmds.select(Loc_name, r=True )
        maya.cmds.select(LH_Joint, add=True )

        maya.cmds.matchTransform(Loc_name, LH_Joint)


        maya.cmds.curve(name=Rig_name, d=1, p=[(1, 0, -1),(-1, 0, -1),(-1, 0, 1),(1, 0, 1),(1, 0, -1)], k=[0,1,2,3,4])
        maya.cmds.parent(Rig_name, Loc_name) #child,parent
        maya.cmds.select(Rig_name, r=True )

        maya.cmds.setAttr(Rig_name +'.translate', 0,0,0)
        maya.cmds.setAttr(Rig_name +'.rotate', 0,0,0)
        maya.cmds.setAttr(Rig_name +'.rotateZ', 90)

        mm.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1 -jointOrient;')

    Count += 1
    Len_Count += 1


    if Count > 3:
        Count = 1
        print("End_Count:",Count)
        print("End_Len_Count:",Len_Count)
        print("RLH[Len_Count-2]:",RLH[Len_Count-2])

        maya.cmds.parent(RLHDummy[Len_Count-1], RLH[Len_Count-2]) #child,parent
        maya.cmds.parent(RLHDummy[Len_Count-2], RLH[Len_Count-3]) #child,parent
        #maya.cmds.parent(RLHDummy[Len_Count-3], 'testmomo02dl02ae05a:RigLeftHand') #child,parent
        maya.cmds.parent(RLHDummy[Len_Count-3], 'RigRightHand') #child,parent
