# Configure the SSH server to authenticates only through SSH keys.
include stdlib

file_line { 'Turn off passwd auth':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
  ensure => present,
}

file_line { 'Declare identity file':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
  ensure => present,
}
