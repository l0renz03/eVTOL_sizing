# Git rules
_Version: 1.0, Last change: 25.04.2024_

This is a set of rules while using git.

## Branches
1. Never work directly on `main` branch (thus do not push to it).
2. Whenever you work on a new feature, create a new branch. This branch should be created from `main` branch.
3. Branch names should be descriptive and short.

## Commits
1. Commit messages should be descriptive and not too long.
2. If you work on a bigger feature, commit frequently. Example: You create a model calculating and graphing something. You can do two commits: one when you create calculations and another when you create the graph.

## Merging and pull requests
1. Before merging, make sure your code is working.
2. Every time you want to merge something, create a pull request on Github.
3. When you create a pull request to `main`, do not merge it instantly (Github should not allow it either way). Assign a person to review your code.
4. When you review someone's code, focus not only on possible errors in the code, though it is the most important, but whether it is written in a clean way.
5. When you finish reviewing, approve the pull request, if it can be merged. If there are any comments which are not resolved, wait until they are resolved.
6. When you find something, which you think should be changed, write a comment in the pull request. Do not change it yourself. Let the author do it. 

