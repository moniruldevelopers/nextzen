  // Function to scroll back to the top
  function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// Show the button when the user scrolls down
window.onscroll = function() {
    var button = document.querySelector(".back-to-top");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}