grammar day18_p1;
expr
    : expr op=(ADD|MULT) expr   #exprOp
    | '(' expr ')'              #exprParens
    | INT                       #exprInt 
    ;

MULT: '*';
ADD : '+';
INT : [0-9]+;
WHITESPACE : [ \r\n\t]+ -> skip;