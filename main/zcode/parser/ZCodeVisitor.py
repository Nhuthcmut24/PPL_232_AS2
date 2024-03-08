# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typdecl.
    def visitTypdecl(self, ctx:ZCodeParser.TypdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varkeydecl.
    def visitVarkeydecl(self, ctx:ZCodeParser.VarkeydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamicdecl.
    def visitDynamicdecl(self, ctx:ZCodeParser.DynamicdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydecl.
    def visitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayparameter.
    def visitArrayparameter(self, ctx:ZCodeParser.ArrayparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayvalue.
    def visitArrayvalue(self, ctx:ZCodeParser.ArrayvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayval.
    def visitArrayval(self, ctx:ZCodeParser.ArrayvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayvallist.
    def visitArrayvallist(self, ctx:ZCodeParser.ArrayvallistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#listarrayval.
    def visitListarrayval(self, ctx:ZCodeParser.ListarrayvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sizelist.
    def visitSizelist(self, ctx:ZCodeParser.SizelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccallstmt.
    def visitFunccallstmt(self, ctx:ZCodeParser.FunccallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccallexpr.
    def visitFunccallexpr(self, ctx:ZCodeParser.FunccallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestmt.
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliflist.
    def visitEliflist(self, ctx:ZCodeParser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifcomponent.
    def visitElifcomponent(self, ctx:ZCodeParser.ElifcomponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relationaloperator.
    def visitRelationaloperator(self, ctx:ZCodeParser.RelationaloperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subexpr.
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexoperator.
    def visitIndexoperator(self, ctx:ZCodeParser.IndexoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexope.
    def visitIndexope(self, ctx:ZCodeParser.IndexopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentlist.
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentprime.
    def visitArgumentprime(self, ctx:ZCodeParser.ArgumentprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argument.
    def visitArgument(self, ctx:ZCodeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#booleanvalue.
    def visitBooleanvalue(self, ctx:ZCodeParser.BooleanvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numbervariable.
    def visitNumbervariable(self, ctx:ZCodeParser.NumbervariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlinelist.
    def visitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlinelistnonull.
    def visitNewlinelistnonull(self, ctx:ZCodeParser.NewlinelistnonullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexexpr.
    def visitIndexexpr(self, ctx:ZCodeParser.IndexexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index.
    def visitIndex(self, ctx:ZCodeParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paralist.
    def visitParalist(self, ctx:ZCodeParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameterlist.
    def visitParameterlist(self, ctx:ZCodeParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paraprime.
    def visitParaprime(self, ctx:ZCodeParser.ParaprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para.
    def visitPara(self, ctx:ZCodeParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)



del ZCodeParser