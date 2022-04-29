# Structured String Search Language
A readable Regex alternative that uses SQL like syntax to select text from a string.

## Command Layout
* Select block
  * Denotes what text to select
* Where block
  * Denotes condition block of text needs to meet
* From block
  * Last block, denotes the string to select from
* Then block //Unimplemented
  * This can be used to end the first statement, and include a second statement.

## Simple Examples
```
> Select [_] where str == ”l” from “Hello World”;
```
\> He```ll```o Wor```l```d
```
> Select word where str == ”e” from “Hello World”; //Unimplemented
```
\> ```Hello``` World
```
> Select [_] where str == “Hello” from “Hello World”;
```
\> ```Hello``` World

// Maybe this, or it will only return the first character.
```
> Select [_] where str == “Hello” from “Hello World”;
```
\> ```H```ello World



## How it works

The interpreter iterates over every character and check every condition. When a character matches the where clause, the interpreter returns what is specified in the select clause.

## Keywords: 
#### Keywords act differently depending on whether they are used in select or where
* Select:
  * [ _ ]
    * Default select clause. Highlights all matching text
  * < >
    * Selection extender. Extends selection to the left or right of the edges of the matching text
    * Example:
      * ```select 3<[_]>4 ``` extends the selection range to 3 characters left of the highlighted text and 4 to the right
        * Example: ```select 2<[_]>2 where "lo" from "Hello World" ``` -> H```ello W```orld
      * ```select [>2_3<]``` extends the selection range inside the bounds by 2 characters to the right and 3 to the left
        * Example: 
        ```select [>2_2<] where "Hello" from "Hello World"  ``` -> ```He```l```lo``` world

* Where:
  * \+
    * Append operator.
    * Looks at the next character in the string 
    * Ex: "He"+"llo" matches “Hello”, not “He llo”
  * Star (\*)
    * Repeat operator
    * Repeats the previous conditional
    * Ex: “eee” is the same as “e”*3
  * Underscore ( _ )
    * Allows any character
  * Conditional Operators //Unimplemented. Not going to implement and, only or and not
    * and, or, not, etc all work properly
  * String Literal
    * Defining a string literal is the same as writing str == “”
    * Ex: “e” is the same as str == “e”
  * Range:
    * Creates a character range, like [a-z] in regex. This is literally parsed into regex, so any range works
    * Defined as range(“a-z”)
    * Valid ranges consist of:
      * a-z
      * A-Z
      * 0-9

## Complex Examples

//Will match any 10 character long string of letters with one number at the end
```
> select [_] where (range(a-z) or range(A-Z))*10 + range(0-9);
```
//Will match any 10 character long string of letters with one number at the end
```
> select [_] where (range(a-z) or range(A-Z))*10 + range(0-9);
```
//Will select H and 3 characters to the left of it
```
> select [_]>3 where "H";
```

## Using the program

the function ```interpret(str)``` in ```main.py``` converts the S3L statement into a S3Lexpression object. The object has the following methods:
//Implemented
* __str__: returns a string with underlined text as the selected text
//Not implemented
* match(): returns whether or not there is a selection in the string
* matches(): returns the amount of matches in the string
* getSelectedIndices(): returns a list with all the indices that are selected
* replace(string replaceWith): replaces selected indices with given string