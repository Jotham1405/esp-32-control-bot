from machine import Pin, time_pulse_us
from time import sleep
import network

SSID = "Jotham"
Password = "Trailer@8642"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected, ip:", wlan.iconfig()[0])
    return wlan.ifconfig()[0]


AIN1 = Pin(25, Pin.OUT)
AIN2 = Pin(33, Pin.OUT)
BIN1 = Pin(27, Pin.OUT)
BIN2 = Pin(14, Pin.OUT)
STBY = Pin(26,Pin.OUT)
pwma = Pin(32, Pin.out)
pwmb = Pin(12, Pin.OUT)

pwma.on()
pwmb.on()
STBY.on()

def forward():
    AIN1.on()
    AIN2.off()
    B1N1.off()
    BIN2.on()
    
def backward():
    AIN1.off()
    AIN2.on()
    BIN1.on()
    BIN2.off()
    
def right():
    AIN1.on()
    AIN2.off()
    BIN1.on()
    BIN2.off()
    
def left():
    AIN1.off()
    AIN2.on()
    BIN1.off()
    BIN2.on()
    
def stop():
    STBY.off()
    
def measure_distance():
    TRIG.off()
    time.sleep_us(2)
    TRIG.on()
    time.sleep_us(10)
    TRIG.off()
    try:
        pulse = time_pulse_us(ECHO, 1, 30000)
        if pulse<0:
            return None
        dist_cm = (pulse/2) * 0.0343
        return dist_cm
    except:
        return None
    
def login_page():
    return """
    <!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
        <style>
            body {
                background-color: black;
                font-family: 'Pacifico', cursive;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .login-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 50px;
            }
            .login-box{
                background: black;
                padding: 32px;
                justify-content: center;
                border: 1px solid dimgray;
                border-radius: 10px;
                color: whitesmoke;
                box-shadow: 0 0 25px cyan;
                width: 350px;
                max-width: 90%;
                /*TOGGLE EFFECT*/
                transition: all 0.5x ease;
                transform: scale(1);
            }
            .login-box:hover{
                transform: scale(1.05);
                box-shadow: 0 0 35px cyan;
            }
            h2 {
                text-align: center;
            }
            input[type="text"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid black;
                border-radius: 5px;
                font: inherit;
                box-sizing: border-box;
                background: white;
                color: black;
            }
            button {
                width: 100%;
                padding: 12px;
                background-color:cyan;
                color:black;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
                font: inherit;
                margin-top: 16px;
            }
            .name {
                text-align: center;
                color: cyan;
                font-size: 1.5rem;
                line-height: 1.4;
            }
            .info {
                margin: 0;
                font-family: 'Share Tech Mono', monospace;
                font-size: 30px; 
                font-weight: bold;
                color: whitesmoke;
                letter-spacing: 1px; 
                text-transform: uppercase;
            }

        </style>
    </head>
    <body>
        <div class="login-container">
            <form class="login-box" method="POST" action="/login">
                <h2>Login</h2>
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Passowrd" required>
                <button type="submit">Sign In</button>
            </form>
        <div class="name">
            <h2 class="info"><strong> HANDS ON ROBOTICS</strong></h2>
        </div>
    </div>
    </body>
</html>
"""

