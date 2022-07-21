given_name = 'Zed A. Shaw'
given_age = 35 # not a lie
measured_height = 74 * 2.54 # centimeters
measured_weight = 180 * 0.453592 #kilograms
eye_color = 'Blue'
teeth_color = 'White'
hair_color = 'Brown'

print(f"Let's talk about {given_name}.")
print(f"He's {measured_height} centimeters tall.")
print(f"He's {measured_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eye_color} eyes and {hair_color} hair.")
print(f"His teeth are usually {teeth_color} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = given_age + measured_height + measured_height
print(f"If I add {given_age}, {measured_height}, and {measured_weight} I get {total}.")