$(window).scroll(function() {
  if(($document).scrollTop() >600 && $("#article_list").attr("displayed")  == "false") {
    $('#article_list').model('show');
    $('#article_list').attr("displayed","true");
  }
}
);