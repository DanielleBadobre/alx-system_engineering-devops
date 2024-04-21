#install package

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
exec { 'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/bin/',
  unless  => 'pip3 list | grep flask',
}
