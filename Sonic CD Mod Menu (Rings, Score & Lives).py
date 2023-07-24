print ("Basic Sonic CD Mod Menu Infinate Lives and Adjustible Rings & Score")
print ("Free to use and modify")
print ("Created by frankiemc1093")
print ("Github: https://github.com/frankiemc1093/BasicSonicCDModMenu")
print ("Only for Sonic CD Remake (2011) PC")
print ("Please Launch Sonic CD if you have not already")
input("Press any Key to continue...")


from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()

process = rwm.get_process_by_name("soniccd.exe")
process.open()


baseaddress = 0xED0000+0x1AD709C

#adresses
livespointer =process.get_pointer(0x1AD709C)
ringspointer =process.get_pointer(0x1B0D6F0)
scorepointer =process.get_pointer(0x1AD7094)

#Freeze (Change to your likeing)
while 1:
#infinate lives
    process.write (livespointer, 99)
#Rings
    process.write (ringspointer, 999)
#Score
    process.write (scorepointer, 99999)
