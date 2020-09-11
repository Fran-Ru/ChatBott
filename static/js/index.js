//https://www.eclipse.org/paho/clients/js/

function Enviar() {	
	C=document.getElementById("campo").value;
	console.log(C)
	message = new Paho.MQTT.Message(C);
	message.destinationName = "saturno101@outlook.com/dispositivo";
	client.send(message);
}



// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.
  random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
   useSSL: false,
    userName: "saturno101@outlook.com",
    password: "10prmillcoma",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Estoy Conectado...");
	
    client.subscribe("saturno101@outlook.com/chatbot");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "saturno101@outlook.com/dispositivo";
    client.send(message);
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    text=(message.payloadString);
	document.getElementById("mensaje").innerHTML=text;
  }
 
  
