build a simple python service in ubuntu with systemd

#copy the demo.service file into 
etc/systemd/system

#reload config
systemctl daemon-reload

#enable service so that can run on boot up
systemctl enable demo.service
systemctl disable demo.service

#start,status,stop
systemctl start demo.service
systemctl status demo.service
systemctl stop demo.service

