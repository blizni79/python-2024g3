import constants

print(f"Zmienna {constants.GRAVITY}")


from constants import *  


print(f"Pole koła to {PI} * ")
print(f"Stała: {GRAVITY}")


class Constants:
    PI = 3.1415
    GRAVITY = 9.81

print(Constants.GRAVITY)