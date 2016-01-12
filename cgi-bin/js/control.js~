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
//onkeypress="return loginControl()" dentro tag form di login
//name="formLogin" dentro tag form di login
//id="logErr" dentro il tag p del messaggio di errore

//pass_recovery.html
//onsubmit="return recoveryControl()" dentro tag form
//onkeypress="return recoveryControl()" dentro tag form di login
//name="pass_recovery" dentro tag form di login
//id="recErr" dentro il tag p del messaggio di errore di recupero password

//registration.html
//onsubmit="return registrationControl()" dentro tag form
//onkeypress="return registrationControl()" dentro tag form di login
//name="registration" dentro tag form di login
//id="regErr" dentro il tag p del messaggio di errore

//profile_change.html
//<script type="text/javascript" src="../../javascript/control.js"></script> nell'head
//onsubmit="return profileChangeControl()" dentro tag form
//name="profileChange" dentro tag form
//id="name","surname","age","email" aggiunti a tutti i tag input della form
//tutti i value=" " dentro i tag della form sono stati sostituiti con value=""; per poter controllare se il campo era stato lasciato vuoto dall'utente

//profile_change.cgi
//aggiunto id="username" al tag input
//onkeypress="return profileChangeControl()" dentro tag form di login

//appunto di codice: document.getElementById("recErr").style.color='red';
/*
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
}*/

//profileChangeControl
function profileChangeControl(){
    document.getElementById("underline").style.color='red';
    var risultato=checkName("name","underline");
    risultato=risultato && checkSurname("surname","underline");
    risultato=risultato && checkAge("age","underline");
    risultato=risultato && checkUser("username","underline");
    risultato=risultato && checkEmail("email","underline");
    return risultato;

}


//registrationControl
function registrationControl(){
    var risultato=checkName("reg_name", "regErr");
    risultato=risultato && checkSurname("reg_surname", "regErr");
    risultato=risultato && checkData("reg_year", "reg_month", "reg_day", "regErr");
    risultato=risultato && checkUser("reg_username", "regErr");
    risultato=risultato && checkEmail("reg_email", "regErr");
    risultato=risultato && checkPassword("reg_pass", "regErr");
    risultato=risultato && checkConfirmPassword("reg_pass", "reg_re_pass" ,"regErr");

    //scrollo la pagina poichè la form è troppo lunga e c'è il rischio che l'utente non veda il suggerimento dell'errore
    var w = window.screen.width;
    var h = window.screen.height;
    window.scrollTo(3/5*w, 5/12*h);
    return risultato;
}


//recoveryControl
function recoveryControl(){
    var risultato=checkName("recover_name", "recErr");
    risultato=risultato && checkSurname("recover_surname", "recErr");
    risultato=risultato && checkEmail("recover_email", "recErr");
    return risultato;
}


//loginControl
function loginControl(){
    var risultato=checkUser("login_user","logErr");
    risultato=risultato && checkPassword("login_password","logErr");
    return risultato;
}



//FUNZIONI DI CONTROLLO
function checkUser(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo username vuoto";
        b=false;
    }
    return b;
}

function checkPassword(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo password vuoto";
        b=false;
    }
    if(b && tag.value.length<'8'){
        document.getElementById(err).innerHTML = "*campo password deve contenere almeno 8 caratteri";
        b=false;
    }
    return b;
}

function checkConfirmPassword(pass, conf_pass, err){
    var tag= document.getElementById(pass);
    var tag2= document.getElementById(conf_pass);
    var b=true;
    if (tag2.value == null || tag2.value == "") {
        document.getElementById(err).innerHTML = "*campo Ripeti la Password vuoto";
        b=false;
    }
    if(b && tag2.value.length<'8'){
        document.getElementById(err).innerHTML = "*campo Ripeti la Password deve contenere almeno 8 caratteri";
        b=false;
    }
    if(b && tag.value!=tag2.value){
        document.getElementById(err).innerHTML = "*campo Password deve coincidere con il campo Ripeti la Password";
        b=false;
    }


    return b;
}


function checkName(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Nome vuoto";
        b=false;
    }
    return b;
}

function checkSurname(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Cognome vuoto";
        b=false;
    }
    return b;
}

function checkEmail(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Email vuoto";
        b=false;
    }
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    if(b && !re.test(tag.value)){
        document.getElementById(err).innerHTML = "*Email non valida";
        b=false;
    }
    return b;
}

function checkAge (par, err) {
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo eta&#768; vuoto";
        b=false;
    }
    var re=/^[0-9]{2,3}$/;
    if(b && !re.test(tag.value)){
        document.getElementById(err).innerHTML = "*eta&#768; campo numerico di massimo 3 cifre";
        b=false;
    }
    if(b && tag.value<18){
        document.getElementById(err).innerHTML = "*l'iscrizione è permessa solo hai maggiorenni";
        b=false;
    }
    if(b && tag.value>110){
        document.getElementById(err).innerHTML = "*l'iscrizione deve essere inferiore a 110";
        b=false;
    }
    return b;
}

function checkData(y, m, d, err){
    var tagy= document.getElementById(y);
    var b=true;
    if (tagy.value == null || tagy.value == "") {
        document.getElementById(err).innerHTML = "*campo Anno di Nascita vuoto";
        b=false;
    }
    //controllo che l'anno sia un numero
    var re=/^[0-9]{4}$/;
    if(b && !re.test(tagy.value)){
        document.getElementById(err).innerHTML = "*Anno deve contenere 4 cifre";
        b=false;
    }
    //controllo che l'anno sia successivo al 1900
    if(b && tagy.value<1900){
        document.getElementById(err).innerHTML = "*anno deve essere successivo al 1900";
        b=false;
    }
    var bisestile=false;
    if(tagy.value%4==0){
        bisestile=true;
    }

    var tagm= document.getElementById(m);
    if (b && (tagm.value == null || tagm.value == "")) {
        document.getElementById(err).innerHTML = "*campo Mese di Nascita vuoto";
        b=false;
    }
    //controllo che il mese sia un numero
    var re=/^[0-9]{1,2}$/;
    if(b && !re.test(tagm.value)){
        document.getElementById(err).innerHTML = "*mese deve contenere 1 o 2 cifre";
        b=false;
    }
    if(b && tagm.value>12){
        document.getElementById(err).innerHTML = "*mese deve contenere un valore da 1 a 12";
        b=false;
    }

    var tagd= document.getElementById(d);
    if (b && (tagd.value == null || tagd.value == "")) {
        document.getElementById(err).innerHTML = "*campo Giorno di Nascita vuoto";
        b=false;
    }
    //controllo che il giorno sia un numero
    var re=/^[0-9]{1,2}$/;
    if(b && !re.test(tagd.value)){
        document.getElementById(err).innerHTML = "*giorno deve contenere 1 o 2 cifre";
        b=false;
    }
    if(b && tagd.value>31){
        document.getElementById(err).innerHTML = "*giorno deve contenere un valore da 1 a 31";
        b=false;
    }
    if(b && tagd.value>28 && tagm.value==2){
        if(tagd.value==29)
        {
            if(!bisestile)
                { 
                    document.getElementById(err).innerHTML = "*anno NON bisestile. Febbraio ha al massimo 28 giorni"; 
                    b=false;
                }
        }
        if(tagd.value>29)
                { document.getElementById(err).innerHTML = "*Febbraio ha al massimo 29 giorni"; b=false;}
    }
    if(b && tagd.value==31 && (tagm.value==11 || tagm.value==4 || tagm.value==6 || tagm.value==9)){
        document.getElementById(err).innerHTML = "*30 giorni al massimo";
        b=false;
    }
    return b;
}
