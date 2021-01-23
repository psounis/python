hours=int(input("Dwse wra : "))
minutes=int(input("Dwse lepta : "))
seconds=int(input("Dwse deyterolepta : "))
if hours<10:
     hours="0"+str(hours)
if minutes<10:
     minutes="0"+str(minutes)
if seconds<10:
     seconds="0"+str(seconds)
print(str(hours)+":"+str(minutes)+":"+str(seconds))