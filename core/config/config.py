# Anongt Version
VERSION = "1.0.0"

# exclude locals
TOR_EXCLUDE = "192.168.0.0/16 172.16.0.0/12 10.0.0.0/8 127.0.0.0/8"
RESV_IANA="0.0.0.0/8 100.64.0.0/10 169.254.0.0/16 192.0.0.0/24 192.0.2.0/24 192.88.99.0/24 198.18.0.0/15 198.51.100.0/24 203.0.113.0/24 224.0.0.0/3"

# tor uid
TOR_UID = "debian-tor"

# tor socks port
TOR_PORT = "9040"

# tor dns port
TOR_DNS = "9053"

# tor virtual address network
VIRTUAL_ADDR = "10.192.0.0/10"




# tor config files
TORRC = "/etc/tor/torrc"

# backup dir
BACKUPDIR = "/var/lib/anongt"

# current dir
CURRTENTDIR = "/usr/share/AnonGT/"

