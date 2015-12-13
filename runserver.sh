logF=log/`date +"%Y%m%d"`.log
#python manage.py runserver --insecure 0.0.0.0:8002 >>$logF 2>&1
python manage.py runserver --insecure 0.0.0.0:8002
