#!/usr/bin/env python

from setuptools import setup

setup(
    name         = "sudokuer",
    version      = "0.00.02",
    description  = "Solve sudokus automatically",
    author       = "Furrer Timo",
    author_email = "tuxtimo@gmail.com",
    url          = "http://github.com/timofurrer/PySudokuer",
    packages     = ["sudokuer"],
    entry_points = {
                    "console_scripts": ["sudokuer = sudokuer.main:main"],
                   }
)
