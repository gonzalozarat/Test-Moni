$(document).ready(()=>{
    let url_loan = $("#new-loan-script").data("url-loan")
    document.getElementById('cargando').style.display = 'none';
    document.getElementById('aceptado').style.display = 'none';
    document.getElementById('rechazado').style.display = 'none';
    document.getElementById('err').style.display = 'none';

    let setErrorForm = (error) =>{
        $(".error").html(error)
    }

    let applyLoan=()=>{
        let first_name = $("#first_name_id").val()
        let last_name = $("#last_name_id").val()
        let email = $("#email_id").val()
        let dni = $("#dni_id").val()
        let gender = $("#gender_id").val()
        let amount = $("#amount_id").val()
        var $crf_token = $("#new-loan-script").data("csrftoken")
        let request = $.ajax({
			type: "POST",
            headers:{"X-CSRFToken": $crf_token},
            url: url_loan,
            data:{
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "dni": dni,
                "gender": gender,
                "monto": amount                
            }
        });
        request.done((response)=>{
            console.log(response)

            if(response.status===1){
                document.getElementById('cargando').style.display = 'none';
                document.getElementById('aceptado').style.display = 'block';


            }else if (response.status==2){
                document.getElementById('cargando').style.display = 'none';
                document.getElementById('rechazado').style.display = 'block';

            }else{
                document.getElementById('cargando').style.display = 'none';
                document.getElementById('err').style.display = 'block';

            }
            setErrorForm("")
        })
        request.fail((response)=>{          
            let text_error = ""
            let errors = response.responseJSON
            for(field in errors){
                text_error += field + " " + errors[field] +"<br>"
            }
            setErrorForm(text_error) 
        })
    }

    
    $(".btn-loan").click((event)=>{
        document.getElementById('ocultar').style.display = 'none';
        document.getElementById('cargando').style.display = 'block';
        event.preventDefault();   
        applyLoan()
    })
})