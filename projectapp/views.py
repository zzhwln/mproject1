import os
import uuid
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import random,string
from captcha.image import ImageCaptcha
# Create your views here.

from projectapp.models import BTable, OneClassify, TwoClassify, MessBook, TUser, TSite, TIndent
from projectapp.send_mail import sendmail


def bookdetails1(request):
    """渲染书籍详情页"""
    nickname = request.session.get('nickname1')
    return render(request,'projectapp/Book details.html',{'nickname':nickname})
def bookdetails(request):
    """书籍详情页逻辑处理"""
    nickname = request.session.get('nickname1')#是否存在登录状态
    id=request.session.get('carid')
    """获取书籍id"""
    id=request.GET.get('id')
    if id:
        table = BTable.objects.get(id=id)
        table1 = MessBook.objects.get(idbook=id)
        return render(request, 'projectapp/Book details.html',{'nickname':nickname,'table':table,'table1':table1})
    return redirect('projectapp:bookdetails1')
def booklist(request):
    """书籍分类显示页
    id1一级表对应id;id2二级表对应id
    pnumber点击排序传过来的值
    number点击上一页下一页传过来的值
    anumber输入框传过来的值
    nickname2点击退出传过来的值
    """
    id1 = request.GET.get('id')
    id2 = request.GET.get('id2')
    number=request.GET.get('number')
    anumber=request.GET.get('anumber')
    pnumber=request.GET.get('pnumber')
    # print(pnumber,type(pnumber))
    # print(anumber,number,'1919')
    nickname = request.session.get('nickname1')
    nickname2 = request.GET.get('nickname')
    print(nickname2)
    if nickname2 == '1':
        print(nickname2, '2')
        nickname = ''
        """判断是否点击了上一页下一页"""
    if number:
        id11= request.session.get('id1')
        id22 = request.session.get('id2')
        """判断是属于一级还是二级分类页面"""
        if id22 != '':
            b = TwoClassify.objects.filter(id=id22)
            bname = b[0].s_name
            bid = b[0].id_classify.id
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            table = BTable.objects.filter(id_cla=id22)
            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(number)
            asum=pagtor.num_pages
            return render(request, 'projectapp/booklist.html', {'asum':asum,'id2':id2,'bid':bid,'aname':aname,'bname':bname,"etwo": etwo, "eone": eone, 'page': page, 'id2': id2})
        else:
            bid = id11
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li = []
            table1 = TwoClassify.objects.filter(id_classify=id11)
            for i in table1:
                ta = BTable.objects.filter(id_cla=i)
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(number)
            asum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html', {'asum':asum,'bid':bid,'aname':aname,"etwo": etwo, "eone": eone, 'li': li, 'id2': id2})
    elif anumber:
        print('11111')
        id11 = request.session.get('id1')
        id22 = request.session.get('id2')
        print(id11, id22, '232323')
        if id22 != '':
            b = TwoClassify.objects.filter(id=id22)
            bname = b[0].s_name
            bid = b[0].id_classify.id
            print(id22, bid)
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('2222')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            table = BTable.objects.filter(id_cla=id22)
            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(anumber)
            asum = pagtor.num_pages
            print(pagtor)
            # psum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'id2': id2, 'bid': bid, 'aname': aname, 'bname': bname, "etwo": etwo,
                           "eone": eone, 'page': page, 'id2': id2})
        else:
            bid = id11
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('33333')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li = []
            table1 = TwoClassify.objects.filter(id_classify=id11)
            print(table1, '26')
            for i in table1:
                ta = BTable.objects.filter(id_cla=i)
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(anumber)
            asum = pagtor.num_pages
            # print(li,type(li))
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'bid': bid, 'aname': aname, "etwo": etwo, "eone": eone, 'li': li, 'id2': id2})
    elif pnumber == '2': #排序
        print('11111')
        id11 = request.session.get('id1')
        id22 = request.session.get('id2')
        print(id11, id22, '232323')
        if id22 != '':
            b = TwoClassify.objects.filter(id=id22)
            bname = b[0].s_name
            bid = b[0].id_classify.id
            print(id22, bid)
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('2222')
            if not number:
                number=1
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            table = BTable.objects.filter(id_cla=id22).order_by("-d_pricing")
            # table = BTable.objects.all().order_by("-d_pricing")

            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(number)
            asum = pagtor.num_pages
            print(pagtor)
            # psum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'id2': id2, 'bid': bid, 'aname': aname, 'bname': bname, "etwo": etwo,
                           "eone": eone, 'page': page, 'id2': id2})
        else:
            if not number:
                number=1
            bid = id11
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('33333')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li = []
            table1 = TwoClassify.objects.filter(id_classify=id11)

            print(table1, '26')
            for i in table1:
                ta = BTable.objects.filter(id_cla=i).order_by("-d_pricing")
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(number)
            asum = pagtor.num_pages
            # print(li,type(li))
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'bid': bid, 'aname': aname, "etwo": etwo, "eone": eone, 'li': li, 'id2': id2})
    elif pnumber=='3':
        print('1111122')
        id11 = request.session.get('id1')
        id22 = request.session.get('id2')
        print(id11, id22, '232323')
        if id22 != '':
            b = TwoClassify.objects.filter(id=id22)
            bname = b[0].s_name
            bid = b[0].id_classify.id
            print(id22, bid)
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('2222')
            if not number:
                number=1
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            table = BTable.objects.filter(id_cla=id22).order_by("d_pricing")
            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(number)
            asum = pagtor.num_pages
            print(pagtor)
            # psum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'id2': id2, 'bid': bid, 'aname': aname, 'bname': bname, "etwo": etwo,
                           "eone": eone, 'page': page, 'id2': id2})
        else:
            if not number:
                number=1
            bid = id11
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('33333')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li = []
            table1 = TwoClassify.objects.filter(id_classify=id11)
            print(table1, '26')
            for i in table1:
                ta = BTable.objects.filter(id_cla=i).order_by("d_pricing")
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(number)
            asum = pagtor.num_pages
            # print(li,type(li))
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'bid': bid, 'aname': aname, "etwo": etwo, "eone": eone, 'li': li, 'id2': id2})
    elif pnumber=='4':
        print('11111')
        id11 = request.session.get('id1')
        id22 = request.session.get('id2')
        print(id11, id22, '232323')
        if id22 != '':
            if not number:
                number=1
            b = TwoClassify.objects.filter(id=id22)
            bname = b[0].s_name
            bid = b[0].id_classify.id
            print(id22, bid)
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('2222')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            table = BTable.objects.filter(id_cla=id22)
            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(number)
            asum = pagtor.num_pages
            print(pagtor)
            # psum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'id2': id2, 'bid': bid, 'aname': aname, 'bname': bname, "etwo": etwo,
                           "eone": eone, 'page': page, 'id2': id2})
        else:
            if not number:
                number=1
            bid = id11
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('33333')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li = []
            table1 = TwoClassify.objects.filter(id_classify=id11)
            print(table1, '26')
            for i in table1:
                ta = BTable.objects.filter(id_cla=i)
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(number)
            asum = pagtor.num_pages
            # print(li,type(li))
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'bid': bid, 'aname': aname, "etwo": etwo, "eone": eone, 'li': li, 'id2': id2})
    elif pnumber=='5':
        print('11111')
        id11 = request.session.get('id1')
        id22 = request.session.get('id2')
        print(id11, id22, '232323')
        if id22 != '':
            b = TwoClassify.objects.filter(id=id22)
            bname = b[0].s_name
            bid = b[0].id_classify.id
            print(id22, bid)
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('2222')
            if not number:
                number=1
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            table = BTable.objects.filter(id_cla=id22)
            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(number)
            asum = pagtor.num_pages
            print(pagtor)
            # psum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'id2': id2, 'bid': bid, 'aname': aname, 'bname': bname, "etwo": etwo,
                           "eone": eone, 'page': page, 'id2': id2})
        else:
            if not number:
                number=1
            bid = id11
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('33333')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li = []
            table1 = TwoClassify.objects.filter(id_classify=id11)
            print(table1, '26')
            for i in table1:
                ta = BTable.objects.filter(id_cla=i)
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(number)
            asum = pagtor.num_pages
            # print(li,type(li))
            return render(request, 'projectapp/booklist.html',
                          {'asum': asum, 'bid': bid, 'aname': aname, "etwo": etwo, "eone": eone, 'li': li, 'id2': id2})

    else:

        print('4444')
        request.session['id1'] = id1
        if id2 !='':
            b = TwoClassify.objects.filter(id=id2)
            bname = b[0].s_name
            bid=b[0].id_classify.id
            print(id2, bid)
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            # print(bid,aname,'6161')
            request.session['id2'] = id2
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            print(11111111111)
            print(bname,'5858')
            if not number:
                number=1
            table=BTable.objects.filter(id_cla=id2)
            pagtor = Paginator(table, per_page=4)
            page = pagtor.page(number)
            print(pagtor)
            asum = pagtor.num_pages
            print(asum,'848484',type(asum))
        # psum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',{'nickname':nickname,'asum':asum,'bid':bid,'id2':id2,'aname':aname,'bname':bname,"etwo":etwo, "eone": eone,'page':page,'id2':id2})
        else:
            bid=id1
            a = OneClassify.objects.filter(id=bid)
            aname = a[0].z_name
            print('55555')
            etwo = TwoClassify.objects.all()
            eone = OneClassify.objects.all()
            li=[]
            if not number:
                number=1
            table1=TwoClassify.objects.filter(id_classify=id1)
            print(table1,'26')
            for i in table1:
                ta=BTable.objects.filter(id_cla=i)
                li.append(ta)
            pagtor = Paginator(li, per_page=2)
            li = pagtor.page(number)
             # print(li,type(li))
            asum = pagtor.num_pages
            return render(request, 'projectapp/booklist.html',{'nickname':nickname,'asum':asum,'aname':aname,'bid':bid,"etwo":etwo, "eone": eone,'li':li,'id2':id2})

