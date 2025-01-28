from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    WalletViewSet, TransactionViewSet, CustomerViewSet,
    SupplementViewSet, ArticleViewSet, PodcastViewSet,HealthConditionViewSet,
    CustomerCreateView,UserLoginView
)

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'supplements', SupplementViewSet, basename='supplement')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'podcasts', PodcastViewSet, basename='podcast')
router.register(r'health-conditions', HealthConditionViewSet, basename='health-condition')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register', CustomerCreateView.as_view(), name='create_customer'),  # Create customer
    path('auth/login', UserLoginView.as_view(), name='login_user'),  # User login
]