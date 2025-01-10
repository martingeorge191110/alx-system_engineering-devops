# create a file in /tmp
file { '/tmp/school':
    owner   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
    group   => 'www-data',
}
