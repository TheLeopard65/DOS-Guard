from flask import Flask, render_template
import scapy.all as scapy
import threading, sqlite3, os
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FIXER-DETECTOR'

socketio = SocketIO(app, async_mode='eventlet')

logs = sqlite3.connect("Events.db")
if not os.path.exists("Events.db"):
    logs.execute("Create Table Packets (Serial INT PRIMARY KEY, Packet_id INT, Source VARCHAR(15), Destination VARCHAR(15), TTL INT, Protocol VARCHAR(10), Length INT, Checksum INT)")

i = 1
packets = []

protocol_names = { 1:'ICMP', 6:'TCP', 17:'UDP', 27:'RDP', 37:'DDP', 57:'SKIP', 118:'STP', 121:'SMP', 136:'UDPLite'}

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    pass

@socketio.on('disconnect')
def handle_disconnect():
    pass

def get_protocol_name(proto_num):
    return protocol_names.get(proto_num, '<N/A>')

def printer(packet):
    if scapy.IP in packet:
        pkt = packet[scapy.IP]
        global i
        protocol_name = get_protocol_name(pkt.proto)
        packet_data = {"i": i,"id": pkt.id, "src": pkt.src, "dst": pkt.dst, "ttl": pkt.ttl, "proto": protocol_name, "len": pkt.len, "chksum": pkt.chksum}
        packets.append(packet_data)
        socketio.emit('packet', packet_data)
        insert = f'''Insert into Packets (Serial, Packet_id, Source, Destination, TTL, Protocol, Length, Checksum) VALUES ("{i}", "{pkt.id}", "{pkt.src}", "{pkt.dst}", "{pkt.ttl}", "{protocol_name}", "{pkt.len}", "{pkt.chksum}")'''
        logs = sqlite3.connect("Events.db")
        logs.execute(insert)
        logs.commit()
        logs.close()
        i += 1

def packet_sniffer():
    scapy.sniff(prn=printer, store=False)

if __name__ == "__main__":
    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.start()
    socketio.run(app, debug=False)
