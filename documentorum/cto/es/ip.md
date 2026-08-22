> The **Linux `ip` program** is a command-line utility used for configuring and managing network interfaces, routing tables, IP addresses, tunnels, and various network-related settings in Linux, replacing older tools like `ifconfig` and `route` with a more powerful and unified interface.
> 

## Index

## Implementation

> The **`ip` command** utility in Linux is implemented as a user-space tool that interacts with the **netlink** subsystem in the Linux kernel.
> 

- **Netlink (`net/netlink/`)** → Handles communication between `ip` and the kernel.
- **Routing (`net/ipv4/fib.c`, `net/ipv6/route.c`)** → Manages IP routes.
- **Device Management (`net/core/dev.c`)** → Manages network interfaces.
- **Neighbor Discovery (`net/ipv4/arp.c`, `net/ipv6/ndisc.c`)** → Handles ARP/NDP.
- rtnetlink → …

## Objects

| **IP Object** | **Definition** |
| --- | --- |
| **address** | Manages IP addresses assigned to network interfaces. |
| **addrlabel** | Configures address labels for IPv6 policy-based routing. |
| **fou** | Foo-over-UDP (FOU) encapsulation configuration. |
| **help** | Displays help information for `ip` commands. |
| **ila** | Identifier-Locator Addressing (ILA) configuration for IPv6. |
| **ioam** | In-situ Operations, Administration, and Maintenance (IOAM) configuration for network telemetry. |
| **l2tp** | Configures L2TP (Layer 2 Tunneling Protocol) tunnels. |
| **link** | Manages network interfaces (links), including their state and properties. |
| **macsec** | Configures MACsec (Media Access Control Security) for securing Ethernet frames. |
| **maddress** | Manages multicast addresses for network interfaces. |
| **monitor** | Captures and displays real-time network events. |
| **mptcp** | Configures Multipath TCP (MPTCP) settings. |
| **mroute** | Manages multicast routing entries in the kernel. |
| **mrule** | Manages multicast routing rules. |
| **neighbor** | Manages ARP/NDP neighbor cache entries. |
| **neighbour** | Alias for `neighbor`, same function. |
| **netconf** | Manages per-namespace network configurations. |
| **netns** | Manages Linux network namespaces. |
| **nexthop** | Manages next-hop entries for advanced routing. |
| **ntable** | Configures ARP/NDP cache settings (neighbor tables). |
| **ntbl** | Alias for `ntable`, same function. |
| **route** | Manages routing table entries. |
| **rule** | Configures policy-based routing rules. |
| **sr** | Manages Segment Routing (SR) settings. |
| **tap** | Manages TAP devices (virtual network interfaces for user-space applications). |
| **tcpmetrics** | Configures and displays TCP performance metrics. |
| **token** | Manages IPv6 tokenized interface identifiers. |
| **tunnel** | Manages network tunnels (GRE, IPIP, SIT, etc.). |
| **tuntap** | Configures TUN/TAP virtual network devices. |
| **vrf** | Manages Virtual Routing and Forwarding (VRF) instances. |
| **xfrm** | Configures IPsec and policy-based encryption. |

## References

- https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf
- https://www.cyberciti.biz/faq/linux-ip-command-examples-usage-syntax/
- https://man7.org/linux/man-pages/man8/ip.8.html