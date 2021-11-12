document.addEventListener('DOMContentLoaded', () => {
    reload_profile_pic()
})

function reload_profile_pic() {
    var rando = Math.floor(Math.random() * 200);
    profile_pic = document.getElementById('profile_pic');
    profile_pic.src = profile_pic.src + "?" + rando;
    console.log(profile_pic.src)    
}