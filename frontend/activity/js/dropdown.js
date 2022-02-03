const dropdown = document.querySelectorAll(".dropdown");
const toggleButton = document.querySelectorAll(".dropdown-toggle");
const menu = document.querySelectorAll(".dropdown-menu");
const options = document.querySelectorAll(".dropdown-option");

toggleButton.forEach((tgBtn) =>
  tgBtn.addEventListener("click", function () {
    this.nextElementSibling.classList.toggle("show"); // .dropdown-menu
  })
);

toggleButton.forEach((tgbtn) =>
  tgbtn.addEventListener("blur", function () {
    this.nextElementSibling.classList.toggle("show");
  })
);

options.forEach(function (item) {
  item.addEventListener("click", function (e) {
    const buttonLabel = e.currentTarget.textContent.trim();
    this.offsetParent.offsetParent.children[0].textContent = buttonLabel; // .dropdown-toggle
    this.offsetParent.offsetParent.children[0].classList.add("selected");
  });
});
