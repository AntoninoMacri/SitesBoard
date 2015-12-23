//Aggiunto controllo javascript in tutte le pagine

//COSA NON HO FATTO:controllo della correttezza della data di nascita inserita dentro la pagina registration.html
//NOTA BENE: Per la Data preferirei che venissero inseriti 3 campi input per giorno,mese ed anno er evitare problemi di forma es: dd.mm.yyyy oppure mm.dd.yyyy, vincolando l'utente ad un solo modo valido per l'inserimento dei dati (dd mm yyyy)
//NOTA BENE2: controllare che il regex usato sia corretto per tutte le possibili e-mail(intanto controllare solo che le email che abbiamo siano tutte accettate)

//COSA HO FATTO
//AZIONI
//1)controllo campi non vuoti
//2)controllo campo password almeno di 8 caratteri
//3)controllo campo password=reinserisci la password
//4)controllo email valida tramite regex

//AGGIUNTE DI CODICE (nelle pagine HTML DI DAVIDE E JACK)
//IN TUTTI I FILE DI DAVIDE
//<script type="text/javascript" src="../javascript/control.js"></script> nell'head

//home.html, pass_recovery.html e registration.html
//onsubmit="return loginControl()" dentro tag form di login
//name="formLogin" dentro tag form di login
//id="logErr" dentro il tag p del messaggio di errore

//pass_recovery.html
//onsubmit="return recoveryContol()" dentro tag form
//name="pass_recovery" dentro tag form di login
//id="recErr" dentro il tag p del messaggio di errore di recupero password

//registration.html
//onsubmit="return registrationControl()" dentro tag form
//name="registration" dentro tag form di login
//id="regErr" dentro il tag p del messaggio di errore

//profile_change.html
//<script type="text/javascript" src="../../javascript/control.js"></script> nell'head
//onsubmit="return profileChangeControl()" dentro tag form
//name="profileChange" dentro tag form
//id="name","surname","age","email" aggiunti a tutti i tag input della form
//tutti i value=" " dentro i tag della form sono stati sostituiti con value=""; per poter controllare se il campo era stato lasciato vuoto dall'utente
function profileChangeControl(){
    var x=document.forms["profileChange"]["name"].value;
    if (x == null || x == "") {
        document.getElementById("underline").style.color='red';
        document.getElementById("underline").innerHTML = "*campo nome vuoto";
        return false;
    }
    var x=document.forms["profileChange"]["surname"].value;
    if (x == null || x == "") {
        document.getElementById("underline").style.color='red';
        document.getElementById("underline").innerHTML = "*campo cognome vuoto";
        return false;
    }
    var x=document.forms["profileChange"]["age"].value;
    if (x == null || x == "") {
        document.getElementById("underline").style.color='red';
        document.getElementById("underline").innerHTML = "*campo eta&#768; vuoto";
        return false;
    }
    var re =/^[0-9]+$/;
    if(!re.test(x)){
      document.getElementById("underline").style.color='red';
      document.getElementById("underline").innerHTML = "eta&#768; non valida";
      return false;
    }
    if( x<=0 || x>140){
      document.getElementById("underline").style.color='red';
      document.getElementById("underline").innerHTML = "le eta&#768; accettate sono comprese tra 1 e 140";
      return false;
    }
    var x=document.forms["profileChange"]["username"].value;
    if (x == null || x == "") {
        document.getElementById("underline").style.color='red';
        document.getElementById("underline").innerHTML = "*campo username vuoto";
        return false;
    }
    var x=document.forms["profileChange"]["email"].value;
    if (x == null || x == "") {
        document.getElementById("underline").style.color='red';
        document.getElementById("underline").innerHTML = "*campo email vuoto";
        return false;
    }    
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    if(!re.test(x)){
      document.getElementById("underline").style.color='red';
      document.getElementById("underline").innerHTML = "*Email non valida";
      return false;
    }
}

function registrationControl(){ //controllare validita' della data nascita
    var x=document.forms["registration"]["reg_name"].value;
    if (x == null || x == "") {
        document.getElementById("regErr").innerHTML = "*campo nome vuoto";
        return false;
    }
    x=document.forms["registration"]["reg_surname"].value;
    if (x == null || x == "") {
        document.getElementById("regErr").innerHTML = "*campo cognome vuoto";
        return false;
    }
    //caso data nascita vuoto->da sostituire
    x=document.forms["registration"]["reg_eta"].value;
    if (x == null || x == "") {
        document.getElementById("regErr").innerHTML = "*campo data nascita vuoto";
        return false;
    }
    x=document.forms["registration"]["reg_username"].value;
    if (x == null || x == "") {
        document.getElementById("regErr").innerHTML = "*campo username vuoto";
        return false;
    }
    x=document.forms["registration"]["reg_email"].value;
    if (x == null || x == "") {
        document.getElementById("regErr").innerHTML = "*campo Email vuoto";
        return false;
    }
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    if(!re.test(x)){
      document.getElementById("regErr").innerHTML = "*Email non valida";
      return false;
    }
    x=document.forms["registration"]["reg_pass"].value;
    if (x == null || x == "") {
        document.getElementById("regErr").innerHTML = "*campo password vuoto";
        return false;
    }    
    if( x.length<'8'){
        document.getElementById("regErr").innerHTML = "*campo password deve contenere almeno 8 caratteri";
        return false;
    }
    var y=document.forms["registration"]["reg_re_pass"].value;
    if (y == null || y == "") {
        document.getElementById("regErr").innerHTML = "*campo ripeti la password vuoto";
        return false;
    }
    if( y.length<'8'){
        document.getElementById("regErr").innerHTML = "*campo ripeti la password deve contenere almeno 8 caratteri";
        return false;
    }
    if(x!=y){
        document.getElementById("regErr").innerHTML = "*i campi pssword e ripeti password devono coincidere";
        return false;
    }
}

function recoveryContol(){
    var x=document.forms["pass_recovery"]["recover_name"].value;
    if (x == null || x == "") {
        document.getElementById("recErr").innerHTML = "*campo nome vuoto";
        return false;
    }
    x=document.forms["pass_recovery"]["recover_surname"].value;
    if (x == null || x == "") {
        document.getElementById("recErr").innerHTML = "*campo cognome vuoto";
        return false;
    }
    x=document.forms["pass_recovery"]["recover_email"].value;
    if (x == null || x == "") {
        document.getElementById("recErr").style.color='red';
        document.getElementById("recErr").innerHTML = "*campo Email vuoto";
        return false;
    }
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    if(!re.test(x)){
      document.getElementById("recErr").innerHTML = "*Email non valida";
      return false;
    }
}

function loginControl(){
    var x=document.forms["formLogin"]["login_user"].value;
    if (x == null || x == "") {
        document.getElementById("logErr").innerHTML = "*campo username vuoto";
        return false;
    }
    x=document.forms["formLogin"]["login_password"].value;
    if (x == null || x == "") {
        document.getElementById("logErr").innerHTML = "*campo password vuoto";
        return false;
    }
    if( x.length<'8'){
        document.getElementById("logErr").innerHTML = "*campo password deve contenere almeno 8 caratteri";
        return false;
    }
}
