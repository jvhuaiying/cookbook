import json

from django.shortcuts import render, HttpResponse

from . import models


# Create your views here.
def xzcpu(request):
    return render(request, 'hxnrong/xzcpu.html')


def xzcpunrong(request):
    g = json.loads(request.body)
    cpmcheng = g['cpmcheng']
    zscmchengarr = g['zscmchengarr']
    zsczliangarr = g['zsczliangarr']
    zlmchengarr = g['zlmchengarr']
    zlzliangarr = g['zlzliangarr']
    tlmchengarr = g['tlmchengarr']
    tlzliangarr = g['tlzliangarr']
    zhunbeibuzhou = g['zhunbeibuzhou']
    sjiedianarr = g['sjiedianarr']
    hliarr = g['hliarr']
    dzuoarr = g['dzuoarr']
    zysxiang = g['zysxiang']
    for h in zscmchengarr:
        models.Zscai(cpmcheng_zscai=cpmcheng, scmcheng_zscai=h,
                     sczliang_zscai=zsczliangarr[zscmchengarr.index(h)]).save()
    for i in zlmchengarr:
        models.Zliao(cpmcheng_zliao=cpmcheng, scmcheng_zliao=i, sczliang_zliao=zlzliangarr[zlmchengarr.index(i)]).save()
    for j in tlmchengarr:
        models.Tliao(cpmcheng_tliao=cpmcheng, scmcheng_tliao=j, sczliang_tliao=tlzliangarr[tlmchengarr.index(j)]).save()
    models.Zbzhou(cpmcheng_zbzhou=cpmcheng, zbzhou_zbzhou=zhunbeibuzhou).save()
    for k in sjiedianarr:
        models.Caibzhou(cpmcheng_caibzhou=cpmcheng, sjiedian_caibzhou=int(k),
                        hliang_caibzhou=int(hliarr[sjiedianarr.index(k)]),
                        dzuo_caibzhou=dzuoarr[sjiedianarr.index(k)]).save()
    models.Zysxiang(cpmcheng_zysxiang=cpmcheng, zysxiang_zysxiang=zysxiang).save()
    return HttpResponse('添加成功！')


def cpxze(request):
    return render(request, 'hxnrong/cpxze.html')


def hqcplbiao(request):
    a = models.Zbzhou.objects.all()
    b = []
    for c in a:
        b.append(c.cpmcheng_zbzhou)
    return HttpResponse(json.dumps(b))


def hqcliao(request):
    d = json.loads(request.body)
    e = d['xzdcpu']
    f = []
    for g in models.Xzdcpu.objects.all():
        f.append(g.cpmcheng_xzdcpu)
    for h in e:
        if h not in f:
            models.Xzdcpu(cpmcheng_xzdcpu=h).save()
    return HttpResponse('提交成功！')


def clqdan(request):
    return render(request, 'hxnrong/clqdan.html')


