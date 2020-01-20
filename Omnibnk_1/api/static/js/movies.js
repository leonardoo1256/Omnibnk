$(document).ready(function(){
    $.ajax({
      url: '/api/movie',
      method: 'GET'
    }).then(function(data) {
     var row = table.insertRow(table.rows.length);
     for (i = 0; i < data.length; i++) {
            table.innerHTML += "<tr><td>" + data[i].id.toString() + "</td>" + "<td>" + data[i].name + "</td>" + "<td>" + data[i].genre + "</td>" + "<td>" + data[i].director +"</td>" + "<td>" + '<button type="button" onclick="deletemovie('+ data[i].id.toString()+');" class="btn btn-danger">Delete</button> <button type="button" onclick="update('+ data[i].id.toString()+');" class="btn btn-primary">Edit</button>' +"</td>"+ "<td>" +  '<button type="button" onclick="onlyone('+ data[i].id.toString()+');" class="btn btn-secundary" data-toggle="modal" data-target="#myModal">Detail </button>' + "</td>"+"</tr>"
        }
    });
});

var id;
function deletemovie(id){
    del_url = './movie/' + id.toString() + '/delete/';
    $(location).attr('href', del_url);
}

function update(id){
    up_url = './movie/' + id.toString() + '/update/';
    $(location).attr('href', up_url);
}

function onlyone(id){
    $.ajax({
      url: '/api/movie/'+ id.toString() +'/',
      method: 'GET'
    }).then(function(data) {
        moviedetail.innerText = "Movie title: "+data.name + "\nGenre: "+data.genre + "\nDirector: " +data.director
    });
};