`parser.py` is a Python script that uses the Natural Language Toolkit (NLTK) to parse sentences based on a predefined context-free grammar (CFG). The CFG is defined by a set of terminal and nonterminal rules. Terminal rules define the actual words (like nouns, verbs, adjectives, etc.) that can be used in the sentences. Nonterminal rules define the structure of the sentences, i.e., how the words can be combined to form valid sentences.

The script can either read a sentence from a file (if a filename is provided as a command-line argument) or get the sentence as an input from the user. The sentence is then parsed using the NLTK's `ChartParser` with the defined CFG. The parsing process breaks down the sentence into its grammatical components based on the rules of the CFG.

This script can be useful in natural language processing tasks, such as syntax analysis, sentence generation, language understanding, and more.
