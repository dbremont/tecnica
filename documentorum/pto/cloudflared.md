# Cloudflared

> An overlay network client that establishes outbound, encrypted control and data channels to Cloudflare’s edge, enabling private services to be exposed without inbound firewall openings.

> Cloudflared is not a tunnel - well yes (it's  a overlay - outbound connection enabler tool) - but it also offerts tunelling.

## Characterization

**Cloudflared is not the tunnel itself.**
It is the **daemon/client** that:

1. Initiates an outbound connection (typically over QUIC or HTTPS) to Cloudflare’s global edge.
2. Authenticates the origin service.
3. Registers a routing rule (hostname → local service).
4. Maintains persistent multiplexed connections.
5. Forwards traffic between the edge and the local origin.

The actual “tunnel” is the **logical connectivity fabric** formed between:

* The Cloudflare edge network, and
* One or more running cloudflared instances associated with a Tunnel ID.

## How's Tos

> `cloudflared tunnel --url http://localhost:8000`

## Architectural Model

### Control Plane

* Tunnel creation (UUID)
* Credential issuance
* Route binding (e.g., `app.example.com → localhost:8080`)
* Managed via Cloudflare Zero Trust / API

### Data Plane

* Outbound encrypted sessions from cloudflared to Cloudflare edge
* Edge receives public traffic
* Traffic is multiplexed over persistent connections
* Forwarded to local service via TCP/HTTP proxying

## Why It Is Not a “Tunnel” in the Classical Sense?

In classical networking:

* A tunnel = encapsulation of packets within another protocol (e.g., GRE, IPSec, VXLAN).
* Typically bidirectional and network-layer oriented.

Cloudflared:

* Operates primarily at L7 (HTTP) or L4 proxy level.
* Does not create a virtual network interface by default.
* Does not expose a routed subnet.
* Does not require inbound NAT/firewall rules.

Thus, more accurately:

> It is an outbound reverse-proxy agent participating in an overlay connectivity system.

## Refernces

- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)
