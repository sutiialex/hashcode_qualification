""" Painting google facade """
import sys

from ortools.linear_solver import pywraplp

def read_image(filename):
    """ read input image """
    with open(filename) as f:
        pass

def print_solution(solution, out_filename):
    solver, commands = solution
    with open(out_filename, 'w') as f:
        pass

def solve():
    pass

def main(in_filename, out_filename):
    """ main """
    image = read_image(in_filename)
    solution = solve(image)
    print_solution(solution, out_filename)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Provide the input and the output files'
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
