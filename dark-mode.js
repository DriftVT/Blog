// On page load, read the stored darkMode setting
const storedDarkMode = localStorage.getItem('darkMode');
if (storedDarkMode === 'true') {
  document.body.classList.add('dark-mode');
}

// Get the toggle button (assuming your HTML has a <button id="dark-mode-toggle">)
const darkModeToggle = document.getElementById('dark-mode-toggle');

// If the button exists on this page, attach a click event
if (darkModeToggle) {
  darkModeToggle.addEventListener('click', () => {
    // Toggle the class
    document.body.classList.toggle('dark-mode');

    // Save the new preference
    const isDarkModeOn = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkModeOn);
  });
}