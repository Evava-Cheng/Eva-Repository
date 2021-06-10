import math
import time

def countdown(seconds):
    """Set a countdown mechanism that give people  + \
    a time to think before they make a decision.
    I learned this function by looking at some examples on the + \
    GeeksforGeeks website, but I did not copy their + \
    code, and I come up with this code by myself.
    URL: https://www.geeksforgeeks.org/how-to- + \
    create-a-countdown-timer-using-python/

    Parameters
    ----------
    seconds : int or float
        Number of seconds need to be countdown.
    """

    time.sleep(seconds)


def sphere_volume(radius):
    """Use radius to calculate the volume of the sphere.

    Parameters
    ----------
    radius : int or float
        The radius which will be used in the volume function of sphere.

    Returns
    -------
    volume : int or float
        The result of the volume function of sphere.
    """

    volume = 4 / 3 * math.pi * math.pow(radius, 3)

    return volume


def cube_volume(length):
    """Use length to calculate the volume of the cube.

    Parameters
    ----------
    length : int or float
        The length which will be used in the volume function of cube.

    Returns
    -------
    volume : int or float
        The result of the volume function of cube.
    """

    volume = math.pow(length, 3)

    return volume


def cuboid_volume(width, height, length):
    """Use width, height, length to calculate the volume of the cuboid.

    Parameters
    ----------
    width : int or float
        The width which will be used in the volume function of cuboid.
    height : int or float
        The heigh which will be used in the volume function of cuboid.
    lenght : int or float
        The length which will be used in the volume function of cuboid.

    Returns
    -------
    volume : int or float
        The result of the volume function of cuboid.
    """

    volume = width * height * length

    return volume


def cone_volume(radius, height):
    """Use radius and height to calculate the volume of the cone.

    Parameters
    ----------
    radius : int or float
        The radius which will be used in the volume function of cone.
    height : int or float
        The height which will be used in the volume function of cone.

    Returns
    -------
    volume : int or float
        The result of the volume function of cone.
    """

    volume = math.pi * math.pow(radius, 2) * height / 3

    return volume


def cylinder_volume(radius, height):
    """Use radius and height to calculate the volume of the cylinder.

    Parameters
    ----------
    radius : int or float
        The radius which will be used in the volume function of cylinder.
    height : int or float
        The height which will be used in the volume function of cylinder.

    Returns
    -------
    volume : int or float
        The result of the volume function of cylinder.
    """

    volume = math.pi * math.pow(radius, 2) * height

    return volume


def calculate_sphere():
    """Get users input and get the output from sphere_volume function. + \
    Print the result of the volume in a string.

    User Input
    ----------
    radius : float
        User input string and converted into a float.

    Returned Value From Other Function
    ----------------------------------
    volume : string
        The volume float get from sphere_volume and convert into a string.
    """

    print("\nYou want to solve for the volume of a Sphere. I need to " + \
          "know the radius of the Sphere to calculate its volume.\n")

    # Ask the user to input the radius of the sphere and check whether
    # the input is a number.
    # If the user input is not a number, the calculator will ask the user
    # to enter a number again.
    while True:

        radius = input("Please enter the radius of the Sphere (you " + \
                       "should enter a number): ")

        # Check if the radius input is numeric.
        # I learned this Method from w3schools.
        # URL: https://www.w3schools.com/python/ref_string_isnumeric.asp
        if radius.isnumeric():
            radius = float(radius)
            break

        else:
            print("\nPlease only enter a number.\n")


    # Call the sphere_volume function with the user input to calculate the
    # volume of the of the sphere.
    volume = str(sphere_volume(radius))

    print("\nThe volume of the Sphere with radius of" + \
          " " + str(radius) + " is " + volume + ".\n")


def calculate_cube():
    """Get users input and get the output from cube_volume function. + \
    Print the result of the volume in a string.

    User Input
    ----------
    length : float
        User input string and converted into a float.

    Returned Value From Other Function
    ----------------------------------
    volume : string
        The volume float get from cube_volume and convert into a string.
    """

    print("\nYou want to solve for the volume of a Cube. I need to " + \
          "know the length of the side the Cube to calculate its volume.\n")

    # Ask the user to input the length of the cube and check whether
    # the input is a number.
    # If the user input is not a number, the calculator will ask the user
    # to enter a number again.
    while True:

        length = input("Please enter the length of the Cube (you " + \
                       "should enter a number): ")

        # Check if the length input is numeric.
        if length.isnumeric():
            length = float(length)
            break

        else:
            print("\nPlease only enter a number.\n")

    # Call the cube_volume function with the user input to calculate the
    # volume of the of the cube.
    volume = str(cube_volume(length))

    print("\nThe volume of the Cube with length of " + str(length) + " is" + \
          " " + volume + ".\n")


