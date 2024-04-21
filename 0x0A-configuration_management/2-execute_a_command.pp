#kills kilmenow

exec { 'kill killmenow':
  command => 'pkill -9 killmenow',
  path    => ['/usr/bin/'],
}
