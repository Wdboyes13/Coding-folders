const { app, BrowserWindow } = require("electron");
const path = require("path");

app.setPath("userData", app.getPath("home") + "/.my-github-app");

let mainWindow;

app.whenReady().then(() => {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        icon: path.join(__dirname, "assets", "icon.png"), // Change to "icon.ico" for Windows or "icon.icns" for macOS
        webPreferences: {
            nodeIntegration: false,
            partition: "persist:github"
        }
    });

    mainWindow.loadURL("https://github.com");

    mainWindow.webContents.once("did-finish-load", () => {
        mainWindow.webContents.executeJavaScript(`
            const disclaimer = document.createElement('div');
            disclaimer.textContent = "This app is not affiliated with or endorsed by GitHub, Inc. GitHub and the GitHub Invertocat logo are trademarks of GitHub, Inc.";
            disclaimer.style.position = "fixed";
            disclaimer.style.bottom = "0";
            disclaimer.style.width = "100%";
            disclaimer.style.background = "#ffcc00";
            disclaimer.style.color = "#000";
            disclaimer.style.textAlign = "center";
            disclaimer.style.padding = "5px";
            disclaimer.style.fontSize = "12px";
            disclaimer.style.fontFamily = "Arial, sans-serif";
            document.body.appendChild(disclaimer);
        `);
    });
});

// Close app when all windows are closed
app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});

// Reopen window on macOS when clicking the dock icon
app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        mainWindow = new BrowserWindow({
            width: 1200,
            height: 800,
            icon: path.join(__dirname, "assets", "icon.png"),
            webPreferences: {
                nodeIntegration: false,
                partition: "persist:github"
            }
        });

        mainWindow.loadURL("https://github.com");

        mainWindow.webContents.once("did-finish-load", () => {
            mainWindow.webContents.executeJavaScript(`
                const disclaimer = document.createElement('div');
                disclaimer.textContent = "This app is not affiliated with or endorsed by GitHub, Inc. GitHub and the GitHub Invertocat logo are trademarks of GitHub, Inc.";
                disclaimer.style.position = "fixed";
                disclaimer.style.bottom = "0";
                disclaimer.style.width = "100%";
                disclaimer.style.background = "#ffcc00";
                disclaimer.style.color = "#000";
                disclaimer.style.textAlign = "center";
                disclaimer.style.padding = "5px";
                disclaimer.style.fontSize = "12px";
                disclaimer.style.fontFamily = "Arial, sans-serif";
                document.body.appendChild(disclaimer);
            `);
        });
    }
});
