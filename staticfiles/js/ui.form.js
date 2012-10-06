$.widget("ui.form", {
	_init : function() {
		var object = this;
		var form = object.element;
		var inputs = form.find("input , select ,textarea");
		var values = {};

		form.find("fieldset").addClass("ui-widget-content");
		form.find("legend").addClass("ui-widget-header ui-corner-all basic-legend");
		form.addClass("ui-widget");
		
		form.find('input[type="submit"]').button();
	
									   //.labelify({ labelledClass: "basic-form-text-input-labeled" });

		
		form.find("button.form-add-button").button({
			icons: {
                primary: "ui-icon-plus"
            }
        });
	}
});

$.widget("ui.label", {
	_init : function(){
		var elements = this.element;
		elements.each(function() {
			var element = $(this);
			var value = element.val();
			if( value == "" ){
				element.val(element.attr('title'));
				element.addClass("basic-form-text-input-labeled");
			}
			
			element.focus(function(){
				var element = $(this);
				if( element.hasClass('basic-form-text-input-labeled') ){
					element.val('');
					element.removeClass('basic-form-text-input-labeled');	
				}
			})
			.blur(function(){
				var element = $(this);
				if( element.val() == "" ){
					element.val(element.attr('title'));
					element.addClass("basic-form-text-input-labeled");
				}
			});
		});
		

	}
});