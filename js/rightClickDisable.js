// Only disable inspect tools in production (not localhost)
if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
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
        (event.key === "I" || event.key === "i" || event.key === "J" || event.key === "j")) ||
      (event.ctrlKey && (event.key === "U" || event.key === "u")) ||
      event.key === "F12"
    ) {
      event.preventDefault();
    }
  }); 
}
