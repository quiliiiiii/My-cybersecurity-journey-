from flask import Flask, render_template
app = Flask(name)
packets = [
{
"source_ip": "192.168.1.10",
"destination_ip": "8.8.8.8",
"protocol": "DNS",
"port": 53,
"status": "Normal",
"reason": "DNS request to a public DNS server"
},
{
"source_ip": "192.168.1.15",
"destination_ip": "192.168.1.1",
"protocol": "HTTP",
"port": 80,
"status": "Normal",
"reason": "Regular web traffic"
},
{
"source_ip": "192.168.1.25",
"destination_ip": "203.0.113.50",
"protocol": "SSH",
"port": 22,
"status": "Suspicious",
"reason": "SSH connection to an unknown external IP"
},
{
"source_ip": "192.168.1.30",
"destination_ip": "198.51.100.20",
"protocol": "RDP",
"port": 3389,
"status": "Suspicious",
"reason": "RDP traffic exposed to an external address"
},
{
"source_ip": "192.168.1.40",
"destination_ip": "142.250.190.14",
"protocol": "HTTPS",
"port": 443,
"status": "Normal",
"reason": "Encrypted web traffic"
}
]
@app.route("/")
def index():
total_packets = len(packets)
suspicious_packets = len([packet for packet in packets if packet["status"] == "Suspicious"])
normal_packets = total_packets - suspicious_packets
return render_template(
    "index.html",
    packets=packets,
    total_packets=total_packets,
    suspicious_packets=suspicious_packets,
    normal_packets=normal_packets
)
if name == "main":
app.run(debug=True)
