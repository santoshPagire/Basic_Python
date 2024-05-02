    
length = int(input("Enter length in feet : "))
width = int(input("Enter width in feet : "))
height = int(input("Enter height in feet : "))
     
     
def volume(l, w, h):
        return l * w * h
     
     
print("volume of prism is " + str(volume(length, width, height)) + " cu.feet.")