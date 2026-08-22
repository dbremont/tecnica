# SSH (Secure Shell)

> SSH is a cryptographic network protocol used to securely access and manage remote computer systems over an unsecured network. It provides a secure and encrypted communication channel between a client and a server, allowing users to execute commands, transfer files, and perform various administrative tasks on remote machines securely.
> 

> SSH is commonly used in the context of remote server administration and secure file transfers, providing a safer alternative to older protocols like Telnet and FTP, which transmit data in plaintext.
> 

> OpenSSH is an open-source implementation of the SSH (Secure Shell) protocol. It provides a suite of tools and utilities that enable secure communication and remote access to computer systems over a network.
> 

> OpenSSH is widely used and highly trusted for secure remote administration, file transfer, and tunneling encrypted network connections. It is the default SSH implementation on most Unix-like operating systems and is also available for Windows and other platforms. The OpenSSH project is actively maintained and developed by a community of volunteers, making it a critical component of secure network communication in modern computing environments.
> 

> SSHD Can block shell connections (see GITHUB sshd).
> 

> **ssh**: The client program used to establish secure shell connections to remote servers.
> 

> **scp**: A utility for securely copying files between local and remote systems.
> 

> **sftp**: A secure file transfer program that allows secure file transfers between local and remote systems, similar to FTP.
> 

> **ssh-add** (Manages keys)
> 

> **ssh-keygen** (Generates keys)
> 

> **ssh-agent** (OpenSSH Authentication Agent)
> 

> **sshd**: The server daemon responsible for accepting incoming SSH connections and managing secure remote access.
> 

> SSH users typically correspond to user accounts on the remote server’s operating system. These user accounts have associated home directories, permissions, and access rights.
> 

> SSH can be configured to create “virtual users” with restricted access to specific directories without direct OS access.
> 

