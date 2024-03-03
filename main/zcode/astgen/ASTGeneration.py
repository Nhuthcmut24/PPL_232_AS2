from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])
    
    def visitPara(self, ctx: ZCodeParser.ParaContext):
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.ID().getText(),self.visit(ctx.typ()))
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
            return self.visit(ctx.para())
        return self.visit(ctx.para()) + self.visit(ctx.paraprime())
    
    def visitParameterlist(self, ctx: ZCodeParser.ParameterlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paraprime())
    
    def visitParalist(self, ctx: ZCodeParser.ParalistContext):
        return self.visit(ctx.parameterlist())
    
    
    def visitIndex(self, ctx: ZCodeParser.IndexContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr())
        return self.visit(ctx.expr()) + self.visit(ctx.index()) 
    
    def visitIndexexpr(self, ctx: ZCodeParser.IndexexprContext):
        if ctx.index():
            return CallExpr(ctx.ID().getText(),self.visit(ctx.index()))
        return CallExpr(ctx.ID().getText(),self.visit(ctx.indexexpr()))

    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.indexexpr():
            return self.visit(ctx.indexexpr())
        else:
            self.visit(ctx.indexoperator())
    
    def visitNewlinelistnonull(self, ctx: ZCodeParser.Newlinelistnonull):
        return
    
    def visitNewlinelist(self, ctx: ZCodeParser.Newlinelist):
        return

    def visitNumbervariable(self, ctx: ZCodeParser.Numbervariable):
        return Id(ctx.ID().getText())
        
    
