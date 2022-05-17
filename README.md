# frontend_dev

## Despligue
Se procedio a desplegar en AWS la solucion utilizando los servicios de ec2 y RDS (por capa gratuita para no incurrir en costos). La URL del web site es http://3.93.149.106/

### Backend
Para el backend se utilizo Python y se desplego con gunicorn, esto debido a que se utilizara el gateway servlet wsgi.

Comandos:
```
pipenv shell
export GUNICORN_CMD_ARGS="--bind=0.0.0.0"
gunicorn content_mng_api.wsgi 
```

### Frontend
Para el frontend se utilizo nginx y se compilo de manera estatica.

Comandos:
```
npm run build
npm run generate
sudo yum install nginx
cp -r ./dist /usr/share/nginx/html
nginx -g daemon off;
```

### Base de datos
Se utilizo el servicio de RDS y el script de migrations de Django.

Comandos:
```
pipenv shell
python3 manage.py makemigrations
python3 manage.py migrate
```
