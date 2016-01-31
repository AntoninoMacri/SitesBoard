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

//addInsertion.cgi
//aggiunto id="addDescrizione"
//onsubmit="return addInsertionControl()" 
//onkeypress="return addInsertionControl()"

//addInsertion
function addInsertionControl(){
    document.getElementById("cont_error").style.color='red';
    var risultato=checkTitolo("addTitolo","cont_error");
    risultato=risultato && checkOggetto("addOggetto","cont_error");
    risultato=risultato && checkDescrizione("addDescrizione","cont_error");
    return risultato;
}


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
    var risultato=checkName("reg_name", "cont_error");
    risultato=risultato && checkSurname("reg_surname", "cont_error");
    risultato=risultato && checkData("reg_year", "reg_month", "reg_day", "cont_error");
    risultato=risultato && checkUser("reg_username", "cont_error");
    risultato=risultato && checkEmail("reg_email", "cont_error");
    risultato=risultato && checkPassword("reg_pass", "cont_error");
    risultato=risultato && checkConfirmPassword("reg_pass", "reg_re_pass" ,"cont_error");

    //scrollo la pagina poichè la form è troppo lunga e c'è il rischio che l'utente non veda il suggerimento dell'errore
    var w = window.screen.width;
    var h = window.screen.height;
    window.scrollTo(3/5*w, 5/12*h);
    return risultato;
}

//recoveryControl
function recoveryControl(){
    var risultato=checkName("recover_name", "cont_error");
    risultato=risultato && checkSurname("recover_surname", "cont_error");
    risultato=risultato && checkData("recover_year", "recover_month", "recover_day", "cont_error");
    risultato=risultato && checkUser("recover_username","cont_error");
    risultato=risultato && checkEmail("recover_email", "cont_error");
    risultato=risultato && checkPassword("recover_pass", "cont_error");
    risultato=risultato && checkConfirmPassword("recover_pass", "recover_re_pass" ,"cont_error");
    return risultato;
}
    

//loginControl
function loginControl(){
    document.getElementById("cont_error").style.color='red';
    var risultato=checkUser("login_user","cont_error");
    risultato=risultato && checkPassword("login_password","cont_error");
    return risultato;
}



//FUNZIONI DI CONTROLLO
function checkUser(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo username vuoto";
        document.getElementById(par).focus();
        b=false;
    }
    return b;
}

function checkPassword(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo password vuoto";
        document.getElementById(par).focus();
        b=false;
    }
    if(b && tag.value.length<'8'){
        document.getElementById(err).innerHTML = "*campo password deve contenere almeno 8 caratteri";
        document.getElementById(par).focus();
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
	document.getElementById(conf_pass).focus();
        b=false;
    }
    if(b && tag2.value.length<'8'){
        document.getElementById(err).innerHTML = "*campo Ripeti la Password deve contenere almeno 8 caratteri";
	document.getElementById(conf_pass).focus();
        b=false;
    }
    if(b && tag.value!=tag2.value){
        document.getElementById(err).innerHTML = "*campo Ripeti la Password deve coincidere con il campo Password";
	document.getElementById(conf_pass).focus();
        b=false;
    }


    return b;
}


function checkName(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Nome vuoto";
    	document.getElementById(par).focus();
        b=false;
    }
    return b;
}

function checkSurname(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Cognome vuoto";
    	document.getElementById(par).focus();
        b=false;
    }
    return b;
}

function checkEmail(par, err){
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Email vuoto";
    	document.getElementById(par).focus();
        b=false;
    }
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    if(b && !re.test(tag.value)){
        document.getElementById(err).innerHTML = "*Email non valida";
	document.getElementById(par).focus();
        b=false;
    }
    return b;
}

function checkAge (par, err) {
    var tag= document.getElementById(par);
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Data di Nascita vuoto";
        document.getElementById(par).focus();
        b=false;
    }
    var re=/^[0-9]{1,3}$/;
    if(b && !re.test(tag.value)){
        document.getElementById(err).innerHTML = "*Data di Nascita campo numerico di massimo 3 cifre";
        document.getElementById(par).focus();
        b=false;
    }
    if(b && tag.value<18){
        document.getElementById(err).innerHTML = "*l'iscrizione è permessa solo ai maggiorenni";
        document.getElementById(par).focus();
        b=false;
    }
    if(b && tag.value>110){
        document.getElementById(err).innerHTML = "*l'iscrizione deve essere inferiore a 110";
        document.getElementById(par).focus();
        b=false;
    }
    return b;
}

