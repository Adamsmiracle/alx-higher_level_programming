document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $('INPUT#btn_search').click(function () {
      $.ajax({
        type: 'GET',
        url: 'https://www.fourtonfish.com/hellosalut/hello/' + $('INPUT#city_search').val() + '%22)&format=json',
        success: function (data) {
          let input = $('INPUT#city_search').val();
          if (input) {
            $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
          }
        }
      });
    });
  });
});
