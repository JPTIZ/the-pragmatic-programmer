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
}

%token AM_PM
%token <digit> DIGIT

%type <int> hours
%type <int> minutes
%type <std::string> complement

%%

time
    : hours[H]
      complement[C]
    ;

hours
    : DIGIT
      { $$ = std::stoi($1); }
    | DIGIT DIGIT
      { $$ = std::stoi($1); }
    ;

minutes
    : ":" DIGIT DIGIT
    {
        std::cout << "hehehe";
        $$ = 0;
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
