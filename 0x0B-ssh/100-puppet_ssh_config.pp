# Configure the SSH server to authenticates only through SSH keys.
include stdlib

file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}
