#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on August 2020
# This program calculates the circumference of a circle
#   with user input using tau

import constants


def main():
    # This function calculates area and perimeter

    # Input
    radius = int(input("Enter Radius of Circle (mm): "))

    # Process
    circumference = constants.TAU * radius

    # Output
    print("")
    print("Circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
