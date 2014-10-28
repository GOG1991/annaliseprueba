$(function(){
	var n = parseInt($('#txtemp').val());
	$('#txtVacante').val(n);
	$('#ok').hide();

	$("#frmVacantes").validate({
        rules: {
            name: "required",
            last_name:'required',
            address:'required',
            email:{required:true,email:true},
            gender:'required',
            job_application:'required',
            captcha_1:'required'
            
        },
        messages: {
            name: "Debes ingresar su nombre.",
            last_name:'Debes ingresar tus apellidos',
            address:'Debes ingresar tu dirección',
            email:"Debes ingresar un correo eléctronico valido",
            gender:"Debes ingresar el género masculino o femenino",
            job_application:"Debes adjuntar el archivo de tu curriculum",
            captcha_1:"Debes ingresar correctamene el código"

        },  
        debug:true,
         submitHandler: function(form){
         	form.submit();

         },
     });

         /*  $.ajax({
		        type: $(form).attr('method'),
		        url: $(form).attr('action'),
		        data: $(form).serialize(),
		        //dataType : 'text',
		        beforeSend:function(){
		        	//$('#spn-msj').html('<i class="fa fa-spinner fa-spin fa-2x"></i>');
				},
				success:function(response){
					//$('#spn-msj').removeClass('col-xs-1 col-xs-offset-9');
					//$('#spn-msj').addClass('col-xs-10 alert alert-success');
					//$('#spn-msj').html(response);
					alert(response);

				},
				error:function(xhr,estado,error){
						alert(error+' '+estado);
				},

				complete:function(xhr){
					
				},
				timeout:10000
		    });
    
    	return false; // required to block normal submit since you used ajax
        }

     });*/

	

});