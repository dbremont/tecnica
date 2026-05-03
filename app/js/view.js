// Tool API for communicating with the loaded tool
const ToolAPI = {
    // Reference to the shadow root
    shadowRoot: null,

    // Send a command to the tool by dispatching an event
    sendCommand: function (command, data = {}) {
        if (!this.shadowRoot) {
            console.warn('Tool not loaded yet');
            return;
        }

        // Dispatch event that the tool's event listeners will catch
        console.log(`Dispatching event: tool-${command}`);
        const event = new CustomEvent(`tool-${command}`, {
            detail: data,
            bubbles: true,
            composed: true
        });
        this.shadowRoot.dispatchEvent(event);
    },

    // Open the tool's help
    openHelp: function () {
        this.sendCommand('openHelp');
    },

    // Reset the tool
    reset: function () {
        this.sendCommand('reset');
    },

    // Refresh the tool
    refresh: function () {
        this.sendCommand('refresh');
    },

    // Send a custom command
    custom: function (command, data) {
        this.sendCommand(command, data);
    }
};

// Store registered commands
let registeredCommands = [];

// Execute tool script with access to shadow root
function executeScript(root, scriptCode) {
    try {
        // Create a script element within the shadow DOM
        const scriptEl = document.createElement('script');
        scriptEl.textContent = `(function() {
            try {
                ${scriptCode}
            } catch (err) {
                console.error('Error executing tool script:', err);
            }
        })();`;
        
        // Append to shadow DOM to execute
        // Script executes immediately and stays in DOM so event listeners persist
        root.appendChild(scriptEl);
    } catch (err) {
        console.error('Error in executeScript:', err);
    }
}

// Load the tool from the URL parameter
async function loadTool() {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const toolContentWrapper = document.getElementById('tool-content-wrapper');
    const toolContentHost = document.getElementById('tool-content-host');
    const toolLoading = document.getElementById('tool-loading');
    const toolControls = document.getElementById('tool-controls');
    const errorMessage = document.getElementById('errorMessage');
    const toolTitle = document.getElementById('tool-title');
    const toolPath = document.getElementById('tool-path');
    const navToolName = document.getElementById('nav-tool-name');
    const toolHeader = document.querySelector('.tool-header');

    // Get the tool name from the URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const toolName = urlParams.get('tool');

    if (!toolName) {
        loading.style.display = 'none';
        error.style.display = 'flex';
        errorMessage.textContent = 'No tool specified in URL. Please provide a tool name.';
        return;
    }

    try {
        // Sanitize the tool name to prevent directory traversal
        const sanitizedName = toolName.replace(/[^a-zA-Z0-9_-]/g, '');
        const toolUrl = `/toolbox/tool/src/${sanitizedName}.html`;

        // Update title, path, and navigation display
        const formattedName = sanitizedName.replace(/-/g, ' ').replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
        toolTitle.textContent = formattedName;
        toolPath.textContent = toolUrl;
        navToolName.textContent = formattedName;

        // Hide the duplicate tool header section
        toolHeader.style.display = 'none';

        // Fetch the tool HTML
        const response = await fetch(toolUrl);
        if (!response.ok) {
            throw new Error(`Failed to load tool: ${response.statusText}`);
        }

        const html = await response.text();

        // Listen for command registration
        // Set up the global event listener for tools to register their commands
        console.log('Setting up listener for tool-registerCommands');
        document.addEventListener('tool-registerCommands', (e) => {
            console.log('Received command registration from tool:', e.detail);
            const { commands } = e.detail;
            registeredCommands = commands;
            
            // Clear existing dropdown items (except standard ones)
            clearCustomCommands();
            
            // Add custom commands to dropdown
            commands.forEach(cmd => {
                addCommandToDropdown(cmd);
            });
            
            console.log('Registered commands:', commands);
        });

        // Parse the HTML
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');

        // Create a Shadow DOM for style isolation
        const shadowRoot = toolContentHost.attachShadow({ mode: 'open' });
        ToolAPI.shadowRoot = shadowRoot;

        // Inject HTML body content (without scripts) FIRST
        const bodyClone = doc.body.cloneNode(true);
        const scripts = bodyClone.querySelectorAll('script');
        scripts.forEach(script => script.remove());
        shadowRoot.innerHTML = bodyClone.innerHTML;

        // NOW extract and copy all style elements (after innerHTML so they're not overwritten)
        const styles = doc.querySelectorAll('style');
        styles.forEach(style => {
            const newStyle = document.createElement('style');
            newStyle.textContent = style.textContent;
            shadowRoot.appendChild(newStyle);
        });

        // Extract link elements (for external stylesheets)
        const links = doc.querySelectorAll('link[rel="stylesheet"]');
        links.forEach(link => {
            const newLink = document.createElement('link');
            Array.from(link.attributes).forEach(attr => {
                newLink.setAttribute(attr.name, attr.value);
            });
            shadowRoot.appendChild(newLink);
        });

        // Make shadowRoot globally accessible for script execution
        window.__toolShadowRoot__ = shadowRoot;

        // Execute scripts with proper scope
        const originalScripts = doc.body.querySelectorAll('script');
        console.log('Found', originalScripts.length, 'scripts to execute');

        originalScripts.forEach((script) => {
            const code = script.textContent;
            console.log('Script code length:', code.length);

            if (code.trim()) {
                executeScript(shadowRoot, code);
                console.log('Script executed');
            }
        });

        // Clean up global variable
        delete window.__toolShadowRoot__;

        // Wait for tool to initialize
        await new Promise(resolve => setTimeout(resolve, 300));

        // Listen for tool-to-viewer events
        document.addEventListener('tool-ready', (e) => {
            console.log('Tool is ready:', e.detail);
        });

        document.addEventListener('tool-stateChanged', (e) => {
            console.log('Tool state changed:', e.detail);
        });

        document.addEventListener('tool-error', (e) => {
            console.error('Tool error:', e.detail);
        });

        // Set up control panel buttons
        setupControlPanel();

        // Hide loading and show content
        loading.style.display = 'none';
        toolContentWrapper.style.display = 'block';
        toolControls.style.display = 'flex';
        toolLoading.style.display = 'none';

    } catch (err) {
        console.error('Error loading tool:', err);
        loading.style.display = 'none';
        toolContentWrapper.style.display = 'none';
        toolControls.style.display = 'none';
        error.style.display = 'flex';
        errorMessage.textContent = err.message || 'Failed to load the tool. Please try again.';
    }
}

