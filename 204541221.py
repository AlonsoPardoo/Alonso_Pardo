nativeVLAN = 99
SW1VLAN = 10,20,30
SW1vlan = 10,20,30
nativeVLAN2 = 200
SW2VLAN = 40,50,60
SW2vlan = 40,50,60

if nativeVLAN == SW1VLAN:
    print("La VLAN nativa del SW1 y los datos VLAN son iguales.")
else:
     print("La VLAN nativa del SW1 y los datos VLAN son diferentes.")

if SW1VLAN == SW1vlan:
    print("Las VLAN del SW1 y los datos VLAN son iguales.")
else:
    print("Las VLAN del SW1 y los datos VLAN son diferentes.")

if nativeVLAN2 == SW2VLAN:
    print("La VLAN nativa del SW2 y los datos VLAN son iguales.")
else:
       print("La VLAN nativa del SW2 y los datos VLAN son diferentes.")

if SW2VLAN == SW2vlan:
    print("Las VLAN del SW2 y los datos VLAN son iguales.")
else:
    print("Las VLAN del SW2 y los datos VLAN son diferentes.")

