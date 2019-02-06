$( document ).ready(function () {
  $(".grid").slice(0, 1).show();
    if ($(".grid:hidden").length != 0) {
      $("#loadMore").show();
    }   
    $("#loadMore").on('click', function (e) {
      e.preventDefault();
      $(".grid:hidden").slice(0, 6).slideDown();
      
    });
  });

