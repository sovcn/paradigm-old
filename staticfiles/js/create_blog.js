
///  ibd.tags module
ibd.tags = {};
(function(){
	// Provide a local scope for all javascript within the tag module
	var tag_list = [];
	var list_displayed = false;
	
	ibd.tags.remove_tag = function(tag_num){
		tag_list = tag_list.slice(0,tag_num).concat(tag_list.slice(tag_num+1,tag_list.length));
		draw_tags();
		$("#id_tags").focus();
	};
	
	ibd.tags.add_tag = function(tag){
		tag_list.push(tag);
		draw_tags();
	}
	
	var draw_tags = function(){
		var tags = $("#cb_used_tags");
		var html = "";
		for(var i=0;i<tag_list.length;i++){
			html += '<span class="cb_tag_container">' + tag_list[i] + '<span onclick="ibd.tags.remove_tag(' + i + ')"  class="ui-icon ui-icon-circle-close"></span></span> ';
		}
		
		$("#cb_used_tags").html(html);
		
		if( !list_displayed ){
			$('#cb_used_tags').show('highlight', {}, 500);
			$("span.helptext:contains('Comma')").html("Click to remove.");
			list_displayed = true;
		}
		
	}
	
	var initialize = function(){
		// Tag collection
		var input = $("#id_tags");
		$("#cb_used_tags").hide();
		
		input.keyup(function(event){
			if( event.which == 188 ){ // presses the , key
				var tag = input.attr('value');
				tag_list.push(tag.substring(0,tag.length-1));
				input.attr('value', '');
				console.log(tag_list);
				draw_tags();
			}
		});
		
		// Add prexisting tags to the list
		if( input.attr('value') != "" ){
			tag_list = input.attr('value').split(",");
			input.attr('value', '');
			draw_tags();
		}

		// Prepare existing tag links for use
		var tags = $('a.tag_link');
		tags.click(function(){
			var tag = this.id.replace('tag_', '');
			ibd.tags.add_tag(tag);
			return false;
		});
		
	}
	
	var catch_data = function(){
		$("#cb_form").submit(function(){
			// Collect all of the tags that have been added and submit them as part of the form.
			
			var input = $("#id_tags");
			
			var value = "";
			for(var i=0;i<tag_list.length;i++){
				value += tag_list[i] + ',';
			}
			
			console.log(value);
			var last_value = input.attr('value');
			if( input.attr('value').length > 0 ){
				value += last_value;
				input.attr('value', '');
			}else{
				value = value.substring(0,value.length-1);
			}
			
			$('#id_tags_hidden').attr('value', value); // Update the hidden variable to contain the correct values.
		});
	};
	
	$("document").ready(function(){
		initialize();
		catch_data();
	});
})();


/// ibd.category module
ibd.category = {};
(function(){
	
	ibd.category.initalize_selectable = function(id, hidden_id){
		
		
		var value = $("#" + hidden_id).val();
		if( value.length > 0 ){
			// Existing values have been loaded. Select them.
			var values = value.split(",");
			for(var i=0;i<values.length;i++){
				$('#cat_' + values[i]).addClass("ui-selected");
			}
		}
		
		$( "#" + id ).bind( "selectablestop", function(event, ui) {
			var ids = [];
			$( ".ui-selected", this ).each(function() {
				var id = this.id.replace("cat_", "");
				ids.push(id);
			});
			console.log(ids);
			$( "#" + hidden_id ).val(ids.join(","));
		});
	}
	
	ibd.category.initialize_add_dialog = function(id, link_id, container_id){
		
		$("#" + id).dialog({ 
			autoOpen: false,
			show: "blind",
			hide: "explode",
			buttons: [
		    {
		        text: "Create",
		        click: function() {
		        	var slug = $("#new_category").val();
		        	var name = $("#new_category_name").val();
		        	
		        	var request = $.ajax({
					  url: "/async/blog/add-category/",
					  type: "POST",
					  data: {name: name, slug: slug},
					  dataType: "json"
					});
					
					request.done(function(data) {
					  if( data.status == false ){
					  	$("#" + id).prepend('<div class="error">' + data.message + '</div>');
					  }else{
					  	var category = $('<li class="ui-widget-content" id="cat_' + data.slug + '">' + data.name + '</li>');
					  	category.addClass('ui-selectee');
					  	category.addClass('ui-selected');
					  	category.addClass('ui-helper-hidden');
					  	$('#' + container_id).append(category);
					  	category.show('highlight', {}, 1000);
					  	
					  	$("#" + id).dialog("close");
					  	
					  	// Update the current list of selected categories
					  	$('#' + container_id).trigger('selectablestop');
					  }
					});
					
					request.fail(function(jqXHR, textStatus) {
					  alert( "Request failed: " + textStatus );
					});

		        }
		    }
		] });
		
		$("#" + link_id).click(function(){
			$( "#" + id ).dialog( "open" );
			return false;
		});
	};
	
})();



/// ibd.images module
ibd.images = {};
(function(){
	
	var image_button;
	var url_dom;
	
	ibd.images.dropped_event = function(event, ui){
		$( this ).addClass( "ui-state-highlight" );
		console.log(ui.draggable.attr('id'));
		var dropped = ui.draggable;
		var id = dropped.attr('id').replace('form-image-', '');
		$('#id_image_hidden').val(id);
		
		dropped.hide();
		dropped.css('left', '0px');
		dropped.css('top', '0px');
		
		var place_holder = dropped.clone();
		$("#primary_image_drop").html(place_holder);
		
		dropped.fadeIn(function(){
		}); 
		place_holder.show('highlight', {}, 500);
	};
	
	ibd.images.strip_dimensions = function(url){
		var new_url = url.replace(/=s\d+/, '');
		if(new_url == url){
			new_url = "Error. Invalid url.";	
		}
		return new_url;
	}
	
	// Finds the text input for the image url, brings up the dialog, and inserts the url
	ibd.images.overwrite_elrte_image = function(event, ui){
		console.log(ui.draggable);
		ui.draggable.css('left', '0px').css('top', '0px');
		
		$('ul.panel-media li[name="image"]').click();

		url_dom = $('input#elrte_image_url_field');
		console.log(url_dom);
		url_dom.val(ibd.images.strip_dimensions(ui.draggable.attr('src')));
	};

})();