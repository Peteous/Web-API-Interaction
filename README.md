# Web-API-Interactions
## A Repo of Assorted Scripts that Interact with Web API’s
### Table of Contents
1. Add to Instapaper
	- Functions
	- Requirements
2. Encode

### 1. Add to Instapaper
#### Functions
The Add to Instapaper script is designed to be used in Pythonista for iOS. Therefore, it imports the apex and clipboard library that are available in Pythonista. It cannot function without these libraries. The script will take your login information for Instapaper and encode it into a string ready for the Instapaper simple API using Encode.py. It gets the bookmark link that you want to save to Instapaper from either the share sheet or the clipboard, depending on whether it is running from the share sheet or not. It then will add the url to Instapaper via the `addToInstapaper()` method. The script is set-up such that it can either be run as a main script or be imported to other scripts. 
#### Requirements
This script requires the `appex` and `clipboard` libraries from Pythonista for iOS. Therefore, it will not run properly without those. Future development will try to circumvent these restrictions. The script also uses the `urlEncode()` method from the `Encode` script, also included in this repository. If that script is not found, this script will establish the method that it needs. 

### 2. Encode
This script contains functions to encode input for usage in urls. This is done through the `urlEncode()` function. It has a variety of parameter combinations to be as flexible as possible. The `urlEncode()` method uses an internal method called `_urlCharShift()` in order to perform the required character changes for url encoding text. The script also contains function `htmlEncode()` which prepares a string input for usage in html text. 

The functionality of this script will be expanded upon in the future to include other necessary encoding functionality. 