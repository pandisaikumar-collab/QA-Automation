> What happens when you type google.com in the browser:

 Step1: DNS Lookup (Layer 7-3)
 -----------------------------
  i. when you type google.com, your system asks DNS:
  ii. what is the IP address of google.com:
  iii. DNS returns the IP address of google.com (e.g., 142.x)
  iv. now your browser knows where to send the request (to 142.x)

  Diagram:
  [Browser] --DNS Lookup--> [DNS Server]
  [DNS Server] --IP Address--> [Browser]


step2: TCP Handshake (Layer 4):
-------------------------------
 > your system sends SYN packet to the server
 > Google replies with SYN-ACK packet
 > your system sends ACK packet to the server
 > TCP connection is established
 > This is called the three-way handshake


 i. Browser initiates a TCP connection to the server at 142.x:
 ii. Browser sends a SYN packet to the server (142.x):
 iii. Server responds with a SYN-ACK packet:
 iv. Browser sends an ACK packet to complete the handshake:
 v. Now, a TCP connection is established between the browser and the server.

 Diagram:
 [Browser] --SYN--> [Server]
 [Server] --SYN-ACK--> [Browser]
 [Browser] --ACK--> [Server]


Step3: TLS Handshake (if HTTPS is used):
----------------------------------------
> because your using https://google.com
> Now encryption starts:
 - browser and server exchange certificates
 - they agree on encryption algorithms
 - they generate session keys for encryption
 - Key exchange happens securely
 - Now, a secure TLS connection is established between the browser and the server.






























