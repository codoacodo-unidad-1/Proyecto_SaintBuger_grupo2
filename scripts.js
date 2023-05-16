jQuery('document').ready(function($) {

    var MenuBtn = $('.Menu__icon'),
        Menu =  $('.Menu ul');

    MenuBtn.click(function() {

        if (Menu.hasClass('Show')) {
            Menu.removeClass('Show')
        }
        else {
            Menu.addClass('Show');
        }

    })
});