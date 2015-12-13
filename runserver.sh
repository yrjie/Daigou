#alias python=/usr/local/bin/python2.7
logF=log/`date +"%Y%m%d"`.log
#python manage.py runserver --insecure 0.0.0.0:8002 >>$logF 2>&1
python manage.py runserver --insecure 0.0.0.0:8002
#python manage.py runserver --insecure 100.74.102.130:80