function checkData(y, m, d, err){
    var tagy= document.getElementById(y);
    var b=true;
    if (tagy.value == null || tagy.value == "") {
        document.getElementById(err).innerHTML = "*campo Anno di Nascita vuoto";
	document.getElementById(y).focus();
        b=false;
    }
    //controllo che l'anno sia un numero
    var re=/^[0-9]{4}$/;
    if(b && !re.test(tagy.value)){
        document.getElementById(err).innerHTML = "*Anno deve contenere 4 cifre";
	document.getElementById(y).focus();
        b=false;
    }
    //controllo che l'anno sia successivo al 1900
    if(b && tagy.value<1900){
        document.getElementById(err).innerHTML = "*anno deve essere successivo al 1900";
	document.getElementById(y).focus();
        b=false;
    }
    var bisestile=false;
    if(tagy.value%4==0){
        bisestile=true;
    }

    var tagm= document.getElementById(m);
    if (b && (tagm.value == null || tagm.value == "")) {
        document.getElementById(err).innerHTML = "*campo Mese di Nascita vuoto";
	document.getElementById(m).focus();
        b=false;
    }
    //controllo che il mese sia un numero
    var re=/^[0-9]{1,2}$/;
    if(b && !re.test(tagm.value)){
        document.getElementById(err).innerHTML = "*mese deve contenere 1 o 2 cifre";
	document.getElementById(m).focus();
        b=false;
    }
    if(b && tagm.value>12){
        document.getElementById(err).innerHTML = "*mese deve contenere un valore da 1 a 12";
	document.getElementById(m).focus();
        b=false;
    }

    var tagd= document.getElementById(d);
    if (b && (tagd.value == null || tagd.value == "")) {
        document.getElementById(err).innerHTML = "*campo Giorno di Nascita vuoto";
	document.getElementById(d).focus();
        b=false;
    }
    //controllo che il giorno sia un numero
    var re=/^[0-9]{1,2}$/;
    if(b && !re.test(tagd.value)){
        document.getElementById(err).innerHTML = "*giorno deve contenere 1 o 2 cifre";
	document.getElementById(d).focus();
        b=false;
    }
    if(b && tagd.value>31){
        document.getElementById(err).innerHTML = "*giorno deve contenere un valore da 1 a 31";
	document.getElementById(d).focus();
        b=false;
    }
    if(b && tagd.value>28 && tagm.value==2){
        if(tagd.value==29)
        {
            if(!bisestile)
                { 
                    document.getElementById(err).innerHTML = "*anno NON bisestile. Febbraio ha al massimo 28 giorni";
		    document.getElementById(d).focus();
                    b=false;
                }
        }
        if(tagd.value>29)
                { 
		    document.getElementById(err).innerHTML = "*Febbraio ha al massimo 29 giorni";
		    document.getElementById(d).focus();
		    b=false;
		}
    }
    if(b && tagd.value==31 && (tagm.value==11 || tagm.value==4 || tagm.value==6 || tagm.value==9)){
        document.getElementById(err).innerHTML = "*30 giorni al massimo";
	document.getElementById(d).focus();
        b=false;
    }
    return b;
}


function addCharCountdown()
{
    var massimo=2000;
    document.getElementById("contaCaratteri").innerHTML = massimo - document.addForm.addDescrizione.value.length + " caratteri ancora disponibili";
    if (document.addForm.addDescrizione.value.length > massimo)
    {
        document.addForm.addDescrizione.value=document.addForm.addDescrizione.value.substr(0, massimo);
        document.getElementById("contaCaratteri").innerHTML = 0;
        alert("Massimo " + massimo + " caratteri!");
    }
    document.getElementById("contaCaratteri").innerHTML=massimo -document.addForm.addDescrizione.value.length + " caratteri ancora disponibili";
}

function checkTitolo(par, err){
    var tag= document.getElementById(par);
	document.getElementById(par).focus();
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Titolo vuoto";
        b=false;
    }
    return b;
}

function checkOggetto(par, err){
    var tag= document.getElementById(par);
    document.getElementById(par).focus();
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Oggetto vuoto";
        b=false;
    }
    return b;
}

function checkDescrizione(par, err){
    var tag= document.getElementById(par);
    document.getElementById(par).focus();
    var b=true;
    if (tag.value == null || tag.value == "") {
        document.getElementById(err).innerHTML = "*campo Descrizione vuoto";
        b=false;
    }
    return b;
}

function alertOnRmProfile()
{
    var x = confirm("Sei sicuro di cancellare definitivamente il tuo profilo da SitesBoard?");
      if (x)
          return true;
      else
        return false;
}
