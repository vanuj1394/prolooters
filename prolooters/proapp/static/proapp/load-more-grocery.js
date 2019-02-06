$( document ).ready(function () {
  $(".grocery").slice(0, 1).show();
    if ($(".grocery:hidden").length != 0) {
      $("#loadMore2").show();
    }   
    $("#loadMore2").on('click', function (e) {
      e.preventDefault();
      $(".grocery:hidden").slice(0, 6).slideDown();
      
    });
  });