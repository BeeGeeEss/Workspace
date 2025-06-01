water_pressure = 3

match water_pressure:
    case 1:
        print("Danger: water pressure critically low! Shut down system!")
    case 2:
        print("Warning: water pressure low. Check for leaks!")
    case 3:
        print("Water pressure nominal.")
    case 4:
        print("Warning: water pressure high. Open valves!")
    case 5:
        print("Danger: water pressure critically high! Damage to system imminent!")
    case _:
        print("Unknown water pressure level!")






class switch:
    on = 1
    off = 0
 
status = 0
 
match status:
    case switch.on :
        print('Switch is on')
    case switch.off :
        print('Switch is off')






list1 = ['a', 'b', 'c', 'd']
 
match list1:
    case ['e','f'] : print("e,f present")
    case ['a','b','c','d'] : print("a,b,c,d present")



sample = True
 
match sample:
    case (True|False):
        print("It is a boolean value")
    case _ :
        print("Not a boolean value")



