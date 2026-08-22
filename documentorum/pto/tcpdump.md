# tcpdump

> `tcpdump` is a powerful command-line packet analyzer used in Linux and other Unix-like operating systems. It captures network packets and displays them in a human-readable format. 

> `tcpdump` relies on the **libpcap** library, which provides a platform-independent API for capturing network traffic. Libpcap abstracts the details of packet capture, allowing `tcpdump` to be portable across different operating systems.


QA:

- …

## Index

## Usage

```c
Usage: tcpdump [-AbdDefhHIJKlLnNOpqStuUvxX#] [ -B size ] [ -c count ] [--count]
		[ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
		[ -i interface ] [ --immediate-mode ] [ -j tstamptype ]
		[ -M secret ] [ --number ] [ --print ] [ -Q in|out|inout ]
		[ -r file ] [ -s snaplen ] [ -T type ] [ --version ]
		[ -V file ] [ -w file ] [ -W filecount ] [ -y datalinktype ]
		[ --time-stamp-precision precision ] [ --micro ] [ --nano ]
		[ -z postrotate-command ] [ -Z user ] [ expression ]
```

## **Packet Capture Process**

`tcpdump` uses the following steps to capture packets:

1. **Open Network Interface**: The user specifies a network interface (e.g., `eth0`, `wlan0`), which `tcpdump` opens for packet capture.
2. **Set Capture Filters**: Users can specify BPF (Berkeley Packet Filter) expressions to filter packets. Libpcap translates these filters into kernel-level instructions, ensuring only relevant packets are captured.
3. **Capture Loop**: `tcpdump` enters a loop where it continuously reads packets from the specified interface. It calls libpcap's functions to retrieve packets, which are then processed.
4. **Display and Process Packets**: As packets are captured, `tcpdump` decodes and displays their contents, including protocol headers and payload data. It formats the output according to user preferences (e.g., verbose, hex output).

## **Packet Decoder**

> `tcpdump` includes a packet decoding engine that interprets various network protocols (e.g., Ethernet, IP, TCP, UDP) and formats the output.
> 

## How’s To

```bash
-- Intercept All Packet From a Process
sudo ss -p | grep <PID>
sudo tcpdump -i <interface> port <port_number> -w capture.pcap
sudo strace -e trace=network -p

```

## References

- https://github.com/the-tcpdump-group/tcpdump
- https://en.wikipedia.org/wiki/Pcap
- https://en.wikipedia.org/wiki/Ngrep
- https://en.wikipedia.org/wiki/Tcpdump
