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

fuel_part1 = 0
for mass in masses:
  fuel_part1 += calc_fuel(mass)
print(fuel_part1)

'''
For each module mass, calculate its fuel and add it to the total. 
Then, treat the fuel amount you just calculated as the input mass 
and repeat the process, continuing until a fuel requirement 
is zero or negative. For example:

    A module of mass 14 requires 2 fuel. This fuel requires no 
      further fuel (2 divided by 3 and rounded down is 0, which 
      would call for a negative fuel), so the total fuel 
      required is still just 2.
    At first, a module of mass 1969 requires 654 fuel. Then, this 
      fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 
      70 more fuel, which requires 21 fuel, which requires 5 fuel, 
      which requires no further fuel. So, the total fuel required 
      for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
    The fuel required by a module of mass 100756 and its fuel is: 
      33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
'''

def calc_fuel2(mass: int) -> int:
    total = 0
    new_fuel = calc_fuel(mass)
    while new_fuel > 0:
      total += new_fuel
      new_fuel = calc_fuel(new_fuel)
    return total

assert calc_fuel2(14) == 2
assert calc_fuel2(1969) == 966
assert calc_fuel2(100756) == 50346

fuel_part2 = 0
for mass in masses:
  fuel_part2 += calc_fuel2(mass)
print(fuel_part2)

     
