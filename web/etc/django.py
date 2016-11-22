CONFIG = {
    'mode': 'django',
    'environment': {
        'PYTHONPATH': '/usr/lib/python2.7',
    },
    'working_dir': '/home/box/web/ask',
    # 'user': 'www-data',
    # 'group': 'www-data',
    'args': (
        '--bind=127.0.0.1:8000',
        # '--workers=4',
        # '--worker-class=egg:gunicorn#sync',
        '--timeout=60',
        # 'settings',
        'ask.wsgi:application'
    ),
}
