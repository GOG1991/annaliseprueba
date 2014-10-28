var btnSug;
var btnQja;
$(function(){

	$.validator.addMethod("dateFormat",
    function(value, element) {
          return value.match(/^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])[ / .]([1-9]|0[1-9]|1[0-2])[ / .](1[9][0-9][0-9]|2[0][0-9][0-9])$/);
    },
    "Please enter a date in the format dd-mm-yyyy.");

	$('#spn-msj').removeClass('alert alert-success');
	$('#spn-msj').html('');
	$("#frmInv").validate({
        rules: {
            nombres: "required",
            apPaterno:"required",
            apMaterno:"required",
            genero:"required",
            //fechNacimiento:{required:true,date:true},
            fechNacimiento:{
            	dateFormat:true,
            },
            pais:"required",
            estadoPais:"required",
            ciudad:"required",
            estadoCivil:"required",
            curp:{required:true,minlength: 18},
            imss:{required:true,minlength:11},
            numHijos:"required",
            colonia:"required",
            calle:"required",
            numExterior:"required",
            //numInterior:"required",
            telCasa:'required',
            celular:{required:true,minlength:10},
            contPrim:"required",
            contSec:"required"
            
        },
        messages: {
            nombres: "Debes ingresar tu nombre",
            apPaterno:"Debes ingresar el apellido paterno",
            apMaterno:"Debes ingresar el apellido materno",
            genero:"Debes ingresar el genero masculino o femenino",
            fechNacimiento:"Debes ingresar una fecha valida ejemplo 29/12/1970",
            pais:"Debes ingresar el país de donde procedes",
            estadoPais:"Debes ingresar el estado de tu ciudad",
            ciudad:"Debes ingresar la ciudad de residencia",
            estadoCivil:"Debes ingresar tu estado civil",
            curp:"La curp debe tener 18 caracteres",
            imss:"El número de seguro social es obligatorio de mínimo 11 digitos",
            numHijos:"Debes ingreasar el numero de hijos que tienes",
            colonia:"Debes ingresar la colonia de tu domicilio",
            calle:"Debes ingresar el nombre de la calle",
            numExterior:"Debes ingresar el número exterior de tu domicilio",
            //numInterior:"Debes ingresar el número interior de tu domicilio"	,
            telCasa:"El número de télefono de casa es obligatorio y debe tener máximo 15 digitos",
            celular:"Debes ingresar tu número de celular con mínimo 10 dígitos",
            contPrim:"Debes ingresar la pricipal forma de contactarte",
            contSec:"Debes ingresar la segunda forma de contactarte"

        },  
        debug:true,
         submitHandler: function (form) {
		    $.ajax({
		        type: $(form).attr('method'),
		        url: $(form).attr('action'),
		        data: $(form).serialize(),
		        //dataType : 'text',
		        beforeSend:function(){
		        	$('#spn-msj').html('<i class="fa fa-spinner fa-spin fa-2x"></i>');
				},
				success:function(response){
					$('#spn-msj').removeClass('col-xs-1 col-xs-offset-9');
					$('#spn-msj').addClass('col-xs-10 alert alert-success');
					$('#spn-msj').html(response);

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
     });

	$(window).scroll(function(){
   		if ($(this).scrollTop() > 50) {
        	$('.lnkUp').fadeIn();
   		} 

   		else 
   		{
        	$('.lnkUp').fadeOut();
  	 	}

	});

	btnSug = $('#btnFormSug');
	btnQja = $('#btnQja');
	btnSug.on('click',procForm);
	btnQja.on('click',procForm);	

	$('#lnkUp').on('click',function(){
		$("html, body").animate({ scrollTop: 0 }, 300);
   		return false;
	});

});

function procForm(e){
	e.preventDefault();
	$('#spn-msg').html('<i class="fa fa-spinner fa-spin fa-2x"></i>');

	if($(this).attr('id') === 'btnQja'){ // revisa si fue el formulario de sugerencias
			$.post('.',$('#frmSug').serialize(),function(response){
				window.setTimeout(function(){
					showMsj(response);
				},10);			
		})

		.fail(function(){
			alert('Error! Consulte a su proveedor de software');
		});
	}

	else
	{
		$.post('/contacto/',$('#frmContacto').serialize(),function(response){
		window.setTimeout(function(){
				showMsj(response);
			},300);
		})

		.fail(function(){
			alert('Error! Consulte a su proveedor de software');
		});

	}
	
}	

function showMsj(datos){
	
	$('#error-msj1').html(datos.msj);
	$('#error-msj1').removeClass('alert alert-warning alert-danger alert-success');

	switch(parseInt(datos.status)){

		case 1:
				$('#error-msj1').addClass('alert alert-success');
				break;

		case 2:
				$('#error-msj1').addClass('alert alert-warning');
				break;

		case 3:
				$('#error-msj1').addClass('alert alert-danger');
				break;

		default:
				$('#error-msj1').addClass('alert alert-danger');
				break;



	}

	$('#error-msj1').show('slow');

	$('#spn-msg').html(' ');

}

function sugerencias(e){
	e.preventDefault();
	$.post('.',$('#frmSug').serialize(),function(response){
		alert(response);
	})

	.fail(function(){
		alert('Error! Consulte a su proveedor de software');
	});

}