def login(request):
    return render(request,'projectapp/login.html')

def login1(request):
    txtPassword=request.POST.get('txtPassword')
    txtUsername=request.POST.get('txtUsername')
    print('379',txtUsername,txtPassword)
    fs=TUser.objects.filter(nickname=txtUsername,password=txtPassword)
    for i in fs:
        aass=i.aass
        print(aass,type(aass))
    print(type(fs),aass,'375')
    dindent=request.session.get('dizhi')
    print(dindent,'379')
    if fs!='' and aass == '1' and dindent == 'a':
        request.session['nickname']=txtUsername#登录成功存入状态
        request.session['dizhi'] = ''
        return redirect('projectapp:indent')
    elif fs!='' and aass=='1':
        print()
        request.session['nickname']=txtUsername#登录成功存入状态
        return redirect('projectapp:index')

    else:
        return render(request, 'projectapp/login.html')


def index(request):
    nickname = request.session.get('nickname1')
    nickname2 = request.GET.get('nickname')
    print(nickname2)
    if nickname2=='1':
        print(nickname2,'2')
        nickname=''
        request.session['nickname']=nickname
    print(nickname,'12312313')
    etwo =TwoClassify.objects.all()
    eone=OneClassify.objects.all()
    etable=BTable.objects.order_by("pricing","-d_pricing")[0:10]
    # aa=1
    # for i in etable:
    #     etable.create(column_9=aa)
    #     aa+=1
    #     print(i.column_9)
    return render(request, 'projectapp/index.html', {"nickname":nickname,"etwo":etwo, "eone": eone,'etable':etable})
