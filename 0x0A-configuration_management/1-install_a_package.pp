#!/usr/bin/pup
# install flask 2.1.0 with provider pip3
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
