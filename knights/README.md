This project is a command-line application developed using Python. It is designed to solve a type of logic puzzle known as "Knights and Knaves". In these puzzles, each character is either a knight, who always tells the truth, or a knave, who always lies. The goal is to determine the identity of each character based on their statements.

The project consists of two main Python files: puzzle.py and logic.py.

puzzle.py contains the logic for the specific puzzle instance, including the statements made by the characters and the logical deductions that can be made from these statements.

logic.py contains a general-purpose logic engine that can handle logical operations such as And, Or, Not, and Implication. This engine is used by puzzle.py to solve the puzzle.

Features
Solve Knights and Knaves puzzles: The application can solve any Knights and Knaves puzzle, given the statements of the characters.
General-purpose logic engine: The logic engine in logic.py can be used independently of the puzzle solver to handle other logic problems.
