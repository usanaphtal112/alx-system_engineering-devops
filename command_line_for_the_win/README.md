# SSH Connection and File Upload using SFTP

# SSH Connection

## Step 1: Generate SSH Key Pair

```
ssh-keygen
```

- Enter the file to save the key: Press Enter to use the default location (C:\Users\Naphtal/.ssh/id_rsa).
- Overwrite existing key: Type 'y' and press Enter.
- Enter passphrase: Optionally, set a passphrase for added security.

## Step 2: Copy Public Key to Remote Server

```
cat ~/.ssh/id_rsa.pub | ssh username@remote_server_ip or host name "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod -R go-rwx ~/.ssh"
```

- Answer 'yes' when prompted to continue connecting.
- Enter the password for the remote server.

## Step 3: Connect to Remote Server via SSH\

```
ssh username@server_ip_or_remote_hostname
```

- Enter the password when prompted.

## Step 1: Connect to Remote Server via SFTP

```
sftp username@server_ip_or_remote_hostname
```

- Enter the password when prompted.

## Step 2: Navigate to the Target Directory on Remote Server

```
cd /root/alx-system_engineering-devops/command_line_for_the_win/
```

### Step 3: Navigate to the Local Directory on Your Computer

```
lcd C:/Users/Naphtal/Desktop/Naphtal
```

### Step 4: Upload File to Remote Server

```
put 0-first_9_tasks.png
```

Confirm the file has been uploaded successfully.

# SFTP COMMANDS

- checking local working directory

```
lpwd
```

- listing all files

```
lls
```

- Navigate to the new directory

```
lcd directory name
```

## Remote Server

- checking remote server working/current directory

```
pwd
```

- listing all files

```
lls
```

- Navigate to the new directory

```
cd directory name
```

