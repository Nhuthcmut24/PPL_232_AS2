from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):    
    def visitPara(self, ctx: ZCodeParser.ParaContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.typ()))
        return self.visit(ctx.arrayparameter())
        
    
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUM_TYPE():
            return NumberType()
        elif ctx.BOOL_TYPE():
            return StringType()
        elif ctx.STRING_TYPE():
            return StringType()
    
    
    def visitParaprime(self, ctx: ZCodeParser.ParaprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.para())]
        return [self.visit(ctx.para())] + self.visit(ctx.paraprime())
    
    
    def visitParameterlist(self, ctx: ZCodeParser.ParameterlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paraprime())
    
    
    def visitParalist(self, ctx: ZCodeParser.ParalistContext):
        return self.visit(ctx.parameterlist())
    
    
    def visitIndex(self, ctx: ZCodeParser.IndexContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.index()) 
    
    
    def visitIndexexpr(self, ctx: ZCodeParser.IndexexprContext):
        if ctx.index():
            return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.index()))
        return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.indexexpr()))


    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.indexexpr():
            return self.visit(ctx.indexexpr())
        else:
            self.visit(ctx.indexoperator())
    
    
    def visitNewlinelistnonull(self, ctx: ZCodeParser.NewlinelistnonullContext):
        return
    
    
    def visitNewlinelist(self, ctx: ZCodeParser.NewlinelistContext):
        return


    def visitNumbervariable(self, ctx: ZCodeParser.NumbervariableContext):
        return Id(ctx.ID().getText())
    
    
    def visitBooleanvalue(self, ctx: ZCodeParser.BooleanvalueContext):
        if ctx.TRUE_BOOLEAN():
            return BooleanLiteral(ctx.TRUE_BOOLEAN().getText() == 'true')
        return BooleanLiteral(ctx.FALSE_BOOLEAN().getText() == 'true')
    
    
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.NUMBER():
            return NumberLiteral(float(ctx.NUMBER().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.booleanvalue())
    
    
    def visitArgument(self, ctx: ZCodeParser.ArgumentContext):
        return self.visit(ctx.expr())
    
    
    def visitArgumentprime(self, ctx: ZCodeParser.ArgumentprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.argument())]
        return [self.visit(ctx.argument())] + self.visit(ctx.argumentprime())     
    
    
    def visitArgumentlist(self, ctx: ZCodeParser.ArgumentlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.argumentprime())
    
    
    def visitIndexope(self, ctx: ZCodeParser.IndexopeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.indexope())
            
            
    def visitIndexoperator(self, ctx: ZCodeParser.IndexoperatorContext):
        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.indexope()))
        return ArrayCell(self.visit(ctx.callstmt()),self.visit(ctx.indexope()))
    
    
    def visitSubexpr(self,ctx: ZCodeParser.SubexprContext):
        return self.visit(ctx.expr())
    
    
    def visitExpr8(self, ctx: ZCodeParser.Expr8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.funccallexpr():
            return self.visit(ctx.funccallexpr())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.arrayvalue():
            return self.visit(ctx.arrayvalue())
        elif ctx.indexoperator():
            return self.visit(ctx.indexoperator())
        else:
            return self.visit(ctx.subexpr())
        
        
    # Can chinh sua
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        return self.visit(ctx.indexoperator()) 
        
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnaryOp(ctx.SUB_OPERATOR().getText(),self.visit(ctx.expr6()))
    
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return UnaryOp(ctx.NOT_OPERATOR().getText(),self.visit(ctx.expr5()))
    
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        elif ctx.MUL_OPERATOR():
            return BinaryOp(ctx.MUL_OPERATOR().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        elif ctx.DIV_OPERATOR():
            return BinaryOp(ctx.DIV_OPERATOR().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        elif ctx.MODULO_OPERATOR():
            return BinaryOp(ctx.MODULO_OPERATOR().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        elif ctx.ADD_OPERATOR():
            return BinaryOp(ctx.ADD_OPERATOR().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        else:
            return BinaryOp(ctx.SUB_OPERATOR().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        elif ctx.AND_OPERATOR():
            return BinaryOp(ctx.AND_OPERATOR().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        else :
            return BinaryOp(ctx.OR_OPERATOR().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        return BinaryOp(self.visit(ctx.relationaloperator()),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
    
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        return BinaryOp(ctx.CONCAT_OPERATOR().getText(),self.visit(ctx.expr1(0)),self.visit(ctx.expr1(1)))
    
    def visitRelationaloperator(self, ctx: ZCodeParser.RelationaloperatorContext):
        if ctx.EQUAL_OPERATOR():
            return '=='
        elif ctx.ASSIGN2_OPERATOR():
            return '='
        elif ctx.NE_OPERATOR():
            return '!='
        elif ctx.GE_OPERATOR():
            return '>='
        elif ctx.G_OPERATOR():
            return '>'
        elif ctx.L_OPERATOR():
            return '<'
        elif ctx.LE_OPERATOR():
            return '<='
        
        
    def visitAssignstmt(self, ctx: ZCodeParser.AssignstmtContext):
        return Assign(self.visit(ctx.lhs()),self.visit(ctx.expr()))
    
        
    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        if ctx.getChildCount() == 7:
            return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.eliflist()))
        return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.eliflist()),self.visit(ctx.statement(1)))
    
   
    def  visitElifcomponent(self, ctx: ZCodeParser.ElifcomponentContext):
        return (self.visit(ctx.expr()),self.visit(ctx.statement()))
    
    
    def visitEliflist(self, ctx: ZCodeParser.EliflistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.elifcomponent())] + self.visit(ctx.eliflist())
     
    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        return Break()
    
    
    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        return For(self.visit(ctx.numbervariable()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.statement()))
    
    
    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        return Continue()
    
    
    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        if ctx.getChildCount() == 3:
            return Return(self.visit(ctx.expr()))
        return Return()

    
    def visitBlockstmt(self, ctx: ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.stmtlist()))
    
    
    def visitStmtlist(self, ctx: ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.statement())] + self.visit(ctx.stmtlist())
    
    
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.funccallstmt():
            return self.visit(ctx.funccallstmt())
        else:
            return self.visit(ctx.blockstmt())
    
    
    def visitSizelist(self, ctx: ZCodeParser.SizelistContext):
        if ctx.getChildCount() == 1:
            return [NumberLiteral(float(ctx.NUMBER().getText()))]
        return [NumberLiteral(float(ctx.NUMBER().getText()))] + self.visit(ctx.sizelist())
    
    
    def visitListarrayval(self, ctx: ZCodeParser.ListarrayvalContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arrayval())
        return self.visit(ctx.arrayval()) + self.visit(ctx.listarrayval())
    
    
    def visitArrayvallist(self, ctx: ZCodeParser.ArrayvallistContext):
        return self.visit(ctx.listarrayval())
    
    
    def visitArrayval(self, ctx: ZCodeParser.ArrayvalContext):
        return ArrayLiteral(self.visit(ctx.index()))
    
    
    def visitArrayvalue(self, ctx: ZCodeParser.ArrayvalueContext):
        if ctx.arrayval():
            return self.visit(ctx.arrayval())
        return self.visit(ctx.arrayvallist())
    
    
    def visitArrayparameter(self, ctx: ZCodeParser.ArrayparameterContext):
        return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.sizelist()), self.visit(ctx.typ())))
    
    def visitArraydecl(self, ctx: ZCodeParser.ArraydeclContext):
        if ctx.ASSIGN1_OPERATOR():
            return VarDecl(name = Id(ctx.ID().getText()),varType = ArrayType(self.visit(ctx.sizelist()), self.visit(ctx.typ())), modifier = None, varInit = self.visit(ctx.arrayvalue()))
        return VarDecl(name = Id(ctx.ID().getText()),varType = ArrayType(self.visit(ctx.sizelist()), self.visit(ctx.typ())), modifier = None, varInit = None)
    
    def visitFunccallstmt(self, ctx: ZCodeParser.FunccallstmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.argumentlist()))

    def visitFunccallexpr(self, ctx: ZCodeParser.FunccallexprContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.argumentlist()))
    
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        if ctx.getChildCount() == 4:
            return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paralist()))
        elif ctx.returnstmt():
            return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paralist()), self.visit(ctx.returnstmt()))
        else:
            return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paralist()), self.visit(ctx.blockstmt()))


    def visitDynamicdecl(self, ctx: ZCodeParser.DynamicdeclContext):
        if ctx.getChildCount() == 3:
            return VarDecl(name = Id(ctx.ID().getText()),varType = None, modifier = "dynamic", varInit = None)
        return VarDecl(name = Id(ctx.ID().getText()),varType = None, modifier = "dynamic", varInit = self.visit(ctx.expr()))
    
    
    def visitVarkeydecl(self, ctx:ZCodeParser.VarkeydeclContext):
        return VarDecl(name = Id(ctx.ID().getText()),varType = None, modifier = "var", varInit = self.visit(ctx.expr()))
    
    
    def visitTypdecl(self, ctx:ZCodeParser.TypdeclContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arraydecl())
        elif ctx.getChildCount() == 3:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()))
        else:
            return VarDecl(name = Id(ctx.ID().getText()), varType = self.visit(ctx.typ()), modifier  = None, varInit = self.visit(ctx.expr()))
        
        
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        if ctx.typdecl():
            return self.visit(ctx.typdecl())
        elif ctx.varkeydecl():
            return self.visit(ctx.varkeydecl())
        else:
            return self.visit(ctx.dynamicdecl())
        
    
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    
    
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
    
    
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))        