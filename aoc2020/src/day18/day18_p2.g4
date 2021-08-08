grammar day18_p2;
expr
    : expr ADD expr             #exprAdd
    | expr MULT expr            #exprMult
    | '(' expr ')'              #exprParens
    | INT                       #exprInt 
    ;

MULT: '*';
ADD : '+';
INT : [0-9]+;
WHITESPACE : [ \r\n\t]+ -> skip;