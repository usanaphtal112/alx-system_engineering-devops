# 0x17. Web stack debugging #3

[![Screenshot](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png)](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png)

## Tasks

1. **Strace is your friend**

   Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

   **Hint:**
   - strace can attach to a current running process
   - You can use tmux to run strace in one window and curl in another one

