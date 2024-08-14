# Fixes the 500 internel error for appache server

exec { 'fix-internal-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
