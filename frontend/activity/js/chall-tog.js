const ctoggle = document.querySelectorAll(".challenge__comment-tog");
const cicon = document.querySelectorAll(".fa-chevron-up");

ctoggle.forEach((toggle) =>
  toggle.addEventListener("click", function () {
    const togId = this.id.replace("tog", "comm");

    if (document.getElementById(togId).style.display === "block") {
      document.getElementById(togId).style.display = "none";
      // console.log(this.children.value);
      // console.dir(this);
      // this.children.classList.remove("fa-chevron-down");
      // this.children.classList.remove("fa-chevron-up");
    } else {
      document.getElementById(togId).style.display = "block";
    }
  })
);

// ctoggle.addEventListener("click", function () {
//   if (ctogCont.style.display === "block") {
//     ctogCont.style.display = "none";
//     cicon.classList.remove("fa-chevron-down");
//     cicon.classList.add("fa-chevron-up");
//   } else {
//     ctogCont.style.display = "block";
//     cicon.classList.remove("fa-chevron-up");
//     cicon.classList.add("fa-chevron-down");
//   }
// });
