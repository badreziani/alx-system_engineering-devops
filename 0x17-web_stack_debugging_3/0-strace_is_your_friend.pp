file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure => 'file',
  source => '/var/www/html/wp-includes/class-wp-locale.phpp',
}

file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => 'absent',
}
