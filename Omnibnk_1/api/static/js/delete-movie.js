var id;
function(id){
    url = './movie/' + id.toString() + '/delete/'
    $(location).attr('href', url)
}