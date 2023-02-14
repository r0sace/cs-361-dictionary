# cs-361-dictionary

Communication Contract for Partner's Microservice<br><br>

1. Requesting Data from the Microservice
    * Program will have a function that will open a socket connection with the microservice.
    * To request a password strength score from the microservice, it will provide an existing or generated password that is passed through the socket

    Example:
    1. User selects if they would like to provide a password or use a generated password to score.
    2. A function will be called where it will open a connection with the microservice and send over the password through the socket.
    3. The microservice will return a password strength score to the client.

2. Retrieving Data from the Microservice
    * My microservice will work by waiting for a socket connection and a password (already-existing or generated from the client's side) that is passed through the socket.
    * It will utilize the password_strength module from PasswordStats with the password passed through the socket to request for a password strength score out of 99.
    * The a string including the score will be sent back through the socket to the client where it can be printed onto the user terminal.
  

   
<img width="992" alt="Screenshot 2023-02-13 at 10 35 49 PM" src="https://user-images.githubusercontent.com/91238002/218633242-b3c537bd-d0e3-4d8d-bc62-1ecf9f0a7948.png">
