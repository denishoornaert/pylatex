/* scanner for a toy Pascal-like language */

%option noyywrap

%{
/* need this for the call to atof() below */
#include <math.h>
#include <stdio.h>
%}

/* Digits and variables */
DIGIT                   [0-9]
IDENTIFIER              [a-z|_][a-z0-9]*

/* Operators */
OPERATOR                ["+"|"-"|"/"|"*"|"="]

/* Structural characters */
STRUCTURAL              [{|}|(|)|;]

%%

if|else                 {printf("Keyword    : %s\n", yytext);}

{DIGIT}+                {printf("Integer    : %s\n", yytext);}
{IDENTIFIER}            {printf("Variable   : %s\n", yytext);}

{OPERATOR}              {printf("Operator   : %s\n", yytext);}

{STRUCTURAL}            {printf("Structural : %s\n", yytext);}

[ \t\n]+                /* eat up whitespace */

.                       {printf("Unknown    : %s\n", yytext);}

%%
