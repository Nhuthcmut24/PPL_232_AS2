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