#! /usr/bin/python3.8

"""
Creates OVPN certs for these guys
"""

# import subprocess
import shutil
import argparse
import re
import subprocess
import ovpnfiles as cfg


def build_cli():
    """ build the arg parse for this script """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--type", help="Name of Certs (either Student or Cadre)",
        type=str
    )
    parser.add_argument(
        "-n", "--name", help="This will be the name of your certs", type=str
    )
    parser.add_argument(
        "-c", "--count", help="How many certs do you need", type=int
    )
    return parser


def valid_cert(cert):
    """ validate cert name convention """
    if re.match("[Ss]tudents?", cert) or re.match("[Cc]adres?", cert):
        return cert
    raise TypeError("Not the correct cert type, either student or cadre")


def valid_name(name):
    """ validate name length/convention """
    if len(str(name)) > 10:
        raise NameError("Thats too long of a name. Less then 10 char pls")


def write_certs(info):
    """
    info = dict
    the loop to start creeating how ever many certs they requested
    added abs just incase they entered a negative int
    """
    for n in range(1, abs(info['count']) + 1):
        # name the client_cert
        client_name = info['name'] + "{:03}".format(n)
        # create the cert
        subprocess.run([
            cfg.file_loc["easyrsa"] + "easyrsa",
            "build-client-full",
            client_name,
            "nopass"
            ], check=True)
        # create the name of the new cert from info
        client_cert = client_name + ".ovpn"
        # copy base config to new cert
        shutil.copyfile(
            cfg.file_loc["client_conf"] + 'client.conf',
            cfg.file_loc["client_conf"] + client_cert
            )
        # open new file for appending certs too
        with open(cfg.file_loc["client_conf"] + client_cert, "a") as newconf:
            newconf.write("<ca>\n")
            with open(cfg.file_loc["key_dir"] + "ca.crt", "r") as ca:
                newconf.write(ca.read())
            newconf.write("<\\ca>\n<cert>\n")
            with open(cfg.file_loc["pub"] + client_name + ".crt", "r") as cert:
                newconf.write(cert.read())
            newconf.write("<\\cert>\n<key>\n")
            with open(cfg.file_loc["priv"] + client_name + ".key", "r") as key:
                newconf.write(key.read())
            newconf.write("<\\key>\n<tls-crypt>\n")
            with open(cfg.file_loc["key_dir"] + "ta.key", "r") as ta:
                newconf.write(ta.read())
            newconf.write("<\\tls-crypt>\n")


def main():
    """ entry point """
    args = vars(build_cli().parse_args())
    # run necessary checks on input
    valid_cert(args['type'])
    valid_name(args['name'])
    write_certs(args)


if __name__ == "__main__":
    main()
