Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tupla=(3,4)
>>> tupla
(3, 4)
>>> type(tupla)
<class 'tuple'>
>>> tupla=(1, "hola")
>>> tupla [1]
'hola'
>>> A=(1,2)
>>> B=(5,10)
>>> A+B
(1, 2, 5, 10)
>>> C=A+B
>>> C
(1, 2, 5, 10)
>>> C.count(0)
0
>>> D=(2,10)
>>> C=C+D
>>> C
(1, 2, 5, 10, 2, 10)
>>> C.count(2)
2
>>> C.count(1)
1
>>> C=C+(2,4,'1')
>>> C
(1, 2, 5, 10, 2, 10, 2, 4, '1')
>>> C.count('1')
1
>>> C.count(2)
3
>>> C
(1, 2, 5, 10, 2, 10, 2, 4, '1')
>>> C.index('1')
8
>>> 
>>> 
>>> C
(1, 2, 5, 10, 2, 10, 2, 4, '1')
>>> C.index(5,10)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    C.index(5,10)
ValueError: tuple.index(x): x not in tuple
>>> C.index(5, 3)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    C.index(5, 3)
ValueError: tuple.index(x): x not in tuple
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> 
>>> help>list
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    help>list
TypeError: '>' not supported between instances of '_Helper' and 'type'
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lista=[]
>>> lista=list()
>>> lista
[]
>>> lista=[1,5,[2,4]]
>>> lsita
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    lsita
NameError: name 'lsita' is not defined
>>> lista
[1, 5, [2, 4]]
>>> lista[0]
1
>>> lista[2][1]
4
>>> lista=[82,5), True]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> lista=[(2,5), True]
>>> lista[0][1]
5
>>> #Busqueda anidada
>>> lista.append(3)
>>> lsita
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    lsita
NameError: name 'lsita' is not defined
>>> lista
[(2, 5), True, 3]
>>> lista.append([3,4,5])
>>> lista
[(2, 5), True, 3, [3, 4, 5]]
>>> len(lista)
4
>>> lista.extend([3,5])
>>> lista
[(2, 5), True, 3, [3, 4, 5], 3, 5]
>>> A=[1,3]
>>> B=[56,100]
>>> A+B
[1, 3, 56, 100]
>>> A.extend(B)
>>> A
[1, 3, 56, 100]
>>> A.remove(1)
>>> A
[3, 56, 100]
>>> A=A+[34]
>>> A+=[34]
>>> A
[3, 56, 100, 34, 34]
>>> A+=[56]
>>> A
[3, 56, 100, 34, 34, 56]
>>> A+=['dos', True]
>>> A
[3, 56, 100, 34, 34, 56, 'dos', True]
>>> A.append([34,78])
>>> A
[3, 56, 100, 34, 34, 56, 'dos', True, [34, 78]]
>>> A.extendo([0,1])
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    A.extendo([0,1])
AttributeError: 'list' object has no attribute 'extendo'
>>> A
[3, 56, 100, 34, 34, 56, 'dos', True, [34, 78]]
>>> A.extend([0,1])
>>> A
[3, 56, 100, 34, 34, 56, 'dos', True, [34, 78], 0, 1]
>>> len(A)
11
>>> A[10]
1
>>> A.pop(9)
0
>>> A
[3, 56, 100, 34, 34, 56, 'dos', True, [34, 78], 1]
>>> A
[3, 56, 100, 34, 34, 56, 'dos', True, [34, 78], 1]
>>> A.insert(1,'hola')
>>> A
[3, 'hola', 56, 100, 34, 34, 56, 'dos', True, [34, 78], 1]
>>> A.clear()
>>> A
[]
>>> A=[56,3,4]
>>> A
[56, 3, 4]
>>> A.extend([3,4,5,6])
>>> A
[56, 3, 4, 3, 4, 5, 6]
>>> A[1:-1]
[3, 4, 3, 4, 5]
>>> 
>>> 



>>> 
>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> D=[]
>>> D=()
>>> D=dict()
>>> type(D)
<class 'dict'>
>>> D={'Nombre':'Aleja','edad':28}
>>> D
{'Nombre': 'Aleja', 'edad': 28}
>>> D['NOMBRE']
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    D['NOMBRE']
KeyError: 'NOMBRE'
>>> D['Nombre']
'Aleja'
>>> usuarios=dict()
>>> type(usuarios)
<class 'dict'>
>>> usuarios[1]={'name':"juan", 'edad':21}
>>> usuarios[2]={'name':"Ana", 'edad':98}
>>> usuarios
{1: {'name': 'juan', 'edad': 21}, 2: {'name': 'Ana', 'edad': 98}}
>>> usuarios[1]['name']
'juan'
>>> 'juan'
'juan'
>>> 4 in usuarios
False
>>> A=[2,3]
>>> 2 in A
True
>>> if 4 in usuarios:
	print(usuarios[4])

	
>>> if 1 in usuarios:
	print("El nombre es %s" "%(usuarios[1]))
	      
SyntaxError: EOL while scanning string literal
>>> 
>>> if 1 in usuarios:
	print("El nombre es %s "%(usuarios[1]))

	
El nombre es {'name': 'juan', 'edad': 21} 
>>> 
>>> if 1 in usuarios:
	print("El nombre es %s "%(usuarios[1]['name']))

	
El nombre es juan 
>>>  