// In your Electron main process file

const { app, BrowserWindow, Menu } = require('electron');

let mainWindow;

app.on('ready', () => {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    // Load the login page initially
    mainWindow.loadFile('index.html');

    // Disable the menu when the app starts
    Menu.setApplicationMenu(null);
});

// Function to enable the application menu
function enableApplicationMenu() {
    const template = [
        // Define your menu template here
        // Example:
        {
            label: 'File',
            submenu: [
                {
                    label: 'Exit',
                    role: 'quit'
                }
            ]
        }
    ];

    const menu = Menu.buildFromTemplate(template);

    // Set the application menu
    Menu.setApplicationMenu(menu);
}

// Example usage: enable the menu when you redirect to hero.html
function redirectToHeroPage() {
    mainWindow.loadFile('hero.html');
    enableApplicationMenu(); // Enable the menu
}
