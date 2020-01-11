import paho.mqtt.client as mqtt  # import the client1
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


mqtt.Client.connected_flag = False  # create flag in class
broker = "127.0.0.1"
client = mqtt.Client("temperature_Sensor")  # create new instance
client.on_connect = on_connect  # bind call back function
# client.loop_start()
print("Connecting to broker ", broker)
client.connect(broker)  # connect to broker

# while not client.connected_flag: #wait in loop
#    print("In wait loop")
#    time.sleep(1)
time.sleep(2)
data = open('Temperature_data','r').read()
dataArray = data.split('\n')
count = 0
for eachLine in dataArray:
    if len(eachLine)>1:
        x = eachLine
        client.publish("TEMP", payload= x, qos= 0, retain=False)
        count += 1
        print("Publish #", count, ": OK")
        time.sleep(2)
