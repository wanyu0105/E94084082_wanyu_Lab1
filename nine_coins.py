#!/usr/bin/env python
# coding: utf-8

# In[1]:


bin1=[]   #建立一個空列表叫做 bin1

#定義一個函式 binary()
def binary(number):
    for i in range(9):   #設定for迴圈執行9次
        if(number!=0):   
            r=number%2   #將number的值除以2的餘數(可能為0或1)的值assign給變數 r
            bin1.append(r)   #利用 append()為列表bin1添加"元素"，即變數r的值
            number=number//2   #把number除以2，並以"向下取整數"的原則返回商的整數部分
        else:   #當number=0時
            r=0
            bin1.append(r) 
            
    bin1.reverse()   #將列表bin1中的元素反向排列，以得到正確的二進位數值


# In[2]:


list1=[]   #建立一個空列表叫做 list1

#建立一個class 'Nine_Coins'
class Nine_Coins:
    def __init__(self,number):   #初始化 / 會自動執行的函式
        self.number = number
        binary(number)   #呼叫函式 binary()
        
    def __repr__(self):
        string='%s' * len(bin1) % tuple(bin1)   #將列表bin1轉換為字串，並將轉換後的值assign給變數string
        length=len(string)   #利用len()計算string的長度，並將計算後得出的值assign給變數length
        
        n=0   #控制while迴圈執行的條件變數
        
        #在while迴圈裡利用if-else條件式判斷列表list1添加的元素為'H'還是'T'
        while(n<length):
            if(string[n]=='0'):   #string[n]的值為字串內位於第'n'個位置的字元的值
                list1.append('H')   #當該字元的值為'0'時，列表list1添加的元素為'H'
                n+=1
            else:
                list1.append('T')   #當該字元的值為'1'時，列表list1添加的元素為'T'
                n+=1
        
        l='%s' * len(list1) % tuple(list1)   #將添加完元素的列表'list1'轉換為字串，並將轉換後的值assign給變數 l
        del list1[:]   #使用del語句將列表list1中的元素刪除，讓list1回歸為空列表
        return f'Nine_Coins: {l}'   #利用f'  '將字符串格式化，{}表示可被替換字段
        
    def __str__(self):   #等同於print的功能
        l2='%s' * len(bin1) % tuple(bin1)   #將列表bin1轉換為字串，並將轉換後的值assign給變數 l2
        return f'binary: {l2} and decimal: {self.number}'   #利用f'  '將字符串格式化，{}表示可被替換字段
        
    def toss(self):   
        from random import randint   #從random模組裡只匯入randint函式
        self.number = randint(0,511)   #利用randint函式隨機產生0~511任一正整數，並將該整數的值assign給self.number
        del bin1[:]   #使用del語句將列表bin1中的元素刪除，讓bin1回歸為空列表，以利binary函式執行
        binary(self.number)   #呼叫binary函式

