from typing import Optional,Callable
num:int=3
string:str="hello"
print(num,string)

#type hint
def concat(a:int,b:str) -> Optional[str]:
    resultant_str=str(a)+b
    if(len(resultant_str)<10): return resultant_str
print(concat(num,string))
print(concat(10,"String and Number"))

#mutables
def mutableParams(lst: list[int], func: Callable[[int,str],Optional[str]]):
    lst.append(44)
    lst.append(20)
    #callable
    print("Callable with typehints:")
    print(func(10,"Hello"))
lst=[10]
mutableParams(lst,concat)
print(lst)

def multiply(*args):
    print(args)
    sum=0
    for n in args:
        sum = sum+n
    print(sum)
multiply(1,3,8,5)

def display(**kwargs):
    print(kwargs["name"],kwargs["age"])
display(name="ragul",age=20)

'''Function calls
with different parameters and types'''





