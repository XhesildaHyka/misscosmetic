
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

// login first
// Example JavaScript code for handling the add to cart AJAX response
function addToCart(productId) {
  $.ajax({
      url: '/add_to_cart/' + productId + '/',
      type: 'GET',
      success: function(response) {
          if (response.message) {
              alert(response.message);  // Show success message
          }
      },
      error: function(xhr, status, error) {
          if (xhr.status == 401) {
              alert("You need to log in first.");  // Show error if not logged in
              window.location.href = "/accounts/login/?next=" + window.location.pathname;  // Redirect to login
          }
      }
  });
}