// Add command to dropdown menu
function addCommandToDropdown(cmd) {
    const menu = document.getElementById('tool-options-menu');
    if (!menu) return;
    
    // Create button element
    const btn = document.createElement('button');
    btn.className = 'tool-option-btn';
    btn.setAttribute('data-custom', 'true');
    btn.title = cmd.description || cmd.label || cmd.command;
    
    // Set button content with icon and label
    btn.innerHTML = `
        ${cmd.icon}
        <span>${cmd.label || cmd.command}</span>
    `;
    
    // Add click handler
    btn.addEventListener('click', () => {
        // Dispatch command to tool
        ToolAPI.sendCommand(cmd.command, cmd.data || {});
        
        // Close menu
        const optionsMenu = document.getElementById('tool-options-menu');
        const menuBtn = document.getElementById('tool-menu-btn');
        if (optionsMenu) optionsMenu.classList.remove('show');
        if (menuBtn) menuBtn.classList.remove('active');
    });
    
    // Insert before the divider (if exists) or append
    const divider = menu.querySelector('.tool-option-divider');
    if (divider) {
        menu.insertBefore(btn, divider);
    } else {
        menu.appendChild(btn);
    }
}

// Clear custom commands from dropdown
function clearCustomCommands() {
    const menu = document.getElementById('tool-options-menu');
    if (!menu) return;
    
    const customButtons = menu.querySelectorAll('.tool-option-btn[data-custom="true"]');
    customButtons.forEach(btn => btn.remove());
}

// Set up control panel event listeners
function setupControlPanel() {
    const btnHelp = document.getElementById('btn-help');
    const btnReset = document.getElementById('btn-reset');
    const btnRefresh = document.getElementById('btn-refresh');
    const menuBtn = document.getElementById('tool-menu-btn');
    const optionsMenu = document.getElementById('tool-options-menu');

    // Toggle menu visibility
    menuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isMenuVisible = optionsMenu.classList.contains('show');
        optionsMenu.classList.toggle('show');
        menuBtn.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!optionsMenu.contains(e.target) && !menuBtn.contains(e.target)) {
            optionsMenu.classList.remove('show');
            menuBtn.classList.remove('active');
        }
    });

    // Menu option clicks
    btnHelp.addEventListener('click', () => {
        ToolAPI.openHelp();
        optionsMenu.classList.remove('show');
        menuBtn.classList.remove('active');
    });

    btnReset.addEventListener('click', () => {
        ToolAPI.reset();
        optionsMenu.classList.remove('show');
        menuBtn.classList.remove('active');
    });

    btnRefresh.addEventListener('click', () => {
        ToolAPI.refresh();
        optionsMenu.classList.remove('show');
        menuBtn.classList.remove('active');
    });
}

// Load tool when page loads
document.addEventListener('DOMContentLoaded', loadTool);