# PySudokuer
> This sudokuer is a smart tool to solve sudokus automatically
> *Version: 0.00.02*

**Author:** tuxtimo <tuxtimo@gmail.com>
**Version:** 0.00.02
**License:** GPL

## What?!
This repo contains a smart and clean tool to solve sudokus automatically. You can pass a file with a predefined `sudoku-syntax`
and this tool will solve it with few seconds..

## How to install
There is a setup script to install the tool to `/usr/local/bin/`. Just execute the following command:

    # python setup.py install

*Note: you may need root privileges to install it*

## How to run
It is very easy to run this tool. You just have to pass one argument: the `sudoku-file`.
You can pass every filetype - the extension doesn't matter - as long as it is written with the predefined `sudoku-syntax`:

    $ sudokuer sudokuToSolve.sdk

This will solve the sudoku in the file `sudokuToSolve.sdk`..

## Sudoku syntax
The syntax is very easy to write.
Just write each line of the sudoku without spaces and other delimiters.
So at the end your file will contain 9 lines with 9 numbers on each line( `9 x 9` ).
The numbers which the tool has to find should be marked with the `0`.
Example:

    530070000
    600195300
    098000060
    800060003
    400803001
    700020006
    060000280
    000419005
    000080079
