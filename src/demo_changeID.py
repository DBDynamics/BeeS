from DBDynamics import BeeS
m = BeeS()
currentID = 0
targetID = 1
m.changeID(currentID,targetID)
print("change ID from "+str(currentID)+" to "+str(targetID)+" successfully!")
m.stop()

