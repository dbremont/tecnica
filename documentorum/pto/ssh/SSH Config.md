`gedit ~/.ssh/config` 

## List of Directives

Here's the updated table with the addition of the `IdentityAgent` directive, which specifies the UNIX socket used to communicate with the agent that holds your private keys:

| Directive | Description |
| --- | --- |
| `Host` | Defines a hostname label with specific configuration. |
| `HostName` | Specifies the real hostname to connect to. |
| `User` | The default username for the connection. |
| `Port` | Specifies the port number to connect on the remote host. |
| `IdentityFile` | Specifies a file from which the identity key (private key) is read. |
| `IdentityAgent` | Specifies the socket used to communicate with an authentication agent. |
| `ProxyCommand` | Command to execute to connect to the server. |
| `LocalForward` | Specifies local port forwarding. |
| `ServerAliveInterval` | Sets a timeout interval in seconds. After that, if no data has been received from the server, SSH will send a message through the encrypted channel to request a response from the server. |
| `Protocol` | Specifies the protocol versions to support (usually `2`). |
| `Compression` | Enables compression of all data. |
| `LogLevel` | Defines the verbosity level that the client uses. Examples are `QUIET`, `FATAL`, `ERROR`, `INFO`, `VERBOSE`, `DEBUG`, `DEBUG1`, `DEBUG2`, and `DEBUG3`. |

This directive, `IdentityAgent`, is particularly useful in environments where multiple keys are managed through an SSH agent, allowing you to specify which agent to use for authentication, thereby simplifying key management.

## Configuration Example

```json
# General defaults applied to all hosts
Host *
    ForwardX11 no
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/id_rsa
    ServerAliveInterval 60
    ServerAliveCountMax 3

# Specific host settings
Host example
    HostName example.com
    User myusername
    Port 2222
    IdentityFile ~/.ssh/example_id_rsa

Host github.com
    User git
    IdentityFile ~/.ssh/github_rsa

Host gitlab.com
	  IdentityAgent ~/.1password/agent.sock

```

## References

- [OpenSSH Manual Pages](https://www.openssh.com/manual.html)