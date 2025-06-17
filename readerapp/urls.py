from django.urls import path
from readerapp import views

urlpatterns=[
    path('reader/home',views.ReaderHome.as_view(),name='reader_home'),
    path('reader/detail/<int:id>',views.ReaderBlogDetail.as_view(),name='reader_blog_detail'),
    path('reader/comment//<int:id>',views.AddCommentView.as_view(),name='reader_add_comment'),
    path('list/comment//<int:id>',views.ListCommentView.as_view(),name='reader_list_comment'),
    

]
