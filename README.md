# Django Library Management System

## 프로젝트 개요
도서 관리와 리뷰 시스템을 구현한 Django 웹 애플리케이션입니다.

## 주요 기능

### 도서 관리
- 도서 목록 조회 (ListView)
- 도서 상세 정보 조회 (DetailView)
- 새로운 도서 등록 (CreateView)
- 도서 삭제 (DeleteView)

### 리뷰 시스템
- 도서별 리뷰 작성
- 리뷰 목록 조회
- 리뷰 삭제

## 모델 구조

### Book 모델
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
```

### Review 모델
```python
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=255, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
```

### URL 구조
```python
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/create/', views.ReviewCreateView.as_view(), name='create_review'),
    path('<int:book_pk>/delete/<int:review_pk>/', views.ReviewDeleteView.as_view(), name='delete_review'),
]
```

## 구현된 View
- IndexView (ListView): 도서 목록 표시
- DetailView: 도서 상세 정보와 리뷰 표시
- CreateView: 새로운 도서 등록
- DeleteView: 도서 삭제
- ReviewCreateView: 리뷰 작성
- ReviewDeleteView: 리뷰 삭제

## 기술 스택
- Django 5.1.3
- Python 3.11.10
- SQLite3
