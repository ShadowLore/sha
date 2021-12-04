document.querySelector('.click-for-video').onclick = function() {
  this.style.display = 'none';
  document.querySelector('div.youtube').style.display = 'block';
  document.querySelector('iframe.youtube')
    .src = "https://www.youtube.com/embed/HLUY1nICQRY;autoplay=1&;controls=0&;showinfo=0";
};



