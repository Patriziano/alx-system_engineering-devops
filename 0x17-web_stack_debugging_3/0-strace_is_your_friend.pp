#using puppet to fix the Apache error Using strace, find out why Apache is returning a 500 error.

exec {'exec':
    command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php;
    service apache2 restart',
    provider => shell
  }
