var splash_current_timeout;
var splash_current_num = 1;

$(document).ready(function() {

   // do stuff when DOM is ready
       $('#splash1').bind('click', function(){
       	  clearTimeout(splash_current_timeout);
          do_splash_change(1, false);
       });

       $('#splash2').bind('click', function(){
       		clearTimeout(splash_current_timeout);
          	do_splash_change(2, false);
       });

       $('#splash3').bind('click', function(){
       		clearTimeout(splash_current_timeout);
          	do_splash_change(3, false);
       });
	   if(!splash_current_timeout)
       	splash_current_timeout = setTimeout("do_splash_change(2, true)", 6000);
 });


function do_splash_change(new_splash, repeat){
	
	// Keep track of which splash is currently being displayed
    var current = splash_current_num;
    splash_current_num = new_splash;
    
    $('#splash' + current).removeClass('current_splash_link');
    $('#splash' + new_splash).addClass('current_splash_link');
    $('#current_splash').html(new_splash);
    
    $('#splash_text_' + current).hide();
    
    $('#splash_link_' + current).fadeOut(function() {
    	$('#splash_text_' + new_splash).show();
	    $('#splash_link_' + new_splash).fadeIn(function(){
	    	var new_new_splash = 0;
		    if( repeat == true ){
		        if( new_splash == 3 ){
		            new_new_splash = 1;
		        }
		        else{
		            new_new_splash = new_splash + 1;
		        }
		        splash_current_timeout = setTimeout("do_splash_change(" + new_new_splash + ", true)", 6000);
		    }
	    });
	});
}