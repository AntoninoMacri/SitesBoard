//Funzioni Javascript
//addInsertion
function addInsertionControl(){
    var risultato=checkTitolo("addTitolo","cont_msg");
    risultato=risultato && checkOggetto("addOggetto","cont_msg");
    risultato=risultato && checkDescrizione("addDescrizione","cont_msg");

    //scrollo la pagina poichè la form è troppo lunga e c'è il rischio che l'utente non veda il suggerimento dell'errore
    window.scroll(0,findPos(document.getElementById("cont_msg")));
    return risultato;
}


//profileChangeControl
function profileChangeControl(){
   var risultato=checkName("name","cont_msg");
   risultato=risultato && checkSurname("surname","cont_msg");
   risultato=risultato && checkData("year", "month", "day", "cont_msg");
   risultato=risultato && checkEmail("email","cont_msg");
   risultato=risultato && checkPassword("password", "cont_msg");
   risultato=risultato && checkConfirmPassword("password", "confirmPsw" ,"cont_msg");

   window.scroll(0,findPos(document.getElementById("cont_msg")));
   return risultato;
}


//registrationControl
function registrationControl(){
    var risultato=checkName("reg_name", "cont_msg");
    risultato=risultato && checkSurname("reg_surname", "cont_msg");
    risultato=risultato && checkData("reg_year", "reg_month", "reg_day", "cont_msg");
    risultato=risultato && checkUser("reg_username", "cont_msg");
    risultato=risultato && checkEmail("reg_email", "cont_msg");
    risultato=risultato && checkPassword("reg_pass", "cont_msg");
    risultato=risultato && checkConfirmPassword("reg_pass", "reg_re_pass" ,"cont_msg");

   window.scroll(0,findPos(document.getElementById("cont_msg")));
   return risultato;
}

//recoveryControl
function recoveryControl(){
    var risultato=checkName("recover_name", "cont_msg");
    risultato=risultato && checkSurname("recover_surname", "cont_msg");
    risultato=risultato && checkData("recover_year", "recover_month", "recover_day", "cont_msg");
    risultato=risultato && checkUser("recover_username","cont_msg");
    risultato=risultato && checkEmail("recover_email", "cont_msg");
    risultato=risultato && checkPassword("recover_pass", "cont_msg");
    risultato=risultato && checkConfirmPassword("recover_pass", "recover_re_pass" ,"cont_msg");
    window.scroll(0,findPos(document.getElementById("cont_msg")));
    return risultato;
}

//loginControl
function loginControl(){
    var risultato=checkUser("login_user","log_msg");
    risultato=risultato && checkPassword("login_password","log_msg");

    window.scroll(0,findPos(document.getElementById("log_msg")));
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
    if(b && tagm.value>12 && tagm.value<1){
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
    if(b && tagd.value>31 && tagd.value<1){
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
    document.getElementById('contaCaratteri').innerHTML ="Descrizione (" + (massimo - document.getElementById('addDescrizione').value.length) + " caratteri ancora disponibili";
    if (document.getElementById('addDescrizione').value.length > massimo)
    {
        document.getElementById('addDescrizione').value=document.getElementById('addDescrizione').value.substr(0, massimo);
        document.getElementById('contaCaratteri').innerHTML = 0;
        alert("Massimo " + massimo + " caratteri!");
    }
    document.getElementById('contaCaratteri').innerHTML="Descrizione (" + (massimo -document.getElementById('addDescrizione').value.length) + " caratteri ancora disponibili)";
}

function changeCharCountdown()
{
    var massimo=2000;
    document.getElementById('contaCaratteri').innerHTML ="Biografia (" + (massimo - document.getElementById('bio').value.length) + " caratteri ancora disponibili";
    if (document.getElementById('bio').value.length > massimo)
    {
        document.getElementById('bio').value=document.getElementById('bio').value.substr(0, massimo);
        document.getElementById('contaCaratteri').innerHTML = 0;
        alert("Massimo " + massimo + " caratteri!");
    }
    document.getElementById('contaCaratteri').innerHTML="Biografia (" + (massimo -document.getElementById('bio').value.length) + " caratteri ancora disponibili)";
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

function cleanField(par){ //uso nel campo input aggiungere: onfocus="cleanField('id_del_campo')"
    document.getElementById(par).value="";
}


//Finds y value of given object
function findPos(obj) {
    var curtop = 0;
    if (obj.offsetParent) {
        do {
            curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
    return [curtop];
    }
}