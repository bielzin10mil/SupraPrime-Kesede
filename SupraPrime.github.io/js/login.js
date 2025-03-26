/* Validação do login */
function logar(){
    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    if(login == "admin" && senha == "admin"){
        location.href = "index.html";
        
        /* Mensagens de erro no formulário */
    }else{
        document.getElementById('email-invalid-error').style.display = 'block'
        document.getElementById('senha-invalid-error').style.display = 'block'
    }
}


/* Validação do login */
function logar(){
    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    if(login == "admin" && senha == "admin"){
        location.href = "index.html";
        
        /* Mensagens de erro no formulário */
    }else{
        document.getElementById('email-invalid-error').style.display = 'block'
        document.getElementById('senha-invalid-error').style.display = 'block'
    }
}


function login() {
    
       firebase.auth().signInWithEmailAndPassword("eduardomeira110@gamil.com", "123456").then(response =>{
           console.log('success', response)
       }).catch(error =>{
           console.log('error', error)
       });
    
    //window.location.href = "index.html";

}





