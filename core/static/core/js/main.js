document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".hint-button").forEach(function (button) {
    button.addEventListener("click", function () {
      const hint = document.getElementById(button.dataset.target);
      const isHidden = hint.hasAttribute("hidden");
      if (isHidden) {
        hint.removeAttribute("hidden");
        button.setAttribute("aria-expanded", "true");
        button.innerHTML = "Hide hint <span>-</span>";
      } else {
        hint.setAttribute("hidden", "");
        button.setAttribute("aria-expanded", "false");
        button.innerHTML = "Show hint <span>+</span>";
      }
    });
  });

  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      const open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }
});
