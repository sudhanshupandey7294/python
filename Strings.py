"""
String:- String is a sequence of characters and its behave like a
tuple
String's method can returns new string, tuple can not

Syntax:-
st = "Aman"


st = 'aman'
st = "aman"
st = '''aman
is
a
good
boy
'''
st = """ """
st = str("Aman")
st = str('123')
st = str(123)
print(st)
print( type(st) )

String works on INDEX
    backward , forward

st = "AMANKUMAR"
print( st )
print( st[3] )
print( st[-4] )


String can be sliced
st = "AMANKUMAR"
print( st )
print( st[2:7] )


String can be Replicate
st = "AMANKUMAR"
print( st )
print( st*3 )


String can be Traversed
st = "AMANKUMAR"
print( st )
for a in st:
    print(a)


st = "AMANKUMAR"
print( st )
for a in range(len(st)):
    print(st[a]*(a+1))


Built-in functions
    sum , max , min , len
A = 65 , B = 66 ---- Z = 90
a = 97 , b = 98 ---- z = 122

st = "AmanKumar"
print( st )
print( max(st) )
print( min(st) )
print( len(st) )


String's Operations
    * , +

st = "Aman"
print(st*3)      # Replicate
print(st+"Kumar")# Concatenation


String's Methods
    upper , lower , capitalize, title , strip , lstrip , rstrip

st = "Aman Kumar"
print(st)
print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.title())
st = "     aman    "
print(st)
print( st.strip() )
print( st.lstrip() )
print( st.rstrip() )

        split , replace , join

st = "aman is a good boy"
print(st)
li = st.split()
print(li)
print( ' '.join(li) )
print(st.replace('good','bad'))


"""
