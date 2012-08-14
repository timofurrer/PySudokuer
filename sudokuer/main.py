#!/usr/bin/python

import sys

from Sudokuer import *

def main( ):
  if len( sys.argv ) > 1:
    filename = sys.argv[1]
  else:
    print( "No sudoku file specified!" )
    raise SystemExit( 1 )

  sdker = Sudokuer( filename )
  sdker.solve( )

if __name__ == "__main__":
  main( )
