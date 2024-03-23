# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  command  => '/usr/local/bin/pip3', # Assuming pip3 is installed at this location
  require  => Package['python3-pip'], # Ensure python3-pip is installed first
}

package { 'python3-pip':
  ensure => installed,
}
