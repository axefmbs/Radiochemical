# -*- coding: utf-8 -*- 
import math

class rc:
    def __init__(self):
        '''
        放射性化学（Radiochemical）的相关计算方法
        '''        
        self.na=6.022e+23
        self.kilo=1e+3
        self.mega=1e+6
        self.giga=1e+9
        self.tera=1e+12
        self.peta=1e+15
        self.exa=1e+18
        self.zetta=1e+21
        self.yotta=1e+24

        self.milli=1e-3
        self.micro=1e-6
        self.nano=1e-9
        self.pico=1e-12
        self.femto=1e-15
        self.atto=1e-18
        self.zepto=1e-21
        self.yocto=1e-24
        
        self.minute=60
        self.hour=3600
        self.day=86400
        self.year=31557600.0
        
        self.T={'H3':12.28*self.year,
                'C14':5730*self.year,
                'C11':20.334*self.minute,
                'I125':60.14*self.day,
                'I131':8.04*self.day,
                'P32':14.29*self.day,
                'P33':25.4*self.day,
                'S35':87.4*self.day,
                'Ca45':163*self.day,
                'Fe55':2.7*self.year,
                'Fe59':44.6*self.year,
                'Mn54':312.7*self.day,
                'Rb86':18.66*self.day,
                'Na22':2.602*self.day,
                'Y90':64.1*self.hour,
                'Cr51':27.7*self.day
                }
        
        
    def eff(self,cpm,dpm):
        '''
        计算efficiency=探测器记录下电离事件的可能性大小
        cpm= counts per minute（每分钟记录的电离事件的次数）
        dpm= disintegrations per minutes（每分钟发生的电离辐射的次数）
        efficiency=探测器记录下电离事件的可能性大小。
        '''
        if dpm==0:return False
        return float(cpm)/dpm
    
    def Ci2Bq(self,Ci):
        '''
        单位换算
        Ci:居里
        return:Bq
        '''
        return Ci*37000000000
    def Ci2dpm(self,Ci):
        '''
        单位换算
        Ci:居里
        return:dpm
        '''
        return Ci*22200000000000

    def Bq2Ci(self,Bq):        
        '''
        单位换算
        Bq:贝克勒尔
        return:Ci
        '''
        return Bq*2.702702703E-11    
    def Bq2dpm(self,Bq):
        '''
        单位换算
        Bq:贝克勒尔
        return:dpm
        '''
        return Bq*60
    
    def dpm2Bq(self,dpm):
        '''
        单位换算
        dpm:每分钟发生的电离辐射的次数
        return:Bq
        '''
        return float(dpm)/60    
    def dpm2Ci(self,dpm):
        '''
        单位换算
        dpm:每分钟发生的电离辐射的次数
        return:Ci
        '''
        return dpm*4.504504505E-12
    
    def lmd(self,e):
        '''
        计算某一核素的衰变常数
        e:核素符号，可以找到该核素的半衰期（单位：s）        '''

        return math.log(2)/self.T[e]
    
    def A0(self,w,e):
        '''
        计算放射性活度(单位:Bq/mol)
        w:质量分数，0.9=90%
        e:核素符号，可以找到该核素的半衰期（单位：s）
        return Bq/mol
        '''
        return float(w)*self.na*(1-math.exp(-self.lmd(e)))

    def A(self,A0,e,t):
        '''
        计算随着时间变化的放射活度变化
        A0：初始放射活度（单位：Bq/mol）
        e:核素符号，可以找到该核素的半衰期（单位：s）
        t:从A0开始到现在多长时间（单位：s）
        return Bq/mol
        '''
        return A0*math.exp(-self.lmd(e)*t)
    def gmzsl(self,A,E,d):
        '''
        计算伽玛照射率
        A：activity in curies
        E：photo energy in MeV
        d：distance in feet to source
        Limitations
        Range 0.07 to 3 MeV
        ±20%
        return R/hr
        '''
        if d==0:return False
        return (6*float(A)*E)/(d*d)
    def btzsl(self,n,C,d):
        '''
        计算贝塔照射率
        n：fraction of disintegrations where a β is emitted
        C：activity in curies
        d：distance in feet to source
        Limitations
        energy＞0.6MeV        
        return R/hr
        '''
        if d==0:return False
        return (300*float(n)*C)/(d*d)
    def D2(self,D1,d1,d2):
        '''
        反比定律，返回D2
        D1=dose at distance 1
        D2=dose at distance 2
        d1=distance 1
        d2=distance 2
        '''
        if d2==0:return False
        return (float(D1)*d1*d1)/(d2*d2)
    def MDCR():
        '''
        计算最低可测计数率(该函数还未实现）
        (不会随本底波动的可测放射性计数率)
        '''
        pass
    
    def C(self,w,M,e):
        '''
        计算比活度(单位:Bq/g)
        w:质量分数，0.9=90%
        M:摩尔质量（单位：g/mol）
        e:核素符号，可以找到该核素的半衰期（单位：s）
        specific activity
        return Bq/g
        '''
        return self.A0(w,e)/M
    def A2w(self,A,e):
        '''
        计算质量分数，已知放射活度（Bq/mol）
        e:核素符号，可以找到该核素的半衰期（单位：s）
        return %
        '''
        return float(A)/(self.na*(1-math.exp(-self.lmd(e))))
    def n(self,m,M):
        '''
        计算摩尔数（单位：mol）
        m：质量（单位：g）
        M：分子量（单位：g/mol）
        returm：mol
        '''
        if M==0:return False
        return float(m)/M
    def m(self,n,M):
        '''
        计算质量（单位：g）
        n：摩尔数（单位：mol）
        M：分子量（单位：g/mol）
        returm：g
        '''
        return n*M
    def M(self,n,m):
        '''
        计算分子量（单位：g/mol）
        n：摩尔数（单位：mol）
        M：分子量（单位：g/mol）
        returm：mol
        '''
        if n==0:return False
        return float(m)/n

if __name__=='__main__':
    t=rc()
    def fun1():
        print 'C14半衰期:',t.T['C14'],'s'
        print 'C14 碳酸钡的放射活度:',t.A0(1,'C14'),'Bq/mol'
        print 'C14 碳酸钡的比活度:',t.C(1,199.34,'C14'),'Bq/g'
        print '',t.A2w(1850,'C14')*100
    def fun2(c,e,k):
        i=0
        A0=c.A0(1,e)
        print A0,'Bq/mol',c.Bq2Ci(A0),'Ci/mol'
        while(1):
            A=c.A(A0,e,i*c.day)
            print i,A,           
            if A<=k:
                print i,A,
                break
            i+=1
    def fun3():
        #计算合格的碳14产品的质量分数范围
        #1.85<A<2.22
        r=10000000
        for i in range(0,r):
            #GBq
            a=t.Bq2Ci(t.A0(float(i)/r,'C14'))
            print float(i)*100/r,'%:',a,'Ci/mol'
            if a>50:
                print float(i)*100/r,'%:',a,'Ci/mol'
                break
    def fun4(c,e):
        A0=c.A0(1,e)
        i=c.T[e]
        while(1):
            A1=c.A(A0,e,i)
            if A1<=0:
                print i/c.year,'y',A1
                break
            i=i*2
            
        
        
    fun3()
    #print t.Ci2Bq(0.050)
    #print t.Bq2Ci(t.A0(1,'C14'))
    #fun2(t,'P32',0.01)
    #fun4(t,'C14')
    #help(rc)
