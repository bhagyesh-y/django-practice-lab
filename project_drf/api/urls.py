from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('fruits',views.FruitViewset,basename='fruit')
router.register('heroes',views.HeroViewset,basename='hero')

urlpatterns = [
    path('students/',views.studentsview),
    path('teachers/',views.teachersview),
    path('students/<int:pk>/',views.studentDetailview),
    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
    path('friends/',views.Friends.as_view()),
    path('friends/<int:pk>/',views.FriendDetail.as_view()),
    path('cricketers/',views.Cricketers.as_view()),
    path('cricketers/<int:pk>/',views.CricketerDetail.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view()),

    
    
]
