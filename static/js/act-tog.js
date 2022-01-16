const toggle = document.querySelectorAll(".activity__comment-tog");
const icon = document.querySelectorAll(".fa-chevron-down");

toggle.forEach((tog) =>
  tog.addEventListener("click", function () {
    const togId = this.id.replace("tog", "comm");

    if (document.getElementById(togId).style.display === "block") {
      document.getElementById(togId).style.display = "none";
      /* icon 변경 안되는거 고치고 있는 코드(신경x)
      console.log(this.children.value);
     console.dir(this);
       this.children.classList.remove("fa-chevron-down");
      this.children.classList.remove("fa-chevron-up");
    */
    } else {
      document.getElementById(togId).style.display = "block";
    }
  })
);

// 실험용(신경x)
// toggle.addEventListener("click", function () {
//  if (togCont.style.display === "block") {
//     togCont.style.display = "none";
//     icon.classList.remove("fa-chevron-down");
//     icon.classList.add("fa-chevron-up");
//   } else {
//     togCont.style.display = "block";
//     icon.classList.remove("fa-chevron-up");
//     icon.classList.add("fa-chevron-down");
//   }
// });
