# Script that creates a file in /tmp using Puppet

file {'/tmp/school':
 ensure => present,
 owner => 'www-data',
 mode => '0744'
 content => 'I love Puppet'
 group => 'www-data'
} 
