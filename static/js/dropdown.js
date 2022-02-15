const dropdown = document.querySelector(".dropdown");
const toggleButton = document.querySelector(".dropdown-toggle");
const dropdownMenu = document.querySelector(".dropdown-menu");
const options = document.querySelectorAll(".dropdown-option");

// 토글버튼 클릭-> 메뉴를 보여준다
// 메뉴 max-height: 0
// 메뉴.show -> 해지
toggleButton.addEventListener("click", function () {
  dropdownMenu.classList.toggle("show");
});

toggleButton.addEventListener("blur", function () {
  dropdownMenu.classList.toggle("show");
});

options.forEach(function (item) {
  item.addEventListener("click", function (e) {
    const buttonLabel = e.currentTarget.textContent.trim();
    toggleButton.textContent = buttonLabel;
    toggleButton.classList.add("selected");
  });
});
