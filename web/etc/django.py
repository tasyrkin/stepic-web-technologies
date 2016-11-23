CONFIG = {
    'mode': 'django',
    'environment': {
      'PYTHONPATH': ('/usr/lib/python2.7:'
      '/usr/local/lib/python2.7/dist-packages:'
      '/usr/lib/python2.7/dist-packages:'
      '/usr/lib/python2.7/plat-x86_64-linux-gnu:'
      '/usr/lib/python2.7/lib-dynload:'
      '/usr/lib/python2.7/lib-tk:'
      '/usr/lib/python2.7/lib-old:'
      '/home/box/web/ask:'
      ),
    },
    'working_dir': '/home/box/web/ask',
    # 'user': 'www-data',
    # 'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8000',
        # '--workers=4',
        # '--worker-class=egg:gunicorn#sync',
        '--timeout=60',
        'ask.settings',
    ),
}
