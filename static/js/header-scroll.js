const statusbar = document.querySelector(".status-bar");
const statusbarHeight = statusbar.getBoundingClientRect().height;

window.addEventListener("scroll", () => {
  if (window.scrollY > statusbarHeight) {
    statusbar.classList.add("status-bar--dark");
  } else {
    statusbar.classList.remove("status-bar--dark");
  }
});
