# 1-user_limit.pp

user { 'holberton':
  ensure => present,
}

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton hard nofile 65536\n",
}
