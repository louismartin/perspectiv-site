# perspectiv-site

## Deploy
https://realpython.com/django-nginx-gunicorn/

```
pip install gunicorn

export BUDGET_INSIGHT_CLIENT_ID=... && export BUDGET_INSIGHT_CLIENT_SECRET='...' sudo apt-get install -y nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

Nginx config
```
sudo nvim /etc/nginx/sites-available/perspectiv
```

Add
```
server_tokens               off;
access_log                  /var/log/nginx/perspectiv.access.log;
error_log                   /var/log/nginx/perspectiv.error.log;

server {
  server_name               .perspectiv.ovh;
  listen                    80;
  location / {
    proxy_pass          http://localhost:8000;
    proxy_set_header    Host $host;
    proxy_set_header    X-Forwarded-Proto $scheme;
  }

  location /static {
    autoindex on;
    alias /var/www/perspectiv.ovh/static/;
  }
}
```

Activate
```
sudo ln -s /etc/nginx/sites-available/perspectiv /etc/nginx/sites-enabled
sudo systemctl restart nginx
```

Static files
```
sudo mkdir -p /var/www/perspectiv.ovh
sudo chown -cR louismartin:louismartin /var/www/perspectiv.ovh/
python manage.py collectstatic
sudo systemctl restart nginx
```

## HTTPS
```
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx --rsa-key-size 4096 --no-redirect
```