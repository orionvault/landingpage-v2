(function($) {
  "use strict"; // Start of use strict

  var showMessage = function(type, msg) {
    var messageBox = $('#message');
    messageBox.removeClass("error success").addClass(type);
    messageBox.text(msg);
  }

  $('#presaleForm').submit(function(event) {
      event.preventDefault();

      var formData = {
          'first_name': $('#presaleForm input[name=first_name]').val(),
          'last_name': $('#presaleForm input[name=last_name]').val(),
          'email': $('#presaleForm input[name=email]').val(),
          'residency': $('#presaleForm .residence option:selected').text(),
          'contribution': $('#presaleForm input[name=contribution]').val(),
          'currency': $('#presaleForm .currency option:selected').val(),
          'investor_type': $('#presaleForm .investor_type option:selected').val(),
      };

      $.ajax({
          type: 'POST', // define the type of HTTP verb we want to use (POST for our form)
          url: 'http://panel.orionvault.com/api/v1/presales/', // the url where we want to POST
          data: formData, // our data object
          dataType: 'json', // what type of data do we expect back from the server
          encode: true
      })
      .done(function(data) {
          $('#presaleForm')[0].reset();
          showMessage('success', 'Registration form sent. Thank you for your interest.');
      })
      .fail(function(data) {
          $('#presaleForm')[0].reset();
          showMessage('error', 'There was an error during sendind data. Try again later.');
      });
  });


})(jQuery); // End of use strict
