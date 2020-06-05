from django.urls import path



from .import views

urlpatterns = [

    path('user/', views.userlist,name='userlist'),
    path('user/<str:pk>/', views.userdetail,name='userdetail'),
    path('user-create/', views.usercreate,name='usercreate'),
    path('user-update/<str:pk>', views.userupdate,name='userupdate'),
    path('user-delete/<str:pk>', views.userdelete,name='userdelete'),


    path('signup/', views.usersignup,name='signup'),
    path('signup/<str:pk>/', views.usersignupdetail,name='profile'),
    #path('login/', views.userlogin,name='login'),
    path('signuplist/', views.signuplist,name='signuplist'),


    path('job/', views.joblist,name='joblist'),
    path('job/<str:pk>/', views.jobdetail,name='jobdetail'),
    path('job-create/', views.jobcreate,name='jobcreate'),
    path('job-update/<str:pk>', views.jobupdate,name='jobupdate'),
    path('job-delete/<str:pk>', views.jobdelete,name='jobdelete'),


    path('order/', views.orderlist,name='orderlist'),
    path('order/<str:pk>/', views.orderdetail,name='orderdetail'),
    path('order-create/', views.checkout,name='ordercreate'),
    path('order-delete/<str:pk>', views.orderdelete,name='orderdelete'),
    path('checkout/', views.paypal, name='paypal'),


    path('google/', views.GoogleLogin.as_view(), name='google_login'),


    ]
