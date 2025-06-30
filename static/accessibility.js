document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll("nav a");
  navLinks.forEach(link => {
    link.addEventListener("focus", () => {
      link.style.outline = "2px solid #007BFF";
    });
    link.addEventListener("blur", () => {
      link.style.outline = "none";
    });
  });
});
