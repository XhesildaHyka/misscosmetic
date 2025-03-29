
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


//   produktet e kartes


  document.addEventListener('DOMContentLoaded', function() {
    const messageContainer = document.getElementById('message-container');
    
    if (messageContainer && messageContainer.children.length > 0) {
      // Add the "show" class to trigger the animation
      messageContainer.style.display = 'block';
      messageContainer.style.opacity = '1';
      messageContainer.style.transform = 'translateX(-50%) translateY(0)';
      
      // Hide the message after 3 seconds
      setTimeout(function() {
        messageContainer.style.display = 'none';
        messageContainer.style.opacity = '0';
        messageContainer.style.transform = 'translateX(-50%) translateY(100px)';
      }, 3000);
    }
  });


  // Show the message when it's added to the cart
document.addEventListener('DOMContentLoaded', function() {
const messageContainer = document.getElementById('message-container');

if (messageContainer && messageContainer.children.length > 0) {
  // Add the "show" class to trigger the animation
  messageContainer.classList.add('show');
  
  // Hide the message after 3 seconds
  setTimeout(function() {
    messageContainer.classList.remove('show');
  }, 3000);
}
});

