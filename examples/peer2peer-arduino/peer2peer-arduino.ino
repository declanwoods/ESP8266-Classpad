#include <WiFiClient.h>
#include <ESP8266WebServer.h>

const int port = 8000;
const char* ssid = "HomeAP"; 
const char* password = "redball727";
ESP8266WebServer server(80);
WiFiClient client;
const char* host = "192.168.0.184";
const char* url = "/data";
String str;
IPAddress ip(192,168,0,229);
IPAddress gateway(192,168,0,1);
IPAddress mask(255,255,255,0);

void setup() {
    Serial.begin(38400, SERIAL_7N1);    
    WiFi.config(ip, gateway, mask);
    WiFi.mode(WIFI_STA);  
    WiFi.begin(ssid, password); // Connect to WIFI network

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println(".");
    }
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
  
    server.on("/data", handleSerialData);
    server.begin(); 
    Serial.println("HTTP server started.");
}
  
void loop() {   
    server.handleClient();
    client.stop();

    if(Serial.available()) { 
        String msg = "";
        if (!client.connect(host, port)) {
            Serial.println("connection failed");
            return;
        }
        
        msg = Serial.readString();
        client.print(String("POST ") + url + " HTTP/1.1\r\n");
        client.print(String("Content-Type: text/plain; charset=utf-8\r\n"));
        client.print(String("Host: ") + host + "\r\n"); 
        client.print("Connection: close\r\n");
        client.print(String("Content-Length: ")+msg.length()+"\r\n\r\n");
        client.print(msg);
        client.println();
        Serial.println(msg);
    }
}

void handleSerialData() {
    String message = "";
    if(server.hasArg("plain") == false) {
        server.send(200, "text/plain", "Invalid request");
        return;
    }
    message = server.arg("plain");
    byte buf[(message.length()/2)];
    for (int i = 0; i < message.length()/2; i++) {
        buf[i] = strtoul(message.substring(i*2, (i*2)+2).c_str(), NULL, 16);
    }
    Serial.write(buf, sizeof(buf));
    //Serial.println();
    server.send(200, "text/plain", message);
    return;
}