![](https://assets.website-files.com/5ff66329429d880392f6cba2/61c1b963247368113bbeef17_Secure%20Shell%20work.png)

SSH Keys

## Index

## SSH Implementation

> Here's a table summarizing the key components of an SSH (Secure Shell) implementation:
> 

| Component | Description |
| --- | --- |
| **SSH Protocol** | The underlying protocol is used for secure communication over a network, providing encryption and authentication. |
| **SSH Client** | Software or application used by the user to initiate and manage SSH connections to a remote server. |
| **SSH Server** | The software runs on a remote machine that listens for incoming SSH connections and handles authentication. |
| **SSH Key Pair** | A set of cryptographic keys (public and private) used for authenticating users and establishing secure connections. |
| **Public Key** | A part of the SSH key pair is shared with the SSH server to verify the client's identity. |
| **Private Key** | A part of the SSH key pair kept secure by the client is used to authenticate to the SSH server. |
| **SSH Agent** | A program that manages private keys and provides them to SSH clients for authentication without user intervention. |
| **SSH Daemon (sshd)** | The SSH server daemon listens for and accepts incoming SSH connections and manages user sessions. |
| **SSH Configuration File** | A file (e.g., `sshd_config` on the server and `config` on the client) that specifies settings and options for SSH connections. |
| **Authentication Methods** | Mechanisms for verifying the identity of users, including password authentication, public key authentication, and more. |
| **Encryption Algorithms** | Cryptographic algorithms used to encrypt data transmitted over the SSH connection to ensure confidentiality. |
| **Port Forwarding** | A feature that allows secure tunneling of other network protocols through an SSH connection, including local and remote port forwarding. |
| **X11 Forwarding** | A feature that enables forwarding graphical applications from the remote server to the client over SSH. |
| **Key Exchange Protocols** | Diffie-Hellman or elliptic curve methods securely exchange cryptographic keys between the SSH client and server. |
| **Session Management** | Mechanisms for managing and controlling active SSH sessions, including session termination and multiplexing. |

## SSH Protocol

> Here’s a table summarizing the main parts of the SSH protocol along with their roles:
> 

| **Protocol Component** | **Role** |
| --- | --- |
| **Transport Layer** | Establishes a secure, encrypted connection. Handles encryption, data integrity, and server authentication. Uses public-key cryptography for session key negotiation. |
| **Authentication** | Verifies the identity of the user or system. It supports various methods, such as password-based, public key-based, and host-based authentication. |
| **Connection Protocol** | Manages multiple channels over a single SSH session. Establishes and handles separate logical channels for different types of data (e.g., terminal sessions, file transfers, port forwarding). |
| **Key Exchange** | Part of the Transport Layer that facilitates the secure exchange of encryption keys between the client and server. |
| **Forwarding** | Includes port forwarding and X11 forwarding mechanisms, allowing secure redirection of network traffic and graphical applications. |
| **Configuration Options** | Settings that define behavior and policies for SSH sessions, such as timeouts, allowed authentication methods, and more. |

## SSH **Authentication**

> Here’s a table summarizing the SSH authentication models
> 

| **Authentication Model** | **Description** | **Security Considerations** |
| --- | --- | --- |
| **Password-Based** | Users provide a password to authenticate. The server checks the password against stored credentials. | Less secure if passwords are weak or intercepted. |
| **Public Key-Based** | Users use a private key (client) and a public key (server). Authentication proves possession of the private key. | More secure than passwords; private keys must be protected with passphrases. |
| **Host-Based** | Authentication is based on the client machine’s identity. The server verifies the host’s credentials using known host files. | It is helpful in trusted networks but less secure in untrusted environments. |
| **Keyboard-Interactive** | The server prompts for one or more authentication information, such as passwords or additional challenge responses. | Flexible but requires secure handling of prompts and responses. |
| **Certificate-Based** | It uses digital certificates issued by a trusted certificate authority (CA) for authentication. The certificate includes a public key and identifying information. | Strong security and scalability; certificates must be appropriately managed and protected. |
| **Two-factor authentication (2FA)** | Requires a second form of authentication (e.g., a code from a token or app) in addition to the primary method. | Enhances security by requiring multiple forms of verification. |
| **Multi-Factor Authentication (MFA)** | Extends 2FA to include more than two forms of authentication (e.g., knowledge, possession, and biometric data). | Provides the highest level of security by integrating multiple authentication factors. |

```bash
ssh-keygen -t rsa -b 2048 -C "<comment>"  # The commend can be empty
ssh-add path_to_private_key # Add private key to agent.
ssh-add -l #  List all private keys.
ssh -i keyu.pk  git@github.com  # Connect  to github.
ssh -v -T git@github.com # Test connection to github.
```

- [Error: Permission denied (publickey)](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey)
- **What is the default ssh stores of keys?** - ~/.ssh

## SSH Tunneling

SSH tunneling, also known as SSH port forwarding or SSH tunnel, is a method used to secure and route network traffic between two computers over an unsecured network, such as the internet. It leverages the Secure Shell (SSH) protocol to create an encrypted communication channel, which can be used for various purposes, including enhancing security, bypassing network restrictions, and accessing services on remote machines securely.

There are three primary types of SSH tunneling:

1. **Local Port Forwarding:** Local port forwarding allows you to securely access a service or resource on a remote server as if it were on your local machine. Here’s how it works:
    - You initiate an SSH connection to a remote server with port forwarding enabled.
    - You specify a local port on your machine (e.g., localhost:8080) and a remote server’s address and port (e.g., remote-server.com:80).
    - All traffic sent to your local port is encrypted and forwarded through the SSH connection to the remote server’s port. This allows you to access a service on the remote server as if it were running locally.
    
    Example command:
    
    ```
    ssh -L 8080:remote-server.com:80 user@remote-server.com
    ```
    
2. **Remote Port Forwarding:** Remote port forwarding allows you to expose a service on your local machine to a remote server securely. It’s useful when you want to make a service running on your machine accessible from the internet via a remote server. Here’s how it works:
    - You initiate an SSH connection to a remote server with port forwarding enabled.
    - You specify a remote port on the remote server (e.g., remote-server.com:8080) and a local service’s address and port (e.g., localhost:80).
    - All traffic sent to the remote server’s port is encrypted and forwarded through the SSH connection to the local service’s port. This allows others to access your local service through the remote server.
    
    Example command:
    
    ```
    ssh -R 8080:localhost:80 user@remote-server.com
    ```
    
3. **Dynamic Port Forwarding (SOCKS Proxy):** Dynamic port forwarding allows you to create a secure SOCKS proxy server that routes traffic through an SSH tunnel. It’s useful for securely accessing the internet or bypassing network restrictions. Here’s how it works:
    - You initiate an SSH connection to a remote server with dynamic port forwarding enabled.
    - Your local machine listens on a specified local port (e.g., localhost:1080) and acts as a SOCKS proxy server.
    - You configure your applications (e.g., web browser) to use the SOCKS proxy, which routes all traffic through the SSH tunnel to the remote server and then out to the internet.
    
    Example command:
    
    ```
    ssh -D 1080 user@remote-server.com
    ```
    

SSH tunneling is a powerful technique that enhances security and enables secure access to resources in various scenarios, such as accessing databases, web services, or internal network resources, as well as bypassing censorship and maintaining privacy when using public Wi-Fi networks. However, it’s essential to use SSH tunneling responsibly and in compliance with applicable laws and policies.

## SSH Environment Variables

| Variable                              | Description                                                                                    | Notes                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `SSH_AUTH_SOCK`                       | Path to the **ssh-agent** socket. SSH uses this to authenticate with keys loaded in the agent. | Set by `ssh-agent` automatically                       |
| `SSH_AGENT_PID`                       | PID of the running **ssh-agent** process.                                                      | Set by `ssh-agent`                                     |
| `SSH_CLIENT`                          | Contains the client IP, client port, and server port for the current SSH connection.           | Example: `192.168.1.5 54321 22`                        |
| `SSH_CONNECTION`                      | Contains client IP, client port, server IP, server port.                                       | Example: `192.168.1.5 54321 192.168.1.100 22`          |
| `SSH_TTY`                             | The path to the **terminal device** for the SSH session.                                       | Useful for terminal-aware scripts                      |
| `SSH_ASKPASS`                         | Program SSH uses to ask for a password or passphrase if no terminal is available.              |                                                        |
| `SSH_KEY_PATH` (custom, not standard) | Sometimes used in scripts to specify a key; not built-in.                                      |                                                        |
| `GIT_SSH_COMMAND`                     | When using Git over SSH, allows overriding the SSH command.                                    | Example: `GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_work"` |
| `SSH_OPTIONS` (custom)                | Rarely used; some scripts let you pass options via env variable.                               |                                                        |

## References

- Ylonen, Tatu. “SSH–secure login connections over the Internet.” Proceedings of the 6th USENIX Security Symposium. Vol. 37. 1996.
- Ylonen, Tatu, and Chris Lonvick. The secure shell (SSH) protocol architecture. No. rfc4251. 2006.
- Barrett, Daniel J., Richard E. Silverman, and Robert G. Byrnes. SSH, The Secure Shell: The Definitive Guide: The Definitive Guide. " O’Reilly Media, Inc.", 2005.
- [Git Internals - Transfer Protocols](https://git-scm.com/book/en/v2/Git-Internals-Transfer-Protocols)
- [Git on the Server - Setting Up the Server](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)
- [How Do I Connect To A Github Repository Using SSH?](https://access.redhat.com/solutions/6116301)
- [SSH Keys](https://www.youtube.com/watch?v=dPAw4opzN9g)
- [How Secure Shell Works (SSH) - Computerphile](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [A Visual Guide to SSH Tunnels: Local and Remote Port Forwarding](https://iximiuz.com/en/posts/ssh-tunnels/)
- [OpenSSH](https://www.openssh.com/)
- [How to sniff the ssh protocol](https://www.comparitech.com/net-admin/decrypt-ssl-with-wireshark/)
- [SSH Agent Explained](https://smallstep.com/blog/ssh-agent-explained/)
- [SSH Agent Protocol](https://datatracker.ietf.org/doc/html/draft-miller-ssh-agent-04)
- [The SSH library!](https://api.libssh.org/master/index.html)
- [Paramiko](https://www.paramiko.org/)
- [LibSSH](https://www.libssh.org/)
- [SSH Essentials: Working with SSH Servers, Clients, and Keys](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH - The Definite Guide](https://github.com/ccceye/computer-book/blob/master/SSH%2C%20The%20Secure%20Shell%2C%202nd%20Edition.pdf)
- [gitssh](https://gist.github.com/nakagami/bdae2e98bab06461041b169936c6bb70#file-gitssh-py)
- [How do I configure SSH so it doesn’t try all the identity files automatically?](https://superuser.com/questions/268776/how-do-i-configure-ssh-so-it-doesnt-try-all-the-identity-files-automatically)
- [SSH over HTTPS](https://trofi.github.io/posts/295-ssh-over-https.html)
- https://www.ssh.com/academy/ssh/tunneling
- How to Understand SSH Tunneling and Its Use Cases https://blogs.perficient.com/2021/08/10/how-to-understand-ssh-tunneling-and-its-use-cases/
- SSH Tunneling in Layman’s term https://superuser.com/questions/802756/ssh-tunneling-in-laymans-term
- [SSH Config](https://www.notion.so/SSH-Config-2bd124a08c1f46c887fd1823fb668cca?pvs=21)
