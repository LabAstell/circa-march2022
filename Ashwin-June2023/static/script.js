document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu ul');

  menuToggle.addEventListener('click', function () {
      navMenu.classList.toggle('show');
  });

  const galleryItems = document.querySelectorAll('.gallery-item');

  galleryItems.forEach(function(item) {
      item.addEventListener('click', function() {
          const imageSrc = this.querySelector('img').getAttribute('src');
          // Redirect to the magnified image page
          window.location.href = `/magnified/${encodeURIComponent(imageSrc)}`;
      });
  });
});
