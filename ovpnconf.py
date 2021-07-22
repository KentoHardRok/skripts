#! /usr/bin/env python3

"""
Creates OVPN certs for these guys
"""

# import subprocess
import argparse
import re
import subprocess
import ovpnfiles as cfg


def build_cli():
    """ build the arg parse for this script """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--type", help="Type of Certs (Student or Cadre)", type=str
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
    if re.match("[Ss]tudents?", cert):
        cert = cfg.CERT["student"]
        return cert
    elif re.match("[Cc]adres?", cert):
        cert = cfg.CERT["cadre"]
        return cert
    raise TypeError("Not the correct cert type, either student or cadre")


def valid_name(name):
    """ validate name length/convention """
    if len(str(name)) > 10:
        raise NameError("Thats too long of a name. Less then 10 char pls")


def write_certs(info, c_type):
    """
    info = dict
    the loop to start creeating how ever many certs they requested
    added abs just incase they entered a negative int
    """
    base_conf_loc = c_type + cfg.FILE["client_conf"] + 'client.conf'
    ca_crt_loc = c_type + cfg.FILE["key_dir"] + "ca.crt"
    ta_key_loc = c_type + cfg.FILE["key_dir"] + "ta.key"
    try:
        for i in range(1, abs(info['count']) + 1):
            # name the client_cert
            client_name = info['name'] + "{:03}".format(i)
            # now we can create the user specific script callouts
            # my logic here is since each cert is numbered, and the
            # number comes from the loop, these variables must be defined
            # in the loop
            user_cert_loc = c_type + cfg.FILE["pub"] + client_name + ".crt"
            user_key_loc = c_type + cfg.FILE["priv"] + client_name + ".key"
            # create the cert
            subprocess.run([
                c_type + cfg.FILE["easyrsa"] + "easyrsa",
                "--pki-dir=" + c_type + cfg.FILE["key_dir"],
                "build-client-full", client_name, "nopass"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT,
                           check=True)
            # create the name of the new cert from info
            client_cert = client_name + ".ovpn"
            # open new file for appending certs too
            with open(
                    c_type + cfg.FILE["client_conf"] + client_cert, "a+"
                    ) as newconf:
                with open(base_conf_loc, "r") as base:
                    newconf.write(base.read())
                newconf.write("<ca>\n")
                with open(ca_crt_loc, "r") as ca_cert:
                    newconf.write(ca_cert.read())
                newconf.write("<\\ca>\n<cert>\n")
                with open(user_cert_loc, "r") as cert:
                    newconf.write(cert.read())
                newconf.write("<\\cert>\n<key>\n")
                with open(user_key_loc, "r") as key:
                    newconf.write(key.read())
                newconf.write("<\\key>\n<tls-crypt>\n")
                with open(ta_key_loc, "r") as ta_key:
                    newconf.write(ta_key.read())
                newconf.write("<\\tls-crypt>\n")
    except Exception:
        print("There was a problem during the cert creation process!")
    else:
        print(
            "Succesfully Created your " + str(abs(info['count'])) + " " +
            info['name'] + " files in " + c_type + cfg.FILE["client_conf"]
            )


def main():
    """ entry point """
    args = vars(build_cli().parse_args())
    # run necessary checks on input
    valid_name(args['name'])
    write_certs(args, valid_cert(args['type']))


if __name__ == "__main__":
    main()
