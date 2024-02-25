import json

# Load JSON data from the file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Extract relevant information
interfaces = data.get('imdata', [])

# Print the formatted output
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    dn = interface.get('fvCEp', {}).get('attributes', {}).get('dn', '')
    description = interface.get('fvCEp', {}).get('attributes', {}).get('descr', 'inherit')
    speed = interface.get('fvCEp', {}).get('attributes', {}).get('speed', 'inherit')
    mtu = interface.get('fvCEp', {}).get('attributes', {}).get('mtu', 'inherit')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
