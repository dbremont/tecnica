# NGINX

> Nginx is a high-performance, open-source web server and reverse proxy server known for its scalability, efficient handling of concurrent connections, and ability to serve static content, load balance requests, and act as a gateway for various protocols.
> 

QA:

- …

## How to configure `Linode`?

```bash
/etc/nginx/sites-available/python-prueba.conf
sudo ln -s /etc/nginx/sites-available/python-prueba.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

```bash
cat /etc/nginx/sites-enabled/python-prueba.conf
server {
    listen       80;
    listen       [::]:80;
    server_name  198.74.55.133;

    access_log  /var/log/nginx/odoo.access.log;
    error_log   /var/log/nginx/odoo.error.log;

    location / {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Proto https;
      proxy_pass http://localhost:8080;
  }
}
```

## References

- [NGINX](https://nginx.org/)
- https://github.com/arut/nginx-rtmp-module
- [https://hg.nginx.org/nginx](https://hg.nginx.org/nginx)