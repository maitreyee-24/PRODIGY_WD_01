window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
      navbar.style.backgroundColor = '#005580';
    } else {
      navbar.style.backgroundColor = '#0077be';
    }
  });
  