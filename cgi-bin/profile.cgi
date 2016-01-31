#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI;

require 'functions/session_function.cgi';
require 'functions/function.cgi';

#prendo eventuali parametri in ingresso con il GET
my $cgi = new CGI;
my $msgParam = $cgi->param('msgError');

my $session=getSession();
if($session == undef)
{
    print redirect(-url => 'login.cgi');
}

my $name=getName($session);
my $surname=getSurname($session);
my $email=getEmail($session);
my $date=getDate($session);
my $bio=getBio($session);

utf8::encode($name);
utf8::encode($surname);
utf8::encode($email);
utf8::encode($date);
utf8::encode($bio);

print "Content-type: text/html\n\n";

print <<PRIMA_PARTE;
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="it">Profilo utente - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Profilo Utente - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina personale dell'utente loggato" />
		<meta name="keywords" content="Profilo, Logged, Siti, Web" />
		<meta name="language" content="italian it" />

		<!-- JS -->
		<script type="text/javascript" src="../js/control.js"></script>

	</head>
	<body>
		<div id="container">
			<!-- HEADER  -->
			<div id="header">
				<a href="home.cgi" hreflang="it"><img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>

PRIMA_PARTE


my $username = getSessionUsername($session);
utf8::encode($username);

print <<EOF;


				<!-- Da caricare nel caso l utente sia loggato (se è qui sicuramente ha una sessione valida, altrimenti viene redirectato a login.cgi) -->

				<div id="header_login">
					<div>
						Benvenuto <span class="notable">$username</span>
					</div>
					<div class="minimal">
						<a class="edit" href="profileChange.cgi" hreflang="it" type="application/xhtml+xml">Modifica Profilo <img id="header_PEL" src="../media/edit_profile.png" alt="Iconcina di modifica profilo" title = "Modifica i dati del profilo"/></a>
						&nbsp&nbsp&nbsp
						<a class="edit" href="logout.cgi" hreflang="it" type="application/xhtml+xml">Logout <img id="logout_logo" src="../media/logout.png" alt="Iconcina del logout" title = "esegui il logout"/></a>
					</div>
				</div>

				
			
			</div>

			<!-- PATH  -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable">Profilo utente</span>
			</div>
			<div id="nav_panel">
				<!-- MENÙ DI NAVIGAZIONE --> 
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<a href="home.cgi" xml:lang="en" lang="en" hreflang="it" >Home</a>
					<p>Tipologia Siti:</p>
					<ul>
						<li><a href="eCommerce.cgi" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="forum.cgi" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="social.cgi" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="personali.cgi" hreflang="it" type="application/xhtml+xml">Personali</a></li>
						<li><a href="aziendali.cgi" hreflang="it" type="application/xhtml+xml">Aziendali</a></li>
						<li><a href="blog.cgi" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">Blog</span></a></li>
					</ul>
				</div>

				<!-- MENÙ AMMINISTRAZIONE-->
				<!-- Da caricare se l utente è loggato-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<p>Annunci:</p>
					<ul>
						<li><a href="addInsertions.cgi" hreflang="it" type="application/xhtml+xml">Nuovo</a></li>
						<li><a href="showInsertions.cgi" hreflang="it" type="application/xhtml+xml">Inseriti</a></li>
						<li><a href="acceptedInsertions.cgi" hreflang="it" type="application/xhtml+xml">Accettati</a></li>
					</ul>
				</div>

			</div>

			<!-- Contenuti della pagina -->
			<div id="contents">

				<h3><span xml:lang="it" lang="it">Il tuo profilo</span></h3>
				<div id="cont_profile">
					<!-- Messaggio di errore  -->
					<p id="cont_error" title="Messaggio di errore">
EOF
if(defined($msgParam))
{
	print $msgParam;
}
print <<EOF;
					</p>
					<p class="info">
					Ti trovi all'interno dell'area personale del tuo profilo. Da qui è possibile gestire tutti i tuoi annunci o quelli a cui sei interessato.
					</p>
					<p class="info underline">
					In particolare puoi: visualizzare gli annunci da te inseriti. Visualizzare gli annunci che hai accettato in attesa di conclusione asta. Aggiungere un nuovo annuncio che apparirà nella bacheca di <span xml:lang="en" lang="en">SitesBoard</span> in ordine, dal più vicino al più lontano, di scadenza. Cancellare i tuoi annunci che per qualche motivo non ti interessa più condividere. 
					</p>

					<span>Nome: $name </span><br/>
  					<span>Cognome: $surname </span><br/>
  					<span>Data di nascita: $date</span><br/>
  					<span><span xml:lang="en" lang="en">Username</span>: $username</span><br/>
  					<span><span xml:lang="en" lang="en">Email</span>: $email</span><br/>
  					<span>Biografia: $bio</span><br/>
  					

					<form name="modulo" method="post" onclick="return alertOnRmProfile()" action="removeProfile.cgi">
					<fieldset id="remove_profile" title="Elimina il tuo profilo">
						<legend id="remove_profile">Clicca qui per rimuovere il tuo profilo</legend>
						<input class="buttons" id="rmProfile" type="submit" onkeypress="return alertOnRmProfile()" value="Elimina profilo">
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
			    <a href="http://validator.w3.org/check?uri=referer" hreflang="en" type="application/xhtml+xml">
			    	<img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" />
			 	</a>
			</span>
			<span title="CSS della pagina validato secondo lo standard">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" type="application/xhtml+xml">
					<img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" />
				</a>
			</span>
			<span title="Accessibile secondo lo standard WCAG2 Livello AAA">
			    <a href="http://www.w3.org/WAI/intro/wcag" type="application/xhtml+xml" hreflang="en-US">
			    	<img src="https://www.totalvalidator.com/images/valid_n_wcag2_aaa.gif" alt="Pagina accessibile" />
			    </a>
			</span>
		</div>
	</body>
</html>
EOF
exit;
