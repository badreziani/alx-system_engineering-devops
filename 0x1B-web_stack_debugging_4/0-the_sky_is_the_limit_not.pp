# Increases the amount of requests

exec { 'increase_nginx_ulimit':
  command => "/usr/bin/env sed -i 's/15"/4096/' /etc/default/nginx",
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
