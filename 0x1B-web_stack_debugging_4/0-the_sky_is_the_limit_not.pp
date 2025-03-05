# Puppet script that increases ULIMIT
exec { 'increase':
    command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

exec {'start-nginx-server':
    command => 'service nginx restart'
}
