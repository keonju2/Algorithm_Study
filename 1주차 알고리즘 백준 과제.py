#!/usr/bin/env python
# coding: utf-8

# # GDSC 파이썬 알고리즘 1주차 과제로 solved.ac의 class 2단계 8문항을 풀어보았다.  
# 
# 파이썬 알고리즘 과제는 알고리즘 공부를 많이 하지 않은 나로써는 조금 어려웠다.  
# 
# <https://solved.ac/search?query=in_class:2>   

# ## 1번 체스판 다시 칠하기  
# 
# <https://www.acmicpc.net/problem/1018>  

# ###### N,M 크기를  받고 보드 만들기  
# 
# nXm형태의 위치를 파악하기 쉽게 리스트 형태로 받았다.  

# In[22]:


n, m=map(int,input().split())
if 8<=n<=50 and 8<=m<=50:
    board = [input() for i in range(n)]


# ###### 위치가 짝수일 때와 홀수일 때로 나눠서  W, B가 아닐 때마다 점수를 추가해준 다음 가장 최소가 되는 값만 찾아내면 된다.  
# 
# 따라서 n * m의 보드에서 가능한 경우의 수는 n-7 * m-7이다. ex)10 13을 입력받을 경우 18가지.  
# 
# 8 * 8로 잘라주기 위해서 k와 l을 (i,i+8), (j,j+8)로 한정짓는다.  
# 
# k+l이 홀수일 경우와 짝수일 경우, W로 시작할 경우와 B로 시작할 경우를 나눠서 모든 경우의 수를 반복문으로 확인해준다.  
# 
# 마지막으로 total_score에 들어있는 값들 중 최솟값을 구해준다.  

# In[25]:


total_score=[]
# 보드에서 경우의 수 나누어주기
for i in range(n-7):
    for j in range(m-7):
        count_w=0 #w가 아닐때
        count_b=0 #b가 아닐때
        #8*8 크기로 잘라주기
        for k in range(i,i+8):
             for l in range (j,j+8):
                #각 경우의 수마다 비교해서 점수 추가하기
                if (k+l)%2==0:
                    if board[k][l]!='W':                            
                        count_w=count_w+1
                    if board[k][l]!='B':
                        count_b=count_b+1
                else:
                    if board[k][l]!='W':
                        count_b=count_b+1
                    if board[k][l]!='B':                            
                        count_w=count_w+1
        # 점수들 한 list에 모아주기
        total_score.append(count_w)
        total_score.append(count_b)
print(min(total_score)) #최솟값 출력


# ## 2번 직사각형에서 탈출  
# 
# <https://www.acmicpc.net/problem/1085>  

# ###### x,y,w,h 입력받기  

# In[31]:


x,y,w,h =map(int,input().split())


# ###### 0과 가까운 경계선은 x, y로 w,h와 가까운 경계선은 w-x, h-y로 표현해주는 대신 음수가 나올수 있기때문에 abs()를 이용하여 절댓값으로 표현.  

# In[30]:


print(min(x,y,abs(w-x),abs(h-y)))


# ## 3번 단어 정렬  
# 
# <https://www.acmicpc.net/problem/1181>  

# ###### 단어 리스트 입력받기  

# In[90]:


n=int(input())
word_list=[input() for i in range(n)]


# ###### 길이가 짧은 것부터 같으면 사전 순으로 정렬하기 (단, 중복 제외)    
# 
# set함수로 중복을 먼저 제거하였다.  
# 
# 단어의 길이를 먼저, 그다음에 단어를 하나의 tuple로 만들어 리스트를 다시 만들어주었다.  
# 
# sort를 이용하면 앞에 숫자가 들어갔기 떄문에 길이, 알파벳 순으로 정렬된다.  

# In[98]:


# 중복 단어 제거
word_list=list(set(word_list))
len_word_list=[]
# (단어 길이, 단어) 형태의 tuple 만들기
for i in word_list:
    len_word_list.append((len(i),i))
# 정렬하기
len_word_list.sort()
print(len_word_list)
# 출력하기
for j,k in len_word_list:
    print(k)


# ## 4번 팰린드롬수  
#   
# <https://www.acmicpc.net/problem/1259>  

# ###### 앞에서 읽어도 뒤에서 읽어도 같은 숫자 찾기
# 
# 0을 입력하면 반복문이 끝나게 while과 if를 이용하였다.  
# 
# 입력받은 숫자는 위치를 찾기 편하게 문자형으로 입력받았다.  
# 
# 입력받은 숫자의 길이/2 만큼의 반복문을 돌리면 반대쪽은 (숫자의 길이-i-1)로 대응된다.  
# 
# 한가지 숫자라도 값이 다르면 False 값을 가지고 'no'를 출력하면 'yes'를 출력하는 것을 만들 때보다 길이가 짧아질 수 있다.  

# In[130]:


while True:
    word=input() # 숫자를 무한으로 입력받기 위해 while문 사용
    quest=True # 한가지 입력값을 처리하고나서 True, False값을 True로 초기화
    if word=='0': # 0을 입력하면 반복문 종료
        break
    else:
        word_len=len(word)
        for i in range(int((word_len)/2)): #단어 길이의 반만 확인하면 반대쪽 숫자와 대응된다.
                if word[i]!=word[word_len-1-i]: #반대쪽 숫자와 대응하기 위해서 word_len-1-i 사용
                    quest=False # 하나의 경우라도 False가 나오면 반복문 종료
                    continue
        if quest==False: # False가 나오면 바로 'no' 출력
            print('no')
        else: print('yes')


