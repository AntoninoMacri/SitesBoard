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

if($session == undef)
{
    print redirect(-url => 'login.cgi');
}

print "Content-type: text/html\n\n";

print <<PRIMA_PARTE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Nuovo annuncio - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Nuovo annuncio - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina per creare un nuovo annuncio" />
		<meta name="keywords" content="Nuovo, Annuncio, New, Insertion, Siti, Web" />
		<meta name="language" content="italian it" />

		<script type="text/javascript" src="../js/control.js"></script>

	</head>
	<body>
		<a class="screen_reader" href="#contents" hreflang="it" type="application/xhtml+xml">Se desideri saltare al contenuto segui questo collegamento</a>
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
				<!-- Da caricare nel caso l utente sia loggato  -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">$username</span>
					</div>
					<div class="minimal">
						<a class="edit" href="profile.cgi" hreflang="it" type="application/xhtml+xml">Il tuo profilo <img id="profile_logo" src="../media/header_profile.png" alt="Iconcina del profilo" title = "Vai al tuo profilo"/></a>
						<a class="edit" href="logout.cgi" hreflang="it" type="application/xhtml+xml">Esci <img id="logout_logo" src="../media/logout.png" alt="Iconcina del logout" title = "esegui il logout"/></a>
					</div>
					
				</div>


			
			</div>

			<!-- PATH  -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable">Nuovo Annuncio</span>
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

				<h3><span xml:lang="it" lang="it">Nuovo annuncio</span></h3>
				<div id="cont_add">
					<p class="info">
					Ti trovi dentro alla pagina per creare un nuovo annuncio.
					</p>
					<p class="info">
					In particolare un annuncio si compone di: un titolo, un oggetto ed una descrizione.  
					</p>
					<p class="info underline">
					Ricordati di fare salva quando hai portato a termine tutte le eventuali operazioni!
					</p>

					<p id="cont_msg" class="msgError" title="Messaggio di errore">
EOF
if(defined($msgParam))
{
	print $msgParam;
}
print <<EOF;
					</p>

					<form method="post" action="insertInsertion.cgi" onsubmit="return addInsertionControl()">
						<fieldset title="Campi da compilare per creare un nuovo annuncio">
							<legend>Campi da compilare per creare un nuovo annuncio</legend>

							<label for="addTitolo">Titolo</label>
			  				<input id="addTitolo" type="text" name="addTitolo" maxlength="100" value="" tabindex="1" />

			  				<label for="addTipologia">Tipologia</label>
				  			<select id="addTipologia" name="addTipologia" tabindex="2" >
								<option value="eCommerce">E-commerce</option>
								<option value="forum">Forum</option>
								<option value="social" selected="selected">Social</option>
								<option value="personali">Personali</option>
	  							<option value="aziendali">Aziendali</option>
								<option value="blog">Blog</option>
							</select>
			  				
			  				<label for="addOggetto">Oggetto</label>
			  				<input id="addOggetto" type="text" name="addOggetto" maxlength="300" value="" tabindex="3" />

		  					<label for="addDescrizione">Descrizione (max 2000 caratteri)</label>
		  					<label for="addDescrizione" id="contaCaratteri">2000 caratteri ancora disponibili</label>
		  					<textarea id="addDescrizione" rows="10" cols="70" name="addDescrizione" onkeyup="addCharCountdown()" onkeydown="addCharCountdown()" onkeypress="addCharCountdown()" tabindex="4"></textarea>
					
							<input class="buttons" id="submit_new" type="submit" value="Crea" onkeypress="return addInsertionControl()" />
							<input class="buttons" id="reset_new" type="reset" value="Azzera" />
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