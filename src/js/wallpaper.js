(function($) {
  "use strict"; // Start of use strict

  var showMessage = function(type, msg) {
    var messageBox = $('#message');
    messageBox.removeClass("error success").addClass(type);
    messageBox.text(msg);
  }

  $('#wallpaperForm').submit(function(event) {
      event.preventDefault();

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

          var mapDeviceName = function(dev_name) {
              if(dev_name === 'iphone6') {
                return 'iPhone 6';
              } else if (dev_name === 'iphone6plus') {
                return 'iPhone 6+';
              } else if (dev_name === 'hd') {
                return 'HD';
              } else if (dev_name === 'uhd') {
                return 'UHD';
              } else if (dev_name === 'iphone7') {
                return 'iPhone 7';
              } else if (dev_name === 'iphone7plus') {
                return 'iPhone 7+';
              } else if (dev_name === 'iphone8') {
                return 'iPhone 8';
              } else if (dev_name === 'iphone8plus') {
                return 'iPhone 8+';
              } else if (dev_name === 'iphonex') {
                return 'iPhone X';
              } else if (dev_name === 'samsung_s8') {
                return 'Samsung S8/S8 Plus';
              } else if (dev_name === 'samsung_s9') {
                return 'Samsung S9/S9 Plus';
              } else {
                return 'Other';
              }
          }

          for(var idx=0; idx<data.wallpaper_images.length; idx++) {
              console.log('loop', idx);
            var i = data.wallpaper_images[idx]; 
            var t = $('<div class="col-md-3 col-sm-6 mx-auto"><a href="' + i.img + '" target="_blank"><img src="' + i.img + '"></a><p>' + mapDeviceName(i.device) + '</p></div>');
            $("#wallpaper_images").append(t);
          }

          $('#wallpaperBox').removeClass('d-none');

      })
      .fail(function(data) {
          $('#wallpaperForm')[0].reset();
          showMessage('error', 'Looks like the code is invalid. Try again.');
      });
  });


})(jQuery); // End of use strict
