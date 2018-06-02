# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 21:46:32
"""

# T1-4 猫狗队列
# 实现一种猫狗队列的结构，要求如下：
# · 用户可以调用add方法将cat类或者dog类放入队列中；
# · 用户可以调用pollAll方法，将队列中所有的实例按照队列的先后顺序依次弹出；
# · 用户可以调用pollDog方法，将队列中dog类的实例按照进队的先后顺序依次弹出；
# · 用户可以调用pollCat方法，将队列中cat类的实例按照进队的先后顺序依次弹出；
# · 用户可以调用isEmpty方法，检查队列中是否有cat或者dog的实例；
# · 用户可以调用isDogEmpty方法，检查队列中是否有dog的实例；
# · 用户可以调用isCatEmpty方法，检查队列中是否有cat的实例；

# 一个queue用来放Dog，另一个用来放Cat，每次入队列，记录放入的次序

class Pet():
    Type = ''
    
    def __init__(self, Type):
        self.Type = Type
    
    def getType(self):
        return self.Type

class Dog(Pet):
    def __init__(self):
        self.Type = "dog"

class Cat(Pet):
    def __init__(self):
        self.Type = "cat"
        
#########################################################################
class DogCatQueue():
    def __init__(self):
        self.DogQueue = []
        self.CatQueue = []
        self.count = 0
    
    def add(self, pet):
        self.count += 1
        if(isinstance(pet, Dog)):
            self.DogQueue.append([self.count, pet])
        elif(isinstance(pet, Cat)):
            self.CatQueue.append([self.count, pet])
    
    def isDogEmpty(self):
        return True if self.DogQueue == [] else False

    def isCatEmpty(self):
        return True if self.CatQueue == [] else False          

    def isEmpty(self):
        return (self.isDogEmpty() and self.isCatEmpty())
        
    def pollAll(self):
        if(not self.isEmpty()):
            if((not self.isDogEmpty()) and (not self.isCatEmpty())):
                if(self.DogQueue[0][0] > self.CatQueue[0][0]):
                    resu = self.CatQueue[0][1]
                    del self.CatQueue[0]
                else:
                    resu = self.DogQueue[0][1]
                    del self.DogQueue[0]
            elif(not self.DogQueue()):
                resu = self.DogQueue[0][1]
                del self.DogQueue[0]
            elif(not self.CatQueue()):
                resu = self.CatQueue[0][1]
                del self.CatQueue[0]

            return resu
            
    def pollDog(self):
        if(not self.isDogEmpty()):
            resu = self.DogQueue[0][1]
            del self.DogQueue[0]
            return resu
    
    def pollCat(self):
        if(not self.isCatEmpty()):
            resu = self.CatQueue[0][1]
            del self.CatQueue[0]
            return resu

if __name__ == "__main__":
    q = DogCatQueue()
    q.add(Cat())
    q.add(Dog())
    q.add(Cat())
    q.add(Cat())
    q.add(Dog())
    print(q.isCatEmpty())
    print(q.isDogEmpty())
    print(q.pollAll())
    print(q.pollAll())
    print(q.pollDog())
    print(q.pollDog())
    print(q.isDogEmpty())