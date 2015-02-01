# Boggle-Solver

Given an NxN board of letters, this algorithm finds all possible words from the board. Words can be formed by letters adjacent to each other (adjacent letters can be in any of the possible 8 spots around a given letter). A letter at a given location cannot be used twice for a given word.

The algorithm uses Depth First Search to search for words. I also use a Trie to quickly eliminate prefixes that are not present in the dictionary.
