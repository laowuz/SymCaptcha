from django.shortcuts import render_to_response,render,get_object_or_404
from django import forms
from captcha.fields import CaptchaField
from captcha.models import Caltech256Image
from django.template import Context, RequestContext, loader
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import datetime

TEST_TEMPLATE = r'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8">
        <title>captcha test</title>
    </head>
    <body>
        {% if passed %}
        <p style="color:green">Form validated</p>    
        {% endif %}
        <form action="{% url captcha-test %}" method="post">
            {{form.as_p}}
            <p><input type="submit" value="Continue &rarr;"></p>
        </form>
    </body>
</html>
'''

def test(request):
    
    class CaptchaTestForm(forms.Form):
        subject = forms.CharField(max_length=100)
        sender = forms.EmailField()
        captcha = CaptchaField(help_text='asdasd')
    
    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            passed = True
    else:
        form = CaptchaTestForm()
        
    t = loader.get_template_from_string(TEST_TEMPLATE)
    return HttpResponse(t.render(RequestContext(request, locals())))

def test_img1(request):
    if request.POST:
        data = request.POST.copy()
        name = data['imgname'].split('/')
        if len(Caltech256Image.objects.filter(imgname=name[1]))==0:
            newRecord = Caltech256Image(imgname=name[1],category=name[0],labeldate=datetime.now(),sympoints=data['coords'])
            newRecord.save()
        else:
            p = get_object_or_404(Caltech256Image,imgname=name[1])
            p.sympoints = p.sympoints + '||' + data['coords']
            p.save()
        #return render_to_response('captcha/temp.html',{'error':True,'hash':hash},context_instance=RequestContext(request))
    return render_to_response('captcha/label.html',context_instance=RequestContext(request))

def test_img(request):
    im = Image.open('img/012_0003.jpg')
    draw = ImageDraw.Draw(im)
    imgtext = ''.join([choice('QWERTYUOPASDFGHJKLZXCVBNM') for i in range(5)])
    draw.text((10,10),imgtext, fill=(100,100,50))
    tempname = 'temp.jpg'
    im.save('img/temp.jpg','JPEG')
    if request.POST:
        return render_to_response('temp.html',{'ok':True,'tempname':tempname})
    else:
        return render_to_response('temp.html',{'error':True,'tempname':tempname})


def test_custom_error_message(request):

    class CaptchaTestForm(forms.Form):
        captcha = CaptchaField(help_text='asdasd', error_messages=dict(invalid='TEST CUSTOM ERROR MESSAGE'))

    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            passed = True
    else:
        form = CaptchaTestForm()

    t = loader.get_template_from_string(TEST_TEMPLATE)
    return HttpResponse(t.render(RequestContext(request, locals())))



def test_per_form_format(request):
    
    class CaptchaTestForm(forms.Form):
        captcha = CaptchaField(help_text='asdasd', error_messages=dict(invalid='TEST CUSTOM ERROR MESSAGE'), \
            output_format=u'%(image)s testPerFieldCustomFormatString %(hidden_field)s %(text_field)s' )

    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            passed = True
    else:
        form = CaptchaTestForm()

    t = loader.get_template_from_string(TEST_TEMPLATE)
    return HttpResponse(t.render(RequestContext(request, locals())))
