/* Custom JavaScript to make navbar sticky */
$(document).ready(function() {
    // get the navbar element
    var navbar = $('.navbar');
    // get the initial position of the navbar
    var navbarOffset = navbar.offset().top;

    // add a scroll event listener to the window
    $(window).scroll(function() {
        // get the current position of the scroll
        var scrollPosition = $(window).scrollTop();

        // if the scroll position is greater than the navbar offset, make the navbar sticky
        if (scrollPosition >= navbarOffset) {
            navbar.addClass('sticky');
        } else {
            navbar.removeClass('sticky');
        }
    });
});
