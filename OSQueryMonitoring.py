import subprocess
import json

def run_osquery(query):
    result = subprocess.run(
        ["osqueryi", "--json", query],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)

def get_listening_ports():
    return run_osquery("SELECT pid, port, address FROM listening_ports;")

def get_processes():
    return run_osquery("SELECT pid, name, path FROM processes;")

def get_users():
    return run_osquery("SELECT * FROM users;")
