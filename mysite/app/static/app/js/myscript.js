$(".dropdown-menu li a").click(function(){
	var selText = $(this).text();
    $(this).parents('.dropdown').find('.dropdown-toggle').html(selText+'<span class="caret"></span>');
});