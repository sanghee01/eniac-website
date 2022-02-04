const modal = document.querySelectorAll(".modal");
const moreBtn = document.querySelectorAll(".more");
const overlay = document.querySelectorAll(".modal__overlay");
const closeBtn = document.querySelectorAll(".modal__close");

for (let i = 0; i < modal.length; i++) {
    moreBtn[i].addEventListener("click", (e) => {
        e.path[0].nextElementSibling.classList.remove("hidden");
    });

    closeBtn[i].addEventListener("click", (e) => {
        e.path[2].classList.add("hidden");
    });
    overlay[i].addEventListener("click", (e) => {
        e.path[1].classList.add("hidden");
    });
}