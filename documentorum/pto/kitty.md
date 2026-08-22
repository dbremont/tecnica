# Kitty

Creating a table of the main user-facing concepts in the kitty terminal emulator involves outlining key features and functionalities that users interact with regularly. Here’s a brief table summarizing some of these concepts:

| Concept | Description |
| --- | --- |
| Configuration | Kitty is highly configurable through a file (`kitty.conf`). Users can set fonts, colors, behaviors, and more. |
| GPU Acceleration | Kitty uses the GPU to render output, which enhances performance significantly with large amounts of text. |
| Keyboard Shortcuts | Extensive support for shortcuts to streamline operations like creating windows, resizing, etc. |
| Ligatures | Supports programming ligatures, making it attractive for coding and reading code. |
| Unicode and Emoji | Excellent support for Unicode and colored emojis, ensuring proper text display from various languages and symbols. |
| Tiling Layouts | Native tiling layouts to organize windows either vertically or horizontally without needing additional tools. |
| Scrollback Buffer | Configurable scrollback buffer that allows users to scroll back through a large amount of terminal output. |
| Mouse Support | Supports mouse interactions, including clicking links and resizing panes. |
| Customizable Themes | Allows users to customize themes, including light and dark modes, and apply different color schemes. |
| OS Window | The top-level graphical interface of the kitty terminal that can be resized, minimized, or maximized like any typical application window. |
| Tab | A grouping mechanism within the kitty OS Window that allows multiple terminal sessions to be organized under single selectable headers. |
| Kitty Window |     An individual terminal session within a tab, capable of running distinct processes, with support for multiple windows per tab arranged in user-defined layouts.

 |
| Layout | A kitty layout refers to the arrangement of multiple **terminal windows (kitty windows)** within a tab, allowing customizable configurations such as horizontal, vertical, stacked, or grid layouts to organize terminal sessions effectively. |

These are just a few main concepts that Kitty offers its users. Kitty’s extensive documentation further expands on these features and how to customize them to fit individual needs. Let me know if you want more detailed explanations of these features or additional concepts!

## Kitty GUI Model

The GUI organization model of the kitty terminal emulator is structured to enhance efficiency and flexibility when managing multiple terminal sessions. Here's a simplified overview:

- **OS Window** is the main graphical interface encompassing all other kitty terminal components. It can include multiple tabs and be adjusted in size, transparency, and other window properties.
- **Tab Bar**: Located at the top of the OS Window (unless configured otherwise), this area displays tabs representing a group of one or more kitty windows. Users can quickly switch between tabs to access different groups of terminal sessions.
- **Tabs**: Each tab functions like a separate workspace, containing one or more kitty windows. Tabs help organize different tasks or projects by grouping related terminal sessions.
- **Kitty Windows (Pane)**: Within each tab, users can open multiple kitty windows, each an individual terminal session. The layout of these windows within a tab can be configured to be horizontal, vertical, stacked, or a grid, among other options.
- **Layouts**: Kitty supports several layouts for organizing windows within a tab, including horizontal and vertical splits, which can be dynamically adjusted. Users can also create custom layouts tailored to their specific workflow needs.

This model is designed to maximize productivity by allowing users to efficiently manage multiple tasks or projects through a combination of tabs and window layouts within a single OS Window.

## Kitty Layouts

> …
> 

## Kitty Plugin System

> …
> 

## Kitty Configuration

> …
> 

```bash
enabled_layouts stack,tall
# map ctrl+shift+c goto_layout stack
```

## Kitty **Startup Sessions**

## References

- [https://sw.kovidgoyal.net](https://sw.kovidgoyal.net/)
- [kitty.conf](https://github.com/dbremont/configs/tree/main/global/config/kitty)
