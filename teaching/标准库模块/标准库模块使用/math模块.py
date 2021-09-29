# @Time    : 
# @Author  : chen
# math库—数学函数 作用：提供函数完成特殊的数学运算。

#%% 特殊常量：很多数学运算依赖于一些特殊的常量。math 包含有 π（pi）和 e 的值
import math
print('π: %.30f' % math.pi)
print('e: %.30f' % math.e)
#%% 测试异常值：浮点数计算可能导致两种类型的异常值。第一种是 INF（无穷大），
# 如果用 double 存储一个浮点数值，而它相对于一个很大绝对的值溢出时，就会出现这个异常值。
import math
print('{:^3}  {:6}  {:6}  {:6}'.format('e', 'x', 'x**2', 'isinf'))
print('{:-^3}  {:-^6}  {:+^6}  {:+^6}'.format('', '', '', '')) # ^表示内容居中，6表示输出宽度约束为6个字符
for e in range(0, 201, 20):
    x = 10.0 ** e
    y = x * x
    print('{:3d}  {!s:6}  {!s:6}  {!s:6}'.format(e, x, y, math.isinf(y), ))# 3d 表示3个宽度的10进制数显示
"""这个例子中的指数变得足够大时，x 的平方无法再存放在一个 double 中，这个值就会记录为无穷大。
不过，并不是所有浮点数溢出都会导致 INF 值。具体地，用浮点数值计算一个指数时，会生成 OverflowError 
而不是保留 INF 结果。"""
#%%
x = 10.0 ** 200
print('x    =', x)
print('x*x  =', x * x)
try:
    print('x**2 =', x ** 2)
except OverflowError as err:
    print(err)

#%%使用无穷大值的除法运算未定义。将一个数除以无穷大值的结果是 NaN（即不是一个数）
import math
x = (10.0 ** 200) * (10.0 ** 200)
y = x / x
print('x =', x)
print('isnan(x) =', math.isnan(x))
print('y = x / x =', x / x)
print('y == nan =', y == float('nan'))
print('isnan(y) =', math.isnan(y))
# math 模块包括 3 个函数用于将浮点
# NaN 不会等于任何值，甚至不等于其自身，所以要想检查 NaN，需要使用 isnan()。
#%% 数值转换为整数。
# math 模块包括 3 个函数用于将浮点数值转换为整数。这 3 个函数分别采用不同的方法，并适用于不同的场合。
"""最简单的是 trunc()，这会截断小数点后的数字，只留下构成这个值整数部分的有效数字。floor() 将其输入
转换为不大于它的最大整数，ceil()（上限）会生成按序列排在这个输入值之后的最小整数。"""
import math
HEADINGS = ('i', 'int', 'trunk', 'floor', 'ceil')
print('{:^5}  {:^5}  {:^5}  {:^5}  {:^5}'.format(*HEADINGS))
print('{:-^5}  {:-^5}  {:-^5}  {:-^5}  {:-^5}'.format('', '', '', '', '', ))
fmt = '  '.join(['{:5.1f}'] * 5)

TEST_VALUES = [-1.5, -0.8, -0.5, -0.2, 0, 0.2, 0.5, 0.8, 1, ]
for i in TEST_VALUES:
    print(fmt.format(i, int(i), math.trunc(i), math.floor(i), math.ceil(i)))
# trunc() 等价于直接转换为 int。
#%% 其他表示：modf() 取一个浮点数，并返回一个 tuple，其中包含这个输入值的小数和整数部分。
import math
for i in range(6):
    print('{}/2 = {}'.format(i, math.modf(i / 2.0)))
# 返回值中的两个数都是浮点数。
#%% frexp() 返回一个浮点数的尾数和指数，可以用来对这个值创建一种更可移植的表示
import math
print('{:^7}  {:^7}  {:^7}'.format('x', 'm', 'e'))
print('{:-^7}  {:-^7}  {:-^7}'.format('', '', ''))
for x in [0.1, 0.5, 4.0]:
    m, e = math.frexp(x)
    print('{:7.2f}  {:7.2f}  {:7d}'.format(x, m, e))
#frexp() 使用公式 x = m * 2**e，并返回值 m 和 e。
# ldexp()与frexp()正好相反。
import math
print('{:^7}  {:^7}  {:^7}'.format('x', 'm', 'e'))
print('{:-^7}  {:-^7}  {:-^7}'.format('', '', ''))
for m, e in [(0.8, -3),
             (0.5, 0),
             (0.5, 3)
             ]:
    x = math.ldexp(m, e)
    print('{:7.2f}  {:7d}  {:7.2f}'.format(m, e, x))
