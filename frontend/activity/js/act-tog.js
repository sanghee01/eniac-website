const toggle = document.querySelector(".activity__comment-tog");
const togCont = document.querySelector(".activity__comment");

toggle.addEventListener("click", function () {
  if (togCont.style.display === "block") {
    togCont.style.display = "none";
    toggle.textContent = " 댓글 ∨";
  } else {
    togCont.style.display = "block";
    toggle.textContent = " 댓글 ∧";
  }
});
