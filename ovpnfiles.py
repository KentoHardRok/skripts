#! /usr/bin/env python

"""
config file for ovpnconf
"""

CERT = {
    "student": "/etc/students-openvpn/",
    "cadre": "/etc/cadre-openvpn/"
    }

FILE = {
    "priv": "easy-rsa/easyrsa3/pki/private/",
    "pub": "easy-rsa/easyrsa3/pki/issued/",
    "key_dir": "easy-rsa/easyrsa3/pki/",
    "client_conf": "easy-rsa/easyrsa3/clients/",
    "easyrsa": "easy-rsa/easyrsa3/"
    }
