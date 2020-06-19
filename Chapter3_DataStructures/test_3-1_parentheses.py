# A common problem for compilers and text editors is determining whether the
# parentheses in a string are balanced and properly nested. For example, the string
# ((())())() contains properly nested pairs of parentheses, which the strings )()( and
# ()) do not. 
# 
# Give an algorithm that returns true if a string contains properly nested
# and balanced parentheses, and false if otherwise. 
# 
# For full credit, identify the position
# of the first offending parenthesis if the string is not properly nested and balanced.

def isBalanced(s: str):
    stk = []
    for p in s:
        if len(stk) == 0 and p == ')':
            return False
        if p == '(':
            stk.append('(')
        if p == ')':
            stk.pop()
    if len(stk) == 0:
        return True
    return False


ex = '((())())()'
bad_ex = ')()('
bad_ex_2 = '())'
bad_ex_3 = '(()'

def test_ex():
    assert isBalanced(ex) == True

def test_bad_ex():
    assert isBalanced(bad_ex) == False

def test_bad_ex_2():
    assert isBalanced(bad_ex_2) == False

def test_bad_ex_3():
    assert isBalanced(bad_ex_3) == False

# WIP
def isBalancedReturnOffendingIndex(s: str):
    stk = []
    for i in range(len(s)):
        if len(stk) == 0 and s[i] == ')':
            return i 
        if s[i] == '(':
            stk.append(i)
        if s[i] == ')':
            stk.pop()
    if len(stk) == 0:
        return True 
    return stk[0]


def test_exi():
    assert isBalancedReturnOffendingIndex(ex) == True

def test_bad_exi():
    assert isBalancedReturnOffendingIndex(bad_ex) == 0

def test_bad_ex_2i():
    assert isBalancedReturnOffendingIndex(bad_ex_2) == 2

def test_bad_ex_3i():
    assert isBalancedReturnOffendingIndex(bad_ex_3) == 0

more_interesting = '()(())(((()()))'

def test_more_int():
    assert isBalancedReturnOffendingIndex(more_interesting) == 6