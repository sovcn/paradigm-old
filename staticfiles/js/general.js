var ibd = {};

var current_page_hover = "nav_home";
var hover_image = new Image(142,49);
hover_image.src = "/static/images/nav_back.png";

$(document).ready(function() {
	$("#"+ current_page_hover).addClass('nav_hover');
	
    $("a.nav").hover(
    function(){
        var element = $(this);
        if( !element.hasClass('nav_hover') ){
			element.addClass('nav_hover');
        }
    },
    function(){
        var element = $(this);
        if( element.attr("id") != current_page_hover ){
            element.removeClass('nav_hover');
        }
    }
  	);

    $(".form_element").bind('focus', function(){
       $(this).addClass('form_element_focus');
    });

    $(".form_element").bind('blur', function(){
       $(this).removeClass('form_element_focus');
    });

});

// Added to allow for proper CSRF protection in ajax post calls.
// From https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
