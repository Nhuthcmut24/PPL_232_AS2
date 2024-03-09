import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
        
        
    def test_simple_program2(self):
        input = """number a
        string s
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(Id("s"), StringType())]))
        self.assertTrue(TestAST.test(input, expect, 301))
    
    
    def test_simple_program3(self):
        input = """number a
        string s <- "Nhut ne"
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(Id("s"), StringType(), None, StringLiteral("Nhut ne"))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program4(self):
        input = """number a
        string s <- "Nhut ne"
        func foo()
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(Id("s"), StringType(), None, StringLiteral("Nhut ne")), FuncDecl(Id("foo"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 303))
    
    def test_simple_program5(self):
        input = """number a
        func foo()
        begin
        end
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), FuncDecl(Id("foo"),[],Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_simple_program6(self):
        input = """func foo()
        begin
        var a <- 3
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([VarDecl(Id("a"), None, "var", NumberLiteral(3.0))]))]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_simple_program7(self):
        input = """func foo()
        return a
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Return(Id("a")))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simple_program8(self):
        input = """func foo()
        begin
        return a
        x <- 2
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Return(Id("a")), Assign(Id("x"), NumberLiteral(2.0))]))]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_simple_program9(self):
        input = """func foo()
        begin
        return a
        x <- 2
        y <- -4.5
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Return(Id("a")), Assign(Id("x"), NumberLiteral(2.0)), Assign(Id("y"), UnaryOp("-",NumberLiteral(4.5)))]))]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_simple_program10(self):
        input = """func foo()
        begin
        return a
        x <- 2
        y <- -4.5
        foo(3)
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Return(Id("a")), Assign(Id("x"), NumberLiteral(2.0)), Assign(Id("y"), UnaryOp("-",NumberLiteral(4.5))), CallStmt(Id("foo"),[NumberLiteral(3.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_simple_program11(self):
        input = """func foo()
        begin
        x <- arr[2,3]
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Assign(Id("x"), ArrayCell(Id("arr"),[NumberLiteral(2.0),NumberLiteral(3.0)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_simple_program12(self):
        input = """func foo()
        begin
        t <- t + 1
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Assign(Id("t"), BinaryOp("+",Id("t"),NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_simple_program13(self):
        input = """func foo()
        begin
        t <- true
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Assign(Id("t"), BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_simple_program14(self):
        input = """func foo()
        begin
        t <- [[2],[3]]
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([Assign(Id("t"), ArrayLiteral([ArrayLiteral([NumberLiteral(2.0)]),ArrayLiteral([NumberLiteral(3.0)])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_simple_program15(self):
        input = """func foo()
        begin
        if (a > b)
        return a
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([If(BinaryOp(">",Id("a"),Id("b")),Return(Id("a")),[])]))]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_simple_program16(self):
        input = """func foo()
        begin
        if (a > b)
        return a
        elif (a == b)
        return b
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([If(BinaryOp(">",Id("a"),Id("b")),Return(Id("a")),[(BinaryOp("==",Id("a"),Id("b")),Return(Id("b")))])]))]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_simple_program17(self):
        input = """func foo()
        begin
        if (a > b)
        return a
        elif (a == b)
        return b
        else return a + b
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([If(BinaryOp(">",Id("a"),Id("b")),Return(Id("a")),[(BinaryOp("==",Id("a"),Id("b")),Return(Id("b")))],Return(BinaryOp("+",Id("a"),Id("b"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_simple_program18(self):
        input = """func foo()
        begin
        for a until a < 10 by a + 1 
        b[a] <- a + 1
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[], Block([For(Id("a"),BinaryOp("<",Id("a"),NumberLiteral(10.0)),BinaryOp(("+"),Id("a"),NumberLiteral(1.0)),Assign(ArrayCell(Id("b"),[Id("a")]),BinaryOp("+",Id("a"),NumberLiteral(1.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_simple_program19(self):
        input = """func foo(number a, number b)
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),NumberType()), VarDecl(Id("b"),NumberType())] )]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_simple_program20(self):
        input = """func foo(number a, number b[2])
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),NumberType()), VarDecl(Id("b"),ArrayType([NumberLiteral(2.0)], NumberType()))])]))
        self.assertTrue(TestAST.test(input, expect, 319))
    
    def test_simple_program21(self):
        input = """func foo(number a, number b[2])
        begin
        break
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),NumberType()), VarDecl(Id("b"),ArrayType([NumberLiteral(2.0)], NumberType()))],Block([Break()]))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_simple_program22(self):
        input = """func foo(number a, number b[2])
        begin
        break
        continue
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),NumberType()), VarDecl(Id("b"),ArrayType([NumberLiteral(2.0)], NumberType()))],Block([Break(),Continue()]))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_simple_program23(self):
        input = """func main () return 1
        """
        expect = str(Program([FuncDecl(Id("main"),[],Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_simple_program24(self):
        input = """func main (number a, string b) return a+b
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), StringType())],Return(BinaryOp("+",Id("a"),Id("b"))))]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_simple_program25(self):
        input = """number a[1,2] <- [1,2,3,4]
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType([NumberLiteral(1.0),NumberLiteral(2.0)],NumberType()),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_simple_program26(self):
        input = """number x<- [1,2,3,4]
        """
        expect = str(Program([VarDecl(Id("x"),NumberType(),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_simple_program27(self):
        input = """number x[2,3]<- [[1,2,4],[1,9,0]]
        """
        expect = str(Program([VarDecl(Id("x"),ArrayType([NumberLiteral(2.0),NumberLiteral(3.0)],NumberType()),None,ArrayLiteral([ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(4.0)]), ArrayLiteral([NumberLiteral(1.0),NumberLiteral(9.0),NumberLiteral(0.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_simple_program28(self):
        input = """var x<- [[1,2,4],[1,9,0]]
        """
        expect = str(Program([VarDecl(Id("x"),None,"var",ArrayLiteral([ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(4.0)]), ArrayLiteral([NumberLiteral(1.0),NumberLiteral(9.0),NumberLiteral(0.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_simple_program29(self):
        input = """dynamic x
        """
        expect = str(Program([VarDecl(Id("x"),None,"dynamic")]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_simple_program30(self):
        input = """dynamic x
        """
        expect = str(Program([VarDecl(Id("x"),None,"dynamic")]))
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test_simple_program31(self):
        input = """func foo()
        """
        expect = str(Program([FuncDecl(Id("foo"),[])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_simple_program32(self):
        input = """func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false
        end
        return true
        end
        """
        expect = str(Program([FuncDecl(Id("isPrime"),[VarDecl(Id("x"),NumberType())],Block([If(BinaryOp("<=",Id("x"),NumberLiteral(1.0)),Return(BooleanLiteral(False)),[]),VarDecl(Id("i"),None,"var",NumberLiteral(2.0)),For(Id("i"),BinaryOp(">",Id("i"),BinaryOp("/",Id("x"),NumberLiteral(2.0))),NumberLiteral(1.0),Block([If(BinaryOp("=",BinaryOp("%",Id("x"),Id("i")),NumberLiteral(0.0)),Return(BooleanLiteral(False)),[])])),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_simple_program33(self):
        input = """func foo()
        begin
        x <- "string literal\t"
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([Assign(Id("x"),StringLiteral("string literal\t"))]))]))
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_simple_program34(self):
        input = """func foo()
        begin
        x[3] <- "string literal\t" + foo(2)
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([Assign(ArrayCell(Id("x"),[NumberLiteral(3.0)]),BinaryOp("+",StringLiteral("string literal\t"),CallExpr(Id("foo"),[NumberLiteral(2.0)])))]))]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_simple_program35(self):
        input = """func foo()
        begin
        if (x) 
        begin
        y<-"string literal\t" + foo(2)
        end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([If(Id("x"),Block([Assign(Id("y"),BinaryOp("+",StringLiteral("string literal\t"),CallExpr(Id("foo"),[NumberLiteral(2.0)])))]),[])]))]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_simple_program36(self):
        input = """func foo()
        begin
        if (x+y) y<-"string literal\t" + foo(2)
        elif a b<-5
        else number x
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([If(BinaryOp("+",Id("x"),Id("y")),Assign(Id("y"),BinaryOp("+",StringLiteral("string literal\t"),CallExpr(Id("foo"),[NumberLiteral(2.0)]))),[(Id("a"),Assign(Id("b"),NumberLiteral(5.0)))],VarDecl(Id("x"), NumberType()))]))]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_simple_program37(self):
        input = """func foo()
        begin
        for y until 5 by y+1 y<-"string literal\t" + foo(2)
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([For(Id("y"),NumberLiteral(5.0),BinaryOp("+",Id("y"),NumberLiteral(1.0)),Assign(Id("y"),BinaryOp("+",StringLiteral("string literal\t"),CallExpr(Id("foo"),[NumberLiteral(2.0)]))))]))]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_simple_program38(self):
        input = """var i <- 0
        func foo()
        begin
        for i until i >= 10 by 1
        return
        end
        """
        expect = str(Program([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),FuncDecl(Id("foo"),[],Block([For(Id("i"),BinaryOp(">=",Id("i"),NumberLiteral(10.0)),NumberLiteral(1.0),Return())]))]))
        self.assertTrue(TestAST.test(input, expect, 337))
    
    def test_simple_program39(self):
        input = """var i <- 0
        func foo() begin
        break
        end
        """
        expect = str(Program([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),FuncDecl(Id("foo"),[],Block([Break()]))]))
        self.assertTrue(TestAST.test(input, expect, 338))
    
    def test_simple_program40(self):
        input = """var i <- 0
        func foo() begin
        continue
        return
        end
        """
        expect = str(Program([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),FuncDecl(Id("foo"),[],Block([Continue(), Return()]))]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_simple_program41(self):
        input = """var i <- 0
        func foo(number x) begin
        for i until i >= 10 by 1
        break
        continue
        return
        end
        """
        expect = str(Program([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),FuncDecl(Id("foo"),[VarDecl(Id("x"),NumberType())],Block([For(Id("i"), BinaryOp(">=",Id("i"),NumberLiteral(10.0)),NumberLiteral(1.0),Break()),Continue(), Return()]))]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_simple_program42(self):
        input = """var i <- 0
        func foo() begin
        for i until i >= 10 by 1
        foo(i)
        end
        """
        expect = str(Program([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),FuncDecl(Id("foo"),[],Block([For(Id("i"), BinaryOp(">=",Id("i"),NumberLiteral(10.0)),NumberLiteral(1.0),CallStmt(Id("foo"),[Id("i")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_simple_program43(self):
        input = """var i <- 0
        func foo() begin
        for i until i >= 10 by 1
        foo(foo(i))
        end
        """
        expect = str(Program([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),FuncDecl(Id("foo"),[],Block([For(Id("i"), BinaryOp(">=",Id("i"),NumberLiteral(10.0)),NumberLiteral(1.0),CallStmt(Id("foo"),[CallExpr(Id("foo"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 342))
    
    def test_simple_program44(self):
        input = """func foo()
        begin
        x <- "abx" + 5
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Assign(Id("x"),BinaryOp("+", StringLiteral("abx"), NumberLiteral(5.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_simple_program45(self):
        input = """func foo()
        begin
        x <- arr[1] + 5.03e-4
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Assign(Id("x"),BinaryOp("+", ArrayCell(Id("arr"),[NumberLiteral(1.0)]), NumberLiteral(5.03e-4)))]))]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_simple_program46(self):
        input = """func foo()
        begin
        x[2+foo(3,4)] <- arr[b[12]] + 5.04e-12
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Assign(ArrayCell(Id("x"),[BinaryOp("+",NumberLiteral(2.0),CallExpr(Id("foo"),[NumberLiteral(3.0),NumberLiteral(4.0)]))]),BinaryOp("+",ArrayCell(Id("arr"),[ArrayCell(Id("b"),[NumberLiteral(12.0)])]),NumberLiteral(5.04e-12)))]))]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_simple_program47(self):
        input = """func foo()
        begin
        y[2+foo(3,4),5] <- 5.04e-12
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Assign(ArrayCell(Id("y"),[BinaryOp("+",NumberLiteral(2.0),CallExpr(Id("foo"),[NumberLiteral(3.0),NumberLiteral(4.0)])),NumberLiteral(5.0)]),NumberLiteral(5.04e-12))]))]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_simple_program48(self):
        input = """func foo() begin
        number x[100]
        x[1,foo(2)]<- "string\\t"
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([VarDecl(Id("x"),ArrayType([NumberLiteral(100.0)],NumberType())),Assign(ArrayCell(Id("x"),[NumberLiteral(1.0),CallExpr(Id("foo"),[NumberLiteral(2.0)])]),StringLiteral("string\\t"))]))]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_simple_program49(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 /4
        end
        """
        expect = str(Program([VarDecl(Id("x"), StringType(),None,StringLiteral("be ba ne \\t")), FuncDecl(Id("foo"),[], Block([Assign(Id("x"), BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_simple_program50(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 /4
        y <- "be ba " ... "ne"
        end
        """
        expect = str(Program([VarDecl(Id("x"), StringType(),None,StringLiteral("be ba ne \\t")), FuncDecl(Id("foo"),[], Block([Assign(Id("x"), BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne")))]))]))
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test_simple_program51(self):
        input = """var x <- 5 <= 6
        """
        expect = str(Program([VarDecl(Id("x"), None, "var", BinaryOp("<=",NumberLiteral(5.0), NumberLiteral(6.0)))]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_simple_program52(self):
        input = """var x <- not (5 <= 6)
        """
        expect = str(Program([VarDecl(Id("x"), None, "var", UnaryOp("not", BinaryOp("<=",NumberLiteral(5.0), NumberLiteral(6.0))))]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_simple_program52(self):
        input = """var x <- not ((5 <= 6) and (4 >=5))
        """
        expect = str(Program([VarDecl(Id("x"), None, "var", UnaryOp("not", BinaryOp("and",BinaryOp("<=",NumberLiteral(5.0), NumberLiteral(6.0)), BinaryOp(">=",NumberLiteral(4.0), NumberLiteral(5.0)))))]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_simple_program53(self):
        input = """dynamic t <- -4
        """
        expect = str(Program([VarDecl(Id("t"), None, "dynamic", UnaryOp("-", NumberLiteral(4.0)))]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_simple_program54(self):
        input = """func foo()
        begin
        if (not(a>=4)) 
        a <- a + 5
        elif (a < 0) 
        a <- 0
        else a <-1
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([If(UnaryOp("not", BinaryOp(">=", Id("a"), NumberLiteral(4.0))),  Assign(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(5.0))), [(BinaryOp("<",Id("a"),NumberLiteral(0.0)),Assign(Id("a"),NumberLiteral(0.0)))],Assign(Id("a"), NumberLiteral(1.0)) ) ]))]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_simple_program55(self):
        input = """func foo() 
        begin 
        for x until x <= 6 by 1
        arr[x] <- 2 * x
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([For(Id("x"),BinaryOp("<=",Id("x"),NumberLiteral(6.0)), NumberLiteral(1.0), Assign(ArrayCell(Id("arr"),[Id("x")]),BinaryOp("*",NumberLiteral(2.0),Id("x"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_simple_program56(self):
        input = """var VoTien <- true and "true" or 1  
        """
        expect = str(Program([VarDecl(Id("VoTien"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_simple_program57(self):
        input = """boolean a[1,2]
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType([NumberLiteral(1.0),NumberLiteral(2.0)], BoolType()))]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_simple_program58(self):
        input = """boolean a[1,2]
        ##hiihiih
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType([NumberLiteral(1.0),NumberLiteral(2.0)], BoolType()))]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_simple_program59(self):
        input = """var a <- 1 ## 12
        """
        expect = str(Program([VarDecl(Id("a"),None,"var",NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_simple_program60(self):
        input = """var a <-  - (not 1)
        """
        expect = str(Program([VarDecl(Id("a"),None,"var",UnaryOp('-',UnaryOp("not", NumberLiteral(1.0))))]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_simple_program61(self):
        input = """var a <- foo(3)[2]
        """
        expect = str(Program([VarDecl(Id("a"),None,"var",ArrayCell(CallStmt(Id("foo"),[NumberLiteral(3.0)]),[NumberLiteral(2.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_simple_program62(self):
        input = """func main()
        begin
        foo(1)
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("foo"),[NumberLiteral(1.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_simple_program63(self):
        input = """func main()
        begin
        main()
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("main"),[])]))]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_simple_program64(self):
        input = """func main()
        begin
        main()
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("main"),[])]))]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_simple_program65(self):
        input = """func main(number a[1],string x) begin
        arr[1] <- 2
        dynamic z <- "nhut"..."hi"
        end
        string t <- "Nguyen Quoc Nhut \\'"
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayType([NumberLiteral(1.0)],NumberType())),VarDecl(Id("x"),StringType())],Block([Assign(ArrayCell(Id("arr"),[NumberLiteral(1.0)]),NumberLiteral(2.0)),VarDecl(Id("z"),None,"dynamic",BinaryOp("...",StringLiteral("nhut"),StringLiteral("hi")))])), VarDecl(Id("t"),StringType(),None,StringLiteral("Nguyen Quoc Nhut \\'"))]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_simple_program66(self):
        input = """func foo(number a,number b) 
        begin
        if ( a != b)
        begin
        dynamic z <- a + b
        return z
        end
        else return a or b
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),NumberType())],Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([VarDecl(Id("z"),None,"dynamic",BinaryOp("+",Id("a"),Id("b"))),Return(Id("z"))]),[],Return(BinaryOp("or",Id("a"),Id("b"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_simple_program67(self):
        input = """func foo(number a,number b) 
        begin
        if ( a != b)
        begin
        dynamic z <- a + b
        return z
        end
        else return a or b
        end
        func main()
        begin
        a[3+foo(2)] <- a[b[2,3]] + 4
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),NumberType())],Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([VarDecl(Id("z"),None,"dynamic",BinaryOp("+",Id("a"),Id("b"))),Return(Id("z"))]),[],Return(BinaryOp("or",Id("a"),Id("b"))))])), FuncDecl(Id("main"),[],Block([Assign(ArrayCell(Id("a"),[BinaryOp("+",NumberLiteral(3.0),CallExpr(Id("foo"),[NumberLiteral(2.0)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[NumberLiteral(2.0),NumberLiteral(3.0)])]),NumberLiteral(4.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_simple_program68(self):
        input = """func foo(number a[5],string b) 
            begin
                var i <- 0
                for i until i >= 5 by 1
                begin
                    a[i] <- i * i + 5
                end
                return -1
            end 
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),ArrayType([NumberLiteral(5.0)],NumberType())),VarDecl(Id("b"),StringType())],Block([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),For(Id("i"),BinaryOp(">=",Id("i"),NumberLiteral(5.0)),NumberLiteral(1.0),Block([Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+",BinaryOp("*",Id("i"),Id("i")),NumberLiteral(5.0)))])),Return(UnaryOp("-",NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_simple_program69(self):
        input = """func foo(number a[5],string b) 
            begin
                var i <- 0
                for i until i >= 5 by 1
                begin
                    a[i] <- i * i + 5
                end
                b <- readNumber()
                return b
            end 
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),ArrayType([NumberLiteral(5.0)],NumberType())),VarDecl(Id("b"),StringType())],Block([VarDecl(Id("i"),None,"var",NumberLiteral(0.0)),For(Id("i"),BinaryOp(">=",Id("i"),NumberLiteral(5.0)),NumberLiteral(1.0),Block([Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+",BinaryOp("*",Id("i"),Id("i")),NumberLiteral(5.0)))])),Assign(Id("b"),CallExpr(Id("readNumber"),[])),Return(Id("b"))]))]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_simple_program70(self):
        input = """func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = str(Program([FuncDecl(Id("areDivisors"),[VarDecl(Id("num1"),NumberType()),VarDecl(Id("num2"),NumberType())],Return(BinaryOp("or",BinaryOp("=",BinaryOp("%",Id("num1"),Id("num2")),NumberLiteral(0.0)),BinaryOp("=",BinaryOp("%",Id("num2"),Id("num1")),NumberLiteral(0.0))))),FuncDecl(Id("main"),[],Block([VarDecl(Id("num1"),None,"var",CallExpr(Id("readNumber"),[])),VarDecl(Id("num2"),None,"var",CallExpr(Id("readNumber"),[])),If(CallExpr(Id("areDivisors"),[Id("num1"),Id("num2")]),CallStmt(Id("writeString"),[StringLiteral("Yes")]),[],CallStmt(Id("writeString"),[StringLiteral("No")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_simple_program71(self):
        input = """func foo()
        begin
            string name <- readString()
            if (length(name) <= 2) 
                writeString("Name must be at least 4 characters")
            else writeString("Welcome Mr [name] to PPL Course term 232 of HCMUT")
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([VarDecl(Id("name"),StringType(),None,CallExpr(Id("readString"),[])),If(BinaryOp("<=",CallExpr(Id("length"),[Id("name")]),NumberLiteral(2.0)),CallStmt(Id("writeString"),[StringLiteral("Name must be at least 4 characters")]),[],CallStmt(Id("writeString"),[StringLiteral("Welcome Mr [name] to PPL Course term 232 of HCMUT")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_simple_program72(self):
        input = """func foo()
        begin
            x <- - 3 + 5
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("+",UnaryOp("-",NumberLiteral(3.0)),NumberLiteral(5.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_simple_program73(self):
        input = """func foo()
        begin
            x <- - 3 + 5 + 7 + not 3
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("+",BinaryOp("+",BinaryOp("+",UnaryOp("-",NumberLiteral(3.0)),NumberLiteral(5.0)),NumberLiteral(7.0)),UnaryOp("not",NumberLiteral(3.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_simple_program74(self):
        input = """
        number a[2,3] <- [[3,4,5],[1,2,3]]
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType([NumberLiteral(2.0),NumberLiteral(3.0)],NumberType()),None, ArrayLiteral([ArrayLiteral([NumberLiteral(3.0),NumberLiteral(4.0),NumberLiteral(5.0)]),ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_simple_program75(self):
        input = """ func empty()
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("empty"),[],Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_simple_program76(self):
        input = """ func empty()
        begin
        return
        end
        """
        expect = str(Program([FuncDecl(Id("empty"),[],Block([Return()]))]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_simple_program77(self):
        input = """ func empty()
        begin
            return arr(2)[3] + foo(1,2)
        end
        """
        expect = str(Program([FuncDecl(Id("empty"),[],Block([Return(BinaryOp("+",ArrayCell(CallStmt(Id("arr"),[NumberLiteral(2.0)]),[NumberLiteral(3.0)]),CallExpr(Id("foo"),[NumberLiteral(1.0),NumberLiteral(2.0)])))]))]))
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test_simple_program78(self):
        input = """ func empty()
        begin
            number a <- readNumber()
            if (a != 0) return a
            elif (a > 0) return a*a
            else return -a
        end
        """
        expect = str(Program([FuncDecl(Id("empty"),[],Block([VarDecl(Id("a"),NumberType(),None,CallExpr(Id("readNumber"),[])),If(BinaryOp("!=",Id("a"),NumberLiteral(0.0)),Return(Id("a")),[(BinaryOp(">",Id("a"),NumberLiteral(0.0)),Return(BinaryOp("*",Id("a"),Id("a"))))],Return(UnaryOp("-",Id("a"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_simple_program79(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_simple_program80(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_simple_program81(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne")))]))]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_simple_program82(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_simple_program83(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        boolean z <- not 5==6
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_simple_program84(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        boolean z <- not 5==6
        if (z) return true
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[])]))]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_simple_program85(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        boolean z <- not 5==6
        if (z) return true
        var w <- true and "true" or 1
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[]), VarDecl(Id("w"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_simple_program86(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        boolean z <- not 5==6
        if (z) return true
        var w <- true and "true" or 1
        string b[3] <- ["ting"...2]
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[]), VarDecl(Id("w"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0))), VarDecl(Id("b"),ArrayType([NumberLiteral(3.0)],StringType()),None,ArrayLiteral([BinaryOp("...",StringLiteral("ting"),NumberLiteral(2.0))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_simple_program87(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        boolean z <- not 5==6
        if (z) return true
        var w <- true and "true" or 1
        string b[3] <- ["ting"...2]
        var g <- -1 * not 1
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[]), VarDecl(Id("w"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0))), VarDecl(Id("b"),ArrayType([NumberLiteral(3.0)],StringType()),None,ArrayLiteral([BinaryOp("...",StringLiteral("ting"),NumberLiteral(2.0))])), VarDecl(Id("g"),None,"var",BinaryOp("*",UnaryOp("-",NumberLiteral(1.0)),UnaryOp("not",NumberLiteral(1.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_simple_program88(self):
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        var n <- 5 <= 6
        boolean z <- not 5==6
        if (z) return true
        var w <- true and "true" or 1
        string b[3] <- ["ting"...2]
        var g <- -1 * not 1
        var b <- foo()
        end
        """
        expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[]), VarDecl(Id("w"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0))), VarDecl(Id("b"),ArrayType([NumberLiteral(3.0)],StringType()),None,ArrayLiteral([BinaryOp("...",StringLiteral("ting"),NumberLiteral(2.0))])), VarDecl(Id("g"),None,"var",BinaryOp("*",UnaryOp("-",NumberLiteral(1.0)),UnaryOp("not",NumberLiteral(1.0)))), VarDecl(Id("b"),None,"var",CallExpr(Id("foo"),[]))]))]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_simple_program89(self):
            input = """string x <- "be ba ne \\t"
            func foo() begin
            x <- 5 + 5 % 3 - 8 * 12 / 4
            y <- "be ba " ... "ne"
            var n <- 5 <= 6
            boolean z <- not 5==6
            if (z) return true
            var w <- true and "true" or 1
            string b[3] <- ["ting"...2]
            var g <- -1 * not 1
            var b <- foo()
            Pi <- 3.14
            end
            """
            expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[]), VarDecl(Id("w"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0))), VarDecl(Id("b"),ArrayType([NumberLiteral(3.0)],StringType()),None,ArrayLiteral([BinaryOp("...",StringLiteral("ting"),NumberLiteral(2.0))])), VarDecl(Id("g"),None,"var",BinaryOp("*",UnaryOp("-",NumberLiteral(1.0)),UnaryOp("not",NumberLiteral(1.0)))), VarDecl(Id("b"),None,"var",CallExpr(Id("foo"),[])), Assign(Id("Pi"),NumberLiteral(3.14))]))]))
            self.assertTrue(TestAST.test(input, expect, 388))
    
    def test_simple_program90(self):
            input = """string x <- "be ba ne \\t"
            func foo() begin
            x <- 5 + 5 % 3 - 8 * 12 / 4
            y <- "be ba " ... "ne"
            var n <- 5 <= 6
            boolean z <- not 5==6
            if (z) return true
            var w <- true and "true" or 1
            string b[3] <- ["ting"...2]
            var g <- -1 * not 1
            var b <- foo()
            Pi <- 3.14
            a[1+2,2] <- 1
            end
            """
            expect = str(Program([VarDecl(Id("x"),StringType(),None,StringLiteral("be ba ne \\t")),FuncDecl(Id("foo"),[],Block([Assign(Id("x"),BinaryOp("-",BinaryOp("+",NumberLiteral(5.0),BinaryOp("%",NumberLiteral(5.0),NumberLiteral(3.0))),BinaryOp("/",BinaryOp("*",NumberLiteral(8.0),NumberLiteral(12.0)),NumberLiteral(4.0)))), Assign(Id("y"),BinaryOp("...",StringLiteral("be ba "),StringLiteral("ne"))), VarDecl(Id("n"),None,"var",BinaryOp("<=",NumberLiteral(5.0),NumberLiteral(6.0))), VarDecl(Id("z"),BoolType(),None,BinaryOp("==",UnaryOp("not",NumberLiteral(5.0)),NumberLiteral(6.0))), If(Id("z"),Return(BooleanLiteral(True)),[]), VarDecl(Id("w"),None,"var",BinaryOp("or",BinaryOp("and",BooleanLiteral(True),StringLiteral("true")),NumberLiteral(1.0))), VarDecl(Id("b"),ArrayType([NumberLiteral(3.0)],StringType()),None,ArrayLiteral([BinaryOp("...",StringLiteral("ting"),NumberLiteral(2.0))])), VarDecl(Id("g"),None,"var",BinaryOp("*",UnaryOp("-",NumberLiteral(1.0)),UnaryOp("not",NumberLiteral(1.0)))), VarDecl(Id("b"),None,"var",CallExpr(Id("foo"),[])), Assign(Id("Pi"),NumberLiteral(3.14)), Assign(ArrayCell(Id("a"),[BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0)),NumberLiteral(2.0)]),NumberLiteral(1.0))]))]))
            self.assertTrue(TestAST.test(input, expect, 389))
    
    def test_simple_program91(self):
            input = """
            var a <- 5 + (3 != 4)
            """
            expect = str(Program([VarDecl(Id("a"),None,"var",BinaryOp("+",NumberLiteral(5.0),BinaryOp("!=",NumberLiteral(3.0),NumberLiteral(4.0))))]))
            self.assertTrue(TestAST.test(input, expect, 390))

    def test_simple_program92(self):
            input = """
            var a <- 5 + (3 != 4)
            """
            expect = str(Program([VarDecl(Id("a"),None,"var",BinaryOp("+",NumberLiteral(5.0),BinaryOp("!=",NumberLiteral(3.0),NumberLiteral(4.0))))]))
            self.assertTrue(TestAST.test(input, expect, 391))
            
    def test_simple_program93(self):
            input = """func main()
            begin
            for x until x <= 6 by 1
            arr[x] <- 2 * x
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([For(Id("x"),BinaryOp("<=",Id("x"),NumberLiteral(6.0)),NumberLiteral(1.0), Assign(ArrayCell(Id("arr"),[Id("x")]),BinaryOp("*",NumberLiteral(2.0),Id("x"))))]))]))
            self.assertTrue(TestAST.test(input, expect, 392))
            
    def test_simple_program94(self):
            input = """boolean a[122,15] <- [1 + 1/2 * 3]
            """
            expect = str(Program([VarDecl(Id("a"),ArrayType([NumberLiteral(122.0),NumberLiteral(15.0)],BoolType()),None,ArrayLiteral([BinaryOp("+",NumberLiteral(1.0),BinaryOp("*",BinaryOp("/",NumberLiteral(1.0),NumberLiteral(2.0)),NumberLiteral(3.0)))]))]))
            self.assertTrue(TestAST.test(input, expect, 393))

    def test_simple_program95(self):
            input = """var VoTien <- "Vo" ... "Tien"
            """
            expect = str(Program([VarDecl(Id("VoTien"),None,"var",BinaryOp("...",StringLiteral("Vo"),StringLiteral("Tien")))]))
            self.assertTrue(TestAST.test(input, expect, 394))

    def test_simple_program96(self):
            input = """func main()
            begin
                for i until i >= 10 by 1 + 1
                    ## comment
                    
                    a <- 1
                ## comment
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([For(Id("i"),BinaryOp(">=",Id("i"),NumberLiteral(10.0)),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(1.0)),Assign(Id("a"),NumberLiteral(1.0)))]))]))
            self.assertTrue(TestAST.test(input, expect, 395))

    def test_simple_program97(self):
            input = """func main()
            begin
                foo([1,2,3], 1+2, a, c ... e)
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("foo"),[ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0)),Id("a"),BinaryOp("...",Id("c"),Id("e"))])]))]))
            self.assertTrue(TestAST.test(input, expect, 396))

    def test_simple_program98(self):
            input = """func main()
            begin
                foo([1,2,3], 1+2, a, c ... e)
                var VoTien <- a(1,2)
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("foo"),[ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0)),Id("a"),BinaryOp("...",Id("c"),Id("e"))]), VarDecl(Id("VoTien"),None,"var",CallExpr(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0)]))]))]))
            self.assertTrue(TestAST.test(input, expect, 397))

    def test_simple_program99(self):
            input = """func main()
            begin
                foo([1,2,3], 1+2, a, c ... e)
                var VoTien <- a(1,2)
                return foo()
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("foo"),[ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0)),Id("a"),BinaryOp("...",Id("c"),Id("e"))]), VarDecl(Id("VoTien"),None,"var",CallExpr(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0)])), Return(CallExpr(Id("foo"),[]))]))]))
            self.assertTrue(TestAST.test(input, expect, 398))

    def test_simple_program100(self):
            input = """func main()
            begin
                foo([1,2,3], 1+2, a, c ... e)
                var VoTien <- a(1,2)
                return foo()
                break
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("foo"),[ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0)),Id("a"),BinaryOp("...",Id("c"),Id("e"))]), VarDecl(Id("VoTien"),None,"var",CallExpr(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0)])), Return(CallExpr(Id("foo"),[])), Break()]))]))
            self.assertTrue(TestAST.test(input, expect, 399))

    def test_simple_program101(self):
            input = """func main()
            begin
                foo([1,2,3], 1+2, a, c ... e)
                var VoTien <- a(1,2)
                return foo()
                break
                continue
            end
            """
            expect = str(Program([FuncDecl(Id("main"),[],Block([CallStmt(Id("foo"),[ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0)),Id("a"),BinaryOp("...",Id("c"),Id("e"))]), VarDecl(Id("VoTien"),None,"var",CallExpr(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0)])), Return(CallExpr(Id("foo"),[])), Break(), Continue()]))]))
            self.assertTrue(TestAST.test(input, expect, 400))