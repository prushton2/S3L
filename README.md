# Structured String Search Language
A readable Regex alternative that uses SQL like syntax to select text from a string.

## Command Layout
* Select block
  * Denotes what text to select
* Where block
  * Denotes condition block of text needs to meet
* From block
  * Last block, denotes the string to select from
* Then block (This doesnt exist yet)
  * This can be used to end the first statement, and include a second statement.

## Simple Examples
```
> Select [*] where str == ”l” from “Hello World”;
```
\> He```ll```o Wor```l```d
```
> Select word where str == ”e” from “Hello World”;
```
\> ```Hello``` World
```
> Select [*] where str == “Hello” from “Hello World”;
```
\> ```Hello``` World

// Maybe this, or it will only return the first character.
```
> Select char where str == “Hello” from “Hello World”;
```
\> ```H```ello World



## How it works

The interpreter iterates over every character and check every condition. When a character matches the where clause, the interpreter returns what is specified in the select clause.

## Definitions:
* currentChar
  * The current iterated character

## Keywords: 
#### Keywords act differently depending on whether they are used in select or where
* Select: //going to rework
  * Word:
    * Entire word when a where clause is true
  * \*
    * Selects everything inside a range
  * [ ]
    * denotes the region selected by the where clause, where the left bracket is the opening and the right bracket is the end. Characters can be inserted inside the brackets
  * < >
    * Used to extend the range of characters selected by the where clause. These can be put inside and outside of the brackets.
    * Use ```3<[]``` to select 3 characters before every selection
    * Use ```"e"<[]``` to select every character before the selection until it finds the e, inclusive.
  
* Where:
  * str:
    * == comparison: Checks all characters after the current character if they match x, where x is a word.
  * \+
    * Append operator.
    * Looks at the next character in the string 
    * Ex: str==”He”+str==”llo matches “Hello”, not “He llo”
  * Star (\*)
    * Repeat operator
    * Repeats the previous conditional
    * Ex: “eee” is the same as “e”*3
  * Underscore ( _ )
    * Allows any character
  * Conditional Operators
    * and, or, not, etc all work properly
  * String Literal
    * Defining a string literal is the same as writing str == “”
    * Ex: “e” is the same as str == “e”
  * Range:
    * Creates a character range, like [a-z] in regex
    * Defined as range(“a-z”)
    * Valid ranges consist of:
      * a-z
      * A-Z
      * 0-9

## Complex Examples

//Will match any 10 character long string of letters with one number at the end
```
> select [*] where (range(a-z) or range(A-Z))*10 + range(0-9);
```

//Will match any 10 character long string of letters with one number at the end
```
> select [*] where (range(a-z) or range(A-Z))*10 + range(0-9);
```
//Will select all letters between H and o in a string
```
> select [*]>"o" where "H";
```



