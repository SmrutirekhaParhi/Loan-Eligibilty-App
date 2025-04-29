const { ipcRenderer } = require('electron');

window.addEventListener('DOMContentLoaded', () => {
  const predictButton = document.getElementById('predictButton');
  const minimizeButton = document.getElementById('minimizeButton');
  const closeButton = document.getElementById('closeButton');

  predictButton.addEventListener('click', () => {
      alert('Predict button clicked! (Functionality coming soon)');
  });

  minimizeButton.addEventListener('click', () => {
    ipcRenderer.send('minimize-window');
  });

  closeButton.addEventListener('click', () => {
    ipcRenderer.send('close-window');
  });
});
