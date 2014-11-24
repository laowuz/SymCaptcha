from math import sqrt
dic_truth = {}
imgs = open(r'img.truth').read().strip().split('\n')
f = open(r'location.txt','w')
x0,y0,x1,y1 = 147,214,149,13
guess = 0
for img in imgs:
    imgname,sympoints = img.split(':')
    sympoints = sympoints.split('||')[0]
    points = sympoints.strip('()').split('); (')
    p0 = points[0].split(',')
    p1 = points[1].split(',')
    dic_truth[imgname] = [int(p0[0]),int(p0[1]),int(p1[0]),int(p1[1])]
    d00 = sqrt((int(p0[0])-x0)**2+(int(p0[1])-y0)**2)
    d01 = sqrt((int(p0[0])-x1)**2+(int(p0[1])-y1)**2)
    d10 = sqrt((int(p1[0])-x0)**2+(int(p1[1])-y0)**2)
    d11 = sqrt((int(p1[0])-x1)**2+(int(p1[1])-y1)**2)
    if (d00 < 20 and d11 < 20) or (d01<20 and d10<20):
        guess += 1
   #f.write(p0[0]+'\t'+p0[1]+'\n'+p1[0]+'\t'+p1[1]+'\n')

print guess,guess/(len(imgs)+0.0)
#f.close()

D = 30
C = 0
C0 = 0
C_p = 0
imgs = open(r'img.label').read().strip().split('\n')
for img in imgs:
    imgname,sympoints = img.split(':')
    if len(sympoints.split('); ('))< 2:
        continue
    #sympoints = sympoints.split('||')[0]
    sympoints = sympoints[:sympoints.rfind(')')]
    points = sympoints.strip('()').split('); (')
    p0 = points[0].split(',')
    p1 = points[1].split(',')
    x0,y0,x1,y1 = float(p0[0]),float(p0[1]),float(p1[0]),float(p1[1])
    C0 += 1
    if imgname in dic_truth:
        C += 1
        x0_t,y0_t,x1_t,y1_t = 147,214,149,13
        #x0_t,y0_t,x1_t,y1_t = dic_truth[imgname]
        d00 = sqrt((x0-x0_t)**2+(y0-y0_t)**2)
        d01 = sqrt((x0-x1_t)**2+(y0-y1_t)**2)     
        d10 = sqrt((x1-x0_t)**2+(y1-y0_t)**2)
        d11 = sqrt((x1-x1_t)**2+(y1-y1_t)**2)
        if (d00 < D and d11 < D) or (d01<D and d10<D):
            C_p += 1
print C0,C, C_p, C_p/(C+0.0)

