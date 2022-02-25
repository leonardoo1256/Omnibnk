function Authenticate() {
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    user = $('#username').val();
    password = $('#password').val();
    $.ajax({
        type: 'POST',
        url:"/api/authenticate",
        headers: {"X-CSRFToken": $crf_token},
        data: JSON.stringify({ 'username': user, 'password': password}),
        contentType: "application/json; charset=utf-8",
        datatype: "json",
        success: function(data) {
            if (data == "Login exitoso") {
                alert('Correcto');
                $(location).attr('href', './movies')
            }
            else {
            console.log('Error');
            alert('Datos incorrectos. Intente de nuevo.');
            $('#username').val('');
            $('#password').val('');
            }
        },
        failure: function (errMsg) {
            alert(errMsg);
        }
    });
}

function Create() {
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    username = $('#username').val();
    password = $('#password').val();
    $.ajax({
        type: 'POST',
        url:"./newuser",
        headers: {"X-CSRFToken": crf_token},
        data: JSON.stringify({ 'username': username, 'password': password}),
        contentType: "application/json; charset=utf-8",
        datatype: "json",
        success: function(data) {
        console.log(data);
                alert('User created successfully');
                $(location).attr('href', 'accounts/login/')
        },
        error: function (errMsg) {
            alert('Try another username');
                $('#username').val('');
                $('#password').val('');
        }
    });
}

