# Fixes the 500 internel error for appache server

file_line { 'edit_error_line':
  path    => '/var/www/html/wp-settings.php',
  line    => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match   => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  replace => true,
}
