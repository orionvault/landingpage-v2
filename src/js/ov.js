(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 48)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 50
  });

  // Menu transparency & shadow handling
  var updateMenuBg = function() {
    if (window.scrollY > 0) {
      $('#mainNav').addClass('nav-opaque');
      $('#mainNav').removeClass('nav-transparent');
    } else if ($('.navbar-toggler').hasClass('collapsed')) {
      $('#mainNav').removeClass('nav-opaque');
      $('#mainNav').addClass('nav-transparent');
    }        
  };

  $(window).scroll(updateMenuBg);
  $('#navbarResponsive').on('hidden.bs.collapse', updateMenuBg);
  $('#navbarResponsive').on('show.bs.collapse', function() {
      $('#mainNav').addClass('nav-opaque');
      $('#mainNav').removeClass('nav-transparent');    
  });

  $(window).scroll(updateMenuBg);

  // Product carousel

  // Expandable section color and arrow pointing changes handling in Benefits and Competitive Advantage section
  var makeGold = function(selector) {
    $(selector).addClass('expandable-gold');
    $(selector).removeClass('expandable-grey');
  };

  var makeGrey = function(selector) {
    $(selector).removeClass('expandable-gold');
    $(selector).addClass('expandable-grey');
  };

  var handleTransition = function(sourceSelector, subjectSelector) {
    $(sourceSelector)
      .on('show.bs.collapse', function() {
        makeGold(subjectSelector);
      })
      .on('hide.bs.collapse', function() {
        makeGrey(subjectSelector);
      });
  };

  handleTransition('#collapseInvestors', '#benefitsInvestors');
  handleTransition('#collapseArtists', '#benefitsArtists');
  handleTransition('#collapseSociety', '#benefitsSociety');
  
  handleTransition('#collapseOwnership', '#advantageOwnership');
  handleTransition('#collapseDigital', '#advantageDigital');
  handleTransition('#collapseSolution', '#advantageSolution');
  handleTransition('#collapseSustainability', '#advantageSustainability');
  handleTransition('#collapseMover', '#advantageMover');

  // Exapndable arrow pointing changes in Market Size and Contact & Info
 var handleArrow = function(sourceSelector, subjectSelector) {
    $(sourceSelector)
      .on('show.bs.collapse', function() {
        $(subjectSelector).addClass('expanded');
      })
      .on('hide.bs.collapse', function() {
        $(subjectSelector).removeClass('expanded');
      });
  };

  handleArrow('#collapseMarketSize', '#market_size .read-more');
  handleArrow('#collapseInfo', '#contact .read-more');

  // Team clickable faces
  var links = [
    "https://www.linkedin.com/in/joanna-pawluk-a313647/",
    "https://www.linkedin.com/in/aleksander-alex-kampa-97436571/",
    "https://www.linkedin.com/in/micha%C5%82-sambora-75732892/",
    "https://www.goldenline.pl/andrzej-nagorski2/",
    "https://www.linkedin.com/in/karivalencia/",
    "https://www.linkedin.com/in/mynseok-kang-09852249/",
    "https://www.saatchiart.com/koper",
    "https://www.linkedin.com/in/therealme/",
    "https://www.linkedin.com/in/krzysztofpawluk/",
    "https://www.linkedin.com/in/ironmonkey/",
    "https://www.linkedin.com/in/denys-rozlomii-636219bb/",
    "https://www.linkedin.com/in/laxpoojary/",
    "https://www.linkedin.com/in/dawid-wr%C3%B3blewski-451b9a15/",
    "https://www.linkedin.com/in/binishsharma/",
    "https://www.linkedin.com/in/piotr-delkowski-52b493113/",
    "https://www.linkedin.com/in/abhishekharee/"
  ];

  var images = $('#our_team .faces img');
  for (var i = 0; i < images.length; i++) {
    var faceLink = $('<a href="' + links[i % links.length] + '" target="_blank"><div class="face-link"></div></a>');
    $(images[i]).after(faceLink);
  }

})(jQuery); // End of use strict