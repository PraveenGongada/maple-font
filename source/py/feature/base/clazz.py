import source.py.feature.ast as ast

cls_zero = ast.Clazz("Zero", ["zero", "zero.zero"])
cls_one = ast.Clazz("One", ["one", "one.cv04"])
cls_digit = ast.Clazz(
    "Digit",
    [
        cls_zero,
        cls_one,
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ],
)
cls_space = ast.Clazz("Space", ["space", "nbspace"])
cls_normal_separator = ast.Clazz(
    "NormalSeparator",
    [
        "{",
        "}",
        "[",
        "]",
        "(",
        ")",
        "|",
        "/",
        "\\",
    ],
)
cls_comma = ast.Clazz("Comma", [",", ast.gly(",", ".cv61")])
cls_question = ast.Clazz("Question", ["?", ast.gly("?", ".cv62")])

cls_uppercase = ast.Clazz(
    "Uppercase",
    [
        "A",
        "Aacute",
        "Abreve",
        "Abreveacute",
        "Abrevedotbelow",
        "Abrevegrave",
        "Abrevehookabove",
        "Abrevetilde",
        "Acaron",
        "Acircumflex",
        "Acircumflexacute",
        "Acircumflexdotbelow",
        "Acircumflexgrave",
        "Acircumflexhookabove",
        "Acircumflextilde",
        "Adieresis",
        "Adotbelow",
        "Agrave",
        "Ahookabove",
        "Amacron",
        "Aogonek",
        "Aring",
        "Atilde",
        "AE",
        "AEacute",
        "B",
        "C",
        "Cacute",
        "Ccaron",
        "Ccedilla",
        "Ccircumflex",
        "Cdotaccent",
        "D",
        "Eth",
        "Dcaron",
        "Dcroat",
        "E",
        "Eacute",
        "Ebreve",
        "Ecaron",
        "Ecircumflex",
        "Ecircumflexacute",
        "Ecircumflexdotbelow",
        "Ecircumflexgrave",
        "Ecircumflexhookabove",
        "Ecircumflextilde",
        "Edieresis",
        "Edotaccent",
        "Edotbelow",
        "Egrave",
        "Ehookabove",
        "Emacron",
        "Eogonek",
        "Eopen",
        "Etilde",
        "Schwa",
        "F",
        "G",
        "Gacute",
        "Gbreve",
        "Gcaron",
        "Gcircumflex",
        "Gcommaaccent",
        "Gdotaccent",
        "H",
        "Hbar",
        "Hcircumflex",
        "I",
        "IJ",
        "IJ_acute",
        "Iacute",
        "Ibreve",
        "Icircumflex",
        "Idieresis",
        "Idotaccent",
        "Idotbelow",
        "Igrave",
        "Ihookabove",
        "Imacron",
        "Iogonek",
        "Itilde",
        "J",
        "Jcircumflex",
        "K",
        "Kcommaaccent",
        "L",
        "Lacute",
        "Lcaron",
        "Lcommaaccent",
        "Ldot",
        "Lslash",
        "M",
        "N",
        "Nacute",
        "Ncaron",
        "Ncommaaccent",
        "Ntilde",
        "Eng",
        "O",
        "Oacute",
        "Obreve",
        "Ocircumflex",
        "Ocircumflexacute",
        "Ocircumflexdotbelow",
        "Ocircumflexgrave",
        "Ocircumflexhookabove",
        "Ocircumflextilde",
        "Odieresis",
        "Odotbelow",
        "Ograve",
        "Ohookabove",
        "Ohorn",
        "Ohornacute",
        "Ohorndotbelow",
        "Ohorngrave",
        "Ohornhookabove",
        "Ohorntilde",
        "Ohungarumlaut",
        "Omacron",
        "Oogonek",
        "Oslash",
        "Oslashacute",
        "Otilde",
        "OE",
        "P",
        "Thorn",
        "Q",
        "R",
        "Racute",
        "Rcaron",
        "Rcommaaccent",
        "S",
        "Sacute",
        "Scaron",
        "Scedilla",
        "Scircumflex",
        "Scommaaccent",
        "Germandbls",
        "T",
        "Tbar",
        "Tcaron",
        "Tcedilla",
        "Tcommaaccent",
        "U",
        "Uacute",
        "Ubreve",
        "Ucircumflex",
        "Udieresis",
        "Udotbelow",
        "Ugrave",
        "Uhookabove",
        "Uhorn",
        "Uhornacute",
        "Uhorndotbelow",
        "Uhorngrave",
        "Uhornhookabove",
        "Uhorntilde",
        "Uhungarumlaut",
        "Umacron",
        "Uogonek",
        "Uring",
        "Utilde",
        "V",
        "W",
        "Wacute",
        "Wcircumflex",
        "Wdieresis",
        "Wgrave",
        "X",
        "Y",
        "Yacute",
        "Ycircumflex",
        "Ydieresis",
        "Ydotbelow",
        "Ygrave",
        "Yhookabove",
        "Ymacron",
        "Ytilde",
        "Z",
        "Zacute",
        "Zcaron",
        "Zdotaccent",
        "A-cy",
        "Be-cy",
        "Ve-cy",
        "Ge-cy",
        "Gje-cy",
        "Gheupturn-cy",
        "Ghestroke-cy",
        "De-cy",
        "Ie-cy",
        "Io-cy",
        "Zhe-cy",
        "Ze-cy",
        "Ii-cy",
        "Iishort-cy",
        "Ka-cy",
        "Kje-cy",
        "El-cy",
        "Em-cy",
        "En-cy",
        "O-cy",
        "Pe-cy",
        "Er-cy",
        "Es-cy",
        "Te-cy",
        "U-cy",
        "Ushort-cy",
        "Ef-cy",
        "Ha-cy",
        "Che-cy",
        "Tse-cy",
        "Sha-cy",
        "Shcha-cy",
        "Dzhe-cy",
        "Softsign-cy",
        "Yeru-cy",
        "Hardsign-cy",
        "Lje-cy",
        "Nje-cy",
        "Dze-cy",
        "E-cy",
        "Ereversed-cy",
        "I-cy",
        "Yi-cy",
        "Je-cy",
        "Tshe-cy",
        "Iu-cy",
        "Ia-cy",
        "Dje-cy",
        "Kadescender-cy",
        "Endescender-cy",
        "Ustraight-cy",
        "Ustraightstroke-cy",
        "Chedescender-cy",
        "Shha-cy",
        "Schwa-cy",
        "Zhedieresis-cy",
        "Zedieresis-cy",
        "Idieresis-cy",
        "Odieresis-cy",
        "Obarred-cy",
        "Chedieresis-cy",
        "Alpha",
        "Beta",
        "Gamma",
        "Delta",
        "Epsilon",
        "Zeta",
        "Eta",
        "Theta",
        "Iota",
        "Kappa",
        "Lambda",
        "Mu",
        "Nu",
        "Xi",
        "Omicron",
        "Pi",
        "Rho",
        "Sigma",
        "Tau",
        "Upsilon",
        "Phi",
        "Chi",
        "Psi",
        "Omega",
        "Alphatonos",
        "Epsilontonos",
        "Etatonos",
        "Iotatonos",
        "Omicrontonos",
        "Upsilontonos",
        "Omegatonos",
        "Iotadieresis",
        "Upsilondieresis",
        "KaiSymbol",
    ],
)


def get_base_class_list():
    return [
        cls_zero,
        cls_one,
        cls_digit,
        cls_comma,
        cls_question,
        cls_uppercase,
        cls_normal_separator,
        cls_space,
    ]
