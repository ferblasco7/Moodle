# -*- coding: utf-8 -*-

"""
Created on Wed Feb 12 17:49:09 2020

@author: fer
"""

variedad1='''\begin{{multi}}[points=1]{{Potencias}}
Escribe ${0}^{{{1}/{2}}}$ en forma de raíz. 
\item* $\sqrt[{2}]{{{0}^{1}}}$
\item $\sqrt[{1}]{{{0}^{2}}}$
\item $\sqrt{{{0}^{{{1}/{2}}}}}$
\item Nada de lo anterior
\end{{multi}}'''

output=''

for uno in range(1,10):
    for dos in range(uno+1,10):
        for tres in range(dos+1,10):
            output = output + variedad1.format(uno, dos, tres) + '\n\n'

            
