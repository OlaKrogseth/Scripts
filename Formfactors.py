import jscatter as js
import numpy as np

#gaussianChain
q=js.loglist(0.1,8,100)
p=js.grace()
for nu in np.r_[0.3:0.61:0.05]:
   iq=js.ff.gaussianChain(q,2,nu)
   p.plot(iq,le='nu= $nu')
p.yaxis(label='I(q)',scale='l',min=1e-3,max=1)
p.xaxis(label='q / nm\S-1',scale='l')
p.legend(x=0.2,y=0.1)
p.title('Gaussian chains')
#p.save(js.examples.imagepath+'/gaussianChain.jpg')


#Sphere
q=js.loglist(0.1,5,300)
p=js.grace()
R=3
sp=js.ff.sphere(q, R)
p.plot(sp.X*R,sp.Y,li=1)
p.yaxis(label='I(q)',scale='l',min=1e-4,max=1e5)
p.xaxis(label='qR',scale='l',min=0.1*R,max=5*R)
p.legend(x=0.15,y=0.1)
#p.save(js.examples.imagepath+'/sphere.jpg')


#Cylinder
q=js.loglist(0.01,8,500)
p=js.grace()
p.multi(1,2)
R=2
for L in [20,40,150]:
    cc=js.ff.cylinder(q,L=L,radius=R)
    p[0].plot(cc,li=-1,sy=0,le='L ={0:.0f} R={1:.1f}'.format(L,R))
L=60
for R in [1,2,4]:
    cc=js.ff.cylinder(q,L=L/R**2,radius=R)
    p[1].plot(cc,li=-1,sy=0,le='L ={0:.2f} R={1:.1f}'.format(L/R**2,R))
p[0].yaxis(label='I(q)',scale='l',min=1e-6,max=10)
p[0].xaxis(label='q / nm\S-1',scale='l',min=0.01,max=6)
p[1].yaxis(label='I(q)',scale='l',min=1e-7,max=1)
p[1].xaxis(label='q / nm\S-1',scale='l',min=0.01,max=6)
p[1].text(r'forward scattering I0\n=(SLD*L\xp\f{}R\S2\N)\S2\N = 0.035530',x=0.02,y=0.1)
p.title('cylinder')
p[0].legend(x=0.012,y=0.001)
p[1].legend(x=0.012,y=0.0001)
#p.save(js.examples.imagepath+'/cylinder.jpg')

#Core shell
q=js.loglist(0.01,5,500)
p=js.grace()
FF=js.ff.sphereCoreShell(q,6,12,-0.2,1)
p.plot(FF,sy=[1,0.2],li=1)
p.yaxis(label='I(q)',scale='l',min=1,max=1e8)
p.xaxis(label='q / nm\S-1',scale='l')
#p.save(js.examples.imagepath+'/sphereCoreShell.jpg')
