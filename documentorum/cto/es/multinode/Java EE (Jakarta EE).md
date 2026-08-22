# Java EE (Jakarta EE)

> Java EE (Jakarta EE) is a specification-driven, enterprise-grade Java platform that defines a set of standardized APIs, runtime environments, and container-managed services for building distributed, scalable, and transactional applications, leveraging a component-based architecture with servlets, JSP, JSF, CDI, EJB, JPA, JMS, JTA, and web services (REST and SOAP) while enforcing dependency injection, declarative security, and multi-threaded request processing within managed execution environments such as application servers (e.g., WildFly, Payara, or **Tomcat with EE extensions**).

| **Category**               | **Specification**                                   | **Description**                                                                                         |
| -------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Web Tier**               | **Jakarta Servlet**                                 | Defines the core HTTP request/response programming model and lifecycle for web applications.            |
|                            | **Jakarta Server Pages (JSP)**                      | Provides a server-side view technology for generating dynamic HTML using Java and tag libraries.        |
|                            | **Jakarta Faces (JSF)**                             | Component-based UI framework for building server-rendered web user interfaces.                          |
|                            | **Jakarta Expression Language (EL)**                | Unified expression language for accessing and manipulating application data in web views and templates. |
| **Web Services**           | **Jakarta RESTful Web Services (JAX-RS)**           | Defines a standard API for building RESTful HTTP-based services.                                        |
|                            | **Jakarta XML Web Services (JAX-WS)**               | Defines APIs and annotations for SOAP-based web services.                                               |
|                            | **Jakarta JSON Processing (JSON-P)**                | Low-level streaming and object-model APIs for parsing and generating JSON.                              |
|                            | **Jakarta JSON Binding (JSON-B)**                   | High-level API for mapping Java objects to and from JSON representations.                               |
| **Persistence**            | **Jakarta Persistence (JPA)**                       | Standard ORM API for managing relational data using entity-based object mapping.                        |
|                            | **Jakarta Data**                                    | Repository-style abstraction for simplified and declarative data access (still evolving).               |
| **Enterprise Integration** | **Jakarta Messaging (JMS)**                         | Messaging API for asynchronous, reliable, and decoupled communication between components.               |
|                            | **Jakarta Batch**                                   | Defines a job-oriented model for offline, bulk, and long-running batch processing.                      |
|                            | **Jakarta Mail**                                    | APIs for composing, sending, and receiving email messages.                                              |
|                            | **Jakarta Concurrency**                             | Managed concurrency utilities for executing asynchronous and scheduled tasks in containers.             |
| **Business Logic**         | **Jakarta Enterprise Beans (EJB)**                  | Component model for transactional, secure, and distributed business logic.                              |
|                            | **Jakarta CDI (Contexts and Dependency Injection)** | Context-aware dependency injection framework with scopes, lifecycle management, and events.             |
|                            | **Jakarta Interceptors**                            | Mechanism for implementing cross-cutting concerns (logging, security, metrics) via interception.        |
| **Security**               | **Jakarta Security**                                | Standardized APIs for authentication, authorization, and identity management integration.               |
| **Transaction Management** | **Jakarta Transactions (JTA)**                      | Defines APIs for demarcating and coordinating distributed transactions.                                 |
|                            | **Jakarta Connectors (JCA)**                        | Architecture for integrating Jakarta EE applications with external enterprise information systems.      |
| **Configuration & Naming** | **Jakarta Annotations**                             | Common annotations used across Jakarta EE for declarative configuration and metadata.                   |
|                            | **Jakarta Dependency Injection (DI)**               | Base dependency injection contract defining injection points and resolution semantics.                  |
|                            | **Jakarta Naming (JNDI)**                           | Naming and directory API for binding and looking up resources in a hierarchical namespace.              |
| **Web & MVC (Optional)**   | **Jakarta MVC**                                     | Action-based MVC framework layered on top of JAX-RS for server-side web applications.                   |
| **Validation**             | **Jakarta Bean Validation**                         | Declarative validation framework using constraints and annotations to enforce data integrity.           |

## Implementation

