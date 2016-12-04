# launch example from working_dir
# gunicorn --config ../etc/django_mac.py --access-logfile=/Users/timofeya/openSource/stepic-web-technologies/web/logs/gunicorn-access.log --log-level=debug --error-log /Users/timofeya/openSource/stepic-web-technologies/web/logs/gunicorn-error.log ask.wsgi
CONFIG = {
    'mode': 'django',
    'environment': {
      'PYTHONPATH': ('/usr/local/CelIlar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7:'
      '/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin:'
      '/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac:'
      '/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages:'
      '/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk:'
      '/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old:'
      '/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload:'
      '/usr/local/lib/python2.7/site-packages:'
      '/Library/Python/2.7/site-packages:'
      '/Users/timofeya/openSource/stepic-web-technologies/web/ask:'
      ),
    },
    'working_dir': '/Users/timofeya/openSource/stepic-web-technologies/web/ask',
    # 'user': 'www-data',
    # 'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8000',
        # '--workers=4',
        # '--worker-class=egg:gunicorn#sync',
        '--timeout=60',
        # '--error-log /Users/timofeya/openSource/stepic-web-technologies/web/logs/gunicorn-error.log'
        # '--access-logfile=/Users/timofeya/openSource/stepic-web-technologies/web/logs/gunicorn-access.log'
        # '--log-level=debug'
        'ask.settings',
    ),
}
