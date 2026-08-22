# Doxygen

> Doxygen is a documentation generation tool that parses code comments in various programming languages to produce structured and formatted documentation.

> The **Doxygen documentation model** involves using special comments within source code to describe elements like functions, classes, and variables, and then running the Doxygen tool to process these comments and generate comprehensive documentation in various output formats (HTML, PDF, etc.) that includes information about the code’s structure, usage, and relationships.

## Doxygen Tags

Certainly, here’s a list of common Doxygen tags that you can use within your code comments to provide documentation and generate structured documentation:

| Tag | Description |
| --- | --- |
| `@brief` | Provides a brief description of the element. |
| `@param` | Describes a function or method parameter, including its purpose and expected input. |
| `@return` | Explains the return value of a function or method. |
| `@see` | Creates a cross-reference to another documented element. |
| `@note` | Adds additional information or clarifications to the documentation. |
| `@warning` | Indicates a warning related to the documented element. |
| `@deprecated` | Marks an element as deprecated, indicating it should not be used in new code. |
| `@code` and `@endcode` | Encloses code snippets to be displayed as preformatted text. |
| `@example` | Provides an example of how to use the documented element. |
| `@namespace` | Documents a namespace. |
| `@class` and `@struct` | Documents a class or structure. |
| `@enum` | Documents an enumeration. |
| `@fn` | Documents a function or method. |
| `@var` | Documents a variable. |
| `@file` | Documents a file. |
| `@mainpage` and `@page` | Create main and secondary pages for the documentation. |
| `@ingroup` | Assigns the documented element to a group for organization. |
| `@todo` | Marks a to-do item within the documentation. |
| `@details` | Provides additional details about the documented element. |
| `@internal` | Marks an element as internal, indicating it’s not intended for external use. |
| `@link` | Creates hyperlinks to external resources. |
| `@latexonly` and `@endlatexonly` | Encloses content that should appear only in LaTeX documentation. |
| `@htmlonly` and `@endhtmlonly` | Encloses content that should appear only in HTML documentation. |
| `@if`, `@elseif`, `@else`, and `@endif` | Conditional blocks for generating different content based on configuration. |

This table organizes the tags and their functions for quick reference.

## Export Formats

> Doxygen supports several export formats for generating documentation. These formats determine how the documentation is presented and organized.
> 

Here are some of the common export formats supported by Doxygen:

| **Export Format** | **Description** |
| --- | --- |
| **HTML** | Generates HTML documentation, viewable in web browsers. This is the default export format. |
| **HTML Help** | Creates compiled HTML Help files (CHM) for standalone documentation or integration into Windows help systems. |
| **LaTeX** | Generates LaTeX files, which can be compiled into printable documents, including PDFs. |
| **RTF** | Creates Rich Text Format (RTF) files, suitable for word processing software. |
| **Man Pages** | Generates manual pages in the Unix/Linux man page format. |
| **XML** | Produces XML output that can be further processed or transformed. |
| **DocBook** | Generates documentation in DocBook XML format, commonly used for technical documentation. |
| **Markdown** | Exports documentation in Markdown format, widely supported for creating readable and formatted text. |
| **Qt Help** | Creates Qt Help files, suitable for integration into Qt applications. |
| **DITA** | Generates output in the Darwin Information Typing Architecture (DITA) format, suitable for structured documentation. |
| **Perl POD** | Produces Perl Plain Old Documentation (POD) format, commonly used for Perl documentation. |
| **Tcl/Tk** | Generates documentation in Tcl/Tk format. |
| **XMI** | Exports documentation in XML Metadata Interchange (XMI) format, suitable for UML modeling tools. |

## References

- [Read the Docs](https://about.readthedocs.com/)
- [Doxygen](https://www.doxygen.nl/)
- https://www.doxygen.nl/manual/starting.html
