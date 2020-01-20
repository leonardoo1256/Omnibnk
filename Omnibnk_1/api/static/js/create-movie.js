function Create() {
    genre = $('#genre').val();
    director = $('#director').val();
    movietitle = $('#movie-title').val();
    $.ajax({
        type: 'POST',
        url:"api/movie/",
        data: JSON.stringify({'name': movietitle, 'genre': genre, 'director': director}),
        contentType: "application/json; charset=utf-8",
        datatype: "json",
        success: function(data) {
                alert('Movie created successfully');
                $(location).attr('href', './movies')
        },
        error: function (errMsg) {
            alert('Try another movie title');
                $('#author').val('');
                $('#director').val('');
                $('#movie-title').val('');
        }
    });
}
var id;
function Update(id) {
    genre = $('#genre').val();
    director = $('#director').val();
    movietitle = $('#movie-title').val();
    $.ajax({
        type: 'PATCH',
        url:"/api/movie/" + id.toString()+'/',
        data: JSON.stringify({'name': movietitle, 'genre': genre, 'director': director}),
        contentType: "application/json; charset=utf-8",
        datatype: "json",
        success: function(data) {
                alert('Movie updated');
                window.location.replace("/movies");
        },
        error: function (errMsg) {
            console.log(genre);
            console.log(director);
            console.log(movietitle);
            alert('Try another movie title');
                $('#author').val('');
                $('#director').val('');
                $('#movie-title').val('');
        }
    });
}


