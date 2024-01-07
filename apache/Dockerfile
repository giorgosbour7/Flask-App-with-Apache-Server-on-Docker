# Use the official Apache image as the base image
FROM httpd:2.4

# Enable necessary Apache modules
RUN sed -i '/LoadModule proxy_module/s/^#//g' /usr/local/apache2/conf/httpd.conf
RUN sed -i '/LoadModule proxy_http_module/s/^#//g' /usr/local/apache2/conf/httpd.conf

# Set ServerName globally to suppress the warning
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/httpd.conf

# Copy Apache vhost file to proxy traffic to the web server
COPY 000-default.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf

# Expose Apache
EXPOSE 80
