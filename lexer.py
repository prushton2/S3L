from sly import Lexer, Parser

import command      as cmd
import selectSyntax as SSyntax
import whereSyntax  as WSyntax
import globalSyntax as GSyntax

class b_Lexer(Lexer): # Full lexer, needs to be able to tokenize everything
    tokens = {
        B_SELECT,
        B_FROM,
        B_WHERE,
        B_SEMICOLON,

        S_OPEN_BRACKET,
        S_CLOSE_BRACKET,
        S_LEFT_ARROW,
        S_RIGHT_ARROW,

        W_STR,
        W_PLUS,
        W_RANGE,

        G_STAR,
        G_STRING_LITERAL,
        G_NUM_LITERAL,
        G_OPEN_PARENTHESIS,
        G_CLOSE_PARENTHESIS,

    }
    
    # Base commands
    B_SELECT = cmd.select.regex
    B_FROM = cmd.from_.regex
    B_WHERE = cmd.where.regex
    B_SEMICOLON = cmd.semicolon.regex
    
    # Select commands
    S_OPEN_BRACKET = SSyntax.openBracket.regex
    S_CLOSE_BRACKET = SSyntax.closeBracket.regex
    S_LEFT_ARROW = SSyntax.leftArrow.regex
    S_RIGHT_ARROW = SSyntax.rightArrow.regex

    # Where commands
    W_STR = WSyntax.str_.regex
    W_PLUS = WSyntax.plus.regex
    W_RANGE = WSyntax.range.regex

    # Global commands
    G_STAR = GSyntax.star.regex
    G_STRING_LITERAL = GSyntax.stringLiteral.regex
    G_NUM_LITERAL = GSyntax.numLiteral.regex
    G_OPEN_PARENTHESIS = GSyntax.openParenthesis.regex
    G_CLOSE_PARENTHESIS = GSyntax.closeParenthesis.regex


    #this is important??
    ignore = r" \t"


class s_Lexer(Lexer): # Select lexer
    tokens = {
        S_OPEN_BRACKET,
        S_CLOSE_BRACKET,
        S_LEFT_ARROW,
        S_RIGHT_ARROW,

        # Global Commands
        G_STAR,
        G_STRING_LITERAL,
        G_NUM_LITERAL,
        G_OPEN_PARENTHESIS,
        G_CLOSE_PARENTHESIS,

    }

    # Select commands
    S_OPEN_BRACKET = SSyntax.openBracket.regex
    S_CLOSE_BRACKET = SSyntax.closeBracket.regex
    S_LEFT_ARROW = SSyntax.leftArrow.regex
    S_RIGHT_ARROW = SSyntax.rightArrow.regex

    # Global commands
    G_STAR = GSyntax.star.regex
    G_STRING_LITERAL = GSyntax.stringLiteral.regex
    G_NUM_LITERAL = GSyntax.numLiteral.regex
    G_OPEN_PARENTHESIS = GSyntax.openParenthesis.regex
    G_CLOSE_PARENTHESIS = GSyntax.closeParenthesis.regex

    ignore = r" \t"


class w_Lexer(Lexer): # Where lexer, needs to be able to tokenize where commands
    tokens = {
        W_STR,
        W_PLUS,
        W_RANGE,

        G_STAR,
        G_STRING_LITERAL,
        G_NUM_LITERAL,
        G_OPEN_PARENTHESIS,
        G_CLOSE_PARENTHESIS,
    }

    # Where commands
    W_STR = WSyntax.str_.regex
    W_PLUS = WSyntax.plus.regex
    W_RANGE = WSyntax.range.regex

    # Global commands
    G_STAR = GSyntax.star.regex
    G_STRING_LITERAL = GSyntax.stringLiteral.regex
    G_NUM_LITERAL = GSyntax.numLiteral.regex
    G_OPEN_PARENTHESIS = GSyntax.openParenthesis.regex
    G_CLOSE_PARENTHESIS = GSyntax.closeParenthesis.regex

    ignore = r" \t"

class f_Lexer(Lexer): #From lexer, only string literals or error
    tokens = {
        G_STRING_LITERAL,
    }

    # Global commands
    G_STRING_LITERAL = GSyntax.stringLiteral.regex
    