

$(function(){

	  var scale = 0.65;
	  $('#video').css({ width: $(window).innerWidth() * scale + 'px', height: $(window).innerHeight() * scale + 'px' });

	  // If you want to keep full screen on window resize
	  $(window).resize(function(){
	    $('#video').css({ width: $(window).innerWidth() * scale + 'px', height: $(window).innerHeight() * scale + 'px' });
	  });
	});


$(function(){

	  if(document.getElementsByTagName('audio').length > 0)
			document.getElementById("app-layout").style.backgroundImage = "url(https://catch.shef.ac.uk/circa/public/resources/media/backgrounds/music.jpg)";

	  if(!!document.getElementById('video'))
			document.getElementById("app-layout").style.backgroundImage = "";
			
	});


function changeVisibility(classname){
	var targets = document.getElementsByClassName("circa-class");
	for(var i=0,ll=targets.length;i<ll;i++) targets[i].style.visibility="hidden";

		var targets = document.getElementsByClassName(classname);
	for(var i=0,ll=targets.length;i<ll;i++) targets[i].style.visibility="visible";
};
function setCIRCABackground(key, colour){
	var filen = "";
	if(key=="") return;

	// horrible fix:
	key = key.replace(new RegExp(String.fromCharCode(228),'g'),'&auml;');
	key = key.replace(new RegExp(String.fromCharCode(246),'g'),'&ouml;');
	key = key.replace(new RegExp(String.fromCharCode(229),'g'),'&aring;');

	switch(key) {
		case "Entertainment":
		filen = "url('https://catch.shef.ac.uk/circa/public/resources/media/backgrounds/entertainment.jpg')";
		break;
		case "Recreation":
		filen = "url('https://catch.shef.ac.uk/circa/public/resources/media/backgrounds/recreation.jpg')";
		break;
		case "Childhood":
		filen = "url('https://catch.shef.ac.uk/circa/public/resources/media/backgrounds/childhood.jpg')";
		break;

		case "greybc":
		filen = "url('https://convertingcolors.com/plain-383838.svg')";
		break;



		default:
		filen = "";
		break;
	}

	document.getElementById("app-layout").style.backgroundImage = filen;
	document.getElementById("app-layout").style.backgroundRepeat = "no-repeat";

	var targets = document.getElementsByClassName("current-topic-input");
	for(var i=0,ll=targets.length;i<ll;i++) targets[i].value=key;
		setCIRCABackgroundColour(colour);

};
function setCIRCABackgroundColour(bc){
	if(bc=="") return;
	var targets = document.getElementsByClassName("dropup");
	for(var i=0,ll=targets.length;i<ll;i++) { 
		targets[i].classList.remove("bg-warning","bg-info","bg-danger"); 
		targets[i].classList.add(bc);
	};
	var targets = document.getElementsByClassName("circa-button");
	for(var i=0,ll=targets.length;i<ll;i++){ 
		targets[i].classList.remove("bg-warning","bg-info","bg-danger"); 
		targets[i].classList.add(bc);	
	};
	var targets = document.getElementsByClassName("dropdown-menu");
	for(var i=0,ll=targets.length;i<ll;i++){
		targets[i].classList.remove("bg-warning","bg-info","bg-danger"); 	
		targets[i].classList.add(bc);
	};
	var targets = document.getElementsByClassName("current-colour-input");
	for(var i=0,ll=targets.length;i<ll;i++) targets[i].value=bc;	
};

function setInstructions(){
	document.getElementById('media-title').innerHTML = "Please select from photographs, video or music, or choose another theme";
}


function showDiv(classname,current_background) {




		var display = document.getElementById(classname).style.display;
		if (display == "none") {
			document.getElementById(classname).style.display = "block";
		}
		else {
			document.getElementById(classname).style.display = "none"
		}

		if (classname == 'closeButton'){
			document.getElementById('music').style.display = "none";
			document.getElementById('yout').style.display = "none";
			document.getElementById('vid').style.display = "none";
			document.getElementById('image_ta').style.display = "none";
			document.getElementById('image_tb').style.display = "none";
			document.getElementById('image_tc').style.display = "none";
		}

		var display2 = document.getElementById('media-title').style.display;
		if (display2 == "none") {
			document.getElementById('media-title').style.display = "block";
			setCIRCABackground(current_background,'bg-warning'); 
			document.getElementById('md').style.display = "block";
			document.getElementById('closeButton').style.display = "none";

		}
		else {
			document.getElementById('media-title').style.display = "none"
			setCIRCABackground('greybc','bg-warning'); 
			document.getElementById('md').style.display = "none"
			document.getElementById('closeButton').style.display = "block";


		}



	}


    jQuery('.youtube-player').each(function(){
    jQuery(this).on('click', '.youtube-link-start', function(){
        jQuery(this).parent().addClass('active');

        var loc = $(this).siblings('iframe').attr('src');
        var startloc = loc + "?autoplay=1";
        $(this).siblings('iframe').attr('src', startloc);
    });

    jQuery(this).on('click', '.youtube-link-stop', function(){
        jQuery(this).parent().removeClass('active');

        var loc = $(this).siblings('iframe').attr('src');
        var stoploc = loc.replace("?autoplay=1", "");
        $(this).siblings('iframe').attr('src', stoploc);
    });
});
