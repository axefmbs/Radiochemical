# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
def fileType(fname):
    '''
    返回文件扩展名
    如x.py则返回py
    '''
    i=len(fname)
    while(1):
        i-=1
        if fname[i]=='.':return fname[i+1:]        
        if i==0:return 'Unknow'
    



class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:

                    if variable == "href":
                        self.links.append(value)
    def getlink(self,type):
        temp=[]
        type=type.lower()
        for i in self.links:
            if fileType(i).lower()==type:
                temp.append(i)
        return temp
        
 
if __name__ == "__main__":
    html_file='./i.txt'
    print html_file
    html_code = open(html_file,'r').read()
   
    hp = MyHTMLParser()
    hp.feed(html_code)
    for i in hp.getlink('pdf'):
        print i
    hp.close()
