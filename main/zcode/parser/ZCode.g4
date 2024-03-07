// My ID: 2212481
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program:
	newlinelist decllist EOF; // Chuong trinh bao gom nhieu khai bao

decllist: //ok
	decl decllist
	| decl; // Bieu dien danh sach khai bao khong rong

decl: //ok
	vardecl
	| funcdecl; // Khai bao co the la khai bao ham hoac khai bao bien

/* KHAI BAO BIEN */

vardecl: //ok
	typdecl
	| varkeydecl
	| dynamicdecl; // Co 3 cach khai bao bien

typdecl: //ok
	typ ID ASSIGN1_OPERATOR expr newlinelistnonull
	| typ ID newlinelistnonull
	| arraydecl; //Khai bao bien kieu nguyen thuy

varkeydecl: //ok
	VAR_KEY ID ASSIGN1_OPERATOR expr newlinelistnonull; //Khai bao bien voi tu khoa var

dynamicdecl: //ok
	DYNAMIC_KEY ID (ASSIGN1_OPERATOR expr)? newlinelistnonull; //Khai bao bien voi tu khoa dynamic

/* KHAI BAO HAM */

funcdecl: //ok
	FUNC_KEY ID paralist newlinelist (returnstmt | blockstmt)
	| FUNC_KEY ID paralist newlinelistnonull; // Khai bao ham (cho phep tien khai bao) //ok

/* KHAI BAO MANG */

arraydecl:
	typ ID LSB sizelist RSB (ASSIGN1_OPERATOR arrayvalue)? newlinelistnonull; //Khai bao array //ok

arrayparameter: //ok
	typ ID LSB sizelist RSB; //Khai bao tham so array

arrayvalue: //ok
	arrayval
	| arrayvallist; //Gia tri cua mang (co the 1 chieu hoac da chieu)

arrayval: LSB index RSB; //Gia tri array 1 chieu //ok

arrayvallist: //ok
	LSB listarrayval RSB; //List cac gia tri array 1 chieu

listarrayval: //ok
	arrayval COMMA listarrayval
	| arrayval; //Gia tri cuoi cung cua array da chieu

sizelist:
	NUMBER COMMA sizelist
	| NUMBER; //Danh sach kich thuoc cua khai bao mang

/* LENH */
statement: // Cau lenh (gom nhieu loai cau lenh) //ok
	vardecl //Lenh Khai bao bien
	| assignstmt //Lenh gan
	| ifstmt //Lenh if
	| forstmt //Lenh for
	| breakstmt //Lenh break
	| continuestmt //Lenh continue
	| returnstmt //Lenh return
	| funccallstmt //Lenh goi ham
	| blockstmt; //Lenh block

stmtlist:
	statement stmtlist
	|; //Danh sach cac cau lenh trong block (co the rong) //ok

blockstmt:
	BEGIN_KEY newlinelistnonull stmtlist END_KEY newlinelistnonull; // Lenh block //ok

funccallstmt:
	ID LB argumentlist RB newlinelist; //Lenh goi ham //ok

returnstmt: //ok
	RETURN_KEY expr? newlinelistnonull; //Lenh Return , can xem xet doan \n

continuestmt: CONTINUE_KEY newlinelistnonull; //ok

forstmt:
	FOR_KEY numbervariable UNTIL_KEY expr BY_KEY expr newlinelist statement; //Lenh for //ok

breakstmt: BREAK_KEY newlinelistnonull; //ok

ifstmt: //Lenh if //ok
	IF_KEY LB expr RB newlinelist statement eliflist (
		ELSE_KEY statement
	)?;

eliflist:
	elifcomponent eliflist //ok
	|; //Danh sach lenh elif co the rong

elifcomponent: ELIF_KEY expr newlinelist statement; //ok

assignstmt:
	lhs ASSIGN1_OPERATOR expr newlinelistnonull; //Lenh gan //ok

/* OPERATORS */

relationaloperator: //ok
	EQUAL_OPERATOR
	| ASSIGN2_OPERATOR
	| NE_OPERATOR
	| GE_OPERATOR
	| G_OPERATOR
	| LE_OPERATOR
	| L_OPERATOR;

/* EXPRESSION */

expr:
	expr1 CONCAT_OPERATOR expr1
	| expr1; //Khai trien bieu thuc //OK

expr1: expr2 relationaloperator expr2 | expr2; //ok

expr2: expr2 (AND_OPERATOR | OR_OPERATOR) expr3 | expr3; //ok

expr3: expr3 (ADD_OPERATOR | SUB_OPERATOR) expr4 | expr4; //ok

