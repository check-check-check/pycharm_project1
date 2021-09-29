# @Time    : 
# @Author  : chen
"""通过该案例，你将学习到：
1、在数据结构上完成基本的Python排序
2、区分sorted()和.sort()函数
3、基于特定的要求在编码中自定义一个复杂的排序
"""
"""
sorted()函数四种重要的特性：
1.sorted()函数不需要定义。它是一个内置函数，可以在标准的Python安装中使用。
2.在没有额外的参数的情况下，sorted()函数按照升序对值进行排列，也就是按照从小到大的顺序。
3.原始的numbers不会改变，因为sorted()函数提供了一个新的有序的输出结果，并且不改变原始值的顺序。
4.当sorted()函数被调用时，它会提供一个有序的列表作为返回值。
"""
#%% 1.对数值进行排序
nums = [6,9,3,1]
print(sorted(nums), nums)
# 元组和集合同样可以使用sorted()函数
#%% 2.对字符串进行排序
"""sorted()函数将一个str看作一个列表，并遍历其中的每一个元素。在一个str中，每一个元素都对应着str中
的一个字符。sorted()函数以相同的方式对待每一个句子，它会对每个字符包括空格进行排序。"""
string_number_sort = '29758271'
string_sort = 'I Love Python 1 4 2 9 1 !'
print(sorted(string_number_sort))
print(sorted(string_sort))
print(sorted(string_sort.split()))
