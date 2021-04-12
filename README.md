# hw-text2pcap
A Python script to parse captured packets on a CLI terminal of Huawei VRP device into Wireshark text2pcap compatible hexdump 

## Framework
* re: Regular expression
* PySimpleGUIWx: GUI front-end of python script

## Getting Started
Install dependency (if GUI front-end is required)
```sh
pip install PySimpleGUIWx
```
## How To Use
Run the script by providing the inputfile path as the argument
```sh
python hw-text2pcap.py inputfile
```
Alternatively, drag and drop the inputfile to the script. The inputfile path is passed as the first argument

## How It Works
1. Input capture-packet information on Huawei VRP platform
```
Packet(inbound): 1
  -------------------------------------------------------
  01 00 5e 0b 01 72 78 1d ba 32 04 a1 81 00 00 01 
  08 00 45 00 05 4c 00 00 40 00 7d 11 fa 66 0a f0 
  02 cd ef 0b 01 72 1f 6a 56 ce 05 38 e2 d7 80 21 
  -------------------------------------------------------

  DMAC: 0100-5e0b-0172      SMAC: 781d-ba32-04a1
  VLAN: 1       8021P: 0
  IPv4 Next Proto: 17       TTL: 125     DSCP: 0
  SIP: 10.240.2.205        DIP: 10.11.1.114
  UDP Multicast Packet RTP SEQ: 23354
  UDP Multicast Packet Time Stamp: 2018/12/11 23:02:40
  -------------------------------------------------------

Packet(inbound): 2
  -------------------------------------------------------
  01 00 5e 0b 01 72 78 1d ba 32 04 a1 81 00 00 01 
  08 00 45 00 05 4c 00 00 40 00 7d 11 fa 66 0a f0 
  02 cd ef 0b 01 72 1f 6a 56 ce 05 38 e2 d7 80 21 
  -------------------------------------------------------

  DMAC: 0100-5e0b-0172      SMAC: 781d-ba32-04a1
  VLAN: 1       8021P: 0
  IPv4 Next Proto: 17       TTL: 125     DSCP: 0
  SIP: 10.240.2.205        DIP: 10.11.1.114
  UDP Multicast Packet RTP SEQ: 23354
  UDP Multicast Packet Time Stamp: 2018/12/11 23:02:40
  -------------------------------------------------------

```
2. The output is the hexdump for Wireshark text2pcap 
```
0000 01 00 5e 0b 01 72 78 1d ba 32 04 a1 81 00 00 01 
0016 08 00 45 00 05 4c 00 00 40 00 7d 11 fa 66 0a f0 
0032 02 cd ef 0b 01 72 1f 6a 56 ce 05 38 e2 d7 80 21 
0000 01 00 5e 0b 01 72 78 1d ba 32 04 a1 81 00 00 01
```
3. Use Wireshark text2pcap to generate pcap
```
text2pcap -o dec <infile> <outfile>
```

## GUI front-end
GUI front-end interface to build argument and invoke the CLI script 
```sh
python hw-text2pcap-gui.py
```
