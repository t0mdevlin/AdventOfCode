from parsimonious.grammar import Grammar, NodeVisitor
from parsimonious.exceptions import ParseError, IncompleteParseError, VisitationError

grammar = Grammar(r"""
    EXPR  = ITEM+
    ITEM  = (BYR / IYR / EYR / HGT / HCL / ECL / PID / CID) WHITE?
    WHITE =  ~r"[\s]+"

    BYR   = "byr:" NUMB
    IYR   = "iyr:" NUMB
    EYR   = "eyr:" NUMB
    HGT   = "hgt:" (HGTCM / HGTIN)
    HCL   = "hcl:" ~r"#[0-9a-f]{6}"
    ECL   = "ecl:" ("amb" / "blu" / "brn" / "gry" / "grn" / "hzl" / "oth") 
    PID   = "pid:" ~r"[0-9]{9}"
    CID   = "cid:" ~r"[0-9a-zA-Z]*"

    HGTCM = NUMB "cm"
    HGTIN = NUMB "in"

    NUMB  = ~r"[0-9]{2,4}"
""")

class PassportVisitor(NodeVisitor):
    def visit_EXPR(self, node, visited_children):
        assert not {"BYR", "IYR", "EYR", "HGT", "HCL", "ECL", "PID"}.difference(visited_children)

    def visit_ITEM(self, node, visited_children):
        return node.children[0].children[0].expr_name

    def visit_BYR(self, node, visited_children):
        assert 1920 <= visited_children[1] <= 2002

    def visit_IYR(self, node, visited_children):
        assert 2010 <= visited_children[1] <= 2020

    def visit_EYR(self, node, visited_children):
        assert 2020 <= visited_children[1] <= 2030

    def visit_HGTCM(self, node, visited_children):
        assert 150 <= visited_children[0] <= 193

    def visit_HGTIN(self, node, visited_children):
        assert 59 <= visited_children[0] <= 76

    def visit_NUMB(self, node, visited_children):
        return int(node.text)

    def generic_visit(self, node, visited_children):
        return visited_children or node

pv = PassportVisitor()
pv.grammar = grammar

data = open("passport").read().split("\n\n")
valid = 0
for entry in data:
    try:
        pv.parse(entry)
    except (ParseError, VisitationError, IncompleteParseError):
        continue
    else:
        valid += 1
print("Valid:", valid)