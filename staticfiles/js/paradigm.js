
var paradigm = {
};

// Filter Definition
(function(){
	
	var initializeHover = function(that, index){
		$("#" + that.id + "_" + index).hover(
				function(){
					if(that.index == index)
						return false;
					
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
					if(that.index == index)
						return false;
					
					// Wait to send the icon back in case the cursor is about to go to a different one
					that.timeout[index] = setTimeout(function(){
						$("#" + that.id).animate({
						    marginLeft: that.offsets[that.index] + "px"
						  }, 200 );
					},300);			
		});
	}
	
	
	paradigm.Filter = function(id, index, offsets){
		this.id = id;
		this.index = index;
		this.offsets = offsets;
		
		this.timeout = {};
	}
	
	paradigm.Filter.prototype.initSelector = function(index, initClick, callback){
		initializeHover(this, index);
		
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
})();
