> `WEBKIT_DISABLE_DMABUF_RENDERER=1` / https://github.com/eclipse-platform/eclipse.platform.swt/issues/1108
> 

## Index

Eclipse Architecture

Eclipse runtime command-line arguments:

- https://help.eclipse.org/latest/index.jsp?topic=/org.eclipse.platform.doc.isv/reference/misc/runtime-options.html

¿How eclipse find mvn dependencies?

Eclipse mvn plugin

- mvn eclipse:eclipse
- mvn eclipse:clean

How to add to eclipse certificates?

The Eclipse platform is written using Java, and a Java VM is required to run it. It is built from small units of functionality called plugins.

Plugins are the basis of the **Eclipse component model**. A plugin is a JAR file with a manifest describing itself, its dependencies, and how it can be utilized or extended. This manifest information was initially stored in a `plug-in.xml` file, which resides in the root of the plugin directory.

Eclipse plugins are written in Java but could also contain non-code contributions, such as HTML files for online documentation.

Each plugin has its class loader.

Plugins can express dependencies on other plugins using the `require`d statements in the `plugin.xml`.

**Extention and extension points**: another element of the Eclipse component model.

One of the most important concepts about Eclipse is that *everything is a plugin*. Whether the plugin is included in the Eclipse platform or you write it yourself, plugins are all first-class components of the assembled application.

The workbench is the most familiar UI element to Eclipse platform users. It provides the structures that organize how Eclipse appears on the desktop. The workbench consists of perspectives, views, and editors.

- Editors are associated with file types, so the correct editor is launched when a file is opened.
- An example of a view is the “problems” view, which indicates errors or warnings in your Java code.
- Together, editors and views form a perspective that presents the tooling to the user in an organized fashion.

---

The Eclipse workbench is built on the Standard Widget Toolkit (SWT) and JFace, and SWT deserves a bit of exploration. Widget toolkits are generally classified as either native or emulated.

- **A native widget** toolkit uses operating system calls to build user interface components such as lists and push buttons. The operating system handles interaction with components. An emulated widget toolkit implements components outside the operating system, handling mouse and keyboard, drawing, focus, and other widget functionality rather than deferring to the operating system. Both designs have different strengths and weaknesses.
- **Native widget** toolkits are “pixel perfect.” Their widgets look and feel like their counterparts in other desktop applications. Operating system vendors constantly change the look and feel of their widgets and add new features. Native widget toolkits get these updates for free. Unfortunately, native toolkits are challenging to implement because their underlying operating system widget implementations are vastly different, leading to inconsistencies and programs that are not portable.
- **Emulated widget** toolkits provide their look and feel, or try to draw and behave like the operating system. Their great strength over native toolkits is flexibility (although modern native widget toolkits such as Windows Presentation Framework (WPF) are equally as flexible). Because the code to implement a widget is part of the toolkit rather than embedded in the operating system, a widget can draw and behave in any manner. Programs that use emulated widget toolkits are highly portable. Early-emulated widget toolkits had a bad reputation. They were often slow and did a poor job of emulating the operating system, making them look out of place on the desktop. In particular, Smalltalk-80 programs at the time were easy to recognize due to their use of emulated widgets. Users knew they were running a “Smalltalk program,” which hurt the acceptance of applications written in Smalltalk.

Eclipse uses Apache Lucene to index and search the online help content.

## JDT: Java Development Tools

The JDT provides Java editors, wizards, refactoring support, a debugger, a compiler, and an incremental builder.

Why did the JDT team write a separate compiler to compile your Java code within Eclipse? They had an initial compiler code contribution from VisualAge Micro Edition. They planned to build tooling on top of the compiler, so writing the compiler itself was a logical decision. This approach also allowed the JDT committers to provide extension points for extending the compiler. This would be difficult if the compiler were a command-line application provided by a third party.

Locate and take the **Java Incremental Builder out of Eclipse**.

## Plug-in Development Environment (PDE)

The Plug-in Development Environment (PDE) provided the tooling to develop, build, deploy, and test plugins and other artifacts that extend Eclipse's functionality. Since Eclipse plugins were a new type of artifact in the Java world, there wasn’t a built-in system that could transform the source into a plugin. Thus, the PDE team wrote a component called PDE Build, which examined the plugins' dependencies and generated Ant scripts to construct the build artifacts.

With the switch to OSGi, Eclipse plugins became known as bundles. A plugin and a bundle are the same: They provide a modular subset of functionality that describes itself with metadata in a manifest.

## Rich Client Platform (RCP)

- RCP to monitor Mars Rover robots developed by NASA and the Jet Propulsion Laboratory
- Bioclipese for data visualization of bioinformatics
- Dutch Railway for monitoring train performance

## Profiles

A profile is a list of UIs in your installation.

## Questions

- How to install plugins
- What are perspectives
- What are workspaces
- How to create a new IDE using Eclipse as based
- How the Eclipse Java debugger is implemented
- How eclipse looks for sources
- How Eclipse debugger for Java looks for sources
- Why project sources and debugging sources are treated differently in Eclipse
- How does the Run / Debug configuration in Eclipse work?

## Debug Sources

> The **sources and dependencies** will depend on the project and it’s dependencies; so in in a maven project; take the root project.
> 

> If not you have to attach the sources manually.
> 

- `mvn clean eclipse:eclipse`
- `mvn dependency:sources`
- `org.hibernate.internal.AbstractSharedSessionContract.checkOpenOrWaitingForAutoClose()`

![image.png](attachment:1fddabf2-0ae6-44c8-8268-f85698bc5c64:image.png)

![image.png](attachment:789f3e48-5f36-4f90-ab6f-db4ba1196c4e:image.png)

![image.png](attachment:ac87a146-22a1-4d39-8bbc-ed2801b91668:image.png)

# Resources

[List of Eclipse-based software](https://en.wikipedia.org/wiki/List_of_Eclipse-based_software)

[The Architecture of Open Source Applications: Eclipse](https://www.aosabook.org/en/eclipse.html)

[Eclipse java debugging: source not found - Stack Overflow](https://stackoverflow.com/questions/6174550/eclipse-java-debugging-source-not-found)

[Eclipse (software)](https://en.wikipedia.org/wiki/Eclipse_(software))

[Standard Widget Toolkit](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit)

[JFace](https://en.wikipedia.org/wiki/JFace)

[Eclipse Equinox](https://en.wikipedia.org/wiki/Equinox_(OSGi))

[Eclipse: A platform for integrating development tools](https://www.ics.uci.edu/~andre/ics228s2006/desriviereswiegand.pdf)

[Using the Eclipse IDE for Java programming - Tutorial](https://www.vogella.com/tutorials/Eclipse/article.html)

[Eclipse Platform Technical Overview](https://www.eclipse.org/articles/Whitepaper-Platform-3.1/eclipse-platform-whitepaper.html)

[Open Services Gateway initiative (OSGI)](https://www.osgi.org/)

[Introduction to OSGi](https://www.baeldung.com/osgi)