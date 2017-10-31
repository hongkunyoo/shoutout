# shoutout
Python jumbo letter printer
Use it on writting your log file. Especially when there are lots of logs on one log file.

```
Oct 31 08:51:09 almond dhclient[1094]: bound to 192.168.0.5 -- renewal in 3172 seconds.
Oct 31 08:51:09 almond NetworkManager[893]: <info>  [1509407469.5067]   server identifier 192.168.0.1
Oct 31 08:51:09 almond NetworkManager[893]: <info>  [1509407469.5067]   lease time 7000
Oct 31 08:51:09 almond NetworkManager[893]: <info>  [1509407469.5067]   nameserver '0.9.0.0'
Oct 31 08:51:09 almond NetworkManager[893]: <info>  [1509407469.5068]   nameserver '1.4.1.2'
Oct 31 08:51:09 almond NetworkManager[893]: <info>  [1509407469.5068] dhcp4 (enp0s31f6): state changed bound -> bound
Oct 31 08:51:09 almond systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 31 08:51:09 almond dbus[848]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Oct 31 08:51:09 almond systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 31 08:51:09 almond nm-dispatcher: req:1 'dhcp4-change' [enp0s31f6]: new request (1 scripts)
Oct 31 08:51:09 almond nm-dispatcher: req:1 'dhcp4-change' [enp0s31f6]: start running ordered scripts...
Oct 31 09:17:01 almond CRON[4317]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct 31 09:32:09 almond systemd[1]: Starting Cleanup of Temporary Directories...
Oct 31 09:32:09 almond systemd-tmpfiles[4321]: [/usr/lib/tmpfiles.d/var.conf:14] Duplicate line for path "/var/log", ignoring.
Oct 31 09:32:09 almond systemd[1]: Started Cleanup of Temporary Directories.

 #   #   ####   #       #        ####     ###    ### 
 #   #   #      #       #       #    #    ###    ### 
 #####   ####   #       #       #    #    ##     ##  
 #   #   #      #       #       #    #               
 #   #   ####   #####   #####    ####     ##     ##  
 
Oct 31 09:44:01 almond NetworkManager[893]: <info>  [1509410641.4999]   address 192.168.0.5
Oct 31 09:44:01 almond NetworkManager[893]: <info>  [1509410641.4999]   plen 24 (255.255.255.0)
Oct 31 09:44:01 almond dbus[848]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service'
Oct 31 09:44:01 almond systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 31 09:44:01 almond dbus[848]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
```

# Install
pip install shoutout

# Usage

```python
import shoutout
print(shoutout.loud("Hello!!"))
```

<pre>         
	
 #   #   ####   #       #        ####     ###    ### 
 #   #   #      #       #       #    #    ###    ### 
 #####   ####   #       #       #    #    ##     ##  
 #   #   #      #       #       #    #               
 #   #   ####   #####   #####    ####     ##     ##  

</pre> 

or you can create an object!

```python
import shoutout

loud_msg = shoutout.ShoutOut("World!!")
print(loud_msg)
```

<pre>         
          
 #       #    ####    #####    #       ####      ###    ### 
 #       #   #    #   #    #   #       #    #    ###    ### 
 #   #   #   #    #   # ###    #       #    #    ##     ##  
  # # # #    #    #   #   #    #       #    #               
   #   #      ####    #    #   #####   ####      ##     ##  
      

</pre> 

