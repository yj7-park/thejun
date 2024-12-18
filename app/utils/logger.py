import logging
import csv
import time
from config import MONITORING

class PerformanceLogger:
    def __init__(self):
        self.log_file = MONITORING['log_file']
        self.setup_logger()
    
    def setup_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('app.log'),
                logging.StreamHandler()
            ]
        )
    
    def log_metrics(self, metrics):
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                time.strftime('%Y-%m-%d %H:%M:%S'),
                metrics['total_analysis'],
                metrics['prediction'],
                metrics['memory_usage']
            ])
