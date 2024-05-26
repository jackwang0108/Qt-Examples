import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file")
ns = parser.parse_args()


file = Path(ns.file)
with file.open(mode="r") as f:
    for line in f.readlines():
        line = line.rstrip()
        line = line.replace("\"", "\\\"")
        line = line.replace("$", "\\\\$")
        print(f"\"{line}\",")
