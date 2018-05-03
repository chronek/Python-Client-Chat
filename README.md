### Developers
* Chris Hronek
* Jacob Huss
* Kirill Kudaev


##### Server program runs on port 5002
##### Server IP address: set to the desired IP address


#### To run the server
```terminal
$ python3 server.py
```
#### To terminate the server program
```terminal
use control + c
```
#### To run the client
```terminal
$ python3 client.py
```

## Server Specifications
  - maintains a list of usernames and passwords
    - usernames and passwords read in from json file when starting up
    - passwords are encrypted prior to transmission or saving
    - new users can be added using a supporting program to encrypt passwords if desired
  - authenticates users through client requests
    - 4 failed authentications locks a user out for 5 minutes
  - once a user has been authenticated the server does the following
    - sends a list of online users to the newly authenticated users
    - sends a broadcast message to all others that the user is now online
  - relays all broadcast messages to all other online users
  - delivers private messages directly to specified user
    - private messages for offline users are stored and delivered when that user comes back online
  - control + c terminates the server program
  - go to util folder and run utililty.py to make a new user

## Client Specifications
- promts a username and a password from users
- authenticate with the server
- repeats if needed and provide feedback to user
- displays list of other online users when provided by server
- displays any server provided messages
- provides method for sending broadcast messages
- provides method for sending private messages
- provides method for going offline and reporting this to the server

```terminal
Type a message to broadcast it to everyone on the server.
Type @<username> <message> to send a PM to a user.
Type !quit to log out.
```