def addd(request):
    return render(request, 'projectapp/addEmp.html')
def index1(request):
    pics = request.FILES.get('pics')  # 接收文件
    exc = os.path.splitext(pics.name)[1]
    pics.name = str(uuid.uuid4()) + exc

    e=BTable.objects.get(id=1)
    # e = BTable( pic=pics)  # 创建对象
    e.pic=pics
    e.save()

    try:

            return render(request, "workapp/emplist.html")

    except:
        return HttpResponse('出错了')

def register(request):
    nickname = request.session.get('nickname1')
    return render(request,'projectapp/register.html',{'nickname':nickname})

def mobilem(request):
    mobile = request.GET.get('mobile')
    print(mobile, '417')
    mobile1 = request.session.get('mobile')
    if mobile == mobile1:
        request.session['mobile'] = '12'
        request.session['aass'] = '1'
        return HttpResponse('ok')
    else:
        request.session['aass'] = '0'
        request.session['mobile1'] = '1'
        return HttpResponse('no')
def register1(request):
    # mobile1 = request.session.get('mobile1')
    aass=request.session.get('aass')
    print(aass,'434')
    if aass!='1':
        aass=='0'
    # mobile=request.POST.get('mobile')
    txt_username=request.POST.get('txt_username')
    username=request.POST.get('username')
    txt_repassword=request.POST.get('txt_repassword')
    fs=TUser.objects.filter(email=txt_username)
    # if fs:
    #     return HttpResponse('注册失败邮箱已存在！')
    #
    TUser.objects.create(email=txt_username,nickname=username,password=txt_repassword,aass=aass)
    print(txt_repassword,username,txt_username,'425')
    dindent = request.session.get('dizhi')
    print(dindent, '379')
    if aass == '1' and dindent == 'a':
        request.session['nickname1'] = username  # 登录成功存入状态
        request.session['dizhi'] = ''
        print(username,aass)
        return redirect('projectapp:indent')
    elif aass!='1':
        return redirect('projectapp:login')
    request.session['nickname'] = username  # 登录成功存入状态
    return redirect('projectapp:registerok')
    # return render(request,'projectapp/register ok.html')

