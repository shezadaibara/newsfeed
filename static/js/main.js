!function ($) {
	$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	
	$(function() {
		   $('a#search_button').bind('click', function() {
			   alert('hi');
		     $.getJSON($SCRIPT_ROOT + '/_feeds', {
		       keyword: $('input[name="keyword"]').val(),
		     }, function(data) {
		       $("#result").text(data.keyword);
		     });
		     return false;
		   });
		 });
	
}(window.jQuery);


	 
