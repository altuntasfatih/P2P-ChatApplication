# P2P CHAT APPLICATION


## Summary

In this project we are operating peer to peer chatting using high level socket programming.
Briefly, P2P chat is a chat method which provides send messages directly communicating
with peers without using servers.

We have two main component which are Server (registry) and Client (peer).

**Simply,** on client side, user will send register request to register himself into Server, after
registering also user will send login request to login Server. After login processes user will be
able to chat with other peers.

On server side, server has ability to accept and reject requests which comes from the users.
If user logins in successfully, server will send online user list to user. And user will see online
users to start chat.

Also server and client has different functionalities like checking and sending “hello”
messages, etc.

## Solution to Approach

We need to do more than one job at the same time. Therefore we are implementing multi-
thread system.

**On server side** , we are using MongoDB to manage and store data. There are TCP socket
which listens port 3131 and UDP socket which listens 5151. We are starting a thread for each
user who wants to communicate with server to listen TCP socket and handle requests. These
threads are working until user are logged out or ends to application. And we are starting one
more thread to listen UDP socket and catch “hello” messages which comes from peers.

**On client side** , after login process, user starts a channel between himself and server. By
using this channel, he makes server operations like sending request and sending “hello”

Also client has two main thread. First one is listening the chat requests which comes from
other peers. Second thread is for get messages from peers and print these messages to chat
screen.

Client has a data structure ( **chat_list** ). If other peers accept our chat request, the peer who
sent the request add the user he want to communicate with into **chat_list**. If user wants to
send a message, message will be sent everyone in the **chat_list**.


## PROTOCOLS

We have 5 type request between server and client:

*  Register : In data part, we are sending “password”.
*  Login: In data part, we are sending “password”.
*  Search: In data part, we are sending the username which we want to search. We
    never use the request. Instead of we used “all online”.
*  Logout: In data part, we are sending ‘LOGOUT’ message.
*  All Online: In data part, we are sending ‘All’ message.

<img width="668" alt="screen shot 2017-12-19 at 00 38 39" src="https://user-images.githubusercontent.com/13722649/34129405-11906292-e455-11e7-8b51-6781447c7be1.png">


### We have 2 different package type between client and client:

*  Message package:

    | Type will be 0 | 
    | -------------  |       
    | Type (b)       |
    | Username (10s) |
    | Message (100s) |
    
    

*   Notify and Request: <br>
    In Notify, type will be “1”, Message will be “New User” and Data will be IP address.
    Also we are sending current chat_list to handle group chat. If new user appears, old
    users will be informed.
    <br>In Request, type will be “0”, Message will be “CHAT REQUEST” and Data will be username. 
    
    | Type will be 1 | 
    | -------------  |
    | Type (b)       |
    | Data (15s)     |
    | Message (10s)  |
    | chat_list      |

<img width="905" alt="screen shot 2017-12-19 at 00 48 02" src="https://user-images.githubusercontent.com/13722649/34129783-6a51f638-e456-11e7-8dfc-35597ca3df25.png">
