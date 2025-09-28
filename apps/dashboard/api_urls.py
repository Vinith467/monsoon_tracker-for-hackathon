from django.urls import path
from . import views

urlpatterns = [
    # Dashboard data API
    path('dashboard-data/', views.get_dashboard_data, name='api_dashboard_data'),
    
    # Weather API endpoints
    path('weather/<str:city>/', views.get_weather_data, name='api_weather_data'),
    path('forecast/<str:city>/', views.get_forecast_data, name='api_forecast_data'),
    
    # Air Quality API endpoints  
    path('air-quality/<str:city>/', views.get_air_quality_data, name='api_air_quality_data'),
    path('air-quality/history/<str:city>/', views.get_air_quality_history, name='api_air_quality_history'),
    
    # Water levels API endpoints
    path('water-levels/', views.get_water_levels, name='api_water_levels'),
    path('water-levels/<str:city>/', views.get_city_water_levels, name='api_city_water_levels'),
    
    # User API endpoints
    path('user/location/', views.update_user_location, name='api_update_location'),
    
    # Utility API endpoints
    path('check-username/', views.check_username_availability, name='api_check_username'),
    path('check-email/', views.check_email_availability, name='api_check_email'),
    
    # Community API endpoints (redirect to community app)
    path('community/reports/map/', views.get_community_reports_map, name='api_community_reports_map'),
]