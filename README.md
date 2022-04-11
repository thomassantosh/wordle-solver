# wordle-solver
Wordle is addictive, but time-consuming. 

Humans make tools to aid them in problem-solving. While having a tool to solve Wordle faster robs one of some
of the pleasurable cognitive load of finding an answer, at times, expediency matters more. This code leverages
the dictionary from this [source](http://www-personal.umich.edu/~jlawler/wordlist.html). 

There are two main files: one, the `mock_wordle.py` which is a mock implementation of Wordle and two,
`solver.py` which is the tool to aid anyone working through the daily Wordle. 

The first file will randomly select a five-letter word and work through the typical Wordle responses.

The second file is an aid to working through the daily Wordle puzzle.

No third-party libraries used. Just standard features of Python 3.10.
