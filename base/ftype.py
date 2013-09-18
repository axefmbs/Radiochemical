import os
def fType(fname):
    '''
    返回文件扩展名
    如x.py则返回py
    '''
    i=len(fname)
    while(1):
        i-=1
        if fname[i]=='.':return fname[i+1:]        
        if i==0:return False

if __name__ == '__main__':
    def main():
        print fType('./x1/x2/n1.n2.n3.py.txt')

    def test(dir):
        for root,dirs,files in os.walk(dir):
            for f in files:
                ft=fType(f)
                if ft not in filetype:
                    print len(filetype),ft
                    filetype.append(ft)

    #main()
    filetype=[]
    test('d:')

