import random
import time
import argparse


def pick_a_line(lines):
    number_of_lines = len(lines)
    n = random.randint(0, number_of_lines - 1)
    print("Picked line: " + str(n))
    line = lines[n].strip()
    print("Picked line [" + line + "]")
    return line


def write_a_line(line, output_file):
    text_file = open(output_file, "w")
    text_file.write(line)
    text_file.close()


def read_input(input_file):
    text_file = open(input_file, "r")
    lines = text_file.readlines()
    number_of_lines = len(lines)
    print("Read in " + str(number_of_lines) + " lines")
    text_file.close()
    return lines


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="The input file containing the list of strings to read", type=str,
                        required=True)
    parser.add_argument("-o", "--output", help="The output file which is read by obs", type=str, required=True)
    parser.add_argument("-s", "--sleep", help="How long we sleep for between rewrites", type=int, required=True)

    args = parser.parse_args()

    lines = read_input(args.input)
    while True:
        # Too right it's an infinite loop, run this sucker till it's cancelled.
        line = pick_a_line(lines)
        write_a_line(line, args.output)
        time.sleep(args.sleep)


print("Loading One Liner")
init()
