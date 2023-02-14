# cs-361-dictionary

Communication Contract<br><br>
A) Requesting Data from the Microservice
  - The microservice will be inside of random_word function which receives no arguments inside of the main (client) code.
  - A user will be prompted if they would like to generate a random word, if so, the random_word function will be called.
  - Once the function is called, the microservice connection will be established and the client will send "Generating random word..." to server.
  
  Example:<br>
  1. User selects that they would like a random word.<br>
  2. random_word() is called.<br>
  3. Server prints "Generating random word..."<br>
    
  B) Retrieving Data from the Microservice
  - The server will then print the message it received from the client and begin generating a random word using a GET request to WordsAPI with
    the random flag set to true. Example: https://wordsapiv1.p.mashape.com/words?random=true
  - The get request will return a JSON structure, however, the microservice just needs to grab the "word" from the JSON.
  - The word will be sent back to the client, and printed to the user.
  

   
<img width="992" alt="Screenshot 2023-02-13 at 10 35 49 PM" src="https://user-images.githubusercontent.com/91238002/218633242-b3c537bd-d0e3-4d8d-bc62-1ecf9f0a7948.png">
