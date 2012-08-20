import sys
import os
import time
import copy

class Sudokuer:
  FIELD_WIDTH  = 9
  FIELD_HEIGHT = 9

  MIN_NUMBER   = 1
  MAX_NUMBER   = 9

  TRIM_COLOR   = "\033[1;37m"

  def __init__( self, filename ):
    self.filename = filename

  def solve( self ):
    if not self.__readFile( ):
      return False
    self.isSolved  = False
    self.startTime = time.time( )
    self.__solve( 0, 0 )

  def __readFile( self ):
    if not os.path.exists( self.filename ):
      print( "Given sudoku file does not exists" )
      return False

    f = open( self.filename, "r" )
    self.playground = [[int( c ) for c in l[:9]] for l in f.readlines( )]
    f.close( )
    self.orig_playground = copy.deepcopy( self.playground )
    return True

  def __solve( self, x, y ):
    if self.isSolved: return False

    if x == Sudokuer.FIELD_WIDTH:
      y += 1
      x  = 0
      if y == Sudokuer.FIELD_HEIGHT: return True

    if self.playground[y][x] > 0: return self.__solve( x + 1, y )

    for i in range( Sudokuer.MIN_NUMBER, Sudokuer.MAX_NUMBER + 1 ):
      if not self.__check( x, y, i ):
        self.playground[y][x] = i
        if self.__solve( x + 1, y ):
          self.__solved( ) # Sudoku solved
    self.playground[y][x] = 0
    return False

  def __check( self, x, y, value ):
    return ( self.__checkRow( y, value ) or self.__checkColumn( x, value ) or self.__checkBox( x, y, value ))

  def __checkRow( self, y, value ):
    for i in range( Sudokuer.FIELD_WIDTH ):
      if self.playground[y][i] == value: return True
    return False

  def __checkColumn( self, x, value ):
    for i in range( Sudokuer.FIELD_HEIGHT ):
      if self.playground[i][x] == value: return True
    return False

  def __checkBox( self, x, y, value ):
    box_x = int( x / 3 ) * 3
    box_y = int( y / 3 ) * 3
    for i in range( box_y, box_y + 3 ):
      for j in range( box_x, box_x + 3 ):
        if self.playground[i][j] == value: return True
    return False

  def __solved( self ):
    self.isSolved = True
    self.endTime  = time.time( )
    self.duration = self.endTime - self.startTime
    print( "Found solution in %f seconds:"%( self.duration ))
    Sudokuer.printSudoku( self.playground )

  @staticmethod
  def printSudoku( playground ):
    print( "\n%s+---+---+---+---+---+---+---+---+---+\033[0m"%( Sudokuer.TRIM_COLOR ))
    for i in range( Sudokuer.FIELD_HEIGHT ):
      sys.stdout.write( "%s|\033[0m"%( Sudokuer.TRIM_COLOR ))
      for j in range( Sudokuer.FIELD_WIDTH ):
        if ( j + 1 ) % 3 == 0:
          sys.stdout.write( " %d %s|\033[0m"%( playground[i][j], Sudokuer.TRIM_COLOR ))
        else:
          sys.stdout.write( " %d |"%( playground[i][j] ))
      if ( i + 1 ) % 3 == 0:
        print( "\n%s+---+---+---+---+---+---+---+---+---+\033[0m"%( Sudokuer.TRIM_COLOR ))
      else:
        print( "\n%s+\033[0m---+---+---%s+\033[0m---+---+---%s+\033[0m---+---+---%s+\033[0m"%( Sudokuer.TRIM_COLOR, Sudokuer.TRIM_COLOR, Sudokuer.TRIM_COLOR, Sudokuer.TRIM_COLOR ))
