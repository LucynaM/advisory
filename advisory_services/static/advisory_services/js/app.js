$(document).ready(function() {

    const setBannerwidth  = () => {
        if (window.innerWidth > 768) {
            $('.wrap-banner .img-holder').width("");
            const windowWidth = window.innerWidth;
            const containerWidth = $('.container').width();
            const bannerWidth = $('.wrap-banner .img-holder').width();
            $('.wrap-banner .img-holder').width(bannerWidth + ((windowWidth - containerWidth) / 2) - 6);
        } else {
            $('.wrap-banner .img-holder').width("");
        }

    };

    setBannerwidth();

    $(window).on('resize', () => {
        setBannerwidth();
    });

    $('[data-type="toggle"]').on('click', function(e) {
        e.preventDefault();
        const href = $(this).attr('href');
        $(this).toggleClass('active');
        if ($(this).hasClass('active')) {
            $(href).slideDown('slow');
        } else {
            $(href).slideUp('slow');
        }
    });
});