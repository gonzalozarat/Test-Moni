$(document).ready(()=>{
        let url_genders = $("#list-genders-script").data("url-genders")
    
        let fillGenders=()=>{
            let request = $.ajax({
                type: "GET",
                url: url_genders,
            });
            request.done((response)=>{
                let gender
                for(i in response){
                    gender = response[i]
                    console.log(gender)
                    $("#gender_id").append(new Option(gender.name, gender.slug_name));
                }
            })
        }
        fillGenders()
    })