def registerok(request):
    nickname=request.session.get('nickname')
    return render(request,'projectapp/register ok.html',{'nickname':nickname})
def getcaptc(request):
    image=ImageCaptcha()
    rand_code=random.sample(string.ascii_letters+string.digits,4)
    rand_code="".join(rand_code)
    request.session['code']=rand_code
    data=image.generate(rand_code)
    print(rand_code)
    return HttpResponse(data,'image/png')

def yzm(request):
    # time.sleep(5)
    code1=request.GET.get('txt_vcode')
    print(code1,'111111111')
    code=request.session.get('code')

    if code.lower()==code1.lower():
        return HttpResponse('ok')
    else:
        return HttpResponse('no')
def shopcart (request):
    # li = []
    b=0
    id=request.GET.get('id')
    bsum=request.GET.get('bsum')
    print(id,bsum,'498')
    shop=request.session.get('shopca')
    request.session['carid'] = id
    if shop:
        print(shop,'496')
        for i in shop:
            print(i,'498')
            if i['id']==id:
                a=i['bsum']+bsum
                i['bsum']=a
                print(i['bsum'],'499')
                print(i)
                print(b,'505')
                shop[b]=i
                # print(shop)
                request.session['shopca'] = shop
                return redirect('projectapp:bookdetails')

            table = BTable.objects.get(id=int(id))
            bname = table.b_name
            bpic = str(table.pic)
            bdpri = table.d_pricing
            bpri = table.pricing
            zt = 1
            bsum = bsum
            li1 = {'id': id, 'bname': bname, 'bpic': bpic, 'bdpri': bdpri, 'bpri': bpri, 'zt': zt, 'bsum': bsum}
            shop.append(li1)
            print(shop, '521')
            b += 1
            request.session['shopca'] =shop
            return redirect('projectapp:bookdetails')

        # return redirect('projectapp:bookdetails')
    else:
        shop = [{'id':'', 'bname':'', 'bpic':'', 'bdpri':'', 'bpri':'', 'zt': '', 'bsum':''},]
        table = BTable.objects.get(id=int(id))
        bname = table.b_name
        bpic = str(table.pic)
        bdpri = table.d_pricing
        bpri = table.pricing
        zt = 1
        bsum = bsum
        li1 = {'id': id, 'bname': bname, 'bpic': bpic, 'bdpri': bdpri, 'bpri': bpri, 'zt': zt, 'bsum': bsum}
        shop.append(li1)
        print(li1)
        request.session['shopca'] = shop
        return redirect('projectapp:bookdetails')

def car(request):
    nickname = request.session.get('nickname1')
    b=0
    data = request.session.get('shopca')
    print(data,'557')
    sdel=request.GET.get('del')
    recover=request.GET.get('recover')
    sum=0
    jsum=0
    print(sdel,type(sdel))
    if data != None:
        for i in data:
            if sdel == i['id']:
                print(535)
                i['zt'] = ''
                data[b] = i
            if i['bsum']:
                if i['zt']==1:
                    sum+=int(i['bdpri'])*int(i['bsum'])
                    aa= int(i['bdpri'])*int(i['bsum'])
                    i['bpri']=str(aa)
                    jsum+=(int(i['bpri'])*int(i['bsum'])-int(i['bdpri'])*int(i['bsum']))
            elif recover==i['id']:
                i['zt'] = 1
                data[b] = i
            request.session['shopca'] = data
            b+=1
    request.session['shopca'] =data
    return render(request,'projectapp/car.html',{'nickname':nickname,'data':data,'sum':sum,'jsum':jsum})


