#!/usr/bin/env python
# coding: utf-8

# # 스택에 관련된 7문제를 풀어보았다.  
# 
# <https://www.acmicpc.net/problemset?sort=ac_desc&algo=71>

# ## 10828번 스택  
# 
# <https://www.acmicpc.net/problem/10828>  
# 
# input()을 이용하면 시간 초과가 발생한다. (sys.stdin.readline() 사용)  
# 입력받은 값에 각 명령어들이 있으면 명령어에 따라 작동하도록 해주면 된다.  
# push는 뒤에 숫자가 따라오기 때문에 split() 함수를 통해 뒤에 숫자를 분리해줘서 스택에 넣어준다.  
# pop은 스택의 길이가 0 보다 클 때와 작을 때를 구분하여 pop 함수를 실행하거나 -1을 출력해주면 된다. 
# size는 스택의 길이와 같다.  
# empty는 스택의 길이가 0 인가 아닌가를 판별해주면 된다.  
# top은 pop과 유사하지만 pop 함수를 사용하면 가장 위에 숫자가 스택에서 사라지기 때문에 stack[-1]을 출력해주면 된다.  

# In[3]:


# 처음 문제만 읽고 풀었을 때 작성한 코드

import sys
stack=[]
for i in range(int(input())):
    command=input()
    if 'push' in command:
        a,b=command.split()
        b=int(b)
        stack.append(b)
    if 'top' in command:
        if len(stack)>0:
            print(stack[-1])
        else:
            print('-1')
    if 'size' in command:
        print(len(stack))
    if 'empty' in command:
        if len(stack)==0:
            print('1')
        else: print('0')
    if 'pop' in command:
        if len(stack)>0:
            print(stack.pop())
        else:
            print('-1')


# In[11]:


# 클래스와 함수를 이용하는 것이 훨씬 보기 좋을 것 같아서 새로 작성한 코드
# 클래스와 함수에 익숙하지 않아서 생각보다 오래 걸렸다.
# 마찬가지로 input 대신 sys.stdin.readline()를 사용하여 제출해야한다.

class stack:
    def __init__(self): 
        self.stack_list = []
    def push(self, num):
        self.stack_list.append(num)
    def pop(self):
        if len(self.stack_list) == 0:
            print("-1")
        else:
            print(self.stack_list.pop())
    def size(self):
        print(len(self.stack_list))
    def empty(self):
        if len(self.stack_list) == 0:
            print("1")
        else :
            print("0")
    def top(self):
        if len(self.stack_list) == 0:
            print("-1")
        else :
            print(self.stack_list[-1])

import sys

number = int(input())
stack=stack()
for _ in range(number):
    command = input().split()
    if command[0] == "push":
        stack.push(command[1])
    if 'pop' in command:
        stack.pop()
    if 'size' in command:
        stack.size()
    if 'empty' in command:
        stack.empty()
    if 'top' in command:
        stack.top()


# ## 10773번 제로  
# 
# <https://www.acmicpc.net/problem/10773>  
# 
# 스택에서 pop과 append를 이용하여 해결할 수 있는 간단한 문제였다.  
# 재현이가 0 을 외치면 pop을 이용해서 최근의 숫자를 지워주면 된다.  
# 반대로 0이 아닌 숫자를 외치면 스택에 append 해주면 된다.  
# 출력하는 값은 stack에 남아있는 숫자이기 때문에 sum을 이용해서 출력해준다.  

# In[14]:


import sys

stack=[]
for i in range(int(input())):
    money=int(input())
    if money==0:
        stack.pop()
    else:
        stack.append(money)
print(sum(stack))


# ## 1874번 스택 수열  
# 
# <https://www.acmicpc.net/problem/1874>  
# 스택과 푸쉬, 팝 이해하기  
# push를 세 번 하면 [1,2,3] 스택이 쌓이게 되고 여기서 pop을 하면 3이 출력된다.  
# 
# n을 통해 입력할 숫자의 갯수를 입력받고 num을 통해 숫자를 입력받는다.  
# count는 입력받을 숫자가 stack에 입력되도록 해준다. 0으로 두면 0부터 시작이다.  
# 따라서 1로 한다. result를 통해 +와 -를 입력받고 stack에는 count에 생긴 숫자들을 쌓아둔다.  
# while문을 통해 stack을 완성하고 if문을 통해 해당 숫자가 나오면 -를 입력한 뒤 pop해서 숫자를 제거한다.  

# In[2]:


n=int(input())
count=1
result=[]
stack=[]
temp=True
for i in range(n):
    num=int(input())
    while count<=num:
        stack.append(count)
        result.append('+')
        count=count+1
    if stack[-1]==num:
        stack.pop()
        result.append('-')
    else:
        temp=False
        

if temp==False:
    print('NO')
else:
    for j in result:
        print(j)


# # 10799번 쇠막대기  
# 
# <https://www.acmicpc.net/problem/10799>  
# 
# ()가 쌍을 이룰 때는 레이저이므로 L로 대체했다.  
# stack=[]을 이용하여 막대가 몇 개 있는지 저장하는 용도로 사용하였다.  
# (가 되면 막대가 계속 쌓이는 데, 레이저를 만나면 레이저 왼쪽으로 막대의 개수만큼 잘린다.  
# 그 다음 )를 만나면 막대가 끝난 경우이므로 또 잘린 막대가 생긴다.  
# 따라서 if 문으로 (가 나오면 막대 개수를 추가해주고  
# L은 막대의 개수만큼 답을 더해주고 )는 잘린 막대 1개를 추가해준다.  

