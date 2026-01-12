const loginform =document.getElementById('login-form');
if(loginform){
    loginform.addEventListener('submit',async(e)=>{
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        console.log(username,password);
        const response = await fetch('http://localhost:8000/api/token/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
          
            body:JSON.stringify({username,password})
        });
        const data = await response.json();
        if(response.ok){
            localStorage.setItem('access_token',data.access);
            localStorage.setItem('refresh_token',data.refresh);
            alert('Login successful');
            window.location.href = '/';
        }else{
            alert('Login failed: ' + (data.detail || 'Unknown error'));
        }
    });
}