# 使用与frexp()相同的公式，ldexp()取尾数和指数值作为参数，将返回一个浮点数。
#%%正号和负号:一个数的绝对值就是不带正负号的本值。使用 fabs() 可以计算一个浮点数的绝对值。
import math
print(math.fabs(-1.1))
print(math.fabs(-0.0))
print(math.fabs(0.0))
print(math.fabs(1.1))
#%%确定一个值的符号，比如为一组值给定相同的符号或者要比较两个值，可以使用 copysign() 来设置正确值的符号。
import math
HEADINGS = ('f', 's', '< 0', '> 0', '= 0')
print('{:^5}  {:^5}  {:^5}  {:^5}  {:^5}'.format(*HEADINGS))
print('{:-^5}  {:-^5}  {:-^5}  {:-^5}  {:-^5}'.format('', '', '', '', '', ))
for f in [-1.0,
          0.0,
          1.0,
          float('-inf'),
          float('inf'),
          float('-nan'),
          float('nan'),
          ]:
    s = int(math.copysign(2, f))
    print('{:5.1f}  {:5d}  {!s:5}  {!s:5}  {!s:5}'.format(
        f, s, f < 0, f > 0, f == 0,))
# %% 常用计算
"""在二进制浮点数内存中表示精确值很有难度。有些值无法准确地表示，而且一个值如果通过反复计算来处理，这样处理越
频繁就越容易引入表示错误。math 包含一个函数来计算一系列浮点数的和，它使用一种高效的算法以尽量减少这种错误"""
import math
values = [0.1] * 10
print('Input values:', values)
print('sum()       : {:.20f}'.format(sum(values)))
s = 0.0
for i in values:
    s += i
print('for-loop    : {:.20f}'.format(s))
print('math.fsum() : {:.20f}'.format(math.fsum(values))) #求和
"""给定一个包含 10 个值的序列，每个值都等于 0.1，这个序列的总和期望值为 1.0。不过，由于 0.1 不能精确地表示为一个浮点值，
所以会在总和中引入错误，除非用 fsum() 来计算。"""
#%%  factorial() 常用于计算一系列对象的排列和组合数。一个正整数 n 的阶乘（表示为 n!）递归地定义为 (n-1)!*n，并在 0!==1 停止递归。
# factorial()只能处理整数，不过它确实接受float参数，只要这个参数可以转换为一个整数而不会丢值
import math
for i in [0, 9.0, 2.0, 3.1, 4.0, 5.0, 6.0]:
    try:
        print('{:2.0f}  {:6.0f}'.format(i, math.factorial(i)))
    except ValueError as err:
        print('Error computing factorial(%s):' % i, err)

#%%  gamma() 类似于 factorial()，不过它可以处理实数，而且值会下移一个数（gamma 等于 (n-1)!）。
import math
for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]: #由于 0 会导致开始值为负，这是不允许的。
    try:
        print('{:2.1f}  {:6.2f}'.format(i, math.gamma(i)))
    except ValueError as err:
        print('Error computing gamma(%s):' % i, err)
# %% lgamma() 返回的结果是对输入值求 gamma 所得绝对值的自然对数。
import math
for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
    try:
        print('{:2.1f}  {:.20f}  {:.20f}'.format(i, math.lgamma(i), math.log(math.gamma(i))))
    except ValueError as err:
        print('Error computing lgamma(%s):' % i, err)
# 使用 lgamma() 会比使用 gamma() 的结果单独计算对数更精确。
#%% 求模操作符 (%)
"""求模操作符 (%) 会计算一个除法表达式的余数（例如，5%2=1）。Python 语言内置的这个操作符可以很好地处理整数，但是与很多
其他浮点数运算类似，中间计算可能导致表示问题，进一步造成数据丢失。fmod() 可以为浮点值提供一个更精确的实现。"""
import math
print('{:^4}  {:^4}  {:^5}  {:^5}'.format('x', 'y', '%', 'fmod'))
print('----  ----  -----  -----')
for x, y in [(5, 2), (5, -2), (-5, 2),]:
    print('{:4.1f}  {:4.1f}  {:5.2f}  {:5.2f}'.format(x, y, x % y, math.fmod(x, y),))
