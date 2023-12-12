from django.urls import path

from .views import index, deleteView, addView, signupView, createuserView, userView

urlpatterns = [
    path('', index, name='index'),
    path('search/<str:search>', index, name='search'),
    path('delete/<str:id>', deleteView, name='delete'),
    path('add', addView, name='add'),
    path('signup', signupView, name='signup'),
    path('createuser', createuserView, name='createuser'),
    
    # Flaw 3: Remove the path below to fix
    path('users', userView, name='user'),
]