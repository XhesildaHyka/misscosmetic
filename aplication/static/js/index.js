
  document.addEventListener("DOMContentLoaded", function () {
      const items = document.querySelectorAll(".Timeline__Item");
      const buttons = document.querySelectorAll(".Timeline__NavItem");
      const list = document.querySelector(".Timeline__ListItem");

      buttons.forEach((button, index) => {
          button.addEventListener("click", function () {
              // Remove active class from all buttons
              buttons.forEach(btn => btn.classList.remove("is-selected"));
              button.classList.add("is-selected");

              // Slide movement
              list.style.transform = `translateX(-${index * 100}%)`;
          });
      });
  });