# connect to a server without typing a password

exec { 'ssh_connect':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config; echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
