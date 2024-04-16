window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 72 || document.documentElement.scrollTop > 72) {
    document.getElementById("sub-header").classList.add('scrolled');
    document.getElementById("top-button").classList.add('hidden');
  } else {
    document.getElementById("sub-header").classList.remove('scrolled');
    document.getElementById("top-button").classList.remove('hidden');
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}