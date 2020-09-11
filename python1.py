import paho.mqtt.client as mqtt 
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup (7, GPIO.OUT)
GPIO.setup (11, GPIO.IN)

def prender():
	GPIO.output(7, True)
def apagar():
	GPIO.output(7, False)


def on_message(client, obj, msg):    
	a=(msg.payload.decode("utf-8"))
	cadena = a.split()
	print(cadena)
	for x in cadena:
		if x== 'enciende' or x== 'prende' or x== 'activa' :
			mqttc.publish("saturno101@outlook.com/chatbot","A tus oredenes Luz encendida")
			prender()
		if x== 'apaga' or x== 'desactiva' or x== 'desconecta' :
			mqttc.publish("saturno101@outlook.com/chatbot","A tus oredenes Luz encendida")
			apagar()
		if x == 'hola':
			mqttc.publish("saturno101@outlook.com/chatbot","Hola como estas")
		if x == 'llamas'or x== 'nombre' :
			mqttc.publish("saturno101@outlook.com/chatbot","Me llamo Wally")
		if x == 'donde' or x=='naciste':
			mqttc.publish("saturno101@outlook.com/chatbot","Soy de Riobamba")
		if x == 'gusta'or x== 'comer' :
			mqttc.publish("saturno101@outlook.com/chatbot","Me encanta comer papas con cuy")
		if x=='cuy':
			mqttc.publish("saturno101@outlook.com/chatbot","El cuy es delicioso")

mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("saturno101@outlook.com","10prmillcoma") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("saturno101@outlook.com/dispositivo", 0)

rc=0
print("Conexion...")
i = 0
while rc == 0:
	time.sleep(2)
	rc = mqttc.loop()
	i =i+1
	if GPIO.input(11):
		GPIO.output(7, True)
	else:
		GPIO.output(7, False)
	
