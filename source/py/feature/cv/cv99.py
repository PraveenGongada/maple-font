import source.py.feature.ast as ast
from source.py.feature.base.locl import lookup_tw


def cv99_subst():
    return [lookup_tw.use()]


cv99_name = "Traditional centered punctuations"
cv99_feat_cn = ast.CharacterVariant(
    id=99, desc=cv99_name, content=cv99_subst(), version="7.0", example="，。"
)
