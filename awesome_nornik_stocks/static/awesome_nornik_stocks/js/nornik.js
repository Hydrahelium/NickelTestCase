$(document).ready( function () {

  // Timers for ajax call
  var timer = window.setInterval(getData, 1000);
  // Timer for fetching pagination when database is empty
  var pagination_timer = window.setInterval(getPagination ,5000)
  const baseUrl = 'http://127.0.0.1:8000/';

  var url = baseUrl;
  // Ajax for update table every second
  function getData(id='#stocks', url_call=url) {
    $.ajax({
      type: 'GET',
      url: url_call,
      success: function(data) {
        $(id).html(data);
        if (document.getElementById('exist') != null) {
          clearInterval(pagination_timer);
        }
      }
    });
    console.log('Request sended ' + url_call);
  };
  // Function for detching initial pagination, stops when pagination fetched
  function getPagination() {
    $.ajax({
      type: 'GET',
      url: baseUrl + '?pagination=True',
      success: function(data) {
          console.log('pagination fetched');
          $('#pagination').html(data);
        }
    });
  };
  // Prevent and redirect request to ajax when paginate
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
