# ⚙️ C-Subset to MIPS Compiler

[![Language: C](https://img.shields.io/badge/Language-C-blue.svg)](#)
[![Tools: Flex & Bison](https://img.shields.io/badge/Tools-Flex%20%7C%20Bison-orange.svg)](#)
[![Topic: Compiler Design & Architecture](https://img.shields.io/badge/Topic-Compiler%20Design-success.svg)](#)

A fully functional, custom compiler built from scratch using **C, Lex/Flex, and Yacc/Bison**. This project translates a subset of the C programming language into **MIPS assembly code**, demonstrating a deep understanding of low-level architecture, memory management, and parsing algorithms.

## 🚀 Key Features

* **Lexical & Syntactic Analysis:** Tokenization and strict grammar validation using LALR(1) parsing.
* **Semantic Validation & Symbol Table:** Robust management of variable scopes and constants. Prevents redeclaration and illegal constant modification.
* **Intermediate Code Generation:** Implements syntax-directed translation to generate operational MIPS assembly.
* **Dynamic Register Allocation:** Custom simulation of MIPS register management (`$t0` - `$t9`) for instruction processing.
* **Control Flow Structures:** Full native support for `if-else` branching and `while` loops with automatic label generation for assembly jumps.

## 💻 Example: From C to Assembly

**Input (C-Subset):**
```c
void main() {
    var int a, b;
    a = 2 + 1;
    if (a) {
        b = a;
    }
}
