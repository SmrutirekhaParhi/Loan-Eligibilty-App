const { ipcRenderer } = require('electron');

window.addEventListener('DOMContentLoaded', () => {
  const predictButton = document.getElementById('predictButton');
  const minimizeButton = document.getElementById('minimizeButton');
  const closeButton = document.getElementById('closeButton');
  const menuButton = document.getElementById('menuButton');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');

  predictButton.addEventListener('click', () => {
      alert('Predict button clicked! (Functionality coming soon)');
  });

  minimizeButton.addEventListener('click', () => {
    ipcRenderer.send('minimize-window');
  });

  closeButton.addEventListener('click', () => {
    ipcRenderer.send('close-window');
  });

  // Sidebar toggle logic
  menuButton.addEventListener('click', () => {
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
  });
  
  overlay.addEventListener('click', () => {
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
  });

});
