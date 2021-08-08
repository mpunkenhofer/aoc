# Generated from day18_p1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\25\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\13\n\2\3\2\3\2")
        buf.write("\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\2\2\3\2\3\2\2\3\3\2")
        buf.write("\5\6\2\25\2\n\3\2\2\2\4\5\b\2\1\2\5\6\7\3\2\2\6\7\5\2")
        buf.write("\2\2\7\b\7\4\2\2\b\13\3\2\2\2\t\13\7\7\2\2\n\4\3\2\2\2")
        buf.write("\n\t\3\2\2\2\13\21\3\2\2\2\f\r\f\5\2\2\r\16\t\2\2\2\16")
        buf.write("\20\5\2\2\6\17\f\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21")
        buf.write("\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2\4\n\21")
        return buf.getvalue()


class day18_p1Parser ( Parser ):

    grammarFileName = "day18_p1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "MULT", "ADD", 
                      "INT", "WHITESPACE" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MULT=3
    ADD=4
    INT=5
    WHITESPACE=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return day18_p1Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a day18_p1Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(day18_p1Parser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprInt" ):
                listener.enterExprInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprInt" ):
                listener.exitExprInt(self)


    class ExprParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a day18_p1Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(day18_p1Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParens" ):
                listener.enterExprParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParens" ):
                listener.exitExprParens(self)


    class ExprOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a day18_p1Parser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(day18_p1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(day18_p1Parser.ExprContext,i)

        def ADD(self):
            return self.getToken(day18_p1Parser.ADD, 0)
        def MULT(self):
            return self.getToken(day18_p1Parser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOp" ):
                listener.enterExprOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOp" ):
                listener.exitExprOp(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = day18_p1Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [day18_p1Parser.T__0]:
                localctx = day18_p1Parser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(day18_p1Parser.T__0)
                self.state = 4
                self.expr(0)
                self.state = 5
                self.match(day18_p1Parser.T__1)
                pass
            elif token in [day18_p1Parser.INT]:
                localctx = day18_p1Parser.ExprIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(day18_p1Parser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = day18_p1Parser.ExprOpContext(self, day18_p1Parser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 10
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 11
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==day18_p1Parser.MULT or _la==day18_p1Parser.ADD):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 12
                    self.expr(4) 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




