$(function() {
  var distance = $('.navbar').offset().top,
      $window = $(window);
      $window.scroll(function() {
      var dh = $('.navbar').height();
      $('.navbar').toggleClass('fixed', $window.scrollTop() >= distance, "easeOutSine");
      if($('.navbar').hasClass('fixed')){
      $('body').css('margin-top', dh );
      }else{
      $('body').css('margin-top', 0 );
      }
  });
  })