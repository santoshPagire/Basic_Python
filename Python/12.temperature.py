
tempc = int(input("Enter temperature value : "))

def far(tempf):
     return 1.8 * tempc + 32

print("Temparature "+str(tempc)+" degree celcius = " + str(far(tempc))+ " fahrenheit")