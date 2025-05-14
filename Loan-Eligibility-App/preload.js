const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  predictLoan: (data) => ipcRenderer.invoke('predict-loan', data),
  minimize: () => ipcRenderer.send('minimize-window'),
  close: () => ipcRenderer.send('close-window'),
  maximize: () => ipcRenderer.send('maximize-window'),
});
