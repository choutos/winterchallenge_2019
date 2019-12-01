'''
Fuel required to launch a given module is based on its mass. 
Specifically, to find the fuel required for a module, take its mass, 
divide by three, round down, and subtract 2.

For example:

  - For a mass of 12, divide by 3 and round down to get 4, 
    then subtract 2 to get 2.
  - For a mass of 14, dividing by 3 and rounding down still yields 4, 
    so the fuel required is also 2.
  - For a mass of 1969, the fuel required is 654.
  - For a mass of 100756, the fuel required is 33583.

The Fuel Counter-Upper needs to know the total fuel requirement. 
To find it, individually calculate the fuel needed for the mass of 
each module (your puzzle input), then add together all the fuel values.
'''

def calc_fuel(mass: int) -> int:
    return mass // 3 -2

assert calc_fuel(12) == 2
assert calc_fuel(14) == 2
assert calc_fuel(1969) == 654
assert calc_fuel(100756) == 33583

with open("input.txt") as f:
    masses = [int(line.strip()) for line in f]

fuel = 0
for mass in masses:
    fuel += calc_fuel(mass)
print(fuel)
