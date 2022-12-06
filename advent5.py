#!/usr/bin/env python

def parse():

  crates = []
  instructions = []

  with open('input.txt', 'r') as f:
    for line in f:
      if any(char.isdigit() for char in line):
        instructions.append(line.strip('\n'))
      else:
        crates.append(line.strip('\n'))
      
  return crates[:-1], instructions[1:], int(instructions[0][-2])

def improve_crates(crates, nb_crates):
  data_crates = [[] for i in range(nb_crates)]
  for crate_line in crates:
    for i in range(nb_crates):
      candidate = crate_line[i*4+1]
      if candidate != ' ':
        data_crates[i].append(candidate)
  return data_crates

def improve_instructions(instructions):
  cpu_instructions = []
  for instruction in instructions:
    splitted = instruction.split()
    cpu_instructions.append([splitted[1], splitted[3], splitted[5]])
  return cpu_instructions

if __name__ == '__main__':

  crates, instructions, nb_crates = parse()
  
  # modify data structure for crates
  data_crates = improve_crates(crates, nb_crates)
  
  # modify data structure for instructions
  cpu_instructions = improve_instructions(instructions)
  print(cpu_instructions)
