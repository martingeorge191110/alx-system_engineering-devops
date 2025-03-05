# Puppet script that increases ULIMIT
exec { 'increase':
    provider => shell,
    command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

exec {'start-nginx-server':
    provider => shell,
    command => 'service nginx restart'
}
