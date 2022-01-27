const midTabList_1 = document.querySelectorAll(".mlist-1");
const midTabList_2 = document.querySelectorAll(".mlist-2");
const midTabList_3 = document.querySelectorAll(".mlist-3");
const midTabList_4 = document.querySelectorAll(".mlist-4");
const midTabList_5 = document.querySelectorAll(".mlist-5");
const midTabList_6 = document.querySelectorAll(".mlist-6");
const midTabBtn_1 = document.querySelectorAll(".mbtn-1");
const midTabBtn_2 = document.querySelectorAll(".mbtn-2");
const midTabBtn_3 = document.querySelectorAll(".mbtn-3");
const midTabBtn_4 = document.querySelectorAll(".mbtn-4");
const midTabBtn_5 = document.querySelectorAll(".mbtn-5");
const midTabBtn_6 = document.querySelectorAll(".mbtn-6");

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

for (let i = 0; i < midTabList_3.length; i++) {
  midTabBtn_3[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList_3.length; j++) {
      midTabList_3[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}

for (let i = 0; i < midTabList_4.length; i++) {
  midTabBtn_4[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList_4.length; j++) {
      midTabList_4[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}

for (let i = 0; i < midTabList_5.length; i++) {
  midTabBtn_5[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList_5.length; j++) {
      midTabList_5[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}

for (let i = 0; i < midTabList_6.length; i++) {
  midTabBtn_6[i].addEventListener("click", function (e) {
    e.preventDefault();
    for (let j = 0; j < midTabList_6.length; j++) {
      midTabList_6[j].classList.remove("is_on");
    }
    this.parentNode.classList.add("is_on");
  });
}
