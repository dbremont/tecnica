# Apache Tomcat

> **Apache Tomcat** is an open-source **web server** and **servlet** container that serves Java-based web applications.
> 

QA:

- Which Jakarta EE does Apache Tomcat implements by default?
- …

## Index

## Build, Test & Debug

> …
> 

```jsx
git clone https://github.com/apache/tomcat.git
cd tomcat

git checkout 10.1.x

ant
cd output/build
./bin/catalina.sh run

## Debug
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005
jps
```

Test War

```jsx
....
```

## Configuration

> [User Creation → …]
> 

Users

```jsx
tomcat-users.xml
```

## JavaServer Faces (JSF)

> Yes, you can add **JavaServer Faces (JSF)** to an **Apache Tomcat** server. Tomcat is a **Servlet container** and does not include JSF by default, but you can manually add the necessary JSF libraries.
> 

**Download the JSF Libraries:**

> You can download **Mojarra** from [Eclipse Mojarra](https://projects.eclipse.org/projects/ee4j.mojarra) or use **MyFaces** from [Apache MyFaces](https://myfaces.apache.org/).
> 

JSF implementations include:

- **Mojarra (official reference implementation by Jakarta EE)**
- **MyFaces (alternative Apache implementation)**

**Copy JSF JARs to Tomcat's `lib` Directory:**

After downloading, copy the necessary `.jar` files (e.g., `javax.faces.jar`, `jsf-api.jar`, `jsf-impl.jar`) into:

```
<TOMCAT_HOME>/lib/

```

**Configure `web.xml` for JSF**

In your **web application (`WEB-INF/web.xml`)**, define the JSF servlet:

```xml
<web-app xmlns="http://jakarta.ee/xml/ns/jakartaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://jakarta.ee/xml/ns/jakartaee
    http://jakarta.ee/xml/ns/jakartaee/web-app_4_0.xsd"
    version="4.0">

    <servlet>
        <servlet-name>FacesServlet</servlet-name>
        <servlet-class>jakarta.faces.webapp.FacesServlet</servlet-class>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>FacesServlet</servlet-name>
        <url-pattern>*.xhtml</url-pattern>
    </servlet-mapping>

</web-app>

```

**Create a Simple JSF Page (`index.xhtml`)**

Inside your web application's `webapp` folder, create a sample **JSF page**:

```
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:h="http://xmlns.jcp.org/jsf/html">
<h:head>
    <title>JSF on Tomcat</title>
</h:head>
<h:body>
    <h1>Welcome to JSF on Apache Tomcat!</h1>
    <h:form>
        <h:inputText value="#{helloBean.message}" />
        <h:commandButton value="Submit" action="#{helloBean.sayHello}" />
        <h:outputText value="#{helloBean.response}" />
    </h:form>
</h:body>
</html>

```

**Create a Backing Bean (`HelloBean.java`)**

This Java class should be in your project's `src/main/java` directory.

```java
import jakarta.enterprise.context.RequestScoped;
import jakarta.inject.Named;

@Named
@RequestScoped
public class HelloBean {
    private String message;
    private String response;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getResponse() {
        return response;
    }

    public void sayHello() {
        response = "Hello, " + message + "!";
    }
}

```

**Deploy and Run**

1. Place your web application inside `webapps/` in your Tomcat installation.
2. Start Tomcat:
    
    ```
    <TOMCAT_HOME>/bin/startup.sh  (Linux/macOS)
    <TOMCAT_HOME>/bin/startup.bat (Windows)
    
    ```
    
3. Open your browser and go to:
    
    ```
    http://localhost:8080/your-app/index.xhtml
    
    ```
    

## References

- [Apache Tomcat](https://tomcat.apache.org/)
- [Apache Tomcat SRC](https://github.com/apache/tomcat/tree/main)
- [’How to Deploy a WAR File to Tomcat](https://www.baeldung.com/tomcat-deploy-war)
- https://tomcat.apache.org/whichversion.html
- [What is Tomcat? A web container or EE container?](https://stackoverflow.com/questions/19377821/what-is-tomcat-a-web-container-or-ee-container)
- https://tomcat.apache.org/tomcat-11.0-doc/index.html
- https://www.google.com/search?client=ubuntu-sn&channel=fs&q=apache+tomee++jsp%2C+and+jsf+hello+world
- https://balusc.omnifaces.org/2013/10/how-to-install-cdi-in-tomcat.html
- https://weld.cdi-spec.org/documentation/
- https://openwebbeans.apache.org/
- https://tomee.apache.org/
- https://en.wikipedia.org/wiki/Jakarta_Enterprise_Beans
- https://github.com/csiglab/web-frameworks-labs