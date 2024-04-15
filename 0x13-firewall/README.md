## 0x13. Firewall

![Firewall Diagram](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

### Tasks

#### 0. Block all incoming traffic but

Let’s install the ufw firewall and setup a few rules on web-01.

**Requirements:**
- The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
- Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)

#### 1. Port forwarding

Firewalls can not only filter requests, they can also forward them.

**Requirements:**
- Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
- Your answer file should be a copy of the ufw configuration file that you modified to make this happen

**Terminal in web-01:**

```
ubuntu@4929-web-01:~$ netstat -lpn
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.247.34.178:68        0.0.0.0:*                           -                   
raw6       0      0 :::58                   :::*                    7           -                   
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
unix  2      [ ACC ]     STREAM     LISTENING     1186816  129474/systemd       /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     1186822  129474/systemd       /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     1186823  129474/systemd       /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     294141   -                    @/org/kernel/linux/storage/multipathd
unix  2      [ ACC ]     STREAM     LISTENING     1186824  129474/systemd       /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     1186825  129474/systemd       /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     1186826  129474/systemd       /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     1186827  129474/systemd       /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     1186828  129474/systemd       /run/user/1000/pk-debconf-socket
unix  2      [ ACC ]     STREAM     LISTENING     1186829  129474/systemd       /run/user/1000/snapd-session-agent.socket
unix  2      [ ACC ]     STREAM     LISTENING     196192   -                    /run/systemd/journal/io.systemd.journal
unix  2      [ ACC ]     STREAM     LISTENING     59384    -                    /var/snap/lxd/common/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     14370    -                    /run/lvm/lvmpolld.socket
unix  2      [ ACC ]     STREAM     LISTENING     14375    -                    /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     102829   -                    /var/lib/amazon/ssm/ipc/health
unix  2      [ ACC ]     STREAM     LISTENING     14385    -                    /run/systemd/journal/stdout
unix  2      [ ACC ]     SEQPACKET  LISTENING     14390    -                    /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     102830   -                    /var/lib/amazon/ssm/ipc/termination
unix  2      [ ACC ]     STREAM     LISTENING     20730    -                    /run/acpid.socket
unix  2      [ ACC ]     STREAM     LISTENING     20744    -                    /run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     20767    -                    /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     91970    -                    /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     91971    -                    /run/snapd-snap.socket
unix  2      [ ACC ]     STREAM     LISTENING     20761    -                    @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ACC ]     STREAM     LISTENING     195482   -                    /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     195486   -                    /run/systemd/userdb/io.systemd.DynamicUser
ubuntu@4929-web-01:~$

```

- My web server nginx is only listening on port 80
- netstat shows that nothing is listening on 8080


**Terminal in web-02:**

```
ubuntu@4929-web-02:~$ curl -sI web-01.naphtal.tech:80
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 15 Apr 2024 14:51:27 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Sat, 06 Apr 2024 17:35:21 GMT
Connection: keep-alive
ETag: "661187d9-d"
X-Served-By: 4929-web-01
Accept-Ranges: bytes

ubuntu@4929-web-02:~$ 

```

