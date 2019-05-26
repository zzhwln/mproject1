from django.urls import path
from projectapp import views
app_name='projectapp'
urlpatterns = [
   path('bookdetails/',views.bookdetails,name='bookdetails'),
   path('booklist/', views.booklist, name='booklist'),
   path('index/', views.index, name='index'),
   path('addd/', views.addd, name='addd'),
   path('index1/', views.index1, name='index1'),
   path('register/', views.register, name='register'),
   path('register1/', views.register1, name='register1'),
   path('registerok/', views.registerok, name='registerok'),
   path('getcaptc/', views.getcaptc, name='getcaptc'),
   path('yzm/', views.yzm, name='yzm'),
   path('login/', views.login, name='login'),
   path('login1/', views.login1, name='login1'),
   path('shopcart/', views.shopcart, name='shopcart'),
   path('bookdetails1/', views.bookdetails1, name='bookdetails1'),
   path('car/', views.car, name='car'),
   path('add/', views.add, name='add'),
   path('bdel/', views.bdel, name='bdel'),
   path('carcheck/', views.carcheck, name='carcheck'),
   path('mail/', views.mail, name='mail'),
   path('mobilem/', views.mobilem, name='mobilem'),

   path('indent/', views.indent, name='indent'),
   path('indentok/', views.indentok, name='indentok'),

]