# ## 5번 영화감독 숌  
# 
# <https://www.acmicpc.net/problem/1436>  

# ###### 666이 적어도 3개이상 연속으로 들어가는 수를 만든다  
# 
# 처음에 문제를 풀 때 중간에 666이 3개 이상 들어가는 경우를 제외해서 틀렸다.  
# 
# list666에 가장 작은 숫자인 666부터 '666'이 문자열로 들어가있는 숫자들을 확인해서 추가하였다.  
# 
# 입력받은 숫자가 list666의 길이보다 크면 계속 추가해주었고 list666[num-1]을 통하여 값을 출력해준다.  

# In[169]:


num=int(input())
list666=[]
i=666
while len(list666)<num:
    if '666' in str(i):
        list666.append(i)
    i=i+1
print(list666[num-1])


# ## 6번 랜선 자르기
# 
# <https://www.acmicpc.net/problem/1654>  

# ###### 숫자 입력받기   

# In[1]:


k,n=map(int,input().split())

lan=[int(input()) for i in range(k)]


# ###### 시간초과된 코드  
# 
# for문을 이용하니까 연산자가 너무 많아서 시간이 초과되었던 것 같다.  

# In[2]:


div_list=[]
for i in range(min(lan)):
    div=int(min(lan))-i
    count=[]
    for w in lan:
        count.append(w//div)
    n_result=0
    for j in range(k):
        n_result=n_result+count[j]
    if n_result==n:
        div_list.append(div)
print(max(div_list))


# ###### 이진탐색을 이용하여보자.   
# 
# 이진탐색이란 마치 병뚜껑 숫자맞추기를 할 때 50을 먼저 외치고 다음에 25나 75를 외치는 것처럼 가운데에 위치한 값들을 기반으로 탐색하는 것이다.  
# 정렬된 데이터일 때 사용 가능하다.  
# 따라서 입력받은 값들을 기준으로 max값과 1을 양 끝 값으로 놓는다.  
# 시작과 끝이 같을 때 까지 while문을 돌련준다.  
# 중간값을 구하고 이 값으로 입력받은 값들을 나누어준다.  
# 이때 잘라진 갯수가 n보다 크면 시작값에 중간값+1을, 작으면 끝값을 중간값-1을 해준다.  
# while문이 다 돌고 나면 그 중 작은 값이 정답이다.

# In[10]:


start , end= 1,max(lan) #시작값과 끝값 구하기
while start<=end: #루프를 돌기위한 조건문
    mid=(start+end)//2 #중간값 설정
    cutting=0 #잘라진 선의 갯수 선언
    for i in lan:
        cutting+=i//mid #잘라진 선의 갯수 구하는 for문
    if cutting>=n: #n과 잘라진 선의 크기 비교를 통한 중간값 찾기
        start=mid+1 
    else:
        end=mid-1
print(min(start,end))


# ## 7번 스택 수열
# 
# <https://www.acmicpc.net/problem/1874>  

# ###### 스택과 푸쉬, 팝 이해하기  
# 
# push를 세 번 하면 [1,2,3] 스택이 쌓이게 되고 여기서 pop을 하면 3이 출력된다.  
# 
# n을 통해 입력할 숫자의 갯수를 입력받고 num을 통해 숫자를 입력받는다.  
# count는 입력받을 숫자가 stack에 입력되도록 해준다. 0으로 두면 0부터 시작이다.  
# 따라서 1로 한다.
# result를 통해 +와 -를 입력받고 stack에는 count에 생긴 숫자들을 쌓아둔다.
# while문을 통해 stack을 완성하고 if문을 통해 해당 숫자가 나오면 -를 입력한 뒤  
# pop해서 숫자를 제거한다.

# In[28]:


n=int(input())
count=1 #count=1로 해줘야 0부터 숫자를 세지않는다.
result=[] # +와 -를 저장하기 위한 리스트
stack=[] # 쌓인 숫자를 저장하기 위한 리스트
temp=True # 불가능한 경우에 False처리하기 위한 temp
for i in range(n):
    num=int(input()) 
    while count<=num: #num과 같거나 작아질때 까지 stack에 숫자를 입력받는다.
        stack.append(count)
        result.append('+') #입력받은 숫자만큼 결과에 +를 입력해준다.
        count=count+1
    if stack[-1]==num: #스택의 마지막 숫자가 num과 같을 경우 해당 숫자를 pop하고 -를 입력해준다.
        stack.pop()
        result.append('-')
    else:
        temp=False # if문이 적용되지 않는 경우에는 False를 전달해준다.
        

if temp==False:
    print('NO')
else:
    for j in result:
        print(j)


# ## 8번 스택 수열
# 
# <https://www.acmicpc.net/problem/1920>  

# ###### 시간초과    
# 
# list를 사용했을 때는 시간초과가 나왔고 set을 이용했을 때는 정상적으로 나왔다.  
# 리스트의 in연산자를 통한 포함 여부의 시간 복잡도는 O(N)이다.  
# 이분 탐색의 시간 복잡도는 O(logN) 이다.  
# Set과 Dictionary의 in연산을 통한 포함 여부 확인의 시간 복잡도는 O(1)이다.  
# 따라서 N만 set으로 받아줘도 시간이 매우 단축된다.

# In[60]:


n=int(input())
N=set(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))


# In[62]:


for i in range(m):
    if M[i] in N:
        print(1)
    else:
        print(0)

