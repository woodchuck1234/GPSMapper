import paho.mqtt.client as mqtt #import the client1

import time
############
def on_message(client, userdata, message):
    try:
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)
        #client.publish("home/OpenMQTTGateway/commands/MQTTtoLORA","{flash}")
    except:
        pass


def on_publish(client,userdata,result):             #create function for callback
    print("published")
    pass

########################################

broker_address="10.0.0.17"

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.username_pw_set('omg',password='omg')
client.on_message=on_message #attach function to callback
client.on_publish=on_publish
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","home/OpenMQTTGateway/LORAtoMQTT")
client.subscribe("home/OpenMQTTGateway/LORAtoMQTT")

#print("Publishing to topic","home/OpenMQTTGateway/commands/MQTTtoLORA")
#client.publish("home/OpenMQTTGateway/commands/MQTTtoLORA","flash")

time.sleep(60) # wait
client.loop_stop() #stop the loop
