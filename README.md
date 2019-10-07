# Welcome to Docker Remote UI application 
## This is written by chandu

**To Run this application follow the below steps**

* ## `Stop` the docker in your machine ``The machine which you want to control over UI``
  * ### `sudo systemctl stop docker`
* ## Now start the docker with the following command 
  * ### `sudo nohup dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375 &`
* ## The above command will start the docker application and make the docker API to listen on port 2375 
* ### update the [IP.py](https://github.com/ChanduReddy123/DjangoApp/blob/master/dockerpages/IP.py) file with your docker machine IP address.



## Issues you might face 

* ### Application not able to connect with docker 
  *  Reason 1: Docker might be running but it is not exposing the API run 
    * stop the docker and start with the command mentioned above.
  * Reason 2: Your machine might not be rechable on the specifed port 
    * Try `telnet ipaddress 2375`
    * example `telnet 1.2.3.4 2375`
    * If you get a positive response you should be fine 


## This application still needs a lot of Error handiling 
## There are only minimal feature available such as 
* List image
* List containers 
* List Containers based on Image 
* Start containers 
* Stop containers 
* Run New containers with basic properties like contianer name,host port,continaer port,detached mode.


## Let me know your suggestions.


