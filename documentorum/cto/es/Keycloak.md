> ….
> 

## Run

```bash
docker run -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin jboss/keycloak
```

## Redirect URI

When configuring redirect URIs for a client in Keycloak, if you're working with a local development environment, you'll typically want to include URIs that match your local setup. Here's how you can configure valid redirect URIs for localhost:

1. **Exact URI Matching**:
If your application runs on a specific port on localhost, you can specify the exact URI:
    
    ```
    <http://localhost:3000/*>
    ```
    
    Replace `3000` with the port number your application is running on.
    
2. **Wildcard Matching for Dynamic Ports**:
If your development server uses dynamic ports (e.g., with tools like `create-react-app` or `webpack-dev-server`), you can use a wildcard for the port:
    
    ```
    <http://localhost>:*
    ```
    
    This allows any port on localhost to be accepted as a valid redirect URI.
    
3. **Localhost with HTTPS**:
If your development server runs over HTTPS (which is common, especially if you're developing a Progressive Web App), you'll need to include the `https` scheme:
    
    ```
    <https://localhost:3000/*>
    ```
    
    Again, adjust the port number as necessary.
    
4. **Loopback Addresses**:
Sometimes, development environments may use loopback addresses. You can specify these as well:
    
    ```
    <http://127.0.0.1:3000/*>
    ```
    
    or
    
    ```
    http://[::1]:3000/*
    ```
    
    These address localhost but can be helpful if there are any differences in how your system resolves `localhost`.
    
5. **Localhost with Subdirectories**:
If your application runs in a subdirectory, make sure to include it:
    
    ```
    <http://localhost:3000/myapp/*>
    ```
    
    Replace `/myapp` with the actual subdirectory path.
    

Adjust these URIs to your specific development setup, including the correct port number and subdirectory paths. These configurations should allow Keycloak to properly handle redirects during the authentication process in your local development environment.

## References

- [Keycloak](https://news.ycombinator.com/item?id=36384636)
- [Keycloak: Open-source identity and access management](https://news.ycombinator.com/item?id=22871180)
- [Keycloak – Open-source identity and access management interview](https://news.ycombinator.com/item?id=36384636)
- [Console #162 - Interview with Michal of Keycloak - Open Source Identity and Access Management](https://console.substack.com/p/console-162#%C2%A7interview-with-michal-of-keycloak-open-source-identity-and-access-management-for-modern-applications)
- …