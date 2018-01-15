%require "3.0"

%verbose

%{

#include <cstdio>
#include <iostream>
#include <string>

extern "C" int yylex();
extern "C" int yyparse();
extern "C" FILE* yyin;

void yyerror(const char*);

%}

%union {
    char digit;
    char two_digits[2];
}

%token AM_PM
%token <char> DIGIT
%token <std::array<char, 2>> TWO_DIGITS

%type <int> hours
%type <int> minutes
%type <std::string> complement

%%

time
    : hours[H]
      { std::cout << "hours: " << $H << "\n"; }
      complement[C]
      { std::cout << "complement: " << $C << "\n"; }
    ;

hours
    : DIGIT
      { $$ = int{std::stoi($1)}; }
    | TWO_DIGITS
      { $$ = int{std::stoi($1)}; }
    ;

minutes
    : ":" TWO_DIGITS
    {
        std::cout << "hehehe";
    }
    ;

complement
    : AM_PM
    {
        std::cout << "found am/pm";
        $$ = "am/pm";
    }
    | minutes
    {
        $$ = std::to_string($1);
    }
    | minutes AM_PM
    {
        $$ = std::to_string($1);
    }
    ;

%%

int main() {
    yyin = stdin;

    while (not feof(yyin)) {
        yyparse();
    }
}

void yyerror(const char* s) {
    std::cout << "Invalid time format: " << s << '\n';
    exit(-1);
}
