
function runDropBoxSetup(board){
	
$(function(){
	var dropbox = $('#dropbox'),
		message = $('.message', dropbox);

	
	dropbox.filedrop({
		clearBox: false,
		maxfiles: 25,
    	maxfilesize: 50,
    	paramname: 'file',
		url: '/postFile?script_name=' + script_name,

		uploadFinished:function(i,file,response){
			$.data(file).addClass('done');
			console.log(response);
			
			// var parsed = $.parseJSON(response.data);
			// response.properties = parsed;
			// response.file_data = parsed
			// nodes.push(response);
			//placeNodeAtFront(response);
			write_output(response)

			message.show();
			$(".preview").remove();

			//win.focus();

		},

    	error: function(err, file) {
			switch(err) {
				case 'BrowserNotSupported':
					showMessage('Your browser does not support HTML5 file uploads!');
					break;
				case 'TooManyFiles':
					alert('Too many files! Please select ' + this.maxfiles + ' at most!');
					break;
				case 'FileTooLarge':
					alert(file.name+' is too large! Please upload files up to ' + this.maxfilesize + '.');
					break;
				default:
					break;
			}
		},
		dragEnter: function(){
			if (this.clearBox == true){
				$("#output").html("");
			}
		},
		afterAll: function(){
			this.clearBox = true;
		},
		// Called before each upload is started
		beforeEach: function(file){
//			if(!file.type.match(/^image\//)){
//				alert('Only images are allowed!');

				// Returning false will cause the
				// file to be rejected
//				return false;
//			}
		},

		uploadStarted:function(i, file, len){
			createImage(file);
		},

		progressUpdated: function(i, file, progress) {
			$.data(file).find('.progress').width(progress);
		}

	});

	var template = '<div class="preview">'+
						'<span class="imageHolder">'+
							'<img />'+
							'<span class="uploaded"></span>'+
						'</span>'+
						'<div class="progressHolder">'+
							'<div class="progress"></div>'+
						'</div>'+
					'</div>';


	function createImage(file){

		var preview = $(template),
			image = $('img', preview);

		var reader = new FileReader();

		image.width = 25;
		image.height = 25;

		reader.onload = function(e){

			// e.target.result holds the DataURL which
			// can be used as a source of the image:

			image.attr('src',e.target.result);
			//image.attr('onerror', "this.src='/img/unknown.png';");

		};

		// Reading the file as a DataURL. When finished,
		// this will trigger the onload function above:
		reader.readAsDataURL(file);

		message.hide();
		preview.appendTo(dropbox);

		// Associating a preview container
		// with the file, using jQuery's $.data():

		$.data(file,preview);
	}

	function showMessage(msg){
		message.html(msg);
	}

});

}