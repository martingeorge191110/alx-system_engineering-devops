# Puppet script that increases holberton user
exec { 'increase-Hard-Limit':
    provider => shell,
    command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
}

exec { 'increase-Soft-Limit':
    provider => shell,
    command  => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf'
}