# 还有一点很可能经常产生混淆，fmod() 计算模所使用的算法与 % 使用的算法也有所不同，所以结果的符号不同?

# %% 指数和对数:指数生长曲线在经济学、物理学和其他科学中经常出现。Python 有一个内置的幂运算符（**），不过如果需要将一个可调用函数作为另一个的参数，可能需要用到 pow()。
import math
for x, y in [
    # Typical uses
    (2, 3),
    (2.1, 3.2),

    # Always 1
    (1.0, 5),
    (2.0, 0),

    # Not-a-number
    (2, float('nan')),

    # Roots
    (9.0, 0.5),
    (27.0, 1.0 / 3),]:

    print('{:5.1f} ** {:5.3f} = {:6.3f}'.format(
        x,
        y,
        math.pow(x, y),
    ))
"""1 的任何次幂总返回 1.0，同样的，任何值的指数为 0.0 时也总是返回 1.0。对于“不是一个数”值 nan，大多数运算都返回 nan。
如果指数小于 1，pow() 会计算一个根。由于平方根（指数为 1/2）使用非常频繁，所以有一个单独的函数来计算平方根。"""

import math

print(math.sqrt(9.0))
print(math.sqrt(3))
try:
    print(math.sqrt(-1))
except ValueError as err:
    print('Cannot compute sqrt(-1):', err)
# 计算负数的平方根需要用到复数，这不在 math 的处理范围内。试图计算一个负值的平方根时，会导致一个 ValueError。

#%% 对数函数math.log
"""对数函数查找满足条件 x = b ** y 的 y。默认情况下，log() 计算自然对数（底数为 e）。如果提供了第二个参数，
则使用这个参数值作为底数。"""
import math
print(math.log(math.e))
print(math.log(8, 2))
print(math.log(0.5, 2))
#%%log10() 完成 log(x, 10) 计算，但是会使用一种比 log() 更精确的算法。
import math
print('{:2}  {:^12}  {:^10}  {:^20}  {:8}'.format(
    'i', 'x', 'accurate', 'inaccurate', 'mismatch',))
print('{:-^2}  {:-^12}  {:-^10}  {:-^20}  {:-^8}'.format(
    '', '', '', '', '',))
for i in range(0, 10):
    x = math.pow(10, i)
    accurate = math.log10(x)
    inaccurate = math.log(x, 10)
    match = '' if int(inaccurate) == i else '*'
    print('{:2d}  {:12.1f}  {:10.8f}  {:20.18f}  {:^5}'.format(
        i, x, accurate, inaccurate, match,))

# %% loglp() 会计算 Newton-Mercator 序列（1+x 的自然对数）。
import math
x = 0.0000000000000000000000001
print('x       :', x)
print('1 + x   :', 1 + x)
print('log(1+x):', math.log(1 + x))
print('loglp(x):', math.log1p(x))
#%%
"""对于非常接近于 0 的 x，loglp() 会更为精确，因为它使用的算法可以补偿由初始加法带来的取整错误。
exp() 会计算指数函数（e**x）。"""

import math
x = 2
fmt = '%.20f'
print(fmt % (math.e ** 2))
print(fmt % math.pow(math.e, 2))
print(fmt % math.exp(2))
"""与其他特殊情况函数类似，exp() 使用的算法可以生成比与之等价的通用函数 math.pow(math.e, x) 更为精确的结果。
expml() 与 loglp() 正相反，会计算 e**x - 1。"""
#%% 与其他特殊情况函数类似，exp() 使用的算法可以生成比与之等价的通用函数 math.pow(math.e, x) 更为精确的结果。
# expml() 与 loglp() 正相反，会计算 e**x - 1。
import math
x = 0.0000000000000000000000001
print(x)
print(math.exp(x) - 1)
print(math.expm1(x))
# 类似于loglp()，x值很小时，如果单独完成减法会损失精度
#%% 角度和弧度
import math
print('{:^7}  {:^7}  {:^7}'.format('Degrees', 'Radians', 'Expected'))
print('{:^7}  {:^7}  {:^7}'.format('', '', ''))
for deg, expected in [(0, 0),
                      (30, math.pi / 6),
                      (45, math.pi / 4),
                      (60, math.pi / 3),
                      (90, math.pi / 2),
                      (180, math.pi),
                      (270, 3 / 2.0 * math.pi),
                      (360, 2 * math.pi),
                      ]:
    print('{:7d}  {:7.2f}  {:7.2f}'.format(deg, math.radians(deg), expected,))
