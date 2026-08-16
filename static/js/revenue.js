setInterval(() => {
    let rev = 18450; // هذا المنطق نحطوه لاحقاً من الـ Database
    document.getElementById('liveRevenue').innerText = '$' + (rev + Math.floor(Math.random()*100)).toLocaleString();
}, 3000);