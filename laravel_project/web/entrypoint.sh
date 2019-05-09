#!/bin/bash

cp -r /tmp/cache/node_modules/. /home/www/web/node_modules/
cp -r /tmp/cache/vendor/. /home/www/web/vendor/
php-fpm
