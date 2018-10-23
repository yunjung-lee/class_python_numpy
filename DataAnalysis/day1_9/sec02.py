"""
딕셔너리 : 키 벨류의 쌍

"""

d={'a':[1,2,3], "b":"kim", "c":'123'}
print(d)
d['b']='lee'
print(d['c'])
print(d.keys())
print(d.values())
print(d.items())
print(d['b'])
print(d.get('b'))

x={}
print(x)
x=dict()
print(x)
x1=dict(a=10,b=20)
print(x1)
x2=dict(zip(['a','b'],[10,20]))
print(x2)

x3=dict(zip(range(1,11),[2**i for i in range (1,11)]))
print(x3)
print(len(x3))
"""
딕셔너리 내부에 또 딕셔너리가 있는 구조(딕셔너리의 중첩)
{키1:{키a:밸류,키b:밸류},키2:{키aa:밸류,키bb:밸류}}
"""
test = {'gildong':{'W':70 , 'H':170, 'b':'a'},
        'donggil': {'W': 75, 'H': 160, 'b': 'ab'},
        'gildo': {'W': 72, 'H': 150, 'b': 'o'},
        }
print(test)
print(test['gildong'])
print(test['gildong']['H'])

test['gildong']['H'] +=10
#x+=10 <=>x=x+10

print("="*100)
print(test['gildong'])
print("="*100)

test['gildong']['H']=200
print(test['gildong'])


