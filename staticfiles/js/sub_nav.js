$(document).ready(function() {

   jQuery.each($('img.sub_nav'), function(){
       var element = $(this);
       add_sub_nav_effect(element);
   });
});


function add_sub_nav_effect(element){
   element.hover(function(){
       var element = $(this);
       element.stop();
       var dims = get_original_dim(element.attr('id'));
       element.animate({
           width: dims[0] + "px",
           height: dims[1] + "px"
       },
        200);
   },
   function(){
       var element = $(this);
       element.stop();
       var dims = get_original_dim(element.attr('id'));
       element.animate({
           width: (dims[0] * .95) + "px",
           height: (dims[1] * .95) + "px"
       },
        200);
   });
}

function get_original_dim(id){
   var element = $('#'+id+'_dim');

   var width = element.attr('width');
   width = width.replace('px', '');

   var height = element.attr('height');
   height = height.replace('px', '');

   var array = new Array(width, height);
   return array;
}