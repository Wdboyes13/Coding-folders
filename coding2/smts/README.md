# Simple Message Transfer Service
### A message transfer protocol written in python3  

To send data
```py
import smts
smts.send('host', port, sender_uid, receiver_uid, "Message", message_id)
```