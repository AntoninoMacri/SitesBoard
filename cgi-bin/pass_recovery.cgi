#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use strict;

require 'functions/function.cgi';
require 'functions/session_function.cgi';

#prendo eventuali parametri in ingresso con il GET
my $cgi = new CGI;
my $msgParam = $cgi->param('msgError');

#ridireziono l'utente loggato alla home
my $session=getSession();
if($session != undef)
{
	print $cgi->redirect( 'home.cgi' );
}

#altrimenti continuo la stapa della pagina
print "Content-type: text/html\n\n";
print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Recupero Password Utente - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag-->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Recupero Password Utente - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Form di recupero password utente per SitesBoard, il sito per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Recupero, Password, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />
		<script type="text/javascript" src="../js/control.js"></script>
	</head>
	<body>
		<div class="screen_reader"><a href="#contents" hreflang="it" type="text/html">Se desideri saltare al contenuto segui questo collegamento</a></div>
		<div id="container">
			<!-- HEADER-->
			<div id="header">
				<a href="home.cgi" hreflang="it" ><img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>
			</div>



			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable">Recupero <span xml:lang="en" lang="en">Password</span> Utente</span>
			</div>

			<div id="nav_panel">




				<!-- MENÙ DI NAVIGAZIONE -->
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<ul>
						<li><span xml:lang="en" lang="en"><a href="home.cgi" hreflang="it" >Home Page</a></span></li>
						<li><a href="eCommerce.cgi" hreflang="it" ><span xml:lang="en" lang="en">Tipologia E-commerce</span></a></li>
						<li><a href="forum.cgi" hreflang="it" ><span xml:lang="en" lang="en">Tipologia Forum</span></a></li>
						<li><a href="social.cgi" hreflang="it" ><span xml:lang="en" lang="en">Tipologia Social</span></a></li>
						<li><a href="personali.cgi" hreflang="it" >Tipologia Personali</a></li>
						<li><a href="aziendali.cgi" hreflang="it" >Tipologia Aziendali</a></li>
						<li><a href="blog.cgi" hreflang="it" ><span xml:lang="en" lang="en">Tipologia Blog</span></a></li>
					</ul>
				</div>


				<!-- MENÙ DI LOGIN-->
				<div id="nav_login" class="menu" title="Menù di Login del sito">
					<h3><span xml:lang="en" lang="en">Login</span></h3>
					<!-- Messaggio di errore -->
					<p id="log_msg" class="msgError" title="Messaggio di errore compilazione form login">
					</p>
					<!-- Form da compilare -->
					<form onsubmit="return loginControl()" method="post" action="checkLogin.cgi">
						<fieldset title="Campi da compilare per effettuare il Login">
							<legend>Effettua il <span  xml:lang="en" lang="en">Login</span></legend>
							<label for="login_user" xml:lang="en" lang="en">Username</label>
							<input type="text" name="login_user" id="login_user"/><br/>
							<label for="login_password" xml:lang="en" lang="en">Password</label>
							<input type="password" name="login_password" id="login_password"/><br/>
							<input type="submit" name="login_submit" id="login_submit" value="Accedi al sito" onkeypress="return loginControl()"/>
						</fieldset>
					</form>
					<div>
						<a class ="minimal" href="registration.cgi" hreflang="it" >Non ti sei ancora registrato?</a>
					</div>

				</div>

			</div>




			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3>Recupero <span xml:lang="en" lang="en">Password</span> Utente</h3>

				<!-- Div contenuto della registrazione -->
				<div id="cont_pass_recovery" title="Form da compilare per il recupero della password">
					<p>Inserire i dati relativi al proprio profilo e la nuova password.</p>
					<p class="underline">Se i dati sono corretti verrà reimpostata automaticamente la password.</p>
					<!-- Messaggio di errore -->
					<p id="cont_msg" class="msgError" title="Messaggio di errore compilazione form di recupero password">
					</p>
					<form onsubmit="return recoveryControl()" method="post" action="recoveryUser.cgi">
						<fieldset title="Dati dell'Utente Obbligatori">
							<legend>Dati dell'Utente:</legend>
							<label for="recover_name">Nome</label>
							<input type="text" name="recover_name" id="recover_name" tabindex="1" />
							<label for="recover_surname">Cognome</label>
							<input type="text" name="recover_surname" id="recover_surname" tabindex="2" />
							<label for="recover_year">Anno di Nascita</label>
							<input type="text" name="recover_year" id="recover_year" tabindex="3"/>
							<label for="recover_month">Mese di Nascita</label>
							<input type="text" name="recover_month" id="recover_month" tabindex="4"/>
							<label for="recover_day">Giorno di Nascita</label>
							<input type="text" name="recover_day" id="recover_day" tabindex="5"/>
						</fieldset>
						<fieldset title="Dati Riguardanti il Sito Obbligatori">
							<legend>Dati Riguardanti il Sito:</legend>
							<label for="recover_username" xml:lang="en" lang="en">Username</label>
							<input type="text" name="recover_username" id="recover_username" tabindex="6" />
							<label for="recover_email" xml:lang="en" lang="en">Email</label>
							<input type="text" name="recover_email" id="recover_email" maxlength="32" tabindex="7" />
							<label for="recover_pass">Nuova <span xml:lang="en" lang="en">Password</span></label>
							<input type="password" name="recover_pass" id="recover_pass" maxlength="16" tabindex="8" />
							<label for="recover_re_pass">Ripeti la nuova <span xml:lang="en" lang="en">Password</span></label>
							<input type="password" name="recover_re_pass" id="recover_re_pass" maxlength="16" tabindex="9" />
							<input class="buttons" type="submit" name="recover_submit" id="recover_submit" value="Recupera" tabindex="10"  title="Procedi con la reimpostazione della password"/>
							<input class="buttons" type="reset" name="recover_reset" id="recover_reset" value="Cancella i Campi" tabindex="11" title="Resetta i valori dei campi" onkeypress="return recoveryControl()"/>
						</fieldset>
					</form>
				</div>
			</div>

			<!-- Div necessario per spostare il footer in fondo alla pagina -->
			<div id="push_block">
			</div>
		</div>



		
		<!-- FOOTER -->
		<div id="footer">
			<span title="Pagina validata con lo standard XHTML 1.0 Strict">
			    <a href="http://validator.w3.org/check?uri=referer" hreflang="en" >
			    	<img class="img_validator" src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
			</span>
			<span title="CSS della pagina validato secondo lo standard CSS2">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" > 
			        <img class="img_validator" src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" /></a>
			</span>
			<span title="Accessibile secondo lo standard WCAG2 Livello AA">
			    <a href="http://www.w3.org/WAI/intro/wcag"  hreflang="en-US">
			        <img class="img_validator" src="https://www.totalvalidator.com/images/valid_n_wcag2_aa.gif" alt="Pagina accessibile" />
			    </a>
			</span>
		</div>
	</body>
</html>
EOF
exit;