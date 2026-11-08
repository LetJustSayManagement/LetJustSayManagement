import subprocess
import json

def Run_Osquery(query):
    result = subprocess.run(
        ["osqueryi", "--json", query],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)
def pretty(data):
    return json.dumps(data, indent=4, sort_keys=True)
def get_listening_ports():
    ports = Run_Osquery("SELECT pid, port, address FROM listening_ports;")
    filtered = [
    p for p in ports
    if p["port"] != "0" and p["address"] != "" and p["pid"] != "-1"]
    return filtered

def get_processes():
    return Run_Osquery("SELECT pid, name, path FROM processes;")

def get_users():
    return Run_Osquery("SELECT * FROM users;")