| **Jakarta EE Specification**                        | **Implementation**             | **Provider**               | **Application Server Support**                          |
| --------------------------------------------------- | ------------------------------ | -------------------------- | ------------------------------------------------------- |
| **Jakarta Servlet**                                 | Apache Tomcat / Jetty          | Apache Software Foundation | Tomcat, Jetty, WildFly, Payara, GlassFish, Open Liberty |
| **Jakarta Server Pages (JSP)**                      | Jasper                         | Apache Software Foundation | Tomcat, WildFly, Payara, GlassFish, Open Liberty        |
| **Jakarta Faces (JSF)**                             | Mojarra / MyFaces              | Eclipse / Apache           | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Expression Language (EL)**                | Eclipse EL                     | Eclipse Foundation         | Tomcat, WildFly, Payara, GlassFish, Open Liberty        |
| **Jakarta RESTful Web Services (JAX-RS)**           | RESTEasy / Jersey / CXF        | JBoss / Eclipse / Apache   | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta XML Web Services (JAX-WS)**               | Metro / CXF                    | Eclipse / Apache           | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta JSON Processing (JSON-P)**                | Eclipse JSON-P                 | Eclipse Foundation         | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta JSON Binding (JSON-B)**                   | Eclipse Yasson                 | Eclipse Foundation         | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Persistence (JPA)**                       | Hibernate / EclipseLink        | Red Hat / Eclipse          | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Data**                                    | Eclipse JNoSQL (early)         | Eclipse Foundation         | *Emerging* (experimental in EE servers)                 |
| **Jakarta Messaging (JMS)**                         | Apache ActiveMQ / Artemis      | Apache / Red Hat           | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Batch**                                   | Eclipse Batch                  | Eclipse Foundation         | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Mail**                                    | Eclipse Angus                  | Eclipse Foundation         | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Concurrency**                             | Eclipse Concurrency            | Eclipse Foundation         | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Enterprise Beans (EJB)**                  | OpenEJB / WildFly EJB          | Apache / Red Hat           | WildFly, Payara, GlassFish                              |
| **Jakarta CDI (Contexts and Dependency Injection)** | Weld / OpenWebBeans            | Red Hat / Apache           | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Dependency Injection**                    | Integrated with CDI            | Various                    | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Interceptors**                            | Provided by CDI implementation | Various                    | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Naming (JNDI)**                           | Container-provided             | Various                    | Tomcat*, WildFly, Payara, GlassFish, Open Liberty       |
| **Jakarta Security**                                | Soteria                        | Eclipse Foundation         | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Transactions (JTA)**                      | Narayana / Geronimo            | Red Hat / Apache           | WildFly, Payara, GlassFish, Open Liberty                |
| **Jakarta Connectors (JCA)**                        | IronJacamar                    | Red Hat                    | WildFly, Payara, GlassFish                              |
| **Jakarta Annotations**                             | Eclipse Annotations            | Eclipse Foundation         | Tomcat, WildFly, Payara, GlassFish, Open Liberty        |
| **Jakarta Config**                                  | SmallRye Config                | Red Hat                    | WildFly, Payara, Open Liberty                           |
| **Jakarta MVC**                                     | Ozark                          | Eclipse Foundation         | WildFly, Payara, GlassFish                              |
| **Jakarta Bean Validation**                         | Hibernate Validator            | Red Hat                    | Tomcat, WildFly, Payara, GlassFish, Open Liberty        |

## **Jakarta Faces**

> aka. Java Server Faces.
> 

QA:

- How events are handle?
- How data binding works?
- How partial updates works?
- What is the execution model?
- How `DemuxCompositeELResolver` works?
- What is the different between `Jakarta EE Server` vs `Application Server`?

Phases:

- com.sun.faces.lifecycle.RestoreViewPhase@4793eed2
- com.sun.faces.lifecycle.ApplyRequestValuesPhase@4f2666db
- com.sun.faces.lifecycle.ProcessValidationsPhase@382e51f1
- com.sun.faces.lifecycle.UpdateModelValuesPhase@26a93b9b
- com.sun.faces.lifecycle.InvokeApplicationPhase@7e14a4e2 -> Use dr.gov.esigef.pds.presentacion.nucleo.evento.EventoEjecutadoCambioValor@42185d63
- com.sun.faces.lifecycle.RenderResponsePhase@2f80545

Expression Language (EL):

- …

## QA

- How does WildFly determine which **JSP** file to serve for a given **URL**, and where must the **JSP** be located inside the **WAR**?

## References

- https://github.com/weld/core [weld/core]
- https://en.wikipedia.org/wiki/Jakarta_EE
- https://jakarta.ee/specifications/faces/3.0/jsdoc/jsf.ajax.html
- https://stackoverflow.com/questions/7295096/what-exactly-is-java-ee
- https://jakarta.ee/specifications/
- [distributed-system-lab](https://github.com/dbremont/distributed-system-lab)
- [Java: Modularization](https://righteous-guardian-68f.notion.site/Java-Modularization-210c0f5171ec809b8108ee6acba4db9c?source=copy_link)
- [What is the difference between application server and web server?](https://stackoverflow.com/questions/936197/what-is-the-difference-between-application-server-and-web-server?rq=3)
- [Wildfly](https://github.com/dbremont/documentorum/blob/main/cto/es/multinode/Wildfly.md)
