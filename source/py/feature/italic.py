import source.py.feature.ast as ast
from source.py.feature.calt import get_calt
from source.py.feature.cv import (
    cv01,
    cv04,
    cv31,
    cv32,
    cv33,
    cv34,
    cv35,
    cv36,
    cv37,
    cv38,
    cv39,
    cv40,
    cv41,
    cv61,
    cv62,
    cv63,
)
from source.py.feature.ss import (
    ss01,
    ss02,
    ss03,
    ss04,
    ss05,
    ss06,
    ss07,
    ss08,
    ss09,
    ss10,
    ss11,
)
from source.py.feature.base.clazz import get_base_class_list, cls_digit


cls_a = ast.Clazz("A", ["A", "a", "a.cv31"])
cls_b = ast.Clazz("B", ["B", "b"])
cls_c = ast.Clazz("C", ["C", "c"])
cls_d = ast.Clazz("D", ["D", "d"])
cls_e = ast.Clazz("E", ["E", "e"])
cls_f = ast.Clazz("F", ["F", "f", "f.cv32"])
cls_g = ast.Clazz("G", ["G", "g", "g.cv38"])
cls_h = ast.Clazz("H", ["H", "h"])
cls_i = ast.Clazz("I", ["I", "i", "i.cv33", "i.cv39"])
cls_j = ast.Clazz("J", ["J", "j", "j.cv33", "J.cv40"])
cls_k = ast.Clazz("K", ["K", "k", "k.cv34"])
cls_l = ast.Clazz("L", ["L", "l", "l.cv35"])
cls_m = ast.Clazz("M", ["M", "m"])
cls_n = ast.Clazz("N", ["N", "n"])
cls_o = ast.Clazz("O", ["O", "o"])
cls_p = ast.Clazz("P", ["P", "p"])
cls_q = ast.Clazz("Q", ["Q", "q", "Q.cv01"])
cls_r = ast.Clazz("R", ["R", "r"])
cls_s = ast.Clazz("S", ["S", "s"])
cls_t = ast.Clazz("T", ["T", "t"])
cls_u = ast.Clazz("U", ["U", "u"])
cls_v = ast.Clazz("V", ["V", "v"])
cls_w = ast.Clazz("W", ["W", "w"])
cls_x = ast.Clazz("X", ["X", "x", "x.cv36"])
cls_y = ast.Clazz("Y", ["Y", "y", "y.cv37"])
cls_z = ast.Clazz("Z", ["Z", "z"])
a_l = ast.Clazz(
    "AL",
    [
        ast.gly("al"),
        ast.gly("al", ".cv31"),
        ast.gly("al", ".cv35"),
        ast.gly("al", ".cv31.cv35"),
        ast.gly("al", ".cv04"),
        ast.gly("al", ".cv04.cv31"),
        ast.gly("al", ".ss06"),
    ],
)

cls_letters_list = [
    cls_a,
    cls_b,
    cls_c,
    cls_d,
    cls_e,
    cls_f,
    cls_g,
    cls_h,
    cls_i,
    cls_j,
    cls_k,
    cls_l,
    cls_m,
    cls_n,
    cls_o,
    cls_p,
    cls_q,
    cls_r,
    cls_s,
    cls_t,
    cls_u,
    cls_v,
    cls_w,
    cls_x,
    cls_y,
    cls_z,
]

cls_var = ast.Clazz("Var", ["_", "__", *cls_letters_list, cls_digit])
cls_hex_letter = ast.Clazz("HexLetter", [cls_a, cls_b, cls_c, cls_d, cls_e, cls_f])

class_list_italic = [
    *get_base_class_list(),
    *cls_letters_list,
    a_l,
    cls_var,
    cls_hex_letter,
]


calt_italic = get_calt(cls_var, cls_hex_letter, is_italic=True)

cv_list_italic = [
    cv01.cv01_feat_italic,
    cv04.cv04_feat_italic,
    cv31.cv31_feat_italic,
    cv32.cv32_feat_italic,
    cv33.cv33_feat_italic,
    cv34.cv34_feat_italic,
    cv35.cv35_feat_italic,
    cv36.cv36_feat_italic,
    cv37.cv37_feat_italic,
    cv38.cv38_feat_italic,
    cv39.cv39_feat_italic,
    cv40.cv40_feat_italic,
    cv41.cv41_feat_italic,
    cv61.cv61_feat_italic,
    cv62.cv62_feat_italic,
    cv63.cv63_feat_italic,
]

ss_list_italic = [
    ss01.ss01_feat,
    ss02.ss02_feat,
    ss03.ss03_feat,
    ss04.ss04_feat,
    ss05.ss05_feat,
    ss06.ss06_feat,
    ss07.ss07_feat,
    ss08.ss08_feat,
    ss09.ss09_feat,
    ss10.ss10_feat,
    ss11.ss11_feat,
]
