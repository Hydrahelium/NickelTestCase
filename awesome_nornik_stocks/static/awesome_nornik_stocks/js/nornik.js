$(document).ready( function () {

  var timer = window.setInterval(getData, 1000);
  const baseUrl = 'http://127.0.0.1:8000/';

  var url = baseUrl;

  function getData(id='#stocks', url_call=url) {
    $.ajax({
      type: 'GET',
      url: url_call,
      success: function(data) {
        $(id).html(data);
        return data;
      }
    });
    console.log('Запрос отправлен ' + url_call);
  };

  $(document).click(function(e) {
    if ($(e.target).is('[href]')) {
      e.preventDefault();
      var page = $(e.target).attr("href");
      url = baseUrl + page;
      getData(id='#pagination', url_call = baseUrl + page + '&pagination=True');
      getData();
    };
  });
});
