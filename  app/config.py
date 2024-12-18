# 전역 설정
SETTINGS = {
    'max_image_size': 5 * 1024 * 1024,  # 5MB
    'supported_formats': ['jpg', 'jpeg', 'png'],
    'model_input_size': (224, 224),
    'cache_duration': 3600,  # 1시간
    'memory_limit': 1024,  # 1GB
    'food_categories': ['김치찌개', '비빔밥', '불고기', '김밥', '된장찌개']
}

# 성능 모니터링 설정
MONITORING = {
    'log_file': 'performance_logs.csv',
    'metrics': ['total_analysis', 'prediction', 'memory_usage'],
    'alert_threshold': {
        'response_time': 3.0,  # 초
        'memory_usage': 900  # MB
    }
}

# 캐시 설정
CACHE = {
    'ttl': 3600,
    'max_entries': 1000
}
