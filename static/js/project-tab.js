const projectList = document.querySelectorAll(".project-menu__list");
const projectBtn = document.querySelectorAll(".project-menu__btn");

for (let i = 0; i < projectList.length; i++) {
    projectBtn[i].addEventListener("click", function(e) {
        e.preventDefault();
        for (let j = 0; j < projectList.length; j++) {
            projectList[j].classList.remove("is_on");
        }
        this.parentNode.classList.add("is_on");
    });
}