"""
WSGI config for tenants_aws project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# default wsgi.py file
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tenants_aws.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# alternative wsgi.py file

# import os
# import sys
# import site

# site.addsitedir('/home/dimm/Desktop/pythondir/tenants_aws/v_env/local/lib/python2.7/site-packages')

# sys.path.append('/home/dimm/Desktop/pythondir/tenants_aws')
# sys.path.append('/home/dimm/Desktop/pythondir/tenants_aws/tenants_aws')

# os.environ['DJANGO_SETTINGS_MODULE'] = 'tenants_aws.settings'

# activate_env=os.path.expanduser("/home/dimm/Desktop/pythondir/tenants_aws/v_env/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))

# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()