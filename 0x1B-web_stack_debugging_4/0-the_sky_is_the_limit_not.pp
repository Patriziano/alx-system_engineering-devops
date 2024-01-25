# let's fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

exec { 'com':
  command  => 'sed -i s/15/4096/g /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