expr4:
	expr4 (MUL_OPERATOR | DIV_OPERATOR | MODULO_OPERATOR) expr5 //ok
	| expr5;

expr5: NOT_OPERATOR expr5 | expr6; //ok

expr6: SUB_OPERATOR expr6 | expr7; //ok

expr7: expr7 indexoperator | expr8; // can chinh sua

expr8:
	ID
	| funccallstmt
	| literal
	| arrayvalue // Co the phai sua //ok
	| indexoperator
	| subexpr;

subexpr: LB expr RB; //ok

indexoperator: (ID | funccallstmt) LSB indexope RSB; //ok

indexope: expr | expr COMMA indexope; //ok

argumentlist:
	argumentprime
	|; //Danh sach doi so (co the rong) //ok

argumentprime: argument COMMA argumentprime | argument; //ok

argument: expr; //ok

literal: STRINGLIT | NUMBER | ID | booleanvalue; //ok

booleanvalue: TRUE_BOOLEAN | FALSE_BOOLEAN; //OK

numbervariable: ID; //ok

newlinelist: NEW_LINE newlinelist |; //ok

newlinelistnonull: NEW_LINE newlinelistnonull | NEW_LINE; //ok

lhs: ID | indexexpr | indexoperator; // ok

indexexpr: ID LSB index RSB | ID LSB indexexpr RSB; //ok

index: expr COMMA index | expr; //ok

paralist:
	LB parameterlist RB; //Danh sach tham so cua ham (co the rong) co ngoac //ok

parameterlist:
	paraprime
	|; //Danh sach tham so cua ham (co the rong) khong ngoac //ok

paraprime:
	para COMMA paraprime
	| para; //Danh sach tham so khong rong //ok

para:
	typ ID
	| arrayparameter; //tham so (nguyen thuy hoac array) //ok

/* PRIMITIVE TYPE */

typ:
	NUM_TYPE
	| BOOL_TYPE
	| STRING_TYPE; //Kieu du lieu (gom 3 kieu du lieu nguyen thuy) //ok

//KEY WORD

COMMENT: '##' ~[\r\n]* -> skip;

RETURN_KEY: 'return';

VAR_KEY: 'var';

DYNAMIC_KEY: 'dynamic';

FUNC_KEY: 'func';

FOR_KEY: 'for';

UNTIL_KEY: 'until';

BY_KEY: 'by';

BREAK_KEY: 'break';

CONTINUE_KEY: 'continue';

IF_KEY: 'if';

ELSE_KEY: 'else';

ELIF_KEY: 'elif';

BEGIN_KEY: 'begin';

END_KEY: 'end';

// TYPE

NUM_TYPE: 'number';

BOOL_TYPE: 'boolean';

STRING_TYPE: 'string';

//OPERATOR

EQUAL_OPERATOR: '==';

CONCAT_OPERATOR: '...';

ASSIGN1_OPERATOR: '<-';

GE_OPERATOR: '>=';

G_OPERATOR: '>';

LE_OPERATOR: '<=';

L_OPERATOR: '<';

NE_OPERATOR: '!=';

ASSIGN2_OPERATOR: '=';

OR_OPERATOR: 'or';

AND_OPERATOR: 'and';

NOT_OPERATOR: 'not';

MODULO_OPERATOR: '%';

ADD_OPERATOR: '+';

SUB_OPERATOR: '-';

MUL_OPERATOR: '*';

DIV_OPERATOR: '/';

//BOOLEAN

TRUE_BOOLEAN: 'true';

FALSE_BOOLEAN: 'false';

//SEPARATOR

LB: '(';

RB: ')';

LSB: '[';

RSB: ']';

COMMA: ',';

//COMMENT

//IDENTIFIER

ID: [A-Za-z_][0-9A-Za-z_]*;

//LITERAL

NUMBER: (INTPART DECPART EXPPART? | INTPART DECPART? EXPPART?);
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: ('e' | 'E') ('+' | '-')? [0-9]+;

STRINGLIT:
	'"' (~["\n\\] | LI_ESCAPE | [']["])* '"' {self.text = self.text[1:-1]};

//ERROR

UNCLOSE_STRING:
	'"' (~["\n\\] | LI_ESCAPE | [']["])* {raise UncloseString(self.text[1:])};

fragment LI_ESCAPE: ('\\' ['bftrn\\]);

ILLEGAL_ESCAPE:
	'"' (~["\n\\] | LI_ESCAPE | [']["])* ILL_ESCAPE {raise IllegalEscape(self.text[1:])};

fragment ILL_ESCAPE: '\\' ~['bntfr\\];

//NEWLINE & WS

NEW_LINE: '\n';

WS: [ \t\r\f]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};