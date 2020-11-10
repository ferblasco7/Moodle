# -*- coding: utf-8 -*-

"""
Created on Nov 2020

Crea variantes a partir de una pregunta tipo. 
Pensada para usar junto con el paquete moodle de LaTeX, para crear cuestionarios.

@author: fer
"""

#No ponemos la primera línea porque el \begin da problemas (\b es un carácter especial en python)

variedad1='''Escribe ${0}^{{{1}/{2}}}$ en forma de raíz. 
\item* $\sqrt[{2}]{{{0}^{1}}}$
\item $\sqrt[{1}]{{{0}^{2}}}$
\item $\sqrt{{{0}^{{{1}/{2}}}}}$
\item Nada de lo anterior
\end{{multi}}''' 

output=[]

for uno in range(2,10):
    for dos in range(uno+1,10):
        for tres in range(dos+1,10):
            output.append(variedad1.format(uno, dos, tres) + '\n\n')
            print(r'\begin{multi}[points=1]{Potencias}') #Hay que imprimirla "en crudo"
            print(variedad1.format(uno, dos, tres) + '\n\n')

          
