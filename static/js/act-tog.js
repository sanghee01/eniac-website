const toggle = document.querySelector(".activity__comment-tog");
const headerListtogCont = document.querySelector(".activity__comment");
const icon = document.querySelector(".fa-chevron-down");

toggle.addEventListener("click", function() {
    if (togCont.style.display === "block") {
        togCont.style.display = "none";
        icon.classList.remove("fa-chevron-down");
        icon.classList.add("fa-chevron-up");
    } else {
        togCont.style.display = "block";
        icon.classList.remove("fa-chevron-up");
        icon.classList.add("fa-chevron-down");
    }
});