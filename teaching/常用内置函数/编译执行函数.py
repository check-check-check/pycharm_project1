# @Time    : 
# @Author  : chen
#%% compile：将字符串编译为代码或者AST对象，使之能够通过exec语句来执行或者eval进行求值
#流程语句使用exec
code1 = 'for i in range(0,10): print (i)'
compile1 = compile(code1,'','exec')
exec(compile1)

#简单求值表达式用eval
code2 = '1 + 2 + 3 + 4'
compile2 = compile(code2,'','eval')
print(compile2)
print(eval(compile2))

#%% eval()：执行动态表达式求值
print(eval('1+2+3+4'))

#%%exec：执行动态语句块
exec('a=1+2') #执行语句
print(a)
#%%repr：返回一个对象的字符串表现形式(给解释器)
a = 'some text'
print(str(a))
print(repr(a))