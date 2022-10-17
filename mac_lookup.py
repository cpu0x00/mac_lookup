from mac_vendor_lookup import MacLookup 
import argparse


parser = argparse.ArgumentParser(epilog="Mac Address vendor lookup utility")

parser.add_argument('--mac', '-m', help='the mac address to lookup')
parser.add_argument('--update', action='store_true', help='update the mac address lookup database')

arg = parser.parse_args()

mac = arg.mac

def update_database():
   print('[+] updating the mac addresses database')
   MacLookup().update_vendors()
   print('[*] done !')

def lookup(mac):

   try:

      vendor = MacLookup().lookup(mac)
      print(f'[*] vendor found: {vendor}')

   except Exception as e:

      if "could not be found" in str(e):
         exit('[-] the vendor is not found, try updating the database with [./mac_lookup.py --update] and try again ')
   



if arg.update:

   update_database()

if mac:
   lookup(mac)
