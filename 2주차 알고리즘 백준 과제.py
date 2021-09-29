#!/usr/bin/env python
# coding: utf-8

# # GDSC 파이썬 알고리즘 2주차 과제로 문자열에 관련된 7문항을 풀어보았다.    
# 
#   
# 
# <https://www.acmicpc.net/problemset?sort=ac_desc&algo=158>   

# ## 11720번 숫자의 합    
# 
# <https://www.acmicpc.net/problem/11720>      

# ###### 공백없는 숫자들의 합구하기    
# 
# 방법 1. for문을 이용해서 풀기    

# In[9]:


n=int(input())
m=input()


# range를 이용한 풀이 방법   

# In[10]:


result=0
for i in range(n):
    result=int(m[i])+result
print(result)


# m을 읽어가면서 더해주는 방법   

# In[11]:


result=0
for i in m:
    result=int(i)+result
print(result)


# 방법 1. sum과 map을 이용해서 풀기   

# In[12]:


print(sum(map(int,input())))


# ## 8958 번 OX퀴즈
# 
# <https://www.acmicpc.net/problem/8958>  
# 
# for문을 이용하여 입력받을 ox의 개수를 입력받고 for문 중첩을 이용하여 ox의 길이를 파악하고 if문으로 ox 여부를 확인하였다.
# ox의 연속성에 따른 점수변화를 num_score로 두고 total_score을 num_score의 합으로 설정하였다.

# In[1]:


num=int(input())
for i in range(num):
    ox=input()
    total_score=0
    num_score=0
    for i in range(len(ox)):
        if (ox[i]=='O') is True:
            num_score=num_score+1
        else:
            num_score=0
        total_score=total_score+num_score
    print(total_score)


# ## 1152번 단어의 개수   
# <https://www.acmicpc.net/problem/1152>  
# 
# 단어의 개수=공백의 위치마다 구분해줘서 입력받았다.  

# In[2]:


sentence=list(map(str,input().split()))
print(len(sentence))


# ## 10809번 알파벳찾기
# 
# <https://www.acmicpc.net/problem/10809>  

# ###### for문과 알파벳 list 선언

# In[14]:


s=list(map(str,input()))
alpha=list('abcdefghijklmnopqrstuvwxyz')
array=[-1 for i in range(len(alpha))]
for i in range(len(s)):
    if array[alpha.index(s[i])]==-1:
        array[alpha.index(s[i])]=i
for j in array:
    print(j,end=' ')


# ###### 아스키코드 이용
# 알파벳의 아스키코드는 (97,123)이다.

# In[16]:


s=input()
alpha=list(range(97,123))
for i in alpha:
    print(s.find(chr(i)),end=' ')


# ## 10809번 알파벳찾기  
# 
# <https://www.acmicpc.net/problem/10809>  
# upper을 이용한 대문자 받기  
# count로 dictionary형태로 word 개수 세기
# 개수가 중복되는 단어들이 있으므로 max_list에서 따로 추출하기
# 조건에 맞게 최댓값이 하나면 알파벳을, 아니면 물음표를 출력하기

# In[44]:


word=input().upper()
count={}
for i in word:
    if i not in count:
        count[i]=0
    count[i]+=1
max_list=[j for j,k in count.items() if max(count.values())==k]
if len(max_list)==1:
    print(max_list[0])
else:
    print('?')


# ## 9012번 괄호
# 
# <https://www.acmicpc.net/problem/9012>   
# while문을 통해 '()'가 vps에 존재한다면 계속 replace를 통해 제거해주었다.
# 만약 VPS 문장이었다면 문자열에 아무것도 남지않고 VPS 문장이 아니라면 어떤 문자라도 남았을 것이다.  
# 따라서 결과물의 길이로 YES와 NO를 구분지어줬다.  

# In[17]:


num=int(input())
for i in range(num):
    vps=input()
    while '()' in vps:
        vps=vps.replace('()','')
    if len(vps)==0:
        print('YES')
    else:
        print('NO')


# ## 11718번 그대로 출력하기
# 
# <https://www.acmicpc.net/problem/11718>  
# 
# while True로 반복문을 만들어주고 try~except문으로 오류가 발생했을때는 멈출수 있게 해준다.

# In[4]:


while True:
    try:
        print(input())
    except:
        break

