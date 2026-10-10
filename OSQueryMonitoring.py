import subprocess
import json

def run_osquery(query):
    result = subprocess.run(
        ["osqueryi", "--json", query],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)
def pretty():
    json.dumps(indent=4, sort_keys=True)
def get_listening_ports():
    ports = run_osquery("SELECT pid, port, address FROM listening_ports;")
    filter = [
    p for p in ports
    if p["port"] != "0" and p["address"] != "" and p["pid"] != "-1"]
    return filter

def get_processes():
    return run_osquery("SELECT pid, name, path FROM processes;")

def get_users():
    return run_osquery("SELECT * FROM users;")