def calculate_cuboid():
    """Get users input and get the output from cuboid_volume function. + \
    Print the result of the volume in a string.

    User Input
    ----------
    width : float
        User input string and converted into a float.
    height : float
        User input string and converted into a float.
    length : float
        User input string and converted into a float.

    Returned Value From Other Function
    ----------------------------------
    volume : string
        The volume float get from cuboid_volume and convert into a string.
    """

    print("\nYou want to solve for the volume of a Cuboid. I need to " + \
          "know the width, height, and length of the Cuboid to " + \
          "calculate its volume.\n")

    # Ask the user to input the width, height, and length of cuboid
    # and check whether the inputs are numbers.
    # If the user inputs are not numbers, the calculator will ask the user
    # to enter a number again.
    while True:

        width = input("Please enter the width of the Cuboid (you " + \
                      "should enter a number): ")
        height = input("Please enter the height of the Cuboid (you " + \
                       "should enter a number): ")
        length = input("Please enter the length of the Cuboid (you " + \
                       "should enter a number): ")

        # Check if the width, height, length inputs are numeric.
        if width.isnumeric() and height.isnumeric() and length.isnumeric():
            width = float(width)
            height = float(height)
            length = float(length)
            break

        else:
            print("\nPlease only enter numbers.\n")

    # Call the cuboid_volume function with the user input to calculate the
    # volume of the of the cuboid.
    volume = str(cuboid_volume(width, height, length))

    print("\nThe volume of the Cuboid with width of " + str(width) + "," + \
          " height of " + str(height) + ", and length of " + str(length) + " " + \
          "is " + volume + ".\n")


def calculate_cone():
    """Get users input and get the output from cone_volume function. + \
    Print the result of the volume in a string.

    User Input
    ----------
    radius : float
        User input string and converted into a float.
    height : float
        User input string and converted into a float.

    Returned Value From Other Function
    ----------------------------------
    volume : string
        The volume float get from cone_volume and convert into a string.
    """

    print("\nYou want to solve for the volume of a Cone. I need to know " + \
          "the radius and height of the Cone to calculate its volume.\n")

    # Ask the user to input the radius and height of cone
    # and check whether the inputs are numbers.
    # If the user inputs are not numbers, the calculator will ask the user
    # to enter a number again.
    while True:

        radius = input("Please enter the radius of the Cone (you " + \
                       "should enter a number): ")
        height = input("Please enter the height of the Cone (you " + \
                       "should enter a number): ")

        # Check if the radius and height inputs are numeric.
        if radius.isnumeric() and height.isnumeric():
            radius = float(radius)
            height = float(height)
            break

        else:
            print("\nPlease only enter numbers.\n")

    # Call the cone_volume function with the user input to calculate the
    # volume of the of the cone.
    volume = str(cone_volume(radius, height))

    print("\nThe volume of the Cone with radius of " + str(radius) + " and " + \
          "height of " + str(height) + " is " + volume + ".\n")


def calculate_cylinder():
    """Get users input and get the output from cylinder_volume function. + \
    Print the result of the volume in a string.

    User Input
    ----------
    radius : float
        User input string and converted into a float.
    height : float
        User input string and converted into a float.

    Returned Value From Other Function
    ----------------------------------
    volume : string
        The volume float get from cylinder_volume and convert into a string.
    """

    print("\nYou want to solve for the volume of a Cylinder. I need to know " + \
          "the radius and height of the Cylinder to calculate its volume.\n")

    # Ask the user to input the radius and height of cylinder
    # and check whether the inputs are numbers.
    # If the user inputs are not numbers, the calculator will ask the user
    # to enter a number again.
    while True:
        radius = input("Please enter the radius of the Cylinder (you " + \
                       "should enter a number): ")
        height = input("Please enter the height of the Cylinder (you " + \
                       "should enter a number): ")

        # Check if the radius and height inputs are numeric.
        if radius.isnumeric() and height.isnumeric():
            radius = float(radius)
            height = float(height)
            break

        else:
            print("\nPlease only enter numbers.\n")

    # Call the cylinder_volume function with the user input to calculate the
    # volume of the of the cylinder.
    volume = str(cylinder_volume(radius, height))

    print("\nThe volume of the Cylinder with radius of " + str(radius) + " " + \
          "and height of " + str(height) + " is " + volume + ".\n")


def volume_calculator():
    """Drive the main conversation, let user choose the object, and not + \
    break the loop until the user type in 'Stop'.

    User Input
    ----------
    Stop : string
        User input 'Stop' to stop the infinite loop.
    """

    print("\nWelcome!\n")

    countdown(1)

    print("\nThis program is going to help you to find the volume " + \
          "of the object which you would like to know.\n")

    countdown(2)

    while(1):
    # Loop to keep the program running.

        print("\nWe currently can help you with Sphere, Cube, Cuboid, " + \
              "Cone, and Cylinder.\n")

        countdown(2)

        print("\nPlease choose one type from the objects above.\n")

        # Ask the user to input an object name.
        chosen_object = input("What type of the obeject would you " + \
                              "like to solve its volume for: ")
        # Lower case the user input to avoid the error if the user
        # type the object name in different cases.
        chosen_object = chosen_object.lower()

        # Call on a specific function depend on the user input.
        if chosen_object == "sphere":
            calculate_sphere()

        elif chosen_object == "cube":
            calculate_cube()

        elif chosen_object == "cuboid":
            calculate_cuboid()

        elif chosen_object == "cone":
            calculate_cone()

        elif chosen_object == "cylinder":
            calculate_cylinder()

        else:
            print("\nSorry, currently we cannot solve the volume of" + \
                  " " + chosen_object + ". Please only choose from " + \
                  "Sphere, Cube, Cuboid, Cone, and Cylinder.\n")

        countdown(2)

        # Stop the loop if the user inputs 'stop'
        stop = input("\nDo you want to try again? Type anything to " + \
                     "continue, or type the word 'Stop' to end the " + \
                     "program.\n")
        stop = stop.lower()

        if stop == "stop":
            break

    print("\nThank you for using. Have a good day!\n")


if __name__ == '__main__':
    volume_calculator()
