file { '/etc/ssh/ssh_config':
	ensure => presesnt,
}

file_line { 'Turn off passwd auth':
	path	=> '/etc/ssh/ssh config',
	line	=> 'PasswordAuthentication no',
	match	=> '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
	path	=> '/etc/ssh/ssh config',
	line	=> 'IdentityFile ~/.ssh/school',
	match	=> '^#IdentityFile',
}
