document.addEventListener(
  "contextmenu",
  function (e) {
    e.preventDefault();
  },
  false
);

// Disable Specific Keyboard Shortcuts
document.addEventListener("keydown", function (event) {
  // Disable Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U (View Source), and F12 (DevTools)
  if (
    (event.ctrlKey &&
      event.shiftKey &&
      (event.key === "I" || event.key === "J")) ||
    (event.ctrlKey && event.key === "U") ||
    event.key === "F12"
  ) {
    event.preventDefault();
  }
}); 
