const hamburger = document.querySelector(".status-bar__hamburger");
const menu = document.querySelector(".status-bar__menu");

hamburger.addEventListener("click", () => {
  menu.classList.toggle("menu-on");
});
