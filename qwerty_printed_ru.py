
from consts import *

QWERTY_PRINTED_RU = [

# ROW 1 ###############################################################
    {
        REPL_KEYCODE: "ESCAPE",
        REPLACE: [
            (BASE, r"fallback BACK"),
        ]
    },
    {
        REPL_KEYCODE: "1",
        REPLACE: [
            (BASE, r"'1'"),
            (FN, r"'!'"),
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            (BASE, r"'2'"),
            (FN, r"'@'"),
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            (BASE, r"'3'"),
            (FN, r"'#'"),
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            (BASE, r"'4'"),
            (FN, r"'$'"),
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            (BASE, r"'5'"),
            (FN, r"'%'"),
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            (BASE, r"'6'"),
            (FN, r"'^'"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            (BASE, r"'7'"),
            (FN, r"'&'"),
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            (BASE, r"'8'"),
            (FN, r"'*'"),
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            (BASE, r"'9'"),
            (FN, r"'('"),
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            (BASE, r"'0'"),
            (FN, r"')'"),
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            (BASE, r"'-'"),
            (FN, r"'_'"),
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            (BASE, r"'='"),
            (FN, r"'+'"),
        ]
    },
# ROW 2 ###############################################################
    {    
        REPL_KEYCODE: "TAB",
        REPLACE: [
            (BASE, r"'\t'"),            
        ]
    },
    {    
        REPL_KEYCODE: "GRAVE",
        REPLACE: [
            (BASE, r"'\u0451'"),
            (SHIFT, r"'\u0401'"),
            (CAPSLOCK, r"'\u0401'"),
            (FN, r"'~'"),
        ]
    },
    {
        REPL_KEYCODE: "Q",
        REPLACE: [
            (BASE, r"'\u0439'"),
            (SHIFT, r"'\u0419'"),
            (CAPSLOCK, r"'\u0419'"),            
        ]
    },
    {
        REPL_KEYCODE: "W",
        REPLACE: [
            (BASE, r"'\u0446'"),
            (SHIFT, r"'\u0426'"),
            (CAPSLOCK, r"'\u0426'"),
        ]
    },
    {
        REPL_KEYCODE: "E",
        REPLACE: [
            (BASE, r"'\u0443'"),
            (SHIFT, r"'\u0423'"),
            (CAPSLOCK, r"'\u0423'"),
        ]
    },
    {
        REPL_KEYCODE: "R",
        REPLACE: [
            (BASE, r"'\u043A'"),
            (SHIFT, r"'\u041A'"),
            (CAPSLOCK, r"'\u041A'"),
        ]
    },
    {
        REPL_KEYCODE: "T",
        REPLACE: [
            (BASE, r"'\u0435'"),
            (SHIFT, r"'\u0415'"),
            (CAPSLOCK, r"'\u0415'"),
        ]
    },
    {
        REPL_KEYCODE: "Y",
        REPLACE: [
            (BASE, r"'\u043D'"),
            (SHIFT, r"'\u041D'"),
            (CAPSLOCK, r"'\u041D'"),
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
            (BASE, r"'\u0433'"),
            (SHIFT, r"'\u0413'"),
            (CAPSLOCK, r"'\u0413'"),
        ]
    },
    {
        REPL_KEYCODE: "I",
        REPLACE: [
            (BASE, r"'\u0448'"),
            (SHIFT, r"'\u0428'"),
            (CAPSLOCK, r"'\u0428'"),
        ]
    },
    {
        REPL_KEYCODE: "O",
        REPLACE: [
            (BASE, r"'\u0449'"),
            (SHIFT, r"'\u0429'"),
            (CAPSLOCK, r"'\u0429'"),
        ]
    },
    {
        REPL_KEYCODE: "P",
        REPLACE: [
            (BASE, r"'\u0437'"),
            (FN, r"'/'"),
            (SHIFT, r"'\u0417'"),
            (CAPSLOCK, r"'\u0417'"),
        ]
    },
    {
        REPL_KEYCODE: "SEMICOLON",
        REPLACE: [
            (BASE, r"'\u0436'"),
            (FN, r"':'"),
            (SHIFT, r"'\u0416'"),
            (CAPSLOCK, r"'\u0416'"),
        ]
    },
# ROW 3 ###############################################################
    {    
        REPL_KEYCODE: "BACKSLASH",
        REPLACE: [
            (BASE, r"'.'"),
            (FN, r"'|'"),
			(SHIFT, r"','"),
            (CAPSLOCK, r"'.'"),
        ]
    },
    {
        REPL_KEYCODE: "A",
        REPLACE: [
            (BASE, r"'\u0444'"),
            (SHIFT, r"'\u0424'"),
            (CAPSLOCK, r"'\u0424'"),
            #(LALT, r"'à'"),
        ]
    },
    {
        REPL_KEYCODE: "S",
        REPLACE: [
            (BASE, r"'\u044B'"),
            (SHIFT, r"'\u042B'"),
            (CAPSLOCK, r"'\u042B'"),
            #(LALT, r"'ß'"),
        ]
    },
    {
        REPL_KEYCODE: "D",
        REPLACE: [
            (BASE, r"'\u0432'"),
            (SHIFT, r"'\u0412'"),
            (CAPSLOCK, r"'\u0412'"),
        ]
    },
    {
        REPL_KEYCODE: "F",
        REPLACE: [
            (BASE, r"'\u0430'"),
            (SHIFT, r"'\u0410'"),
            (CAPSLOCK, r"'\u0410'"),
        ]
    },
    {
        REPL_KEYCODE: "G",
        REPLACE: [
            (BASE, r"'\u043F'"),
            (SHIFT, r"'\u041F'"),
            (CAPSLOCK, r"'\u041F'"),
        ]
    },
    {
        REPL_KEYCODE: "H",
        REPLACE: [
            (BASE, r"'\u0440'"),
            (SHIFT, r"'\u0420'"),
            (CAPSLOCK, r"'\u0420'"),
        ]
    },
    {
        REPL_KEYCODE: "J",
        REPLACE: [
            (BASE, r"'\u043E'"),
            (SHIFT, r"'\u041E'"),
            (CAPSLOCK, r"'\u041E'"),
        ]
    },
    {
        REPL_KEYCODE: "K",
        REPLACE: [
            (BASE, r"'\u043B'"),
            (SHIFT, r"'\u041B'"),
            (CAPSLOCK, r"'\u041B'"),
        ]
    },
    {
        REPL_KEYCODE: "L",
        REPLACE: [
            (BASE, r"'\u0434'"),
            (FN, r"'?'"),
            (SHIFT, r"'\u0414'"),
            (CAPSLOCK, r"'\u0414'"),
        ]
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPLACE: [
            (BASE, r"'\u044D'"),
            (FN, r"'\"'"),
			(SHIFT, r"'\u042D'"),
            (CAPSLOCK, r"'\u042D'"),
        ]
    },
    {
        REPL_KEYCODE: "ENTER",
        REPLACE: [
            (BASE, r"'\n'"),
        ]
    },
# ROW 4 ###############################################################
    {    
        REPL_KEYCODE: "LEFT_BRACKET",
        REPLACE: [
            (BASE, r"'\u0445'"),
            (FN, r"'{'"),
			(SHIFT, r"'\u0425'"),
            (CAPSLOCK, r"'\u0425'"),
        ]
    },
    {
        REPL_KEYCODE: "RIGHT_BRACKET",
        REPLACE: [
            (BASE, r"'\u044A'"),
            (FN, r"'}'"),
			(SHIFT, r"'\u042A'"),
            (CAPSLOCK, r"'\u042A'"),
        ]
    },
    {
        REPL_KEYCODE: "Z",
        REPLACE: [
            (BASE, r"'\u044F'"),
            (SHIFT, r"'\u042F'"),
            (CAPSLOCK, r"'\u042F'"),
        ]
    },
    {
        REPL_KEYCODE: "X",
        REPLACE: [
            (BASE, r"'\u0447'"),
            (SHIFT, r"'\u0427'"),
            (CAPSLOCK, r"'\u0427'"),
        ]
    },    
    {
        REPL_KEYCODE: "C",
        REPLACE: [
            (BASE, r"'\u0441'"),
            (SHIFT, r"'\u0421'"),
            (CAPSLOCK, r"'\u0421'"),
        ]
    },
    {
        REPL_KEYCODE: "V",
        REPLACE: [
            (BASE, r"'\u043C'"),
            (SHIFT, r"'\u041C'"),
            (CAPSLOCK, r"'\u041C'"),
        ]
    },
    {
        REPL_KEYCODE: "B",
        REPLACE: [
            (BASE, r"'\u0438'"),
            (SHIFT, r"'\u0418'"),
            (CAPSLOCK, r"'\u0418'"),
        ]
    },
    {
        REPL_KEYCODE: "N",
        REPLACE: [
            (BASE, r"'\u0442'"),
            (SHIFT, r"'\u0422'"),
            (CAPSLOCK, r"'\u0422'"),
        ]
    },
    {
        REPL_KEYCODE: "M",
        REPLACE: [
            (BASE, r"'\u044C'"),
            (SHIFT, r"'\u042C'"),
            (CAPSLOCK, r"'\u042C'"),
        ]
    },
    {
        REPL_KEYCODE: "COMMA",
        REPLACE: [
            (BASE, r"'\u0431'"),
            (FN, r"'<'"),
			(SHIFT, r"'\u0411'"),
            (CAPSLOCK, r"'\u0411'"),
        ]
    },
    {
        REPL_KEYCODE: "PERIOD",
        REPLACE: [
            (BASE, r"'\u044E'"),
            (FN, r"'>'"),
			(SHIFT, r"'\u042E'"),
            (CAPSLOCK, r"'\u042E'"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_UP",
        REPLACE: [
        ]
    },
# ROW 5 ###############################################################
    {    
        REPL_KEYCODE: "ASSIST", #SYM
        REPLACE: [
        ]
    },    
    {    
        REPL_KEYCODE: "SPACE",
        REPLACE: [
            (BASE, r"' '"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_LEFT",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "DPAD_DOWN",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "DPAD_RIGHT",
        REPLACE: [
        ]
    }

]


