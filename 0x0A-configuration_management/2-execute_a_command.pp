#creating a manifest that kills a process :killmenow

exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow',
}