# %% 转换公式为 rad = deg * π / 180.要从弧度转换为度，可以使用 degrees()。
import math
print('{:^8}  {:^8}  {:^8}'.format('Radians', 'Degrees', 'Expected'))
print('{:-^8}  {:-^8}  {:-^8}'.format('', '', ''))
for rad, expected in [(0, 0),
                      (math.pi / 6, 30),
                      (math.pi / 4, 45),
                      (math.pi / 3, 60),
                      (math.pi / 2, 90),
                      (math.pi, 180),
                      (3 * math.pi / 2, 270),
                      (2 * math.pi, 360),
                      ]:
    print('{:8.2f}  {:8.2f}  {:8.2f}'.format(rad,
                                       math.degrees(rad),
                                       expected,
                                       ))
#%% 三角函数
import math
print('Degrees  Radians  Sine     Cosine    Tangent')
print('-------  -------  -------  --------  -------')
fmt = '   '.join(['%7.2f'] * 5)
for deg in range(0, 361, 30):
    rad = math.radians(deg)
    if deg in (90, 270):
        t = float('inf')
    else:
        t = math.tan(rad)
    print(fmt % (deg, rad, math.sin(rad), math.cos(rad), t))
#%%
# 给定一个点(x, y)，点[(0, 0), (x, 0), (x, y)] 构成的三角形中斜边长度为 (x**2 + y**2) ** 1/2，
# 可以用 hypot() 来计算。
import math
print('{:^7}  {:^7}  {:^10}'.format('x', 'y', 'Hypotenuse'))
print('{:-^7}  {:-^7}  {:-^10}'.format('', '', ''))
for x, y in [  # simple points
    (1, 1),
    (-1, -1),
    (math.sqrt(2), math.sqrt(2)),
    (3, 4),  # 3-4-5 triangle
    # on the circle
    (math.sqrt(2) / 2, math.sqrt(2) / 2),  # pi/4 rads
    (0.5, math.sqrt(3) / 2),  # pi/3 rads
]:
    h = math.hypot(x, y)
    print('{:7.2f}  {:7.2f}  {:7.2f}'.format(x, y, h))
# 对于圆上的点，总能得到斜边 == 1。还可以用这个函数查看两个点之间的距离。
#%% 还可以用这个函数查看两个点之间的距离。
import math
print('{:^8}  {:^8}  {:^8}  {:^8}  {:^8}'.format('X1', 'Y1', 'X2', 'Y2', 'Distance',))
print('{:^8}  {:^8}  {:^8}  {:^8}  {:^8}'.format('', '', '', '', '',))
for (x1, y1), (x2, y2) in [((5, 5), (6, 6)),
                           ((-6, -6), (-5, -5)),
                           ((0, 0), (3, 4)),  # 3-4-5 truanle
                           ((-1, -1), (2, 3)),  # 3-4-5 triangle
                           ]:
    x = x1 - x2
    y = y1 - y2
    h = math.hypot(x, y)
    print('{:8.2f}  {:8.2f}  {:8.2f}  {:8.2f}  {:8.2f}'.format(x1, y1, x2, y2, h,))

#%%
import math
for r in [0, 0.5, 1]:
    print('arcsine(%.1f)    = %5.2f' % (r, math.asin(r)))
    print('arccosine(%.1f)  = %5.2f' % (r, math.acos(r)))
    print('arctangent(%.1f) = %5.2f' % (r, math.atan(r)))
#%%
import math
print('{:^6}  {:^6}  {:^6}  {:^6}'.format(
    'X', 'sinh', 'cosh', 'tanh',))
print('{:-^6}  {:-^6}  {:-^6}  {:-^6}'.format('', '', '', ''))
fmt = '   '.join(['{:6.4f}'] * 4)
for i in range(0, 11, 2):
    x = i / 10.0
    print(fmt.format(x, math.sinh(x), math.cosh(x), math.tanh(x)))
#%%
import math
print('{:^5}  {:7}'.format('x', 'erf(x)'))
print('{:-^5}  {:-^7}'.format('', ''))
for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
    print('{:5.2f}  {:7.4f}'.format(x, math.erf(x)))

#%%
import math
print('{:^5}  {:7}'.format('x', 'erfc(x)'))
print('{:-^5}  {:-^7}'.format('', ''))
for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
    print('{:5.2f}  {:7.4f}'.format(x, math.erfc(x)))
