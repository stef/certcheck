$(document).ready(function() {
  $('.item').hover(
    function(){
      icon = $(this).children().children();
      icon.attr('off', icon.attr('src'));
      icon.attr('src', '/static/img/scary.svg');
    },
    function(){
      icon.attr('src', icon.attr('off'));
    }
  )
});
