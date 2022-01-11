const midTabList = document.querySelectorAll(".mid-tab-menu__list");
const midTabBtn = document.querySelectorAll(".mid-tab-menu__btn");

for (let i = 0; i < midTabList.length; i++) {
  midTabBtn[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList.length; j++) {
      midTabList[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}
