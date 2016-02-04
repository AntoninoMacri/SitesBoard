#!/usr/bin/perl

use Encode;

require 'functions/function.cgi';
require 'functions/session_function.cgi';

my $session=getSession();

if($session == undef)
{
    print redirect(-url => 'login.cgi');
}

my $cgi = new CGI;
my $user = $cgi->param('user');

if(!defined($user))
{
    print redirect(-url => 'home.cgi');
}
else
{
	#controllo che se è l'utente stesso venga ridirezionato al suo profilo
	my $sessionUserUsername=getSessionUsername($session);
	if($sessionUserUsername eq $user)
	{
		print redirect(-url => 'profile.cgi');
	}

	my @utente=getUtente($user);

	$email=$utente[3];
	$biografia=$utente[4];

	utf8::encode($email);
	utf8::encode($biografia);
}

print "Content-type: text/html\n\n";

print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Profilo utente - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Profilo Utente - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina personale dell'utente loggato" />
		<meta name="keywords" content="Profilo, Logged, Siti, Web" />
		<meta name="language" content="italian it" />

		<!-- JS -->
		<script type="text/javascript" src="../js/control.js"></script>

	</head>
	<body>
				<div class="screen_reader"><a href="#contents" hreflang="it" type="application/xhtml+xml">Se desideri saltare al contenuto segui questo collegamento</a></div>
		<div id="container">
			<!-- HEADER  -->
			<div id="header">
				<a href="home.cgi" hreflang="it"><img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>


				<div id="header_login">
					<div>
						Benvenuto <span class="notable">$username</span>
					</div>
					<div class="minimal">
						<a class="edit" href="profileChange.cgi" hreflang="it" type="application/xhtml+xml">Modifica Profilo <img id="header_PEL" src="../media/edit_profile.png" alt="Iconcina di modifica profilo" title = "Modifica i dati del profilo"/></a>
						<a class="edit" href="logout.cgi" hreflang="it" type="application/xhtml+xml">Esci <img id="logout_logo" src="../media/logout.png" alt="Iconcina del logout" title = "esegui il logout"/></a>
					</div>
				</div>
			</div>

			<!-- PATH  -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable">Profilo Utente</span>
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

				<!-- MENÙ DI AMMINISTRAZIONE-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<ul>
						<li><a href="addInsertions.cgi" hreflang="it" type="application/xhtml+xml">Nuova Inserzione</a></li>
						<li><a href="showInsertions.cgi" hreflang="it" type="application/xhtml+xml">Inserzioni Inserite</a></li>
						<li><a href="acceptedInsertions.cgi" hreflang="it" type="application/xhtml+xml">Inserzioni Accettate</a></li>
					</ul>
				</div>

			</div>

			<!-- Contenuti della pagina -->
			<div id="contents">
				<h3><span xml:lang="it" lang="it">Profilo utente di $user</span></h3>

				<div id="cont_profile">
					<p class="underline">
					Ti trovi all interno della pagina profilo di un utente iscritto a SitesBoard. Da qui puoi visualizzare i suoi dati.
 					</p>

					<dl class="block_profile">
						<dt><span xml:lang="en" lang="en">Username</span>:</dt>
						<dd>$user</dd>
	  					<dt><span xml:lang="en" lang="en">Email</span>:</dt>
	  					<dd><a href="mailto:$email">$email</a></dd>
	  					<dt>Biografia:</dt>
	  					<dd>$biografia</dd>
	  				</ul>
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
			    	<img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
			</span>
			<span title="CSS della pagina validato secondo lo standard">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" type="application/xhtml+xml"> 
			        <img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" /></a>
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
