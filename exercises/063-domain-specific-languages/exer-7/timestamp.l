%{

#include <iostream>

#include "timestamp.tab.h"

#define YY_DECL extern "C" int yylex()

%}

%%

[0-9] { std::cout << "digit: " << yytext << '\n'; return DIGIT; }

"am"|"pm" { return AM_PM; }

<<EOF>> { std::cout << "the end\n"; }

. { std::cout << "found: " << yytext << '\n'; }

%%