def htm_page():
    return"""
    <!DOCTYPE html>
<html>
    <head>
        <title>ESP32 Bot control</title>
        <style>
        
            *{box-sizing: border-box;}
            body{
                padding-top: 20px;
                font-family:Arial,sans-serif;
                background-color:black;
                display:flex;
                font-size:1.5rem;
                flex-direction:column;
                align-items:center;
                margin:0;
            }
            h1{
                text-align: center;
                color:cyan;
            }
            .button,.info{
                background-color: dimgrey;
                color:cyan;
                margin-bottom: 10px;
            }
            .button-container{
                display:grid;
                grid-template-columns:1fr 1fr 1fr;
                grid-template-rows:1fr 1fr 1fr;
                gap:10px;
                width:300px;
                height:300px;
                margin-bottom:30px;
                margin-left: -50px;
            }
            .button{
                padding:15px 30px;
                font-size:16px;
                font-weight:bold;
                background:black;
                color: cyan;
                border:2px solid cyan;
                width: 105px;
                height: 90px;
                border-radius: 12px;
                cursor:pointer;
                display:flex;
                align-items:center;
                justify-content:center;
                text-decoration:none;
                transition:all 0.2s;
            }
            .button:hover{
                background-color: cyan;
                color: #000;
                box-shadow:0 6px 15px rgba(0,255,180,0.5);
                transform:translateY(-8px);
            }
            .button:active{transform:translateY(0);}
            .center-dot{
                width:16px;
                height:16px;
                background-color:cyan;
                border-radius:50%;
                align-self:center;
                justify-self:center; 
            }
            .info{
                background-color: black;
                margin-top:30px;
                font-size:18px;
                padding:15px 30px;      
                border-radius:8px;
                color: whitesmoke;
                border: 2px solid cyan;
            }
            .forward{grid-column:2;grid-row:1;}
            .left{grid-column:1;grid-row:2;}
            .right{grid-column:3;grid-row:2;}
            .backward{grid-column:2;grid-row:3;}
            .center-dot{grid-column:2;grid-row:2;}
            .name{
                text-align: center;
                margin-top: 20px;
                color: cyan;
                font-size: 1.3rem;
                line-height: 1.4;
            }

        </style>
        
    </head>
    <body>
        <div class="button-container">
            <div class="button forward"
                onmousedown="sendCommand('forward',true)" 
                onmouseup="sendCommand('forward',false)" 
                ontouchstart="sendCommand('forward',true)" 
                ontouchend="sendCommand('forward',false)">Forward</div>
            <div class="button left" 
                onmousedown="sendCommand('left',true)"
                onmouseup="sendCommand('left',false)" 
                ontouchstart="sendCommand('left',true)" 
                ontouchend="sendCommand('left',false)">Left</div>
            <div class="center-dot"></div>
            <div class="button backward"
                onmousedown="sendCommand('backward',true)" 
                onmouseup="sendCommand('backward',false)" 
                ontouchstart="sendCommand('backward',true)" 
                ontouchend="sendCommand('backward',false)">Backward</div>
            <div class="button right"
                onmousedown="sendCommand('right',true)" 
                onmouseup="sendCommand('right',false)" 
                ontouchstart="sendCommand('right',true)" 
                ontouchend="sendCommand('right',false)">Right</div>
        </div>
        <div class="info" id="distance">Loading...</div>
        <div class="name">
            <h2><strong>HANDS ON ROBOTICS</strong></h2>
            <p>By <b>Robovitics club</b></p>
        </div>
        <script>
        function updateDistance() {
            fetch('/distance')
                .then(res => res.text())
                .then(data => {
                    document.getElementById("distance").innerText = data;
                });
        }
        setInterval(updateDistance, 500);
        window.onload = updateDistance;
        // Movement handling (hold button = move, release = stop)
        function sendCommand(cmd, isDown) {
            fetch(isDown ? '/' + cmd : '/stop');
        }
    </script>
    </body>
</html>
"""

USERNAME = "admin"
PASSWORD_AUTH = "1234"
session = False

def handle_client():
    global session
    request = client.recv(1024).decode("utf-8")
    method = request.split(" ")[0]
    path = request.split(" ")[1]
    
    if path.startswith('/login') and method == "POST":
        body = request.split("\r\n\r\n")[-1]
        data = {}
        
        for pair in body.split("&"):
            if "=" in pair:
                key, value = pair.split("=")
                data[key] = value
            username = data.get("username")
            password = data.get("password")
            if username = USERNAME and password = PASSWORd_AUTH:
                session = True
                client.send('HTTPS/1.1 302 Found\r\nLocation:/\r\n\r\n')
            else:
                session = False
                client.send('HTTP/1.1 401 Unauthorized\r\n\r\n<h1>Unauthorized<h1>')
            client.close()
            return
        if not session and path != "/login":
            client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
            client.send(login_page())
            client.close()
            return
        if path == "/distance":
            dist = measure_distance()
            if dist is None or Dist>100:
                msg = 'No obstacles detected'
            else:
                msg = f"Obstacle detected ahead: {dist:.2f} cm"
            client.send("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n")
            client.send(msg)
            client/.close()
            return
        if path == "/forward":
            forward()
        elif path == "/backward":
            backward()
        elif path == "/right":
            right()
        elif path == "/left":
            left()
        elif path == "/stop":
            stop()
        else:
            stop()
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(html)
        client.close()
        
ip = connect_wifi()

aadr = socket.getaddrinfo(ip,80)(0)[-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)

while True:
    try:
        client, addr = s.accept()
        handle_client(client)
    except Exception as e:
        print("Error:", e)
            
        
        
# print('Bot is running...')
# 
# forward()
# sleep(5)
# back()
# sleep(5)
# right()
# sleep(5)
# left()
# sleep(5)
# stop()
# 
# print('Bot has stopped...')
    