def getclqdan(request):
    a = models.Xzdcpu.objects.all()
    b = []
    for c in a:
        b.append(c.cpmcheng_xzdcpu)
    zscmcheng1 = []
    zsczliang1 = []
    zlcmcheng1 = []
    zlczliang1 = []
    tlcmcheng1 = []
    tlczliang1 = []
    zbzhou1 = []
    zscmcheng2 = []
    zsczliang2 = []
    zlcmcheng2 = []
    zlczliang2 = []
    tlcmcheng2 = []
    tlczliang2 = []
    zbzhou2 = []
    zscmcheng3 = []
    zsczliang3 = []
    zlcmcheng3 = []
    zlczliang3 = []
    tlcmcheng3 = []
    tlczliang3 = []
    zbzhou3 = []
    zscmcheng4 = []
    zsczliang4 = []
    zlcmcheng4 = []
    zlczliang4 = []
    tlcmcheng4 = []
    tlczliang4 = []
    zbzhou4 = []
    d = len(b)
    e1 = models.Zscai.objects.all()
    e2 = models.Zliao.objects.all()
    e3 = models.Tliao.objects.all()
    e4 = models.Zbzhou.objects.all()
    if len(b) == 1:
        for f in e1:
            if f.cpmcheng_zscai == b[0]:
                zscmcheng1.append(f.scmcheng_zscai)
                zsczliang1.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[0]:
                zlcmcheng1.append(f.scmcheng_zliao)
                zlczliang1.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[0]:
                tlcmcheng1.append(f.scmcheng_tliao)
                tlczliang1.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[0]:
                zbzhou1.append(f.zbzhou_zbzhou)
        return HttpResponse(
            json.dumps({'cpmcheng': b, 'zscmcheng1': zscmcheng1, 'zsczliang1': zsczliang1, 'zlcmcheng1': zlcmcheng1,
                        'zlczliang1': zlczliang1, 'tlcmcheng1': tlcmcheng1, 'tlczliang1': tlczliang1,
                        'zbzhou1': zbzhou1}))
    elif len(b) == 2:
        for f in e1:
            if f.cpmcheng_zscai == b[0]:
                zscmcheng1.append(f.scmcheng_zscai)
                zsczliang1.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[0]:
                zlcmcheng1.append(f.scmcheng_zliao)
                zlczliang1.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[0]:
                tlcmcheng1.append(f.scmcheng_tliao)
                tlczliang1.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[0]:
                zbzhou1.append(f.zbzhou_zbzhou)
        for f in e1:
            if f.cpmcheng_zscai == b[1]:
                zscmcheng2.append(f.scmcheng_zscai)
                zsczliang2.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[1]:
                zlcmcheng2.append(f.scmcheng_zliao)
                zlczliang2.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[1]:
                tlcmcheng2.append(f.scmcheng_tliao)
                tlczliang2.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[1]:
                zbzhou2.append(f.zbzhou_zbzhou)
        return HttpResponse(
            json.dumps({'cpmcheng': b, 'zscmcheng1': zscmcheng1, 'zsczliang1': zsczliang1, 'zlcmcheng1': zlcmcheng1,
                        'zlczliang1': zlczliang1, 'tlcmcheng1': tlcmcheng1, 'tlczliang1': tlczliang1,
                        'zbzhou1': zbzhou1,
                        'zscmcheng2': zscmcheng2, 'zsczliang2': zsczliang2, 'zlcmcheng2': zlcmcheng2,
                        'zlczliang2': zlczliang2, 'tlcmcheng2': tlcmcheng2, 'tlczliang2': tlczliang2,
                        'zbzhou2': zbzhou2}))
    elif len(b) == 3:
        for f in e1:
            if f.cpmcheng_zscai == b[0]:
                zscmcheng1.append(f.scmcheng_zscai)
                zsczliang1.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[0]:
                zlcmcheng1.append(f.scmcheng_zliao)
                zlczliang1.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[0]:
                tlcmcheng1.append(f.scmcheng_tliao)
                tlczliang1.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[0]:
                zbzhou1.append(f.zbzhou_zbzhou)
        for f in e1:
            if f.cpmcheng_zscai == b[1]:
                zscmcheng2.append(f.scmcheng_zscai)
                zsczliang2.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[1]:
                zlcmcheng2.append(f.scmcheng_zliao)
                zlczliang2.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[1]:
                tlcmcheng2.append(f.scmcheng_tliao)
                tlczliang2.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[1]:
                zbzhou2.append(f.zbzhou_zbzhou)
        for f in e1:
            if f.cpmcheng_zscai == b[2]:
                zscmcheng3.append(f.scmcheng_zscai)
                zsczliang3.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[2]:
                zlcmcheng3.append(f.scmcheng_zliao)
                zlczliang3.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[2]:
                tlcmcheng3.append(f.scmcheng_tliao)
                tlczliang3.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[2]:
                zbzhou3.append(f.zbzhou_zbzhou)
        return HttpResponse(json.dumps(
            {'cpmcheng': b, 'zscmcheng1': zscmcheng1, 'zsczliang1': zsczliang1, 'zlcmcheng1': zlcmcheng1,
             'zlczliang1': zlczliang1, 'tlcmcheng1': tlcmcheng1, 'tlczliang1': tlczliang1, 'zbzhou1': zbzhou1,
             'zscmcheng2': zscmcheng2,
             'zsczliang2': zsczliang2, 'zlcmcheng2': zlcmcheng2, 'zlczliang2': zlczliang2, 'tlcmcheng2': tlcmcheng2,
             'tlczliang2': tlczliang2, 'zbzhou2': zbzhou2, 'zscmcheng3': zscmcheng3, 'zsczliang3': zsczliang3,
             'zlcmcheng3': zlcmcheng3,
             'zlczliang3': zlczliang3, 'tlcmcheng3': tlcmcheng3, 'tlczliang3': tlczliang3, 'zbzhou3': zbzhou3}))
    elif len(b) == 4:
        for f in e1:
            if f.cpmcheng_zscai == b[0]:
                zscmcheng1.append(f.scmcheng_zscai)
                zsczliang1.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[0]:
                zlcmcheng1.append(f.scmcheng_zliao)
                zlczliang1.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[0]:
                tlcmcheng1.append(f.scmcheng_tliao)
                tlczliang1.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[0]:
                zbzhou1.append(f.zbzhou_zbzhou)
        for f in e1:
            if f.cpmcheng_zscai == b[1]:
                zscmcheng2.append(f.scmcheng_zscai)
                zsczliang2.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[1]:
                zlcmcheng2.append(f.scmcheng_zliao)
                zlczliang2.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[1]:
                tlcmcheng2.append(f.scmcheng_tliao)
                tlczliang2.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[1]:
                zbzhou2.append(f.zbzhou_zbzhou)
        for f in e1:
            if f.cpmcheng_zscai == b[2]:
                zscmcheng3.append(f.scmcheng_zscai)
                zsczliang3.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[2]:
                zlcmcheng3.append(f.scmcheng_zliao)
                zlczliang3.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[2]:
                tlcmcheng3.append(f.scmcheng_tliao)
                tlczliang3.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[2]:
                zbzhou3.append(f.zbzhou_zbzhou)
        for f in e1:
            if f.cpmcheng_zscai == b[3]:
                zscmcheng4.append(f.scmcheng_zscai)
                zsczliang4.append(f.sczliang_zscai)
        for f in e2:
            if f.cpmcheng_zliao == b[3]:
                zlcmcheng4.append(f.scmcheng_zliao)
                zlczliang4.append(f.sczliang_zliao)
        for f in e3:
            if f.cpmcheng_tliao == b[3]:
                tlcmcheng4.append(f.scmcheng_tliao)
                tlczliang4.append(f.sczliang_tliao)
        for f in e4:
            if f.cpmcheng_zbzhou == b[3]:
                zbzhou4.append(f.zbzhou_zbzhou)
        return HttpResponse(json.dumps(
            {'cpmcheng': b, 'zscmcheng1': zscmcheng1, 'zsczliang1': zsczliang1, 'zlcmcheng1': zlcmcheng1,
             'zlczliang1': zlczliang1, 'tlcmcheng1': tlcmcheng1, 'tlczliang1': tlczliang1, 'zscmcheng2': zscmcheng2,
             'zsczliang2': zsczliang2, 'zlcmcheng2': zlcmcheng2, 'zlczliang2': zlczliang2, 'tlcmcheng2': tlcmcheng2,
             'tlczliang2': tlczliang2, 'zscmcheng3': zscmcheng3, 'zsczliang3': zsczliang3, 'zlcmcheng3': zlcmcheng3,
             'zlczliang3': zlczliang3, 'tlcmcheng3': tlcmcheng3, 'tlczliang3': tlczliang3, 'zscmcheng4': zscmcheng4,
             'zsczliang4': zsczliang4, 'zlcmcheng4': zlcmcheng4, 'zlczliang4': zlczliang4, 'tlcmcheng4': tlcmcheng4,
             'tlczliang4': tlczliang4, 'zbzhou1': zbzhou1, 'zbzhou2': zbzhou2, 'zbzhou3': zbzhou3, 'zbzhou4': zbzhou4}))


