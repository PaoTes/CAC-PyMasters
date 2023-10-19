

const validarFormulario = (event) => {
    event.preventDefault();
    
    const firstname =document.querySelector('#firstname');
    const lastname = document.querySelector('#lastname');
    const email = document.querySelector('#email');
    const consulta = document.querySelector('#consulta');

    let validation = true;

    if(firstname.value===''){
      
        validation=false;
        alert('Por favor, ingresa tu nombre.');
    }
    if(lastname.value===''){
        validation=false;
        alert('Por favor, ingresa tu apellido.');
    }

    if(email.value===''){
        
        validation=false;
        alert('Por favor, ingresa tu email.');
    }

    if(consulta.value===''){
        
        validation=false;
        alert('Por favor, ingresa tu consulta.');
    }
    

    if(validation){
   
        let data = {
            'firstname': firstname.value,
            'lastname': lastname.value,
            'email': email.value,
            'consulta': consulta.value,
        }
        localStorage.setItem('user',JSON.stringify(data));
    }else{
        return false;
    }
}

formRegister.addEventListener('submit', validarFormulario);

console.log('Accediendo al localStorage');
let user = JSON.parse(localStorage.getItem('user'));
console.log(typeof(user));

console.log(`Nombre enviado: ${user.firstname}`);
console.log(`Apellido enviado: ${user.lastname}`);
console.log(`email enviado: ${user.email}`);
console.log(`Consulta enviada: ${user.consulta}`);
