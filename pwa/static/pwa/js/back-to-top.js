$(window).on("scroll",function(){
	var scrollTop=$(window).scrollTop();
	if(scrollTop>500) {
		$('#back-to-top').addClass('show');
	}else{
		$('#back-to-top').removeClass('show');
	}

$('#back-to-top').on('click',function(e){
	e.preventDefault();
	$('html,body').stop(true).animate({
		scrollTop:0
	},800);
});
});