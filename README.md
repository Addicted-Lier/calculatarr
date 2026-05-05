# CLI Calculator (Python)

## Description

A simple command-line calculator that evaluates expressions like:
20+30, 50*2, 100/5.

Built to practice string parsing, conditionals, and regex in Python.


## Features
- Supports +, -, *, /, %
- Takes full expression input (e.g., 20+30)
- Continuous loop until user exits

## How to Run
1. Clone the repo
2. Run: python main.py
3. Enter expressions like: 20+30


## Challenges Faced
- Faced a regex error: "bad character range +-*"
- Learned that '-' inside [] is treated as a range operator
- Fixed it by escaping '-' → [+\-*/%]

This improved my understanding of how regex character classes work.

## Future Improvements
- Handle expressions like 20+30*2 (operator precedence)
- Add support for decimals
- Build GUI version