import matplotlib.pyplot as plt
import numpy as np

def grid_options(start, stop, stepsize, numpoints, option):
    """
    This function demonstrates the difference between the arange and linspace methods of Numpy for creating
    ordered ranges of values. Some more ways of doing this are listed in G0_ranges.py   
    """
    if option == "arange":
        # arange creates a set of values between a start point and a stop point in steps of stepsize.
        # the stop point is usually excluded, but rounding errors may cause it to be included
        # this can be prevented using the argument endpoint=False
        x, y = np.meshgrid(np.arange(start, stop, stepsize), np.arange(start, stop, stepsize))
    elif option == "linspace":
        # linspace creates a set of numpoints values between a start point and a stop point
        # start point and stop point are both always included
        # note that the number of points is equal to the number of steps + 1
        # e.g. linspace(0, 5, 6) returns [0, 1, 2, 3, 4, 5]
        # while linspace (0, 5, 5) returns [0, 1.25, 2.5, 3.75, 5]
        x, y = np.meshgrid(np.linspace(start, stop, numpoints), np.linspace(start, stop, numpoints))
    else:
        raise NameError("Invalid option {} selected.".format(option))
    return x, y
