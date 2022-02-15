const headerSpan = document.querySelectorAll(".status-bar__list");

// 잴 앞에거만 냄겨놓고 잴 앞에것만 is_on실행

if (this.location.href === "http://127.0.0.1:8000/notice") {
  headerSpan[0].classList.add("is_on");
} else if (this.location.href === "http://127.0.0.1:8000/project") {
  headerSpan[1].classList.add("is_on");
} else if (this.location.href === "http://127.0.0.1:8000/activity") {
  headerSpan[2].classList.add("is_on");
} else if (this.location.href === "http://127.0.0.1:8000/recommend") {
  headerSpan[3].classList.add("is_on");
}
