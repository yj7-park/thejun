import time
import psutil
import csv
from contextlib import contextmanager
from config import MONITORING

class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}
        self.log_file = MONITORING['log_file']
    
    @contextmanager
    def track_time(self, operation):
        start = time.time()
        yield
        duration = time.time() - start
        self.metrics[operation] = duration
        
        # 임계값 체크
        if operation in MONITORING['alert_threshold']:
            if duration > MONITORING['alert_threshold'][operation]:
                self.alert_slow_operation(operation, duration)
    
    def get_metrics(self):
        metrics = self.metrics.copy()
        metrics['memory_usage'] = psutil.Process().memory_info().rss / 1024 / 1024
        return metrics
    
    def log_metrics(self):
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            metrics = self.get_metrics()
            writer.writerow([
                time.strftime('%Y-%m-%d %H:%M:%S'),
                *[metrics.get(m, 0) for m in MONITORING['metrics']]
            ])
