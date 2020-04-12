from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blogpost_detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger_detail'),
    path('topics/', views.TopicListView.as_view(), name='topics'),
    path('topic/<int:pk>', views.TopicDetailView.as_view(), name='topic_detail'),
]

urlpatterns += [
    path('comments/', views.CommenterListView.as_view(), name='comments'),
]

urlpatterns += [
    path('blog/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment_create'),
    path('comment/<uuid:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment/<uuid:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]

urlpatterns += [
    url(r'^signup/$', views.signup, name='signup'),
]    
