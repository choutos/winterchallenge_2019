#!/usr/bin/env python3
'''
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).

Integer 1, called opcode, indicates what to do. Opcodes:
  99: Program finished and should halt.
   1: adds together numbers read from two positions and 
      stores the result in a third position.
   2: Same as 1, but it multiplies the two inputs.

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
intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0]

def computer(intcode: list) -> list:
    pos = 0
    while intcode[pos] != 99:
        (opcode, num1, num2, target) = intcode[pos], intcode[pos+1], intcode[pos+2], intcode[pos+3]
        if opcode == 1:
            intcode[target] = intcode[num1] + intcode[num2]
        elif opcode == 2:
            intcode[target] = intcode[num1] * intcode[num2]
        else:
            raise RuntimeError("invalid opcode: {intcode[pos]}")
        pos +=4
    return intcode

def alarm(incode: list, noun: int = 12, verb: int = 2) -> list:
    intcode[1] = noun
    intcode[2] = verb
    new_code = computer(intcode)
    return new_code[0]

def reverse(target, incode):
    for noun in range(len(intcode)):
        for verb in range(len(intcode)):
            result = alarm(intcode, noun, verb)
            if result == target:
                return target

    
#print(alarm(intcode))
print(reverse(19690720,intcode))
assert computer([1,0,0,0,99]) == [2,0,0,0,99]
assert computer([2,3,0,3,99]) == [2,3,0,6,99]
assert computer([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert computer([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
