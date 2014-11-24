from django.shortcuts import render_to_response, get_object_or_404
from captcha.models import Caltech256Image
from symcaptcha.models import ImgSymLabel
from django.template import Context, RequestContext
from random import randint
from datetime import datetime
from math import sqrt

def index(request):
    if request.POST:
        data = request.POST.copy()
        name = data['imgname'].split('/')
        rd = ImgSymLabel(category=name[0],imgname=name[1],labeltime=datetime.now(),sympoints=data['coords'],labelusr="laowuz")
        rd.save()
        test_name = data['test_imgname']
        test_cate = data['test_cate']
        test_sym = data['test_sympoints']
        test_rd = ImgSymLabel(category=test_cate,imgname=test_name,labeltime=datetime.now(),sympoints=data['test_coords'],labelusr="laowuz")
        test_rd.save()
        input_sym = data['test_coords']
        if len(input_sym)==0 or len(test_sym)==0:
            return render_to_response('captcha/index1.html', {'failure':True,'test_category':test_cate,'test_imgname':test_name,'test_sympoints':test_sym}, context_instance=RequestContext(request))
        p = test_sym.strip('()').split('); (')
        x0,y0 = p[0].split(',')
        x1,y1 = p[1].split(',')
        p = input_sym.strip('()').split('); (')
        tx0,ty0 = p[0].split(',')
        tx1,ty1 = p[1].split(',')
        d00 = sqrt((int(x0)-int(tx0))**2+(int(y0)-int(ty0))**2)
        d01 = sqrt((int(x0)-int(tx1))**2+(int(y0)-int(ty1))**2)
        d10 = sqrt((int(x1)-int(tx0))**2+(int(y1)-int(ty0))**2)
        d11 = sqrt((int(x1)-int(tx1))**2+(int(y1)-int(ty1))**2)
        if (d00 < 20 and d11 < 20) or (d01<20 and d10<20):
            #test_rd.save()
            max = Caltech256Image.objects.count()
            p = get_object_or_404(Caltech256Image,pk=randint(1,max))
            return render_to_response('captcha/index1.html', {'ok':True,'test_category':p.category,'test_imgname':p.imgname,'test_sympoints':p.sympoints}, context_instance=RequestContext(request))
        else:
            return render_to_response('captcha/index1.html', {'failure':True,'test_category':test_cate,'test_imgname':test_name,'test_sympoints':test_sym}, context_instance=RequestContext(request))
    else:
        max = Caltech256Image.objects.count()
        p = get_object_or_404(Caltech256Image,pk=randint(1,max))
        return render_to_response('captcha/index1.html', {'test_category':p.category,'test_imgname':p.imgname,'test_sympoints':p.sympoints}, context_instance=RequestContext(request))

def submit_label_result(request):
    if request.POST:
        data = request.POST.copy()
        name = data['imgname'].split('/')
        user = data['usr']
        rd = ImgSymLabel(category=name[0],imgname=name[1],time=datetime.now(),sympoints=data['coords'],labelusr=user)
        rd.save()
    return render_to_response('captcha/index.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('captcha/index-with-rotation.html', context_instance=RequestContext(request))

def index_rotate(request):
    if request.POST:
        data = request.POST.copy()
        name = data['imgname'].split('/')
        rd = ImgSymLabel(category=name[0],imgname=name[1],labeltime=datetime.now(),sympoints=data['coords_rot'],labelusr="laowuz")
        rd.save()
        test_name = data['test_imgname']
        test_cate = data['test_cate']
        test_sym = data['test_sympoints']
        test_rd = ImgSymLabel(category=test_cate,imgname=test_name,labeltime=datetime.now(),sympoints=data['test_coords'],labelusr="laowuz")
        test_rd.save()
        input_sym = data['test_coords_rot']
        if len(input_sym)==0 or len(test_sym)==0:
            return render_to_response('captcha/index-with-rotation.html', {'failure':True,'test_category':test_cate,'test_imgname':test_name,'test_sympoints':test_sym}, context_instance=RequestContext(request))
        syms = test_sym.split('||')
        for sym in syms:
            p = test_sym.strip('()').split('); (')
            x0,y0 = p[0].split(',')
            x1,y1 = p[1].split(',')
            p = input_sym.strip('()').split('); (')
            tx0,ty0 = p[0].split(',')
            tx1,ty1 = p[1].split(',')
            d00 = sqrt((int(x0)-int(tx0))**2+(int(y0)-int(ty0))**2)
            d01 = sqrt((int(x0)-int(tx1))**2+(int(y0)-int(ty1))**2)
            d10 = sqrt((int(x1)-int(tx0))**2+(int(y1)-int(ty0))**2)
            d11 = sqrt((int(x1)-int(tx1))**2+(int(y1)-int(ty1))**2)
            if (d00 < 20 and d11 < 20) or (d01<20 and d10<20):
                #test_rd.save()
                max = Caltech256Image.objects.count()
                p = get_object_or_404(Caltech256Image,pk=randint(1,max))
                return render_to_response('captcha/index-with-rotation.html', {'ok':True,'test_category':p.category,'test_imgname':p.imgname,'test_sympoints':p.sympoints}, context_instance=RequestContext(request))
        return render_to_response('captcha/index-with-rotation.html', {'failure':True,'test_category':test_cate,'test_imgname':test_name,'test_sympoints':test_sym}, context_instance=RequestContext(request))
    else:
        max = Caltech256Image.objects.count()
        p = get_object_or_404(Caltech256Image,pk=randint(1,max))
        return render_to_response('captcha/index-with-rotation.html', {'test_category':p.category,'test_imgname':p.imgname,'test_sympoints':p.sympoints}, context_instance=RequestContext(request))
