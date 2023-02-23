## How to create credentials for your mqtt broker
First, you have to install the mosquitto module by:
```
sudo snap install mosquitto
```
Then the following command can be used to create a new username + password, hashed in a file called test.txt
```
sudo mosquitto_passwd -c test.txt <username>
```
In the example of our repository, we create a username and a password test:test.
The result was:
```
test:$6$WgoRASWRnPePPq4Q$Q6g58x1Gf2mcoC/H1hOlm3Zml2dPyKGhqrmtU8fjjLr1/20Ddi+lm46zp4fqO+wgquXp8QHJLq/gW54h+KU7dw==
```
All credentials have to be injected into the configmap, provided in the repository.
You can just list all your credential pairs.

## Deploy the MQTT broker.
First, change everywhere the namespace to an appropiate one.
Then, change in the service.yaml the NodePort that you want to expose.
Afterwards create all ressources via 
```
kubectl apply -f .yaml
```
First the configmap, then the deployment, then the service.

## How to test the broker
We have the 2 test.py files inside the repository to test the broker.
We can specify the master node IP for our broker IP, or our ha-proxy IP if the configuration is set correctly on the haproxy side.
The first file is the publisher, the second is the consumer. Just run the scripts via
```
python3 test.py
```

That's it

