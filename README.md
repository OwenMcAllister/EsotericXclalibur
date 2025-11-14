# EsotericXclalibur
An esoteric implementation of the Xcalibur programming language. AKA ExLang.

# Model of Computation Overview
Esoteric Xcalibur uses an unbounded LIFO stack based model of computation to acheive turing completeness.

# State
- Data stack of unbounded integers
- Program counter
- Lable table L : name -> pc

# Step
Fetch instruction at pc, mutate the stack, then advance pc unless control flow explicitly sets it.

# Stack Opperations
1. Push n: Push an integer n onto the stack
2. Duplicate: Duplicate the top element on the stack
3. Swap: Swap top two stack elements
4. Add: Adds top two stack elements. Pop element B then A and push A + B
5. Subtract: Same convention as Add
6. JumpZ L: Pop top of stack x, if x is 0 set pc to label L, otherwise advance pc
7. Jump L: Jump unconditionally to some label L, set pc to L
8. Out: Pop and print the lowest 8 bits of top of stack x as a character, chr(x & 0xFF)
9. Halt: Stop execution

Addtional stack opperations can be composed from these core 9. 
- pop, eq, not, etc can all be constructed using jump instructions and arithmetic

# Language Semantics
The Esoteric Xclalibur *language*, ExLang, contains 5 valid symbols. 'x', 'tech', 'techx', ':', 'via ad excellentiam'. 

Whitespace and newline characters are ignored, but *may* be included for readability.

- 'x' serves as a delimeter between instructions.
    - instruction1 x instruction2 x etc

- The number of occurances of 'tech' corresponds to opcodes 1-8, as numbered above. Note that the *Halt* instruction has it's own symbol.
    - 1 * 'tech' = push
    - 2 * 'tech' = duplicate
    - 3 * 'tech' = swap
    - etc

- 'techx' represents a 1 positive base 10 integer value. Arithmetic opperations can be used to calculate negatives and large numbers.
    - 'techx' = 1
    - 'techx techx' = 2
    - etc

- ':' is used to seperate parameters from instructions and parameters from eachother, as well as define labels.

    Two ':' characters in succession, written '::', introduce and close a label definition:

        :: <label_name> ::

    The label_name is any non-empty sequence of 'techx' tokens.
    The tokens between the two '::' markers are taken *verbatim* as the label name.Whitespace is ignored.

    Example:

        :: techx techx ::

    defines a label with the name "techxtechx".

- 'via ad excellentiam' halts execution.


**Instruction Shape:**

For instructions with parameters:

- k occurences of 'tech' ':' parameter 1 ':' parameter 2 'x'

For instructions with no parameters:

- k occurences of 'tech' 'x'


**A fully formed EXLang instruction:**

    tech : techx techx x

pushes an integer value of 2 onto the stack.
