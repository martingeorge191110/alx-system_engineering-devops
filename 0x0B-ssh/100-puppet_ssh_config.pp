#configure ssh config

file_line{'Turn off passwd auth':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
    ensure => present,
}

file_line{'Declare identity file':
    ensure => present,
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school'
}
