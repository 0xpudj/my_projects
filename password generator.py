import random as r
import termcolor as t
from math import log

name = input("Name: ").capitalize()

first = ['8124', '29635', 'SDFS', '1CVXV', 'RTUY', 'NVMs', 'lVkVBC', 'baDGs', 'tDFIOn', 'VEW', '@#$', 'wVER', '//JK', 'NFDB', 'AXGR', 'lIYOPU', 'IO.L', 'rZXVAF', 'kSDS', 'UNF356', 'destroys', 'cuts']
second = ['your', 'our', 'racist', 'h345@!', 'ma%9078', 'green', 'gi(&@#^)', 'al(&*%^)', 'thr*&%@#', 'fi(&%(&))', 'hu&*%^ndred', 'ug^&%$ly', 'my%$', 'bl&*(^ck', 'ni%^ce', 'smal*@#&l', 'ho@@r%', 'l&*!@#%e', 'ten', 'loverboy', 'wwe', 'password', 'super']
third = ['23423R', 'DGH|234', '1asdf@$$', 'bJ;F82934', 'SDFG#!@#$', '$!#qwf', '567#%@%|', '2SDFE45','s2346VC', '3C4W4', 'a357B5E7', 'comSDT4W', 'maYOLY', 'diB8T6', 'pXQ3', 'QWZX5#', 'pussies', 'aliens', 'hackers', 'brother',]

separators = ['-', '.', '*', '+', '~', '_', '/', '\\', '@']

t.cprint ('')
t.cprint (' +------------------------------------+---------------------+', 'green')
t.cprint (' | Passwords                          | Entropy             |', 'green')
t.cprint (' +------------------------------------+---------------------+', 'green')
t.cprint (' +--------------------------+-------------------------------+', 'green')
for i in range(0, 15):
    generated_password = name + r.choice(separators) + r.choice(first) + r.choice(separators) + r.choice(second) + r.choice(separators) + r.choice(third)
    t.cprint(' | %-35s| %-20s|' % (generated_password, (log(82)/log(2)) * len(generated_password)), 'green')
t.cprint (' +--------------------------+-------------------------------+', 'green')
