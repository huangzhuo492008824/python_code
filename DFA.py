#-*- coding:utf-8 -*-
from setting import config
from singleton import singleton
import time


class Node(object):
    def __init__(self):
        self.children = None


@singleton
class DFA(object):
    """
    确定有限状态机的算法实现
    """
    def __init__(self):
        """
        初始化根节点和打开敏感文件
        :param path:
        :return:
        """
        self.root = Node()
        cf = config()
        path = cf.get('SensitiveWords', 'keywords')
        self.fp = open(path, 'r')
        for line in self.fp:
            line = line[0:-1]
            self.add_word(line)
        self.fp.close()

    def add_word(self, word):
        """
        增加敏感词汇到链表节点中
        :param word:
        :return:
        """
        node = self.root
        for i in range(len(word)):
            if node.children == None:
                node.children = {}
                node.children[word[i]] = Node()
            elif word[i] not in node.children:
                node.children[word[i]] = Node()
            node = node.children[word[i]]

    def is_contain(self, content):
        """
        判断给定字符中是否含有敏感词汇
        :param content:
        :return:True 包含敏感词，False 不包含敏感词
        """
        for i in range(len(content)):
            p = self.root
            j = i
            while (j<len(content) and p.children!=None and content[j] in p.children):
                p = p.children[content[j]]
                j = j + 1

            if p.children==None:
                return True
        return False

class Normal(object):
    """
    read keywords to dict, traversal dict find 
    """
    def __init__(self):
        cf = config()
        path = cf.get('SensitiveWords', 'keywords')
        self.fp = open(path, 'r')
        self.kw_dict = set()
        for kw in self.fp:
            self.kw_dict.add(kw)
        self.fp.close()

    def is_contain(self, content):
        for i in range(len(content)):
            j = i
            while (j<len(content)):
                if content[i:j] in self.kw_dict:
                    return True
                j = j + 1
        return False

    def is_contains2(self, content):
        #counter=0
        for i in self.kw_dict:
            if content.encode('utf-8').find(i) != -1:
                return True
        #    counter += 1
        #print 'counter:', counter
        return False

#class StrNormal(object):

        
msg = u'四处乱咬乱吠，吓得家中11岁的女儿鐵血三國志躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征得主人同意后，民警和村民合力将这只发疯的狗打死'
msg1 = u'四处乱咬乱吠，吓得家中11岁的女儿鐵血三國志躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征江泽民得主人同意后，民警和村民合力将这只发疯的狗打死'
dfa = DFA()
normal = Normal()

print dfa.is_contain(msg)
print normal.is_contain(msg)
#test dfa
start_time = time.time()
for i in range(1000):
    dfa.is_contain(msg)
end_time = time.time()
print 'dfa time:', end_time - start_time

#test normal
start_time = time.time()
for i in range(1000):
    normal.is_contain(msg)
end_time = time.time()
print 'normal time:', end_time - start_time


#test strnormal
start_time = time.time()
for i in range(1000):
    normal.is_contains2(msg)
end_time = time.time()
print 'strnormal time:', end_time - start_time
