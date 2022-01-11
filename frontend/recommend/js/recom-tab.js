const tabList = document.querySelectorAll(".tab-menu__list");
const tabBtn = document.querySelectorAll(".tab-menu__btn");

for (let i = 0; i < tabList.length; i++) {
  tabBtn[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < tabList.length; j++) {
      tabList[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}
