# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

# teoria dos conjuntos em python

estudantes_python = {'Lucas','Sarah','Pedro','Miriam'}
estudantes_java = {'Lucas','Fabricio','Sarah',"Débora"}

"""posso fazer uma união de um ou mais conjuntos, onde esse conjunto conterá
apenas um conjunto com valores unicos"""

conjunto_união = estudantes_python.union(estudantes_java)
""" Return the union of sets as a new set.

    (i.e. all elements that are in either set.)"""
                           
print(conjunto_união)              

#É possivel gerar conjunto que estão em ambos os cursos

conunto_intersecção = set.intersection(estudantes_java,estudantes_python)
""" Return the intersection of two sets as a new set.

    (i.e. all elements that are in both sets.)"""
print(conunto_intersecção)




