$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.query.results.channel.wind.speed);
    }
  });
});
