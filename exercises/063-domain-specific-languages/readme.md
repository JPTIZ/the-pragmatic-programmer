Domain Specific Languages
=========================

Exercises
---------

5. We want to implement a mini-language to control a simple drawing package
   (perhaps a turtle-graphics system). The language consists of single-letter
   commands. Some commands are followed by a single number. For example, the
   following input would draw a rectangle.

   ```
   P 2 # select pen 2
   D   # pen down
   W 2 # draw west 2cm
   N 1 # then north 1
   E 2 # then east 2
   S 1 # then back south
   U   # pen up
   ```

   Implement the code that parses this language. It should be designed so that it
   is simple to add new commands.

6. Design a BNF grammar to parse a time specification. All of the following
   should be accepted.

   ```
   4pm, 7:38pm, 23:42, 3:16, 3:16am
   ```

7. Implement a parser for the BNF grammar in Exercise 6 using yacc, bison, or a
   similar parser-generator.

8. Implement the time parser using ~~Perl~~ Python. [Hint: Regular expressions
   make good parsers.]
