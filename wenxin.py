class data:
    a=8
    b=6
class graph(data):
    def jx(self):
        s1=(self.a*self.b)
        print "�������Ϊ��%f." %  s1
        return s1     
    def zfx(self):
        s2=(self.a**2)
        print "���������Ϊ��%f" %  s2
        return s2
    def pxsbx(self):
        s3=(self.a*self.b)
        print "ƽ���ı������Ϊ��%f" %  s3
        return s3
    def zjsjx(self):
        s4=((self.a*self.b)/2)
        print "ֱ�����������Ϊ��%f" % s4
        return s4
    def dbsjx(self):
        import math
        a=math.sqrt(3)
        s5=(((self.a**2)*a) /2)
        print "�ȱ����������Ϊ��%f" %  s5
        return s5
    def sjx(self):
        s6=((self.a*self.b)/2)
        print "���������Ϊ��%f" %  s6
        return s6
    def yx(self):
        s7=(3.14*(self.a**2))
        print "Բ�����Ϊ��%f" % s7
        return s7
    def ty(self):
        s8=((self.a*self.b)*3.14)
        print "��Բ���Ϊ��%f" % s8
        return s8

a=graph()
b=[a.jx(),a.zfx(),a.pxsbx(),a.zjsjx(),a.dbsjx(),a.sjx(),a.yx(),a.ty()]

t=0
for i in range(0,7 + 1):
    t=t+b[i]
e=t/8
print "�����Ϊ��%f" % t
print "ƽ�����Ϊ:%f" % e

   

    	
