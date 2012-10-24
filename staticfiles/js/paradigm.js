
var paradigm = {
};

// Filter Definition
(function(){
	paradigm.Filter = function(id, index, offsets){
		this.id = id;
		this.index = index;
		this.offsets = offsets;
		
		this.timeout = {};
	
		$('#' + id).css('margin-left', offsets[index]);
		$('#' + id + '_' + index).addClass("filter_selected");
	}
	
	paradigm.Filter.prototype.initSelector = function(index, initClick, callback){
		_initializeHover(this, index);
		
		if(initClick){
			var that = this;
			$("#" + that.id + "_" + index).click(function(){
				$("#" + that.id + "_" + that.index).removeClass("filter_selected");
				$("#" + that.id + "_" + index).addClass("filter_selected");
				
				$("#" + that.id).animate({
				    marginLeft: that.offsets[index] + "px"
				 }, 200 );
				
				that.index = index;
				
				callback();
				
				return false;
			});
		}
		
	}
	
	var _initializeHover = function(that, index){
		$("#" + that.id + "_" + index).hover(
				function(){
					
					// Prevent the icon from returning until a hoverout event is fired again
					for(var key in that.timeout){
						//console.log(handler);
						var handler = that.timeout[key];
						if(handler != null){
							clearTimeout(handler);
						}
					}
					
					$("#" + that.id).animate({
					    marginLeft: that.offsets[index] + "px"
					  }, 200 );
				},
				function(){
					// hover out
					
					// Wait to send the icon back in case the cursor is about to go to a different one
					that.timeout[index] = setTimeout(function(){
						$("#" + that.id).animate({
						    marginLeft: that.offsets[that.index] + "px"
						  }, 200 );
					},300);			
		});
	}
	
})();


// Gallery Definition
(function(){
	paradigm.Gallery = {};
	paradigm.Gallery.initialize = function(className, contentClassName, hoverClassName, duration){
		
		if(!duration){
			duration = 300;
		}
		
		$("." + className).hover(function(){
			$(this).children("." + contentClassName).addClass(hoverClassName, duration);
			$(this).children("." + contentClassName).children("p").addClass("hover", duration);
		},
		function(){
			$(this).children("." + contentClassName).removeClass(hoverClassName, duration);
			$(this).children("." + contentClassName).children("p").removeClass("hover", duration);
		});
	};
	
})();

// Slide Show
(function(){
	var id;
	var galleryClass;
	var postfix;
	
	paradigm.SlideShow = function(id, galleryClass, postfix){
		this.id = id;
		this.galleryClass = galleryClass;
		this.postfix = postfix;
	}
	
	paradigm.SlideShow.prototype.init = function(){
		console.log("." + this.galleryClass);
		
		console.log("#" + this.id);
		$("#" + this.id).click(function(){
			console.log("TESTINGprim");
		});
		
		var that = this;
		$("." + this.galleryClass).click(function(){
			var newSrc = "";
			
			var thisSrc = $(this).children(":first").attr('src');
			var primarySrc = $("#" + that.id).attr('src');
			
			var newPostfix = primarySrc.match(that.postfix);
			if(newPostfix){
				var oldPostfix = thisSrc.match(that.postfix);
				if( oldPostfix ){
					//console.log(oldPostfix);
					newSrc = thisSrc.replace(oldPostfix[0], newPostfix[0]);
				} else{
					console.error("Unable to assign new postfix to image src. Gallery image url incorrectly formed.");
					return;
				}
			}else {
				console.error("Unable to assign new postfix to image src.  Primary image url incorrectly formed.");
				return;
			}
			
			console.log(newSrc);
			var preload = new Image(newSrc);
			$("#" + that.id).animate({opacity: 0}, 300, function(){
				$("#" + that.id).attr('src', newSrc);
				$("#" + that.id).load(function(){
					$("#" + that.id).animate({opacity: 1}, 300);
					$("#" + that.id).off('load');
				});
			});
		});
	}
})();



// CSRF
//Added to allow for proper CSRF protection in ajax post calls.
//From https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax

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

