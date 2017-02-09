# Components - visualise a number as parts

Educational tool for kids to finds components of a number. This is a
"Scratch" / prototype implementation that will test the idea. The
gist:

    1. A random number is generated

    2. The player gets to write an expression that should evaluate to
     the number. If the expression is correct, a score is calculated
     from the following:
       1. Every addition in the expression gives 1 point
       2. Every subtraction gives 2 points
       3. Every multiplication gives 4 points
       4. Every division gives 8 points
    3. After N numbers have been given, all points are summarised, and
    preferably time taken to complete is factored into the overall
    score (method for this to be worked out).

The initial Python implementation will be used to test the idea on my
own children. If the games seems beneficial I might port it to other
platforms where it's easier to implement more interactivity and nicer
media.

*Update 2017-02-09*: The web-app variant will be re-created in a
separate repository to avoid mixin programming languages in the same
repo.

## Installation

Components is written for Python 3 (tested 3.6, 3.5). Python 2 will
not be supported.

Installation is most conveniently made using @kennethreitz `Pipenv`
tool. For now, you will need to have a recent Python 3 on your
`$PATH`, clone the repo and install:

    $ git clone ...
    $ pipenv install .

You can then run the game like this:

    $ pipenv run python text_ui.py

The text UI version will generate 10 numbers to be expressed and
calculate a total score according to the list above. The player may
give up on a number by responding with a `'q'`, but that carries a
penalty of -3 points from the total score.
