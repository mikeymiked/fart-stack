FROM httpd:latest
RUN rm -fv /usr/local/apache2/conf/httpd.conf
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
CMD ["/usr/local/apache2/bin/httpd", "-D", "FOREGROUND"]
