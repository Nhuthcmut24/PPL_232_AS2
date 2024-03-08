# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0182\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\7\2v\n\2\f\2\16\2y\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\3%\3&\3&")
        buf.write("\3&\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\7,")
        buf.write("\u0123\n,\f,\16,\u0126\13,\3-\3-\3-\5-\u012b\n-\3-\3-")
        buf.write("\5-\u012f\n-\3-\5-\u0132\n-\5-\u0134\n-\3.\6.\u0137\n")
        buf.write(".\r.\16.\u0138\3/\3/\7/\u013d\n/\f/\16/\u0140\13/\3\60")
        buf.write("\3\60\5\60\u0144\n\60\3\60\6\60\u0147\n\60\r\60\16\60")
        buf.write("\u0148\3\61\3\61\3\61\3\61\3\61\7\61\u0150\n\61\f\61\16")
        buf.write("\61\u0153\13\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\7\62\u015d\n\62\f\62\16\62\u0160\13\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\7\64\u016c\n\64\f")
        buf.write("\64\16\64\u016f\13\64\3\64\3\64\3\64\3\65\3\65\3\65\3")
        buf.write("\66\3\66\3\67\6\67\u017a\n\67\r\67\16\67\u017b\3\67\3")
        buf.write("\67\38\38\38\2\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a/c\60e\2g\61i\2k")
        buf.write("\62m\63o\64\3\2\r\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\3\2))\3\2$$\t")
        buf.write("\2))^^ddhhppttvv\5\2\13\13\16\17\"\"\2\u0190\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2g\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5|")
        buf.write("\3\2\2\2\7\u0083\3\2\2\2\t\u0087\3\2\2\2\13\u008f\3\2")
        buf.write("\2\2\r\u0094\3\2\2\2\17\u0098\3\2\2\2\21\u009e\3\2\2\2")
        buf.write("\23\u00a1\3\2\2\2\25\u00a7\3\2\2\2\27\u00b0\3\2\2\2\31")
        buf.write("\u00b3\3\2\2\2\33\u00b8\3\2\2\2\35\u00bd\3\2\2\2\37\u00c3")
        buf.write("\3\2\2\2!\u00c7\3\2\2\2#\u00ce\3\2\2\2%\u00d6\3\2\2\2")
        buf.write("\'\u00dd\3\2\2\2)\u00e0\3\2\2\2+\u00e4\3\2\2\2-\u00e7")
        buf.write("\3\2\2\2/\u00ea\3\2\2\2\61\u00ec\3\2\2\2\63\u00ef\3\2")
        buf.write("\2\2\65\u00f1\3\2\2\2\67\u00f4\3\2\2\29\u00f6\3\2\2\2")
        buf.write(";\u00f9\3\2\2\2=\u00fd\3\2\2\2?\u0101\3\2\2\2A\u0103\3")
        buf.write("\2\2\2C\u0105\3\2\2\2E\u0107\3\2\2\2G\u0109\3\2\2\2I\u010b")
        buf.write("\3\2\2\2K\u0110\3\2\2\2M\u0116\3\2\2\2O\u0118\3\2\2\2")
        buf.write("Q\u011a\3\2\2\2S\u011c\3\2\2\2U\u011e\3\2\2\2W\u0120\3")
        buf.write("\2\2\2Y\u0133\3\2\2\2[\u0136\3\2\2\2]\u013a\3\2\2\2_\u0141")
        buf.write("\3\2\2\2a\u014a\3\2\2\2c\u0157\3\2\2\2e\u0163\3\2\2\2")
        buf.write("g\u0166\3\2\2\2i\u0173\3\2\2\2k\u0176\3\2\2\2m\u0179\3")
        buf.write("\2\2\2o\u017f\3\2\2\2qr\7%\2\2rs\7%\2\2sw\3\2\2\2tv\n")
        buf.write("\2\2\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3\2\2")
        buf.write("\2yw\3\2\2\2z{\b\2\2\2{\4\3\2\2\2|}\7t\2\2}~\7g\2\2~\177")
        buf.write("\7v\2\2\177\u0080\7w\2\2\u0080\u0081\7t\2\2\u0081\u0082")
        buf.write("\7p\2\2\u0082\6\3\2\2\2\u0083\u0084\7x\2\2\u0084\u0085")
        buf.write("\7c\2\2\u0085\u0086\7t\2\2\u0086\b\3\2\2\2\u0087\u0088")
        buf.write("\7f\2\2\u0088\u0089\7{\2\2\u0089\u008a\7p\2\2\u008a\u008b")
        buf.write("\7c\2\2\u008b\u008c\7o\2\2\u008c\u008d\7k\2\2\u008d\u008e")
        buf.write("\7e\2\2\u008e\n\3\2\2\2\u008f\u0090\7h\2\2\u0090\u0091")
        buf.write("\7w\2\2\u0091\u0092\7p\2\2\u0092\u0093\7e\2\2\u0093\f")
        buf.write("\3\2\2\2\u0094\u0095\7h\2\2\u0095\u0096\7q\2\2\u0096\u0097")
        buf.write("\7t\2\2\u0097\16\3\2\2\2\u0098\u0099\7w\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7v\2\2\u009b\u009c\7k\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\20\3\2\2\2\u009e\u009f\7d\2\2\u009f\u00a0")
        buf.write("\7{\2\2\u00a0\22\3\2\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7m\2\2\u00a6\24\3\2\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\26\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7h\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7n\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7\7g\2\2\u00b7\32")
        buf.write("\3\2\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7k\2\2\u00bb\u00bc\7h\2\2\u00bc\34\3\2\2\2\u00bd\u00be")
        buf.write("\7d\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7i\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\36\3\2\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7f\2\2\u00c6 \3")
        buf.write("\2\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca")
        buf.write("\7o\2\2\u00ca\u00cb\7d\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\"\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7p\2\2\u00d5$\3")
        buf.write("\2\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7i\2\2\u00dc&\3\2\2\2\u00dd\u00de\7?\2\2\u00de\u00df")
        buf.write("\7?\2\2\u00df(\3\2\2\2\u00e0\u00e1\7\60\2\2\u00e1\u00e2")
        buf.write("\7\60\2\2\u00e2\u00e3\7\60\2\2\u00e3*\3\2\2\2\u00e4\u00e5")
        buf.write("\7>\2\2\u00e5\u00e6\7/\2\2\u00e6,\3\2\2\2\u00e7\u00e8")
        buf.write("\7@\2\2\u00e8\u00e9\7?\2\2\u00e9.\3\2\2\2\u00ea\u00eb")
        buf.write("\7@\2\2\u00eb\60\3\2\2\2\u00ec\u00ed\7>\2\2\u00ed\u00ee")
        buf.write("\7?\2\2\u00ee\62\3\2\2\2\u00ef\u00f0\7>\2\2\u00f0\64\3")
        buf.write("\2\2\2\u00f1\u00f2\7#\2\2\u00f2\u00f3\7?\2\2\u00f3\66")
        buf.write("\3\2\2\2\u00f4\u00f5\7?\2\2\u00f58\3\2\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7t\2\2\u00f8:\3\2\2\2\u00f9\u00fa")
        buf.write("\7c\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7f\2\2\u00fc<\3")
        buf.write("\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100>\3\2\2\2\u0101\u0102\7\'\2\2\u0102@\3\2")
        buf.write("\2\2\u0103\u0104\7-\2\2\u0104B\3\2\2\2\u0105\u0106\7/")
        buf.write("\2\2\u0106D\3\2\2\2\u0107\u0108\7,\2\2\u0108F\3\2\2\2")
        buf.write("\u0109\u010a\7\61\2\2\u010aH\3\2\2\2\u010b\u010c\7v\2")
        buf.write("\2\u010c\u010d\7t\2\2\u010d\u010e\7w\2\2\u010e\u010f\7")
        buf.write("g\2\2\u010fJ\3\2\2\2\u0110\u0111\7h\2\2\u0111\u0112\7")
        buf.write("c\2\2\u0112\u0113\7n\2\2\u0113\u0114\7u\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115L\3\2\2\2\u0116\u0117\7*\2\2\u0117N\3\2\2")
        buf.write("\2\u0118\u0119\7+\2\2\u0119P\3\2\2\2\u011a\u011b\7]\2")
        buf.write("\2\u011bR\3\2\2\2\u011c\u011d\7_\2\2\u011dT\3\2\2\2\u011e")
        buf.write("\u011f\7.\2\2\u011fV\3\2\2\2\u0120\u0124\t\3\2\2\u0121")
        buf.write("\u0123\t\4\2\2\u0122\u0121\3\2\2\2\u0123\u0126\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125X\3\2\2")
        buf.write("\2\u0126\u0124\3\2\2\2\u0127\u0128\5[.\2\u0128\u012a\5")
        buf.write("]/\2\u0129\u012b\5_\60\2\u012a\u0129\3\2\2\2\u012a\u012b")
        buf.write("\3\2\2\2\u012b\u0134\3\2\2\2\u012c\u012e\5[.\2\u012d\u012f")
        buf.write("\5]/\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131")
        buf.write("\3\2\2\2\u0130\u0132\5_\60\2\u0131\u0130\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0127\3\2\2\2")
        buf.write("\u0133\u012c\3\2\2\2\u0134Z\3\2\2\2\u0135\u0137\t\5\2")
        buf.write("\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\\\3\2\2\2\u013a\u013e")
        buf.write("\7\60\2\2\u013b\u013d\t\5\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f^\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0143\t\6\2")
        buf.write("\2\u0142\u0144\t\7\2\2\u0143\u0142\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0147\t\5\2\2\u0146")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149`\3\2\2\2\u014a\u0151\7$\2\2")
        buf.write("\u014b\u0150\n\b\2\2\u014c\u0150\5e\63\2\u014d\u014e\t")
        buf.write("\t\2\2\u014e\u0150\t\n\2\2\u014f\u014b\3\2\2\2\u014f\u014c")
        buf.write("\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0154\3\2\2\2")
        buf.write("\u0153\u0151\3\2\2\2\u0154\u0155\7$\2\2\u0155\u0156\b")
        buf.write("\61\3\2\u0156b\3\2\2\2\u0157\u015e\7$\2\2\u0158\u015d")
        buf.write("\n\b\2\2\u0159\u015d\5e\63\2\u015a\u015b\t\t\2\2\u015b")
        buf.write("\u015d\t\n\2\2\u015c\u0158\3\2\2\2\u015c\u0159\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3")
        buf.write("\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0161\u0162\b\62\4\2\u0162d\3\2\2\2\u0163\u0164")
        buf.write("\7^\2\2\u0164\u0165\t\13\2\2\u0165f\3\2\2\2\u0166\u016d")
        buf.write("\7$\2\2\u0167\u016c\n\b\2\2\u0168\u016c\5e\63\2\u0169")
        buf.write("\u016a\t\t\2\2\u016a\u016c\t\n\2\2\u016b\u0167\3\2\2\2")
        buf.write("\u016b\u0168\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016f\3")
        buf.write("\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\5i\65\2\u0171")
        buf.write("\u0172\b\64\5\2\u0172h\3\2\2\2\u0173\u0174\7^\2\2\u0174")
        buf.write("\u0175\n\13\2\2\u0175j\3\2\2\2\u0176\u0177\7\f\2\2\u0177")
        buf.write("l\3\2\2\2\u0178\u017a\t\f\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017e\b\67\2\2\u017en\3\2\2")
        buf.write("\2\u017f\u0180\13\2\2\2\u0180\u0181\b8\6\2\u0181p\3\2")
        buf.write("\2\2\24\2w\u0124\u012a\u012e\u0131\u0133\u0138\u013e\u0143")
        buf.write("\u0148\u014f\u0151\u015c\u015e\u016b\u016d\u017b\7\b\2")
        buf.write("\2\3\61\2\3\62\3\3\64\4\38\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    RETURN_KEY = 2
    VAR_KEY = 3
    DYNAMIC_KEY = 4
    FUNC_KEY = 5
    FOR_KEY = 6
    UNTIL_KEY = 7
    BY_KEY = 8
    BREAK_KEY = 9
    CONTINUE_KEY = 10
    IF_KEY = 11
    ELSE_KEY = 12
    ELIF_KEY = 13
    BEGIN_KEY = 14
    END_KEY = 15
    NUM_TYPE = 16
    BOOL_TYPE = 17
    STRING_TYPE = 18
    EQUAL_OPERATOR = 19
    CONCAT_OPERATOR = 20
    ASSIGN1_OPERATOR = 21
    GE_OPERATOR = 22
    G_OPERATOR = 23
    LE_OPERATOR = 24
    L_OPERATOR = 25
    NE_OPERATOR = 26
    ASSIGN2_OPERATOR = 27
    OR_OPERATOR = 28
    AND_OPERATOR = 29
    NOT_OPERATOR = 30
    MODULO_OPERATOR = 31
    ADD_OPERATOR = 32
    SUB_OPERATOR = 33
    MUL_OPERATOR = 34
    DIV_OPERATOR = 35
    TRUE_BOOLEAN = 36
    FALSE_BOOLEAN = 37
    LB = 38
    RB = 39
    LSB = 40
    RSB = 41
    COMMA = 42
    ID = 43
    NUMBER = 44
    STRINGLIT = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47
    NEW_LINE = 48
    WS = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'number'", "'boolean'", "'string'", "'=='", 
            "'...'", "'<-'", "'>='", "'>'", "'<='", "'<'", "'!='", "'='", 
            "'or'", "'and'", "'not'", "'%'", "'+'", "'-'", "'*'", "'/'", 
            "'true'", "'false'", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", "FUNC_KEY", 
            "FOR_KEY", "UNTIL_KEY", "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", 
            "IF_KEY", "ELSE_KEY", "ELIF_KEY", "BEGIN_KEY", "END_KEY", "NUM_TYPE", 
            "BOOL_TYPE", "STRING_TYPE", "EQUAL_OPERATOR", "CONCAT_OPERATOR", 
            "ASSIGN1_OPERATOR", "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", 
            "L_OPERATOR", "NE_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
            "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", "ADD_OPERATOR", 
            "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "TRUE_BOOLEAN", 
            "FALSE_BOOLEAN", "LB", "RB", "LSB", "RSB", "COMMA", "ID", "NUMBER", 
            "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "NEW_LINE", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", "FUNC_KEY", 
                  "FOR_KEY", "UNTIL_KEY", "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", 
                  "IF_KEY", "ELSE_KEY", "ELIF_KEY", "BEGIN_KEY", "END_KEY", 
                  "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", "EQUAL_OPERATOR", 
                  "CONCAT_OPERATOR", "ASSIGN1_OPERATOR", "GE_OPERATOR", 
                  "G_OPERATOR", "LE_OPERATOR", "L_OPERATOR", "NE_OPERATOR", 
                  "ASSIGN2_OPERATOR", "OR_OPERATOR", "AND_OPERATOR", "NOT_OPERATOR", 
                  "MODULO_OPERATOR", "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", 
                  "DIV_OPERATOR", "TRUE_BOOLEAN", "FALSE_BOOLEAN", "LB", 
                  "RB", "LSB", "RSB", "COMMA", "ID", "NUMBER", "INTPART", 
                  "DECPART", "EXPPART", "STRINGLIT", "UNCLOSE_STRING", "LI_ESCAPE", 
                  "ILLEGAL_ESCAPE", "ILL_ESCAPE", "NEW_LINE", "WS", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.STRINGLIT_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[50] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


