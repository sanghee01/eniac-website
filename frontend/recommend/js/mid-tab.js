const midTabList_1 = document.querySelectorAll(".mlist-1");
const midTabList_2 = document.querySelectorAll(".mlist-2");
const midTabBtn_1 = document.querySelectorAll(".mbtn-1");
const midTabBtn_2 = document.querySelectorAll(".mbtn-2");

for (let i = 0; i < midTabList_1.length; i++) {
  midTabBtn_1[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList_1.length; j++) {
      midTabList_1[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}

for (let i = 0; i < midTabList_2.length; i++) {
  midTabBtn_2[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList_2.length; j++) {
      midTabList_2[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}
