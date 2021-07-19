import paho.mqtt.client as mqtt #import the client1

import time

############
def on_message(client, userdata, message):
    try:
    #    print("message received " ,str(message.payload.decode("utf-8")))
    #    print("message topic=",message.topic)
    #    print("message qos=",message.qos)
    #    print("message retain flag=",message.retain)
        if str(message.payload.decode("utf-8")).__contains__("GPS"):
            print("message received ", str(message.payload.decode("utf-8")))
    #        print("Publishing to topic", "home/OpenMQTTGateway/commands/MQTTtoLORA")
            client.publish("home/OpenMQTTGateway/commands/MQTTtoLORA", "LED")

    except Exception as e: print("Exception:",e)

def on_publish(client,userdata,result):             #create function for callback
    #print("published")
    pass

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    print("Subscribing to topic","home/OpenMQTTGateway/LORAtoMQTT")
    client.subscribe("home/OpenMQTTGateway/LORAtoMQTT")
########################################

broker_address="10.0.0.17"

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.username_pw_set('omg',password='omg')
client.on_message=on_message #attach function to callback
client.on_publish=on_publish
#client.on_log=on_log
client.on_connect=on_connect
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_forever()#start the loop

#client.loop_stop() #stop the loop
