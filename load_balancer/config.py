from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOAD_BALANCER_CONFIG = {
    'max_connections': 1000,
    'timeout': 30,
    'retry_attempts': 3,
    'servers': [
        {
            'host': 'server1.example.com',
            'port': 8000,
        },
        {
            'host': 'server2.example.com',
            'port': 8000,
        },
    ],
    'health_check': {
        'enabled': True,
        'interval': 10,
        'timeout': 5,
    },
}