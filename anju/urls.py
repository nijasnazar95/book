# from django.urls import path
# from .import views

# urlpatterns = [

#     path('',views.home),
#     path('index',views.index),
#     # path('about/',views.about),
#     # path('audio/',views.audio),

#     path('view_book/',views.view_book,name='lines'),
#     path('Add_Book/',views.AddBook,name='AddBook'),
#     path('update/<int:id>',views.update_book,name='UpdateBook'),
#     path('delete/<int:id>',views.delete_book,name='delete'),
#     path('rege/',views.register_book,name='register')

# ]

from django.urls import path
from . import views
 
urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index),
    # path('about/',views.about),
    # path('service/',views.service)
    path('view_book/',views.view_book,name='lines'),
    path('Add_book/',views.AddBook,name='AddBook'),
    path('update_book/<int:id>',views.update_book,name='UpdateBook'),
    path('delete_book/<int:id>',views.delete_book,name='delete'),
    path('register/',views.register_book,name='register'),
    path('login/',views.login_user,name='loginpage'),
    path('logout/',views.logout_user,name='logoutpage'),
    path('add_to_cart/<int:book_id>',views.add_to_cart,name='add_to_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('remove_from_cart/<int:book_id>',views.remove_from_cart,name='remove_from_cart'),

    path('buy/<int:book_id>/', views.buy_now, name='buy_now'),
    path('success/', views.payment_success,name='success'),
    path('cancel/', views.payment_cancel,name='cancel'),

]