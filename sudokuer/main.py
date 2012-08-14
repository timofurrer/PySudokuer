#!/usr/bin/python

import sys
from Sudokuer import *

if __name__ == "__main__":
  filename = "../sudokus/sudoku3.sdk"
  if len( sys.argv ) > 1:
    filename = sys.argv[1]
  sdker = Sudokuer( filename )
  sdker.solve( )
