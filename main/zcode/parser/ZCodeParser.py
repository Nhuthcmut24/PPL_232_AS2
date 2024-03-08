# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3}\n\3\3\4\3\4\5\4\u0081")
        buf.write("\n\4\3\5\3\5\3\5\5\5\u0086\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u0093\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u00a9\n\t\3\t\3\t\3\t\3\t\3\t\5\t\u00b0")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b9\n\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00c5\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00d4\n\17\3\20\3\20\3\20\3\20\5\20\u00da\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e5\n\21\3\22\3\22\3\22\3\22\5\22\u00eb\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u0101\n")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u011d\n\32\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0123\n\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0136\n\37\3 \3 \3 \3 \3 \5 \u013d\n \3!\3!\3!\3")
        buf.write("!\3!\3!\7!\u0145\n!\f!\16!\u0148\13!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u0150\n\"\f\"\16\"\u0153\13\"\3#\3#\3#\3#\3")
        buf.write("#\3#\7#\u015b\n#\f#\16#\u015e\13#\3$\3$\3$\5$\u0163\n")
        buf.write("$\3%\3%\3%\5%\u0168\n%\3&\3&\3&\3&\3&\7&\u016f\n&\f&\16")
        buf.write("&\u0172\13&\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u017a\n\'\3(\3")
        buf.write("(\3(\3(\3)\3)\5)\u0182\n)\3)\3)\3)\3)\3*\3*\3*\3*\3*\5")
        buf.write("*\u018d\n*\3+\3+\5+\u0191\n+\3,\3,\3,\3,\3,\5,\u0198\n")
        buf.write(",\3-\3-\3.\3.\3.\3.\5.\u01a0\n.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\61\5\61\u01a9\n\61\3\62\3\62\3\62\5\62\u01ae\n\62")
        buf.write("\3\63\3\63\3\63\5\63\u01b3\n\63\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\5\64\u01bf\n\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u01c6\n\65\3\66\3\66\3\66\3\66\3")
        buf.write("\67\3\67\5\67\u01ce\n\67\38\38\38\38\38\58\u01d5\n8\3")
        buf.write("9\39\39\39\59\u01db\n9\3:\3:\3:\2\6@BDJ;\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnpr\2\b\4\2\25\25\30\35\3\2\36\37")
        buf.write("\3\2\"#\4\2!!$%\3\2&\'\3\2\22\24\2\u01db\2t\3\2\2\2\4")
        buf.write("|\3\2\2\2\6\u0080\3\2\2\2\b\u0085\3\2\2\2\n\u0092\3\2")
        buf.write("\2\2\f\u0094\3\2\2\2\16\u009a\3\2\2\2\20\u00af\3\2\2\2")
        buf.write("\22\u00b1\3\2\2\2\24\u00bc\3\2\2\2\26\u00c4\3\2\2\2\30")
        buf.write("\u00c6\3\2\2\2\32\u00ca\3\2\2\2\34\u00d3\3\2\2\2\36\u00d9")
        buf.write("\3\2\2\2 \u00e4\3\2\2\2\"\u00ea\3\2\2\2$\u00ec\3\2\2\2")
        buf.write("&\u00f2\3\2\2\2(\u00f8\3\2\2\2*\u00fe\3\2\2\2,\u0104\3")
        buf.write("\2\2\2.\u0107\3\2\2\2\60\u0110\3\2\2\2\62\u0113\3\2\2")
        buf.write("\2\64\u0122\3\2\2\2\66\u0124\3\2\2\28\u0129\3\2\2\2:\u012e")
        buf.write("\3\2\2\2<\u0135\3\2\2\2>\u013c\3\2\2\2@\u013e\3\2\2\2")
        buf.write("B\u0149\3\2\2\2D\u0154\3\2\2\2F\u0162\3\2\2\2H\u0167\3")
        buf.write("\2\2\2J\u0169\3\2\2\2L\u0179\3\2\2\2N\u017b\3\2\2\2P\u0181")
        buf.write("\3\2\2\2R\u018c\3\2\2\2T\u0190\3\2\2\2V\u0197\3\2\2\2")
        buf.write("X\u0199\3\2\2\2Z\u019f\3\2\2\2\\\u01a1\3\2\2\2^\u01a3")
        buf.write("\3\2\2\2`\u01a8\3\2\2\2b\u01ad\3\2\2\2d\u01b2\3\2\2\2")
        buf.write("f\u01be\3\2\2\2h\u01c5\3\2\2\2j\u01c7\3\2\2\2l\u01cd\3")
        buf.write("\2\2\2n\u01d4\3\2\2\2p\u01da\3\2\2\2r\u01dc\3\2\2\2tu")
        buf.write("\5`\61\2uv\5\4\3\2vw\7\2\2\3w\3\3\2\2\2xy\5\6\4\2yz\5")
        buf.write("\4\3\2z}\3\2\2\2{}\5\6\4\2|x\3\2\2\2|{\3\2\2\2}\5\3\2")
        buf.write("\2\2~\u0081\5\b\5\2\177\u0081\5\20\t\2\u0080~\3\2\2\2")
        buf.write("\u0080\177\3\2\2\2\u0081\7\3\2\2\2\u0082\u0086\5\n\6\2")
        buf.write("\u0083\u0086\5\f\7\2\u0084\u0086\5\16\b\2\u0085\u0082")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\t\3\2\2\2\u0087\u0088\5r:\2\u0088\u0089\7-\2\2\u0089")
        buf.write("\u008a\7\27\2\2\u008a\u008b\5<\37\2\u008b\u008c\5b\62")
        buf.write("\2\u008c\u0093\3\2\2\2\u008d\u008e\5r:\2\u008e\u008f\7")
        buf.write("-\2\2\u008f\u0090\5b\62\2\u0090\u0093\3\2\2\2\u0091\u0093")
        buf.write("\5\22\n\2\u0092\u0087\3\2\2\2\u0092\u008d\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\13\3\2\2\2\u0094\u0095\7\5\2\2\u0095")
        buf.write("\u0096\7-\2\2\u0096\u0097\7\27\2\2\u0097\u0098\5<\37\2")
        buf.write("\u0098\u0099\5b\62\2\u0099\r\3\2\2\2\u009a\u009b\7\6\2")
        buf.write("\2\u009b\u009e\7-\2\2\u009c\u009d\7\27\2\2\u009d\u009f")
        buf.write("\5<\37\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a1\5b\62\2\u00a1\17\3\2\2\2\u00a2")
        buf.write("\u00a3\7\7\2\2\u00a3\u00a4\7-\2\2\u00a4\u00a5\5j\66\2")
        buf.write("\u00a5\u00a8\5`\61\2\u00a6\u00a9\5*\26\2\u00a7\u00a9\5")
        buf.write("$\23\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00b0")
        buf.write("\3\2\2\2\u00aa\u00ab\7\7\2\2\u00ab\u00ac\7-\2\2\u00ac")
        buf.write("\u00ad\5j\66\2\u00ad\u00ae\5b\62\2\u00ae\u00b0\3\2\2\2")
        buf.write("\u00af\u00a2\3\2\2\2\u00af\u00aa\3\2\2\2\u00b0\21\3\2")
        buf.write("\2\2\u00b1\u00b2\5r:\2\u00b2\u00b3\7-\2\2\u00b3\u00b4")
        buf.write("\7*\2\2\u00b4\u00b5\5\36\20\2\u00b5\u00b8\7+\2\2\u00b6")
        buf.write("\u00b7\7\27\2\2\u00b7\u00b9\5\26\f\2\u00b8\u00b6\3\2\2")
        buf.write("\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\5b\62\2\u00bb\23\3\2\2\2\u00bc\u00bd\5r:\2\u00bd\u00be")
        buf.write("\7-\2\2\u00be\u00bf\7*\2\2\u00bf\u00c0\5\36\20\2\u00c0")
        buf.write("\u00c1\7+\2\2\u00c1\25\3\2\2\2\u00c2\u00c5\5\30\r\2\u00c3")
        buf.write("\u00c5\5\32\16\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2")
        buf.write("\2\u00c5\27\3\2\2\2\u00c6\u00c7\7*\2\2\u00c7\u00c8\5h")
        buf.write("\65\2\u00c8\u00c9\7+\2\2\u00c9\31\3\2\2\2\u00ca\u00cb")
        buf.write("\7*\2\2\u00cb\u00cc\5\34\17\2\u00cc\u00cd\7+\2\2\u00cd")
        buf.write("\33\3\2\2\2\u00ce\u00cf\5\30\r\2\u00cf\u00d0\7,\2\2\u00d0")
        buf.write("\u00d1\5\34\17\2\u00d1\u00d4\3\2\2\2\u00d2\u00d4\5\30")
        buf.write("\r\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\35")
        buf.write("\3\2\2\2\u00d5\u00d6\7.\2\2\u00d6\u00d7\7,\2\2\u00d7\u00da")
        buf.write("\5\36\20\2\u00d8\u00da\7.\2\2\u00d9\u00d5\3\2\2\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00da\37\3\2\2\2\u00db\u00e5\5\b\5\2\u00dc")
        buf.write("\u00e5\58\35\2\u00dd\u00e5\5\62\32\2\u00de\u00e5\5.\30")
        buf.write("\2\u00df\u00e5\5\60\31\2\u00e0\u00e5\5,\27\2\u00e1\u00e5")
        buf.write("\5*\26\2\u00e2\u00e5\5&\24\2\u00e3\u00e5\5$\23\2\u00e4")
        buf.write("\u00db\3\2\2\2\u00e4\u00dc\3\2\2\2\u00e4\u00dd\3\2\2\2")
        buf.write("\u00e4\u00de\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4\u00e0\3")
        buf.write("\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5!\3\2\2\2\u00e6\u00e7\5 \21\2\u00e7\u00e8")
        buf.write("\5\"\22\2\u00e8\u00eb\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea")
        buf.write("\u00e6\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb#\3\2\2\2\u00ec")
        buf.write("\u00ed\7\20\2\2\u00ed\u00ee\5b\62\2\u00ee\u00ef\5\"\22")
        buf.write("\2\u00ef\u00f0\7\21\2\2\u00f0\u00f1\5b\62\2\u00f1%\3\2")
        buf.write("\2\2\u00f2\u00f3\7-\2\2\u00f3\u00f4\7(\2\2\u00f4\u00f5")
        buf.write("\5T+\2\u00f5\u00f6\7)\2\2\u00f6\u00f7\5`\61\2\u00f7\'")
        buf.write("\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9\u00fa\7(\2\2\u00fa\u00fb")
        buf.write("\5T+\2\u00fb\u00fc\7)\2\2\u00fc\u00fd\5`\61\2\u00fd)\3")
        buf.write("\2\2\2\u00fe\u0100\7\4\2\2\u00ff\u0101\5<\37\2\u0100\u00ff")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0103\5b\62\2\u0103+\3\2\2\2\u0104\u0105\7\f\2\2\u0105")
        buf.write("\u0106\5b\62\2\u0106-\3\2\2\2\u0107\u0108\7\b\2\2\u0108")
        buf.write("\u0109\5^\60\2\u0109\u010a\7\t\2\2\u010a\u010b\5<\37\2")
        buf.write("\u010b\u010c\7\n\2\2\u010c\u010d\5<\37\2\u010d\u010e\5")
        buf.write("`\61\2\u010e\u010f\5 \21\2\u010f/\3\2\2\2\u0110\u0111")
        buf.write("\7\13\2\2\u0111\u0112\5b\62\2\u0112\61\3\2\2\2\u0113\u0114")
        buf.write("\7\r\2\2\u0114\u0115\7(\2\2\u0115\u0116\5<\37\2\u0116")
        buf.write("\u0117\7)\2\2\u0117\u0118\5`\61\2\u0118\u0119\5 \21\2")
        buf.write("\u0119\u011c\5\64\33\2\u011a\u011b\7\16\2\2\u011b\u011d")
        buf.write("\5 \21\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\63\3\2\2\2\u011e\u011f\5\66\34\2\u011f\u0120\5\64\33")
        buf.write("\2\u0120\u0123\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u011e")
        buf.write("\3\2\2\2\u0122\u0121\3\2\2\2\u0123\65\3\2\2\2\u0124\u0125")
        buf.write("\7\17\2\2\u0125\u0126\5<\37\2\u0126\u0127\5`\61\2\u0127")
        buf.write("\u0128\5 \21\2\u0128\67\3\2\2\2\u0129\u012a\5d\63\2\u012a")
        buf.write("\u012b\7\27\2\2\u012b\u012c\5<\37\2\u012c\u012d\5b\62")
        buf.write("\2\u012d9\3\2\2\2\u012e\u012f\t\2\2\2\u012f;\3\2\2\2\u0130")
        buf.write("\u0131\5> \2\u0131\u0132\7\26\2\2\u0132\u0133\5> \2\u0133")
        buf.write("\u0136\3\2\2\2\u0134\u0136\5> \2\u0135\u0130\3\2\2\2\u0135")
        buf.write("\u0134\3\2\2\2\u0136=\3\2\2\2\u0137\u0138\5@!\2\u0138")
        buf.write("\u0139\5:\36\2\u0139\u013a\5@!\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u013d\5@!\2\u013c\u0137\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("?\3\2\2\2\u013e\u013f\b!\1\2\u013f\u0140\5B\"\2\u0140")
        buf.write("\u0146\3\2\2\2\u0141\u0142\f\4\2\2\u0142\u0143\t\3\2\2")
        buf.write("\u0143\u0145\5B\"\2\u0144\u0141\3\2\2\2\u0145\u0148\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147A")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\b\"\1\2\u014a")
        buf.write("\u014b\5D#\2\u014b\u0151\3\2\2\2\u014c\u014d\f\4\2\2\u014d")
        buf.write("\u014e\t\4\2\2\u014e\u0150\5D#\2\u014f\u014c\3\2\2\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152C\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0155\b#\1\2")
        buf.write("\u0155\u0156\5F$\2\u0156\u015c\3\2\2\2\u0157\u0158\f\4")
        buf.write("\2\2\u0158\u0159\t\5\2\2\u0159\u015b\5F$\2\u015a\u0157")
        buf.write("\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015dE\3\2\2\2\u015e\u015c\3\2\2\2\u015f")
        buf.write("\u0160\7 \2\2\u0160\u0163\5F$\2\u0161\u0163\5H%\2\u0162")
        buf.write("\u015f\3\2\2\2\u0162\u0161\3\2\2\2\u0163G\3\2\2\2\u0164")
        buf.write("\u0165\7#\2\2\u0165\u0168\5H%\2\u0166\u0168\5J&\2\u0167")
        buf.write("\u0164\3\2\2\2\u0167\u0166\3\2\2\2\u0168I\3\2\2\2\u0169")
        buf.write("\u016a\b&\1\2\u016a\u016b\5L\'\2\u016b\u0170\3\2\2\2\u016c")
        buf.write("\u016d\f\4\2\2\u016d\u016f\5P)\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171K\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u017a\7-\2\2")
        buf.write("\u0174\u017a\5(\25\2\u0175\u017a\5Z.\2\u0176\u017a\5\26")
        buf.write("\f\2\u0177\u017a\5P)\2\u0178\u017a\5N(\2\u0179\u0173\3")
        buf.write("\2\2\2\u0179\u0174\3\2\2\2\u0179\u0175\3\2\2\2\u0179\u0176")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("M\3\2\2\2\u017b\u017c\7(\2\2\u017c\u017d\5<\37\2\u017d")
        buf.write("\u017e\7)\2\2\u017eO\3\2\2\2\u017f\u0182\7-\2\2\u0180")
        buf.write("\u0182\5&\24\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0184\7*\2\2\u0184\u0185\5")
        buf.write("R*\2\u0185\u0186\7+\2\2\u0186Q\3\2\2\2\u0187\u018d\5<")
        buf.write("\37\2\u0188\u0189\5<\37\2\u0189\u018a\7,\2\2\u018a\u018b")
        buf.write("\5R*\2\u018b\u018d\3\2\2\2\u018c\u0187\3\2\2\2\u018c\u0188")
        buf.write("\3\2\2\2\u018dS\3\2\2\2\u018e\u0191\5V,\2\u018f\u0191")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("U\3\2\2\2\u0192\u0193\5X-\2\u0193\u0194\7,\2\2\u0194\u0195")
        buf.write("\5V,\2\u0195\u0198\3\2\2\2\u0196\u0198\5X-\2\u0197\u0192")
        buf.write("\3\2\2\2\u0197\u0196\3\2\2\2\u0198W\3\2\2\2\u0199\u019a")
        buf.write("\5<\37\2\u019aY\3\2\2\2\u019b\u01a0\7/\2\2\u019c\u01a0")
        buf.write("\7.\2\2\u019d\u01a0\7-\2\2\u019e\u01a0\5\\/\2\u019f\u019b")
        buf.write("\3\2\2\2\u019f\u019c\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0[\3\2\2\2\u01a1\u01a2\t\6\2\2\u01a2")
        buf.write("]\3\2\2\2\u01a3\u01a4\7-\2\2\u01a4_\3\2\2\2\u01a5\u01a6")
        buf.write("\7\62\2\2\u01a6\u01a9\5`\61\2\u01a7\u01a9\3\2\2\2\u01a8")
        buf.write("\u01a5\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9a\3\2\2\2\u01aa")
        buf.write("\u01ab\7\62\2\2\u01ab\u01ae\5b\62\2\u01ac\u01ae\7\62\2")
        buf.write("\2\u01ad\u01aa\3\2\2\2\u01ad\u01ac\3\2\2\2\u01aec\3\2")
        buf.write("\2\2\u01af\u01b3\7-\2\2\u01b0\u01b3\5f\64\2\u01b1\u01b3")
        buf.write("\5P)\2\u01b2\u01af\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b3e\3\2\2\2\u01b4\u01b5\7-\2\2\u01b5\u01b6")
        buf.write("\7*\2\2\u01b6\u01b7\5h\65\2\u01b7\u01b8\7+\2\2\u01b8\u01bf")
        buf.write("\3\2\2\2\u01b9\u01ba\7-\2\2\u01ba\u01bb\7*\2\2\u01bb\u01bc")
        buf.write("\5f\64\2\u01bc\u01bd\7+\2\2\u01bd\u01bf\3\2\2\2\u01be")
        buf.write("\u01b4\3\2\2\2\u01be\u01b9\3\2\2\2\u01bfg\3\2\2\2\u01c0")
        buf.write("\u01c1\5<\37\2\u01c1\u01c2\7,\2\2\u01c2\u01c3\5h\65\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c6\5<\37\2\u01c5\u01c0\3")
        buf.write("\2\2\2\u01c5\u01c4\3\2\2\2\u01c6i\3\2\2\2\u01c7\u01c8")
        buf.write("\7(\2\2\u01c8\u01c9\5l\67\2\u01c9\u01ca\7)\2\2\u01cak")
        buf.write("\3\2\2\2\u01cb\u01ce\5n8\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01cc\3\2\2\2\u01cem\3\2\2\2\u01cf\u01d0")
        buf.write("\5p9\2\u01d0\u01d1\7,\2\2\u01d1\u01d2\5n8\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d5\5p9\2\u01d4\u01cf\3\2\2\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d5o\3\2\2\2\u01d6\u01d7\5r:\2\u01d7\u01d8")
        buf.write("\7-\2\2\u01d8\u01db\3\2\2\2\u01d9\u01db\5\24\13\2\u01da")
        buf.write("\u01d6\3\2\2\2\u01da\u01d9\3\2\2\2\u01dbq\3\2\2\2\u01dc")
        buf.write("\u01dd\t\7\2\2\u01dds\3\2\2\2(|\u0080\u0085\u0092\u009e")
        buf.write("\u00a8\u00af\u00b8\u00c4\u00d3\u00d9\u00e4\u00ea\u0100")
        buf.write("\u011c\u0122\u0135\u013c\u0146\u0151\u015c\u0162\u0167")
        buf.write("\u0170\u0179\u0181\u018c\u0190\u0197\u019f\u01a8\u01ad")
        buf.write("\u01b2\u01be\u01c5\u01cd\u01d4\u01da")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'number'", 
                     "'boolean'", "'string'", "'=='", "'...'", "'<-'", "'>='", 
                     "'>'", "'<='", "'<'", "'!='", "'='", "'or'", "'and'", 
                     "'not'", "'%'", "'+'", "'-'", "'*'", "'/'", "'true'", 
                     "'false'", "'('", "')'", "'['", "']'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", 
                      "FUNC_KEY", "FOR_KEY", "UNTIL_KEY", "BY_KEY", "BREAK_KEY", 
                      "CONTINUE_KEY", "IF_KEY", "ELSE_KEY", "ELIF_KEY", 
                      "BEGIN_KEY", "END_KEY", "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", 
                      "EQUAL_OPERATOR", "CONCAT_OPERATOR", "ASSIGN1_OPERATOR", 
                      "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", "L_OPERATOR", 
                      "NE_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
                      "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", 
                      "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", 
                      "TRUE_BOOLEAN", "FALSE_BOOLEAN", "LB", "RB", "LSB", 
                      "RSB", "COMMA", "ID", "NUMBER", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "NEW_LINE", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_typdecl = 4
    RULE_varkeydecl = 5
    RULE_dynamicdecl = 6
    RULE_funcdecl = 7
    RULE_arraydecl = 8
    RULE_arrayparameter = 9
    RULE_arrayvalue = 10
    RULE_arrayval = 11
    RULE_arrayvallist = 12
    RULE_listarrayval = 13
    RULE_sizelist = 14
    RULE_statement = 15
    RULE_stmtlist = 16
    RULE_blockstmt = 17
    RULE_funccallstmt = 18
    RULE_funccallexpr = 19
    RULE_returnstmt = 20
    RULE_continuestmt = 21
    RULE_forstmt = 22
    RULE_breakstmt = 23
    RULE_ifstmt = 24
    RULE_eliflist = 25
    RULE_elifcomponent = 26
    RULE_assignstmt = 27
    RULE_relationaloperator = 28
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_expr7 = 36
    RULE_expr8 = 37
    RULE_subexpr = 38
    RULE_indexoperator = 39
    RULE_indexope = 40
    RULE_argumentlist = 41
    RULE_argumentprime = 42
    RULE_argument = 43
    RULE_literal = 44
    RULE_booleanvalue = 45
    RULE_numbervariable = 46
    RULE_newlinelist = 47
    RULE_newlinelistnonull = 48
    RULE_lhs = 49
    RULE_indexexpr = 50
    RULE_index = 51
    RULE_paralist = 52
    RULE_parameterlist = 53
    RULE_paraprime = 54
    RULE_para = 55
    RULE_typ = 56

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "typdecl", 
                   "varkeydecl", "dynamicdecl", "funcdecl", "arraydecl", 
                   "arrayparameter", "arrayvalue", "arrayval", "arrayvallist", 
                   "listarrayval", "sizelist", "statement", "stmtlist", 
                   "blockstmt", "funccallstmt", "funccallexpr", "returnstmt", 
                   "continuestmt", "forstmt", "breakstmt", "ifstmt", "eliflist", 
                   "elifcomponent", "assignstmt", "relationaloperator", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "subexpr", "indexoperator", 
                   "indexope", "argumentlist", "argumentprime", "argument", 
                   "literal", "booleanvalue", "numbervariable", "newlinelist", 
                   "newlinelistnonull", "lhs", "indexexpr", "index", "paralist", 
                   "parameterlist", "paraprime", "para", "typ" ]

    EOF = Token.EOF
    COMMENT=1
    RETURN_KEY=2
    VAR_KEY=3
    DYNAMIC_KEY=4
    FUNC_KEY=5
    FOR_KEY=6
    UNTIL_KEY=7
    BY_KEY=8
    BREAK_KEY=9
    CONTINUE_KEY=10
    IF_KEY=11
    ELSE_KEY=12
    ELIF_KEY=13
    BEGIN_KEY=14
    END_KEY=15
    NUM_TYPE=16
    BOOL_TYPE=17
    STRING_TYPE=18
    EQUAL_OPERATOR=19
    CONCAT_OPERATOR=20
    ASSIGN1_OPERATOR=21
    GE_OPERATOR=22
    G_OPERATOR=23
    LE_OPERATOR=24
    L_OPERATOR=25
    NE_OPERATOR=26
    ASSIGN2_OPERATOR=27
    OR_OPERATOR=28
    AND_OPERATOR=29
    NOT_OPERATOR=30
    MODULO_OPERATOR=31
    ADD_OPERATOR=32
    SUB_OPERATOR=33
    MUL_OPERATOR=34
    DIV_OPERATOR=35
    TRUE_BOOLEAN=36
    FALSE_BOOLEAN=37
    LB=38
    RB=39
    LSB=40
    RSB=41
    COMMA=42
    ID=43
    NUMBER=44
    STRINGLIT=45
    UNCLOSE_STRING=46
    ILLEGAL_ESCAPE=47
    NEW_LINE=48
    WS=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.newlinelist()
            self.state = 115
            self.decllist()
            self.state = 116
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.decl()
                self.state = 119
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KEY, ZCodeParser.DYNAMIC_KEY, ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typdecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypdeclContext,0)


        def varkeydecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarkeydeclContext,0)


        def dynamicdecl(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.varkeydecl()
                pass
            elif token in [ZCodeParser.DYNAMIC_KEY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.dynamicdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypdecl" ):
                return visitor.visitTypdecl(self)
            else:
                return visitor.visitChildren(self)




    def typdecl(self):

        localctx = ZCodeParser.TypdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typdecl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.typ()
                self.state = 134
                self.match(ZCodeParser.ID)
                self.state = 135
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 136
                self.expr()
                self.state = 137
                self.newlinelistnonull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.typ()
                self.state = 140
                self.match(ZCodeParser.ID)
                self.state = 141
                self.newlinelistnonull()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarkeydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KEY(self):
            return self.getToken(ZCodeParser.VAR_KEY, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varkeydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarkeydecl" ):
                return visitor.visitVarkeydecl(self)
            else:
                return visitor.visitChildren(self)




    def varkeydecl(self):

        localctx = ZCodeParser.VarkeydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varkeydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.VAR_KEY)
            self.state = 147
            self.match(ZCodeParser.ID)
            self.state = 148
            self.match(ZCodeParser.ASSIGN1_OPERATOR)
            self.state = 149
            self.expr()
            self.state = 150
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC_KEY(self):
            return self.getToken(ZCodeParser.DYNAMIC_KEY, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamicdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamicdecl" ):
                return visitor.visitDynamicdecl(self)
            else:
                return visitor.visitChildren(self)




    def dynamicdecl(self):

        localctx = ZCodeParser.DynamicdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dynamicdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(ZCodeParser.DYNAMIC_KEY)
            self.state = 153
            self.match(ZCodeParser.ID)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 154
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 155
                self.expr()


            self.state = 158
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KEY(self):
            return self.getToken(ZCodeParser.FUNC_KEY, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def paralist(self):
            return self.getTypedRuleContext(ZCodeParser.ParalistContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(ZCodeParser.FUNC_KEY)
                self.state = 161
                self.match(ZCodeParser.ID)
                self.state = 162
                self.paralist()
                self.state = 163
                self.newlinelist()
                self.state = 166
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN_KEY]:
                    self.state = 164
                    self.returnstmt()
                    pass
                elif token in [ZCodeParser.BEGIN_KEY]:
                    self.state = 165
                    self.blockstmt()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(ZCodeParser.FUNC_KEY)
                self.state = 169
                self.match(ZCodeParser.ID)
                self.state = 170
                self.paralist()
                self.state = 171
                self.newlinelistnonull()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.typ()
            self.state = 176
            self.match(ZCodeParser.ID)
            self.state = 177
            self.match(ZCodeParser.LSB)
            self.state = 178
            self.sizelist()
            self.state = 179
            self.match(ZCodeParser.RSB)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 180
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 181
                self.arrayvalue()


            self.state = 184
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayparameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayparameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayparameter" ):
                return visitor.visitArrayparameter(self)
            else:
                return visitor.visitChildren(self)




    def arrayparameter(self):

        localctx = ZCodeParser.ArrayparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayparameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.typ()
            self.state = 187
            self.match(ZCodeParser.ID)
            self.state = 188
            self.match(ZCodeParser.LSB)
            self.state = 189
            self.sizelist()
            self.state = 190
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalContext,0)


        def arrayvallist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvallistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvalue" ):
                return visitor.visitArrayvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayvalue)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.arrayval()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.arrayvallist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayval" ):
                return visitor.visitArrayval(self)
            else:
                return visitor.visitChildren(self)




    def arrayval(self):

        localctx = ZCodeParser.ArrayvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(ZCodeParser.LSB)
            self.state = 197
            self.index()
            self.state = 198
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def listarrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ListarrayvalContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvallist" ):
                return visitor.visitArrayvallist(self)
            else:
                return visitor.visitChildren(self)




    def arrayvallist(self):

        localctx = ZCodeParser.ArrayvallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayvallist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.LSB)
            self.state = 201
            self.listarrayval()
            self.state = 202
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListarrayvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def listarrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ListarrayvalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listarrayval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListarrayval" ):
                return visitor.visitListarrayval(self)
            else:
                return visitor.visitChildren(self)




    def listarrayval(self):

        localctx = ZCodeParser.ListarrayvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listarrayval)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.arrayval()
                self.state = 205
                self.match(ZCodeParser.COMMA)
                self.state = 206
                self.listarrayval()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.arrayval()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizelist" ):
                return visitor.visitSizelist(self)
            else:
                return visitor.visitChildren(self)




    def sizelist(self):

        localctx = ZCodeParser.SizelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sizelist)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(ZCodeParser.NUMBER)
                self.state = 212
                self.match(ZCodeParser.COMMA)
                self.state = 213
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 220
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 221
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 222
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 223
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 224
                self.funccallstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 225
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmtlist)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN_KEY, ZCodeParser.VAR_KEY, ZCodeParser.DYNAMIC_KEY, ZCodeParser.FOR_KEY, ZCodeParser.BREAK_KEY, ZCodeParser.CONTINUE_KEY, ZCodeParser.IF_KEY, ZCodeParser.BEGIN_KEY, ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.statement()
                self.state = 229
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END_KEY]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_KEY(self):
            return self.getToken(ZCodeParser.BEGIN_KEY, 0)

        def newlinelistnonull(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistnonullContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,i)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END_KEY(self):
            return self.getToken(ZCodeParser.END_KEY, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ZCodeParser.BEGIN_KEY)
            self.state = 235
            self.newlinelistnonull()
            self.state = 236
            self.stmtlist()
            self.state = 237
            self.match(ZCodeParser.END_KEY)
            self.state = 238
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funccallstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccallstmt" ):
                return visitor.visitFunccallstmt(self)
            else:
                return visitor.visitChildren(self)




    def funccallstmt(self):

        localctx = ZCodeParser.FunccallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funccallstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(ZCodeParser.ID)
            self.state = 241
            self.match(ZCodeParser.LB)
            self.state = 242
            self.argumentlist()
            self.state = 243
            self.match(ZCodeParser.RB)
            self.state = 244
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funccallexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccallexpr" ):
                return visitor.visitFunccallexpr(self)
            else:
                return visitor.visitChildren(self)




    def funccallexpr(self):

        localctx = ZCodeParser.FunccallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funccallexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ZCodeParser.ID)
            self.state = 247
            self.match(ZCodeParser.LB)
            self.state = 248
            self.argumentlist()
            self.state = 249
            self.match(ZCodeParser.RB)
            self.state = 250
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KEY(self):
            return self.getToken(ZCodeParser.RETURN_KEY, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ZCodeParser.RETURN_KEY)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT_OPERATOR) | (1 << ZCodeParser.SUB_OPERATOR) | (1 << ZCodeParser.TRUE_BOOLEAN) | (1 << ZCodeParser.FALSE_BOOLEAN) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 253
                self.expr()


            self.state = 256
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_KEY(self):
            return self.getToken(ZCodeParser.CONTINUE_KEY, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.CONTINUE_KEY)
            self.state = 259
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_KEY(self):
            return self.getToken(ZCodeParser.FOR_KEY, 0)

        def numbervariable(self):
            return self.getTypedRuleContext(ZCodeParser.NumbervariableContext,0)


        def UNTIL_KEY(self):
            return self.getToken(ZCodeParser.UNTIL_KEY, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY_KEY(self):
            return self.getToken(ZCodeParser.BY_KEY, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ZCodeParser.FOR_KEY)
            self.state = 262
            self.numbervariable()
            self.state = 263
            self.match(ZCodeParser.UNTIL_KEY)
            self.state = 264
            self.expr()
            self.state = 265
            self.match(ZCodeParser.BY_KEY)
            self.state = 266
            self.expr()
            self.state = 267
            self.newlinelist()
            self.state = 268
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_KEY(self):
            return self.getToken(ZCodeParser.BREAK_KEY, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.BREAK_KEY)
            self.state = 271
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEY(self):
            return self.getToken(ZCodeParser.IF_KEY, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def ELSE_KEY(self):
            return self.getToken(ZCodeParser.ELSE_KEY, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.IF_KEY)
            self.state = 274
            self.match(ZCodeParser.LB)
            self.state = 275
            self.expr()
            self.state = 276
            self.match(ZCodeParser.RB)
            self.state = 277
            self.newlinelist()
            self.state = 278
            self.statement()
            self.state = 279
            self.eliflist()
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 280
                self.match(ZCodeParser.ELSE_KEY)
                self.state = 281
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifcomponent(self):
            return self.getTypedRuleContext(ZCodeParser.ElifcomponentContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_eliflist)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.elifcomponent()
                self.state = 285
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifcomponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF_KEY(self):
            return self.getToken(ZCodeParser.ELIF_KEY, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifcomponent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifcomponent" ):
                return visitor.visitElifcomponent(self)
            else:
                return visitor.visitChildren(self)




    def elifcomponent(self):

        localctx = ZCodeParser.ElifcomponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elifcomponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZCodeParser.ELIF_KEY)
            self.state = 291
            self.expr()
            self.state = 292
            self.newlinelist()
            self.state = 293
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.lhs()
            self.state = 296
            self.match(ZCodeParser.ASSIGN1_OPERATOR)
            self.state = 297
            self.expr()
            self.state = 298
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationaloperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_OPERATOR(self):
            return self.getToken(ZCodeParser.EQUAL_OPERATOR, 0)

        def ASSIGN2_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN2_OPERATOR, 0)

        def NE_OPERATOR(self):
            return self.getToken(ZCodeParser.NE_OPERATOR, 0)

        def GE_OPERATOR(self):
            return self.getToken(ZCodeParser.GE_OPERATOR, 0)

        def G_OPERATOR(self):
            return self.getToken(ZCodeParser.G_OPERATOR, 0)

        def LE_OPERATOR(self):
            return self.getToken(ZCodeParser.LE_OPERATOR, 0)

        def L_OPERATOR(self):
            return self.getToken(ZCodeParser.L_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relationaloperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationaloperator" ):
                return visitor.visitRelationaloperator(self)
            else:
                return visitor.visitChildren(self)




    def relationaloperator(self):

        localctx = ZCodeParser.RelationaloperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_relationaloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_OPERATOR) | (1 << ZCodeParser.GE_OPERATOR) | (1 << ZCodeParser.G_OPERATOR) | (1 << ZCodeParser.LE_OPERATOR) | (1 << ZCodeParser.L_OPERATOR) | (1 << ZCodeParser.NE_OPERATOR) | (1 << ZCodeParser.ASSIGN2_OPERATOR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT_OPERATOR(self):
            return self.getToken(ZCodeParser.CONCAT_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.expr1()
                self.state = 303
                self.match(ZCodeParser.CONCAT_OPERATOR)
                self.state = 304
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def relationaloperator(self):
            return self.getTypedRuleContext(ZCodeParser.RelationaloperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr1)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.expr2(0)
                self.state = 310
                self.relationaloperator()
                self.state = 311
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND_OPERATOR(self):
            return self.getToken(ZCodeParser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(ZCodeParser.OR_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.OR_OPERATOR or _la==ZCodeParser.AND_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.expr3(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD_OPERATOR(self):
            return self.getToken(ZCodeParser.ADD_OPERATOR, 0)

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OPERATOR or _la==ZCodeParser.SUB_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 332
                    self.expr4(0) 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL_OPERATOR(self):
            return self.getToken(ZCodeParser.MUL_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(ZCodeParser.DIV_OPERATOR, 0)

        def MODULO_OPERATOR(self):
            return self.getToken(ZCodeParser.MODULO_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 341
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 342
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MODULO_OPERATOR) | (1 << ZCodeParser.MUL_OPERATOR) | (1 << ZCodeParser.DIV_OPERATOR))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 343
                    self.expr5() 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr5)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 350
                self.expr5()
                pass
            elif token in [ZCodeParser.SUB_OPERATOR, ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 355
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def indexoperator(self):
            return self.getTypedRuleContext(ZCodeParser.IndexoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 362
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 363
                    self.indexoperator() 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funccallexpr(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallexprContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def indexoperator(self):
            return self.getTypedRuleContext(ZCodeParser.IndexoperatorContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr8)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.funccallexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.arrayvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
                self.indexoperator()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 374
                self.subexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(ZCodeParser.LB)
            self.state = 378
            self.expr()
            self.state = 379
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def indexope(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexoperator" ):
                return visitor.visitIndexoperator(self)
            else:
                return visitor.visitChildren(self)




    def indexoperator(self):

        localctx = ZCodeParser.IndexoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_indexoperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 381
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 382
                self.funccallstmt()
                pass


            self.state = 385
            self.match(ZCodeParser.LSB)
            self.state = 386
            self.indexope()
            self.state = 387
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def indexope(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexope

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexope" ):
                return visitor.visitIndexope(self)
            else:
                return visitor.visitChildren(self)




    def indexope(self):

        localctx = ZCodeParser.IndexopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_indexope)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.expr()
                self.state = 391
                self.match(ZCodeParser.COMMA)
                self.state = 392
                self.indexope()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = ZCodeParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_argumentlist)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OPERATOR, ZCodeParser.SUB_OPERATOR, ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.argumentprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argumentprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentprime" ):
                return visitor.visitArgumentprime(self)
            else:
                return visitor.visitChildren(self)




    def argumentprime(self):

        localctx = ZCodeParser.ArgumentprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentprime)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.argument()
                self.state = 401
                self.match(ZCodeParser.COMMA)
                self.state = 402
                self.argumentprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ZCodeParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def booleanvalue(self):
            return self.getTypedRuleContext(ZCodeParser.BooleanvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.match(ZCodeParser.ID)
                pass
            elif token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.booleanvalue()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE_BOOLEAN(self):
            return self.getToken(ZCodeParser.TRUE_BOOLEAN, 0)

        def FALSE_BOOLEAN(self):
            return self.getToken(ZCodeParser.FALSE_BOOLEAN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_booleanvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanvalue" ):
                return visitor.visitBooleanvalue(self)
            else:
                return visitor.visitChildren(self)




    def booleanvalue(self):

        localctx = ZCodeParser.BooleanvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_booleanvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE_BOOLEAN or _la==ZCodeParser.FALSE_BOOLEAN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumbervariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_numbervariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumbervariable" ):
                return visitor.visitNumbervariable(self)
            else:
                return visitor.visitChildren(self)




    def numbervariable(self):

        localctx = ZCodeParser.NumbervariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_numbervariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_newlinelist)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(ZCodeParser.NEW_LINE)
                self.state = 420
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistnonullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelistnonull

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelistnonull" ):
                return visitor.visitNewlinelistnonull(self)
            else:
                return visitor.visitChildren(self)




    def newlinelistnonull(self):

        localctx = ZCodeParser.NewlinelistnonullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_newlinelistnonull)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(ZCodeParser.NEW_LINE)
                self.state = 425
                self.newlinelistnonull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(ZCodeParser.NEW_LINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def indexexpr(self):
            return self.getTypedRuleContext(ZCodeParser.IndexexprContext,0)


        def indexoperator(self):
            return self.getTypedRuleContext(ZCodeParser.IndexoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_lhs)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.indexexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.indexoperator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def indexexpr(self):
            return self.getTypedRuleContext(ZCodeParser.IndexexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexexpr" ):
                return visitor.visitIndexexpr(self)
            else:
                return visitor.visitChildren(self)




    def indexexpr(self):

        localctx = ZCodeParser.IndexexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_indexexpr)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(ZCodeParser.ID)
                self.state = 435
                self.match(ZCodeParser.LSB)
                self.state = 436
                self.index()
                self.state = 437
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(ZCodeParser.ID)
                self.state = 440
                self.match(ZCodeParser.LSB)
                self.state = 441
                self.indexexpr()
                self.state = 442
                self.match(ZCodeParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = ZCodeParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_index)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.expr()
                self.state = 447
                self.match(ZCodeParser.COMMA)
                self.state = 448
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = ZCodeParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_paralist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(ZCodeParser.LB)
            self.state = 454
            self.parameterlist()
            self.state = 455
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParaprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = ZCodeParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_parameterlist)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.paraprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(ZCodeParser.ParaContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paraprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParaprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paraprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaprime" ):
                return visitor.visitParaprime(self)
            else:
                return visitor.visitChildren(self)




    def paraprime(self):

        localctx = ZCodeParser.ParaprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_paraprime)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.para()
                self.state = 462
                self.match(ZCodeParser.COMMA)
                self.state = 463
                self.paraprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def arrayparameter(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayparameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ZCodeParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_para)
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.typ()
                self.state = 469
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.arrayparameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_TYPE(self):
            return self.getToken(ZCodeParser.NUM_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(ZCodeParser.BOOL_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(ZCodeParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_TYPE) | (1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.STRING_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        self._predicates[36] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




