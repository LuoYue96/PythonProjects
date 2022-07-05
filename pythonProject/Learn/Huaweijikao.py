# # 题目描述：袋子中有N颗玻璃珠（N小于10000），我们通过下面的可选操作，将玻璃珠从袋子中取出，请问最少需要多少步可以将玻璃珠全部取出？
# # 规则1. 移除1颗玻璃珠
# # 规则2. 如果玻璃珠颗数可以被2整除，移除一半玻璃珠
# # 规则3. 如果玻璃珠颗数可以被3整除，移除三分之二的玻璃珠
# N = int(input())
# count= 0
# while True:
#     if N>=3 and N % 3 == 0 :
#         count+=1
#         N=int(N/3)
#     elif N >= 2 and N % 2 = = 0 :
#         count+=1
#         N=int(N/2)
#     elif N >= 1 :
#         count+=1
#         N-=1
#     else:
#         break
# print(count)
'''喊7是一个传统的聚会游戏，N个人围成一圈，按顺时针从1到N编号。编号为1的人从1开始喊数，下一个人喊的数字为上一个人的数字加1，但是当将要喊出来的数
字是7的倍数或者数字本身含有7的话，不能把这个数字直接喊出来，而是要喊"过"。假定玩这个游戏的N个人都没有失误地在正确的时机喊了"过"，当喊到数字K
时，可以统计每个人喊"过"的次数。
现给定一个长度为N的数组，存储了打乱顺序的每个人喊"过"的次数，请把它还原成正确的顺序，即数组的第i个元素存储编号i的人喊"过"的次数。'''
#输入 一个 数字数组 【0,1,0]  out  [1,0,0]
var1 = input().split()
num = len(var1)
count = 0
count2=0
pp = []
for i in range(num):
    pp.append(0)
for i in var1:
    count+=int(i)
for j in range(200):
    if str(j).find('7') or ( j % 7 == 0 and j != 0 ):
        count2+=1
        flag = j % 7 - 1
        pp[flag]+=1
    if count2 == count:
        break
for k in pp:
    print(k,end=',')