#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.upper() == "MTG":
    print("The hostname was found to be MTG")
    print("hostname matches expected config")

    print("Exiting the script")
