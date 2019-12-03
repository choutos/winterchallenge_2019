#!/bin/env python3
'''
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).

Integer 1, called opcode, indicates what to do. Opcodes:
  99: Program finished and should halt.
   1: adds together numbers read from two positions and 
      stores the result in a third position.

The three integers after opcode tell these three positions -the first 
two indicate the positions from which you should read the input values, 
and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read 
the values at positions 10 and 20, add those values, and then overwrite the 
value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs 
instead of adding them. Again, the three integers after the opcode indicate 
where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
'''

def myfunc(input):
    pass

assert myfunc([1,0,0,0,99]) == [2,0,0,0,99]
assert myfunc([2,3,0,3,99]) == [2,3,0,6,99]
assert myfunc([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert myfunc([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]