def chaocaiymian(request):
    return render(request, 'hxnrong/kschaocai.html')


def kschaocai(request):
    a = models.Xzdcpu.objects.all()
    b = []
    for c in a:
        b.append(c.cpmcheng_xzdcpu)
    return HttpResponse(json.dumps(b))


def hqbuzhou(request):
    a1 = models.Caibzhou.objects.all()
    a2 = json.loads(request.body)
    sjiedian = []
    hli = []
    dzuo = []
    for b in a1:
        if b.cpmcheng_caibzhou == a2['cpmcheng']:
            sjiedian.append(b.sjiedian_caibzhou)
            hli.append(b.hliang_caibzhou)
            dzuo.append(b.dzuo_caibzhou)
    c = {'sjiedian': sjiedian, 'dzuo': dzuo, 'hli': hli}
    return HttpResponse(json.dumps(c))


def yjrcpuljie(request):
    a = models.Zbzhou.objects.all()
    a1 = models.Xzdcpu.objects.all()
    b = []
    b1 = []
    for c in a:
        b.append(c.cpmcheng_zbzhou)
    for c in a1:
        if c.cpmcheng_xzdcpu in b:
            b1.append(c.cpmcheng_xzdcpu)
    return HttpResponse(json.dumps(b1))



def yxzcpsjkschuang(request):
    a = json.loads(request.body)
    a1 = models.Xzdcpu.objects.all()
    for b in a1:
        if b.cpmcheng_xzdcpu == a['cpmc']:
            b.delete()
    return HttpResponse('删除成功')


