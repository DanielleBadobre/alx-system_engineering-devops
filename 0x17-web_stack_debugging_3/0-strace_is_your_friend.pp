#trying to fix error with strace
exec { 'Fix and restart':
  command => 'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
