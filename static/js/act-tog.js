const toggle = document.querySelectorAll(".activity__comment-tog");
const abc = document.querySelectorAll(".activity__comment");
const icon = document.querySelectorAll(".fa-chevron-down");

toggle.addEventListener("click", function() {
    if (togCont.style.display === "none") {
        abc.style.display = "block";
        icon.classList.remove("fa-chevron-up");
        icon.classList.add("fa-chevron-down");
    } else {
        abc.style.display = "none";
        icon.classList.remove("fa-chevron-down");
        icon.classList.add("fa-chevron-up");
    }
});