# 数据检索
def ssjsuo(request):
    a = models.Xzdcpu.objects.all()
    a1 = models.Zbzhou.objects.all()
    b = []
    b1 = []
    b2 = []
    for c in a:
        b.append(c.cpmcheng_xzdcpu)
    for c in a1:
        if c.cpmcheng_zbzhou not in b:
            b1.append(c.cpmcheng_zbzhou)
    d = json.loads(request.body)
    d1 = d['jsuo']
    for c in b1:
        if d1 == '':
            print(b1)
            return HttpResponse(json.dumps(b1))
        else:
            if c.find(d1) != -1:
                b2.append(c)
    return HttpResponse(json.dumps(b2))


def gli(request):
    return render(request, 'hxnrong/glymian.html')


def cpgli(request):
    return render(request, 'hxnrong/cpgli.html')


def hqbucp(request):
    a = models.Zbzhou.objects.all()
    b = []
    for c in a:
        b.append(c.cpmcheng_zbzhou)
    return HttpResponse(json.dumps(b))


def hqbucp1(request):
    a = models.Zbzhou.objects.all()
    b = []
    c = json.loads(request.body)
    d = c['nrsuo']
    for e in a:
        if e.cpmcheng_zbzhou.find(d) != -1:
            b.append(e.cpmcheng_zbzhou)
    return HttpResponse(json.dumps(b))


def bjcpu1(request):
    a = json.loads(request.body)
    a1 = a['bjcpu1']
    a2 = models.Xybji.objects.all()
    for b in a2:
        if b.cpmcheng_xybji != '':
            b.delete()
    models.Xybji(cpmcheng_xybji=a1).save()
    return HttpResponse('添加成功')


def cpglxzcpu(request):
    a = models.Xybji.objects.all()
    a1 = models.Xzdcpu.objects.all()
    b = []
    for c in a:
        b.append(c.cpmcheng_xybji)
        c.delete()
    if len(b) == 0:
        return HttpResponse('没有数据')
    else:
        for c in a1:
            if c.cpmcheng_xzdcpu in b:
                c.delete()
        d = b[0]
        a1 = models.Zscai.objects.all()
        b1 = []
        b2 = []
        for c in a1:
            if c.cpmcheng_zscai == d:
                b1.append(c.scmcheng_zscai)
                b2.append(c.sczliang_zscai)
                c.delete()
        a2 = models.Zliao.objects.all()
        b3 = []
        b4 = []
        for c in a2:
            if c.cpmcheng_zliao == d:
                b3.append(c.scmcheng_zliao)
                b4.append(c.sczliang_zliao)
                c.delete()
        a3 = models.Tliao.objects.all()
        b5 = []
        b6 = []
        for c in a3:
            if c.cpmcheng_tliao == d:
                b5.append(c.scmcheng_tliao)
                b6.append(c.sczliang_tliao)
                c.delete()
        a4 = models.Zbzhou.objects.all()
        b7 = []
        for c in a4:
            if c.cpmcheng_zbzhou == d:
                b7.append(c.zbzhou_zbzhou)
                c.delete()
        a5 = models.Caibzhou.objects.all()
        b8 = []
        b9 = []
        b10 = []
        for c in a5:
            if c.cpmcheng_caibzhou == d:
                b8.append(c.sjiedian_caibzhou)
                b9.append(c.hliang_caibzhou)
                b10.append(c.dzuo_caibzhou)
                c.delete()
        a6 = models.Zysxiang.objects.all()
        b11 = []
        for c in a6:
            if c.cpmcheng_zysxiang == d:
                b11.append(c.zysxiang_zysxiang)
                c.delete()
        return HttpResponse(json.dumps(
            {'b': b, 'b1': b1, 'b2': b2, 'b3': b3, 'b4': b4, 'b5': b5, 'b6': b6, 'b7': b7, 'b8': b8, 'b9': b9,
             'b10': b10, 'b11': b11}))


def cpglbji(request):
    return render(request, 'hxnrong/cpglbji.html')
