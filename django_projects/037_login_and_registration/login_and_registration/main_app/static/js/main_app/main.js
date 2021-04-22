$( document ).ready(function() {
    $('#registration_form').validate({
        rules: {
            new_user_password_check: {
                equalTo: "#new_user_password_input"
              }
        }
    })
    $('#login_form').validate()
})
