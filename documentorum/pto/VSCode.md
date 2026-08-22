> **Visual Studio Code (VS Code)** is a popular open-source code editor developed by Microsoft. It’s built using web technologies such as HTML, CSS, and JavaScript and provides a wide range of features for developers.

> **NOTE** (❌) : The used of this tool from (Sat Aug  8 02:00:02 PM AST 2026) - its ban for me. Replace it - with `Neovim`.

## Index

## QA

- How does **`VSCode`** research and resolve symbols from `external libraries`? It’s language-extension specific.
    - How the **`LSP`** research and resolve symbols from `external libraries`?
    - How **`IntelliSense Engine`** research and resolve symbols from `external libraries`?
- How to list the search path of the **`LSP`** Server?

## List of Components

| **Component** | **Description** |
| --- | --- |
| **Electron Framework** | VS Code is built on the Electron framework, combining Chromium for rendering and Node.js for backend functionality, enabling cross-platform desktop applications. |
| **Architecture** | VS Code follows a modular architecture with a primary process for managing the UI and multiple sandboxed renderer processes for displaying different UI parts. |
| **Extensions** | VS Code's extensibility allows developers to add new features, languages, themes, and integrations by writing extensions in JavaScript and interacting with the VS Code API. |
| **Language Services** | Language services in VS Code are provided through the Language Server Protocol (LSP), offering consistent language support with features like autocompletion and linting. |
| **Source Control Integration** | Built-in Git integration in VS Code enables developers to manage version control directly from the editor, with a graphical interface for everyday Git operations. |
| **Workspace and Settings** | VS Code allows the management of workspace settings stored in a `.code-workspace` file, which can override user settings for specific projects. |
| **User Interface** | The UI of VS Code is built with HTML, CSS, and JavaScript, using the Monaco Editor for code editing, and is highly customizable in terms of themes, layout, and more. |
| **Extension Host and APIs** | The Extension Host, a separate Node.js process, loads and manages extensions and provides APIs for interacting with the editor, including UI modification and code analysis. |
| **Keybinding System** | A flexible keybinding system in VS Code allows users to customize keyboard shortcuts through the `keybindings.json` configuration file. |
| **Debugging** | VS Code offers a rich debugging experience, supporting breakpoints, step-throughs, variable inspection, and more across various programming languages. |
| **Remote Development** | VS Code supports remote development, enabling work on projects hosted on remote machines or containers and enhancing workflows for complex setups. |

## Extensions

- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) - [Oracle Developer Tools for VS Code (SQL and PLSQL)](https://marketplace.visualstudio.com/items?itemName=Oracle.oracledevtools)

## **Language Servers (LSP)**

> See more in [Language Server Protocol (LSP)](https://www.notion.so/Language-Server-Protocol-LSP-f3e4edb62b984f1f950fc1039762267b?pvs=21).
> 

## Debug Configs

GDB:

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++ - Build and debug active file",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceRoot}/redis-server",
            "args": [],
            "stopAtEntry": true,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "miDebuggerPath": "/usr/bin/gdb"
        }
    ]
}
```

## How’s To?

- Install Extensions.
- Wrap Text
- `code  --ignore-certificate-errors`

## QA

### How the **`LSP`** research and resolve symbols from `external libraries`?

> The method varies by programming language; this table serves as a reference, so please use it carefully.
> 

| **Language** | **LSP Server / Tool** | **External Library Symbol Resolution Method** | **Notes** |
| --- | --- | --- | --- |
| **C / C++** | clangd | Uses `compile_commands.json` (compilation database) to find full compile flags, include paths, and external headers. | Preferred method for projects with build system support; provides precise symbol info. |
|  |  | Uses `c_cpp_properties.json` to manually specify include paths, macros, and compiler flags for symbol resolution in external libs.  | Useful for manual configuration or simple projects without compilation database. |
| **Rust** | rust-analyzer | Uses Cargo metadata (`Cargo.toml`, `Cargo.lock`) to fetch, cache, and index external crates and symbols. | Fully integrated with Cargo package manager. |
| **Go** | gopls | Uses Go modules (`go.mod`) to download, cache, and index external dependencies and symbols. | Relies on Go tooling for module management. |
| **Python** | pyright, pylance | Uses virtual environment or system interpreter site-packages to index installed libraries and symbols. | Static analysis within interpreter environment. |
| **Java** | Eclipse JDT Language Server | Uses build tool classpaths (Maven, Gradle) to locate external jars, then indexes class files and metadata for symbols. | Build tool driven classpath resolution. |
| **JavaScript / TypeScript** | tsserver (TypeScript Server) | Uses `node_modules` folder and `package.json` to resolve and index external packages and type declarations (`@types`). | Node module resolution and typings. |
| **C#** | OmniSharp | Uses MSBuild project/solution files to resolve NuGet packages and referenced assemblies for symbol info. | NuGet packages referenced via MSBuild metadata. |
| **Ruby** | solargraph | Uses Gemfile and installed gems to index external symbols from gems. | Reads Gemfile.lock and local gem installations. |
| **PHP** | Intelephense | Uses Composer autoload files and vendor directory to find and index external packages. | Composer-driven dependency management. |
| **Swift** | SourceKit-LSP | Uses Swift Package Manager (SwiftPM) and system frameworks to resolve and index external symbols. | Integrates with SwiftPM dependency info. |
| **Kotlin** | Kotlin Language Server | Uses Gradle or Maven build information to resolve dependencies and index external symbols. | Build tool driven dependency resolution. |

### How **`IntelliSense Engine`** research and resolve symbols from `external libraries`?

| Step / Mechanism | Description |
| --- | --- |
| **Include Path Configuration** | IntelliSense uses configured include paths (from `c_cpp_properties.json` or detected from build) to locate header files of external libraries. Without correct include paths, it can’t find declarations. |
| **Macros and Defines** | It processes preprocessor macros and defines (also from config or build info) to parse conditional code correctly in external headers. |
| **Parsing Headers (Static Analysis)** | IntelliSense performs static parsing of the headers found via include paths to understand types, functions, classes, constants, and macros exposed by external libraries. |
| **Indexing and Caching** | After parsing, IntelliSense indexes symbols for quick lookup and caches parsed information to speed up subsequent queries. |
| **Compile Commands / Build Info** | If a `compile_commands.json` or similar compilation database is provided, IntelliSense uses the exact compiler flags, include paths, and defines used during build, improving accuracy for external library resolution. |
| **Fallback to Manual Configuration** | If no compilation database is found, IntelliSense falls back to `c_cpp_properties.json` for manual config of include paths, defines, and compiler flags. |

## References

- [Website for Visual Studio Code states “Free. Open Source.” which is extremely misleading given the download button below is leading to EULA licensed proprietary software. Please don’t mislead users intentionally](https://github.com/Microsoft/vscode/issues/17996)
- [VS Code](https://github.com/microsoft/vscode/tree/main)
- https://netlog-viewer.appspot.com/#events
- https://github.com/microsoft/vscode/issues/107896
- https://github.com/microsoft/vscode/issues/107896
