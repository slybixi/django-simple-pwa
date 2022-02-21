/**
 * DaisyJS Demo Script
 * by Waren Gonzaga
 */

// in vanilla javascript

/*document.addEventListener('DOMContentLoaded', function () {
  daisyjs(document.getElementById('momoland'), {
    dotColor: '#fff',
	density: 7000,
	particleRadius: 4,
	minSpeedX: 0.4,
	lineWidth: 0.7,
	proximity: 70,
	parallax:true,
	parallaxMultiplier: 10,
    lineColor: '#ddd'
  });
}, false); */

// as jquery plugin

 $(document).ready(function() {
  $('#momoland').daisyjs({
    dotColor: '#fff',
	density: 7000,
	particleRadius: 4,
	minSpeedX: 0.4,
	lineWidth: 0.7,
	proximity: 70,
	parallax:true,
	parallaxMultiplier: 10,
    lineColor: '#ddd'
  });
}); 