def indent(request):
    nickname = request.session.get('nickname1')
    data = request.session.get('shopca')
    siteid = request.GET.get('id')
    """jsonResponse转换"""
    def mydefault(u):
        if isinstance(u,TSite):
            return {"id":u.id,"Name":u.addresname,'directin':u.directin,'zipcode':u.zipcode,'mobilephone':u.mobilephone}
    print(siteid,type(siteid))
    """判断是否点击了配送地址"""
    sitedata = TSite.objects.all()
    if data:
        if nickname:
            if siteid=='a':
                return HttpResponse('')
                print(siteid, '591')
            elif siteid:
                page = TSite.objects.filter(id=int(siteid))
                print(page, '599')
                return JsonResponse({"use": list(page)}, json_dumps_params={"default": mydefault})

            return render(request,'projectapp/indent.html',{'sitedata':sitedata,'siteid':siteid,'nickname':nickname,'data':data})
        else:
            request.session['dizhi']='a'
            return redirect('projectapp:login')
    else:
        return redirect('projectapp:index')



def indentok(request):
    uname=request.session.get('nickname1')
    print(uname,'594')
    if uname:
        """地址存入数据库"""
        username=TUser.objects.get(nickname=uname)
        checkname = request.POST.get('checkname')#收件人姓名
        directin = request.POST.get('addcheckname1')  # 收货地址
        zipcode = request.POST.get('checkname2')  # 邮政编码
        mobilephone = request.POST.get('checkname3')  # 手机
        re= username.tsite_set.create( addresname=checkname,directin=directin,zipcode=zipcode,mobilephone=mobilephone)
        print(re,'605')
        data = request.session.get('shopca')
        for i in data:
            """订单信息存入数据库"""
            add=TIndent()
            tradename=i['bname']
            makeprice=i['bpri']
            money=i['bdpri']
            bumber=i['bsum']
            # id_user=uid
            siteid=i['id']  #书本id
            state=i['zt']
            column_12=i['bpic']#书的图片
            # save()
            username.tindent_set.create( column_12=column_12,state=state,bumber=bumber,money=money,tradename=tradename,makeprice=makeprice)
            # print(re,'605')
    nickname = request.session.get('nickname1')
    return render(request,'projectapp/indent ok.html',{'nickname':nickname})
def add(request):
    id=request.GET.get('id')
    b=0
    data = request.session.get('shopca')
    asum=0
    for i in data:
        if i['id']==id:
            bsum = int(i['bsum']) + 1
            sum = int(i['bdpri']) * int(bsum)
            print(bsum,sum,'123')
            i['bsum'] = bsum
            i['sum'] = sum
            data[b] = i
            request.session['shopca'] = data
        if i['bdpri']:
            asum += int(i['bdpri']) * int(i['bsum'])
        b+=1
    return JsonResponse({'bsum':bsum,'sum':sum,'asum':asum})
    # return HttpResponse(123)
def bdel(request):
    id = request.GET.get('id')
    print(id, '588')
    b=0
    data = request.session.get('shopca')
    asum=0
    for i in data:
        print(i['id'], type(i['id']))
        print(id, type(id))
        if i['id'] == id:
            bsum = int(i['bsum']) - 1
            if bsum <1:
                bsum=1
            sum = int(i['bdpri']) * int(bsum)
            print(bsum, sum, '123')
            i['bsum'] = bsum
            i['sum'] = sum
            data[b] = i
            request.session['shopca'] = data
        if i['bdpri']:
            asum += int(i['bdpri']) * int(i['bsum'])
        b+=1
    return JsonResponse({'bsum': bsum, 'sum': sum,'asum':asum})

def carcheck(request):
    id=request.GET.get('id')
    num=request.GET.get('num')
    print(id,'588')
    b=0
    data = request.session.get('shopca')
    asum=0
    for i in data:
        print(i['id'],type(i['id']))
        print(id,type(id))
        if i['id']==id:
            i['bsum'] =int(num)
            sum = int(i['bdpri']) * int(num)
            print(num,sum,'123')
            i['bsum'] = int(num)
            i['sum'] = sum
            data[b] = i
            request.session['shopca'] = data
        if i['bdpri']:
            asum += int(i['bdpri']) * int(i['bsum'])
        print(asum, '689',type(asum))
        b+=1
    return JsonResponse({'bsum':num,'sum':sum,'asum':asum})
"""随机获取字符串"""
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def mail(request):
    a=request.GET.get('id')
    print(a,'123')
    # a1='17319366584@sina.cn'
    if a:
        ma=id_generator()
        request.session['mobile']=ma
        c=sendmail(ma,a)
        print(c)
    return HttpResponse(123)
