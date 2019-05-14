# The abilities of the hexapod

## Files
Declare the port in 1 go from file [tripodgait.py](./walking/tripodgait.py) in module [walking](./walking). Turning, walking forward, and walking in reverse can also be found in the same file. Movements such as sitting and standing can be found in [stableStance.py](./standing/stableStance.py) in module [standing](./standing). Everything will be executed from [main.py](./main.py). In case of a keyboard interrupt it will sit.

## Movements
Tripodgait is used fully except when sitting and standing. Turns will not be taken with stationary legs.
