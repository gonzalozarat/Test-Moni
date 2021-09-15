$(document).ready(()=>{
    let url_loans = $("#list-loan-script").data("url-loan")
    let loan_template = document.querySelector("#row-loan");
    let page = 1   
    
    let getLoans=()=>{
        let request = $.ajax({
			type: "GET",
            url: url_loans,
            data:{
                page:page
            }
        });
        request.done((response)=>{
            
            let loans = response
            console.log(loans)
            let loan, copy_loan_template
            
            if(loans.length>0){
                $(".list-empty").addClass("ho")
                $(".list-filled").removeClass("ho")
                $("table tbody").html("")

                for(i in loans){
                    loan = loans[i]
                    loan_template.content.querySelector(".row-loan").id = loan["id"]
                    loan_template.content.querySelector(".first-name").textContent = loan["first_name"]
                    loan_template.content.querySelector(".last-name").textContent = loan["last_name"]
                    loan_template.content.querySelector(".dni").textContent = loan["dni"]
                    loan_template.content.querySelector(".gender").textContent = loan["gender_name"]
                    loan_template.content.querySelector(".email").textContent = loan["email"]
                    loan_template.content.querySelector(".email").href = "mailto:"+loan["email"]
                    loan_template.content.querySelector(".amount").textContent = loan["monto"]
                    loan_template.content.querySelector(".status").textContent = loan["status_name"][1]
                    
                    copy_loan_template = document.importNode(
                        loan_template.content,
                        true
                    );
                    $("table tbody").append(copy_loan_template);
                }
            }else{
                $(".list-empty").removeClass("ho")
                $(".list-filled").addClass("ho")
            }
        })
    }
    getLoans()


    $(document).on("click",".btn-delete",function(){
        var confirmacion = window.confirm("¿Esta seguro que desea borrar el pedido de prestamo?")
        if(confirmacion==true){
            let id = $(this).parent().parent().attr('id');
            deleteLoan(id)       
         }
    })

    var $crf_token = $("#list-loan-script").data("csrftoken")
    let deleteLoan=(id)=>{
        let request = $.ajax({
            headers:{"X-CSRFToken": $crf_token},
            type: "DELETE",
            contentType: "application/json",
            url: url_loans+id,
        });
        request.done((response)=>{
            getLoans()
            alert('Se borro correctamente')
        })
        request.fail((response)=>{                  
            alert('Ocurrio un error al borrar')
        })
    }


})