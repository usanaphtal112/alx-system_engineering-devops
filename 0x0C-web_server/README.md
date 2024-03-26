
![NGINX SERVER](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

## 0x0C. Web server

### Background Context

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.


## Tasks

### 0. Transfer a file to your server

Write a Bash script that transfers a file from our client to a server:

**Requirements:**

- Accepts 4 parameters
  - The path to the file to be transferred
  - The IP of the server we want to transfer the file to
  - The username scp connects with
  - The path to the SSH private key that scp uses
- Display Usage: `0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`

**Example:**

```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html 100% 12 0.1KB/s 00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```


### 1. Install nginx web server

**Readme:**

- `-y` on `apt-get` command
- Web servers are the piece of software generating and serving HTML pages, let’s install one!

**Requirements:**

- Install nginx on your `web-01` server
- Nginx should be listening on port `80`
- When querying Nginx at its root `/` with a `GET` request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- You can’t use `systemctl` for restarting nginx

**Server terminal:**

```
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$
```


**Local terminal:**

sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes


**Maarten’s PRO-tip:**
When you use `sudo su` on your `web-01` you can become root like this to test your file:

```
sylvain@ubuntu$ sudo su
root@ubuntu#
```


### 2. Setup a domain name

.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

YOU can have a free .tech domain for 1 year by following these steps:

- Access the tools space
- Unlock the GitHub student pack: **WARNING** - this invitation link is unique to you and can’t be reclaimed! If you have any issue, please contact GitHub education support

**Requirement:**

- Provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
- Configure your DNS records with an `A` entry so that your root domain points to your `web-01` IP address **Warning:** the propagation of your records can take time (~1-2 hours)
- Go to your profile and enter your domain in the Project website URL field

When your domain name is setup, please verify the Registrar here: [https://whois.whoisxmlapi.com/](https://whois.whoisxmlapi.com/) and you must see in the JSON response: `"registrarName": "Dotserve Inc"`

### 3. Redirection

**Readme:**

- Replace a line with multiple lines with `sed`
- Configure your Nginx server so that `/redirect_me` is redirecting to another page.

**Requirements:**

- The redirection must be a “301 Moved Permanently”
- You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

### 4. Not found page 404

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

**Requirements:**

- The page must return an HTTP 404 error code
- The page must contain the string `Ceci n'est pas une page`
- Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

### 5. Install Nginx web server (w/ Puppet)

Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying `/redirect_me`.

**Requirements:**

- Nginx should be listening on port `80`
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- The redirection must be a “301 Moved Permanently”
- Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements


