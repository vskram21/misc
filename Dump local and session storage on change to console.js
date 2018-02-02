window.addEventListener('storage', function(e){
    for (var i = 0; i < localStorage.length; i++){
    console.log(localStorage.getItem(localStorage.key(i)));
}
    for (var i = 0; i < sessionStorage.length; i++){
    console.log(sessionStorage.getItem(sessionStorage.key(i)));
}
});
