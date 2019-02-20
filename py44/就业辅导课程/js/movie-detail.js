


var movieId=$(location).attr("href").split("?")[1].split("=")[1];



var data=movieData.subjects;
var movieDetail='';
data.forEach(function(element){
    if(element.id==movieId){
        movieDetail=element;
    }

});



console.log(movieDetail)


$(".movie-detail").html(
`<h2>${movieDetail.title}<span>(${movieDetail.year})</span></h2>
<img class="movie-img" src="${movieDetail.images.large}" alt="">
<p class="detail">
    <span>导演：<b>${movieDetail.directors[0].name}</b></span>
    <span>主演：<b>${movieDetail.casts[0].name}/${movieDetail.casts[1].name}/${movieDetail.casts[2].name}</b></span>
    <span>类型：<b>${movieDetail.genres}</b></span>
    <span>制片国家：<b>${movieDetail.countries}</b></span>
    <span>评分：<b>${movieDetail.rating.average}</b></span>
</p>`
)

var actorList='';
movieDetail.casts.forEach(function(element){
    actorList+=`<div class="actor-container">
        <img class="actor-img" src="${element.avatars.large}" alt="">
        <text class="actor-title">${element.name}</text>
    </div>`
})

$(".actor-list").html(actorList)

