import time, requests, getpass, os.path, threading, sys

# This function calls the post action on the Tesla REST API to
# activate the HVAC system with its previous temperature setting.
def start_heating(myVehicleID, myAccessToken):
    chargeStateReq = requests.post('https://owner-api.teslamotors.com/api/1/vehicles/' + str(myVehicleID) + '/command/auto_conditioning_start', headers = {'Authorization' : 'Bearer ' + myAccessToken})
    try:
        response = chargeStateReq.json()["response"]
        print("started: {}".format(response))
    except ValueError:
        print("ValueError")
    pass

# This function calls the post action on the Tesla REST API to
# deactivate the HVAC system.
def stop_heating(myVehicleID, myAccessToken):
    chargeStateReq = requests.post('https://owner-api.teslamotors.com/api/1/vehicles/' + str(myVehicleID) + '/command/auto_conditioning_stop', headers = {'Authorization' : 'Bearer ' + myAccessToken})
    try:
        response = chargeStateReq.json()["response"]
        print("stopped: {}".format(response))
    except ValueError:
        print("ValueError")
    pass

# This function is the main loop to check if the file is present or not.
# If the file is present, the tesla_loop_function for CamperMode will be
# called and executed until the file is not present anymore.
def mainLoopFunction(myVehicleID, myAccessToken):
    if (os.path.isfile("/var/www/tesla/camper/is_currently_heating")):
        print("Heating started...")
        start_heating(myVehicleID, myAccessToken)
    else:
        print("Heating stopped...")
        stop_heating(myVehicleID, myAccessToken)
    time.sleep(20*60)
    return

def theMainLoop():
    while True:
        pass
    print("This should never be executed.")
    pass

# This function queries the access token, vehicle list of the first
# reported vehicle on the account. API errors are ignored and it will
# be tried again after 10 seconds.
def tesla_loop_function():
    global eMail, password
    #general variables
    myAccessToken = ""
    myVehicleID = 0
    accessTokenIsInvalid = True

    #Main Loop
    while (True):
        while (accessTokenIsInvalid):
            try:
                #Getting AccessToken
                accessTokenReq = requests.post('https://owner-api.teslamotors.com/oauth/token', data = {'grant_type' : 'password', 'client_id' : 'e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e', 'client_secret' : 'c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220', 'email' : eMail, 'password' : password, })
                if (str(accessTokenReq) == "<Response [200]>"):
                    myJson = accessTokenReq.json()
                    myAccessToken = myJson["access_token"]
                    #Getting VehicleList
                    vehicleListReq = requests.get('https://owner-api.teslamotors.com/api/1/vehicles', headers = {'Authorization' : 'Bearer ' + myAccessToken})
                    if (str(vehicleListReq) == "<Response [200]>"):
                        myVehicleList = vehicleListReq.json()["response"]
                        myVehicleID = myVehicleList[0]["id"]
                        accessTokenIsInvalid = False
                        mainLoopFunction(myVehicleID, myAccessToken)
                    else:
                        accessTokenIsInvalid = True
                        print("accessTokenIsInvalid = True")
                        time.sleep(10)
                else:
                    accessTokenIsInvalid = True
                    print("accessTokenIsInvalid = True")
                    time.sleep(10)
                pass
            except:
                print("Error... Trying again...")
            pass
    return

def main(argv):
    global eMail, password
    eMail = raw_input('Enter your Tesla Account eMail: ')
    password = getpass.getpass('Enter your Tesla Account password: ')
    tesla_loop_function()
    pass

if __name__ == "__main__":
    main(sys.argv)