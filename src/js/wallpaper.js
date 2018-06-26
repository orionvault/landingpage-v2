(function($) {
  "use strict"; // Start of use strict

  var showMessage = function(type, msg) {
    var messageBox = $('#message');
    messageBox.removeClass("error success").addClass(type);
    messageBox.text(msg);
  }

  var hideMessage = function() {
    var messageBox = $('#message');
    messageBox.removeClass("error success");
    messageBox.text('');
  }

  $('#wallpaperForm').submit(function(event) {
      event.preventDefault();
      hideMessage();
      $("#wallpaper_images").text('');

      var pin_code = $('#wallpaperForm input[name=pin_code]').val();

      $.ajax({
          type: 'GET', 
          url: 'https://panel.orionvault.com/api/v1/wallpapers/' + pin_code + '/', // the url where we want to POST
          dataType: 'json', // what type of data do we expect back from the server
          encode: true
      })
      .done(function(data) {
          $('#wallpaperForm')[0].reset();
          console.log(data);
          $('#wallpaper_title').text(data.title);
          var c = $('<h5><a href="' + data.cert + '" target="_blank">Download certificate</a></h5>');
          $('#wallpaper_cert').html(c);

          var mapDeviceName = function(dev_name) {
              if(dev_name === 'iphone') {
                  return 'iPhone 6/7/8';
              } else if (dev_name === 'iphoneplus') {
                  return 'iPhone 6+/7+/8+';
              } else if (dev_name === 'hd') {
                return 'HD';
              } else if (dev_name === 'uhd') {
                return 'UHD';
              } else if (dev_name === 'iphonex') {
                return 'iPhone X';
              } else if (dev_name === 'samsung') {
                return 'Samsung S8/S8 Plus or S9/S9 Plus';
              } else {
                return 'Other';
              }
          }

          for(var idx=0; idx<data.wallpaper_images.length; idx++) {
              console.log('loop', idx);
            var i = data.wallpaper_images[idx]; 
            var t = $('<div class="col-md-4 col-sm-6 mx-auto"><a href="' + i.img + '" target="_blank"><img src="' + i.img + '"></a><p>' + mapDeviceName(i.device) + '</p></div>');
            $("#wallpaper_images").append(t);
          }

          $('#wallpaperBox').removeClass('d-none');

      })
      .fail(function(data) {
          $('#wallpaperForm')[0].reset();
          showMessage('error', 'Looks like the code is invalid. Try again.');
      });
  });

  $('.carousel').carousel();


})(jQuery); // End of use strict
