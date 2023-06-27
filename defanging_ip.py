'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
'''
address = '1.1.1.1'


def defangIPaddr(address):
    add_arr = address.split('.')
    return '[.]'.join(add_arr)


print(defangIPaddr(address))
