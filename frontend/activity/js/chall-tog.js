const ctoggle = document.querySelector(".challenge__comment-tog");
const ctogCont = document.querySelector(".challenge__comment");
const cicon = document.querySelector(".fa-chevron-up");

ctoggle.addEventListener("click", function () {
  if (ctogCont.style.display === "block") {
    ctogCont.style.display = "none";
    cicon.classList.remove("fa-chevron-down");
    cicon.classList.add("fa-chevron-up");
  } else {
    ctogCont.style.display = "block";
    cicon.classList.remove("fa-chevron-up");
    cicon.classList.add("fa-chevron-down");
  }
});
