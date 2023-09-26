const { app, BrowserWindow,Menu } = require('electron');


let mainWindow;

Menu.setApplicationMenu(null);

app.on('ready', () => {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    mainWindow.loadFile('index.html');
});