# In[8]:


word=input()


# In[15]:


word=word.replace('()','L')


# In[16]:


stack=[]
answer=0
for i in word:
    if i=='(':
        stack.append(0)
    elif i==')':
        stack.pop()
        answer+=1
    else:
        answer+=len(stack)
print(answer)        


# # 4949번 균형잡힌 세상  
# 
# <https://www.acmicpc.net/problem/4949>  
# 
# 하나는 replace와 re.sub을 이용하여 괄호들을 제외한 모든 문자를 지워주는 문제로 풀었다.  
# 하지만 주제가 스택이었으므로 스택으로 다시 한 번 풀었다.  

# In[68]:


# replace와 sub을 이용한 풀이
import re

word='a'
while word != '.':
    word=input()
    if word=='.':
        break
    word=word.replace('.','')
    word=re.sub('[a-zA-Z]','',word)
    word=re.sub(' ','',word)
    while ('[]' in word) or ('()' in word):
        word=word.replace('[]','')
        word=word.replace('()','')
    if word =='':
        print('yes')
    else:
        print('no')


# In[71]:


# stack을 이용한 풀이
while True: # 계속 입력받기 위한 while
    word=input()
    stack=[] # 괄호 저장을 위한 stack
    temp=True # 나중에 stack에 있는지 없는지 판단을 위한 temp
    if word=='.': # .만 입력하면 while이 끝난다.  
        break
        
    for i in word:
        if i =='[' or i=='(': # 괄호 여는 것은 모두 스택에 append한다.
            stack.append(i)
        elif i==']': # 닫힌 괄호가 나왔을 때,
            if len(stack) ==0 or stack[-1]=='(': # 스택에 아무것도 없거나 소괄호만 있다면 no를 출력한다.                
                print('no')
                temp=False #temp를 false로 두어서 나중에 stack에 짝이 맞아서 아무것도 없을 때를 대비한다.
                break
            else:
                stack.pop() # 괄호의 짝이 맞게 있다면 '['를 없애서 스택에서 비워준다.
        elif i==')': 
            if len(stack) ==0 or stack[-1]=='[':
                print('no')
                temp=False
                break
            else:
                stack.pop()
    if temp==True: #괄호의 짝이 모두 맞았다면 stack은 0이 될 것이다.
        if len(stack)==0:
            print('yes')
        else:
            print('no')


# # 1406번 에디터  
# 
# <https://www.acmicpc.net/problem/1406>  
# 
# 처음에 짠 코드는 답은 맞았지만 시간초과가 발생한다.  
# 찾아보니까 insert와 del은 시간 복잡도가 O(n)이라고 한다.  
# 따라서 O(1)인 pop과 append를 사용해서 문제를 해결해야 한다.  
# pop과 append를 이용하여 빈 스택에 'L','D'로 변화된 커서에 대한 정보를 저장한다.  
# B와 P는 처음 푼 것과 다르게 커서 변경없이 pop과 append로 값만 추가, 삭제해주면 된다.  
# word_list에는 새로 입력받은 값이 저장될 것고 새로 만든 스택에 커서 변경된 정보가 순서대로 저장될 것이다.   
# 실제 입력받은 문자에서의 변화와 반대로 저장되기 때문에 [::-1]로 새로운 스택은 합쳐줘야한다.  
# 당연히 sys.stin.readline()으로 입력받아야한다.  

# In[67]:


# 시간 초과된 insert와 def
word_list=list(input())
point=int(input())
j=len(word_list)
for i in range(point):
    command=input()
    if command[0]=='L' and j!=0:
        j=j-1 
        
    elif command[0]=='D' and j!=len(word_list):
        j=j+1
    
    elif command[0]=='B' and j != 0:
        del word_list[j-1]
        j=j-1
        
    elif command[0]=='P':
        if j==len(word_list):
            word_list.insert(len(word_list)+1,command[2])
            j=j+1
            print(j)
        elif j==0:
            word_list.insert(j,command[2])
            print(j)
        else:
            word_list.insert(j,command[2])
            
print(''.join(word_list))


# In[83]:


word_list=list(input())
point=int(input())
j=len(word_list)
stack=[]
for i in range(point):
    command=input()
    if command[0]=='L' and len(word_list) !=0:
        stack.append(word_list.pop())
    elif command[0]=='D' and len(stack) !=0:
        word_list.append(stack.pop())
    elif command[0]=='B'and len(word_list) !=0:
        word_list.pop()
    elif command[0]=='P':
        word_list.append(command[2])

print(word_list)
print(stack)
word_list.extend(stack[::-1])    
print(''.join(word_list))


# # 2493번 탑  
# 
# <https://www.acmicpc.net/problem/2493>  
# 
# answer은 정답을 기록하는 용도로, stack은 비교하는 탑과 인덱스를 저장한다.  
# 즉, for문으로 레이저가 출발하는 송전탑을 고르고, stack에는 이 전에 지나온 송전탑들이 저장된다.  
# i값은 인덱스보다 1 작기 때문에 답에는 1을 추가해줘야한다.  

# In[109]:


n = int(input()) #5
top = list(map(int, input().split())) #[6 9 5 7]
stack = [] #[]
answer = [0 for i in range(n)] #[0 0 0 0 4]
 
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])
 
print(*answer)


# In[107]:


a=[1,2,3]

print(*a)

