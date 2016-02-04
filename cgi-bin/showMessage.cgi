#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use strict;

require 'functions/function.cgi';
require 'functions/session_function.cgi';

#prendo eventuali parametri in ingresso con il GET
my $cgi = new CGI;
my $msgConfirmParam = $cgi->param('confirm');
my $msgErrorParam = $cgi->param('error');

#ridireziono l'utente loggato alla home
my $session=getSession();
my $name;

if($session != undef)
{
   $name = getSessionUsername($session);
}

my @info=getBoard();

print "Content-type: text/html\n\n";

print <<PRIMA_PARTE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="en">Messaggio - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Messaggio - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina Messaggio di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Messaggio, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />
		
	</head>
	<body>
				<div class="screen_reader"><a href="#contents" hreflang="it" type="text/html">Se desideri saltare al contenuto segui questo collegamento</a></div>
		<div id="container">
			<!-- HEADER-->
			<div id="header">
				<a href="home.cgi" hreflang="it" ><img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>

PRIMA_PARTE

if($session != undef){

print <<PEZZO;
				<!-- Da caricare nel caso l utente sia loggato -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">
PEZZO

print $name;			
print <<PEZZO2;
			</span>
					</div>
					<div>
						<div class="edit"><a href="profileChange.cgi" hreflang="it" type="text/html">Modifica Profilo<div id="img_EP"></div></a></div>
						<div class="edit"><a href="logout.cgi" hreflang="it" type="text/html">Esci<div id="img_EL"></div></a></div>
					</div>
				</div>
			
PEZZO2
}

print <<SECONDA_PARTE;

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
SECONDA_PARTE


if($session == undef){
print <<PEZZO;
				<!-- MENÙ DI LOGIN-->
				<div id="nav_login" class="menu" title="Menù di Login del sito">
					<h3><span xml:lang="en" lang="en">Login</span></h3>
					<!-- Messaggio di errore -->
					<p id="log_msg" class="msgError" title="Messaggio di errore compilazione form login">
					</p>
					<!-- Form da compilare -->
					<form onsubmit="return loginControl()" method="post" action="checkLogin.cgi">
						<fieldset title="Campi da compilare per effettuare il Login">
							<legend>Caompilare per effettuare il Login</legend>
							<label for="login_user">Username</label>
							<input type="text" name="login_user" id="login_user"/><br/>
							<label for="login_password">Password</label>
							<input type="password" name="login_password" id="login_password"/><br/>

							<input type="submit" name="login_submit" id="login_submit" value="Accedi al sito" onkeypress="return loginControl()" />
						</fieldset>
					</form>
					<div>
						<a class ="minimal" href="registration.cgi" hreflang="it" >Non ti sei ancora registrato?</a>
						<a class ="minimal" href="../html/pass_recovery.html" hreflang="it" >Non trovi più la <span xml:lang="en" lang="en">password?</span></a>
					</div>
				</div>
PEZZO
}
else
{
print <<PEZZO;
				<!-- MENÙ DI AMMINISTRAZIONE-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<ul>
						<li><a href="addInsertions.cgi" hreflang="it" type="text/html">Nuova Inserzione</a></li>
						<li><a href="showInsertions.cgi" hreflang="it" type="text/html">Inserzioni Inserite</a></li>
						<li><a href="acceptedInsertions.cgi" hreflang="it" type="text/html">Inserzioni Accettate</a></li>
					</ul>
				</div>
PEZZO

}



print <<FINE;
			</div>
			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3><span xml:lang="en" lang="en">Home</span></h3>
				<div id="cont_showMessage"> 
					
FINE
if(defined($msgConfirmParam))
{
	print '<p id="cont_msg" class="msgConfirm" title="Messaggio di conferma">';
	print $msgConfirmParam;
	print '</p>';
}
if(defined($msgErrorParam))
{
	print '<p id="cont_msg" class="msgError" title="Messaggio di errore">';
	print $msgErrorParam;
	print '</p>';
}
print <<FINE;
					
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
	
FINE
exit;
