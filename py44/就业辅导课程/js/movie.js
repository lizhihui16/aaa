



var data=movieData.subjects;

// var html=`<div class="movie-container">
// <img class="movie-img" src="${}" alt="">
// <text class="movie-title">${}</text>
// </div>`

function processData(arg){
    if(!data){
        return
    }
    var html=``;
    arg.forEach(function(element){
        html+=`<div class="movie-container" data-id="${element.id}">
        <img class="movie-img" src="${element.images.large}" alt="">
        <text class="movie-title">${element.title.length<6?element.title:element.title.slice(0,6)+'...'}</text>
    </div>`
    })
    $(".container").html(html);
}


processData(data)

$(".container").on("click",".movie-container",function(){
    var movieId=$(this).attr("data-id");
    $(location).attr("href","movie-detail.html?movieId="+movieId)
})



