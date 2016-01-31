#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;
require 'functions/function.cgi';
require 'functions/session_function.cgi';

#ottengo dati dalla sessione
my $session=getSession();
my $userUsername;
if($session == undef)
{
    print redirect(-url => 'login.cgi');
    $userUsername = getSessionUsername($session);
}

#ottengo i dati passati alla pagina
my $cgi = new CGI;
my $idUserParam = $cgi->param('idUser');
my $idInsertionParam = $cgi->param('idInsertion');

if(defined($idUserParam) && defined($idInsertionParam)){
my @info=getAd($idUserParam, $idInsertionParam); #ritorna un array{username,titolo,oggetto,descrizione,tipologia,data} per le info dell annuncio

$autore=$info[0];
$titolo=$info[1];
$oggetto=$info[2];
$descrizione=$info[3];
$tipologia=$info[4];
$data=$info[5];

utf8::encode($autore);
utf8::encode($titolo);
utf8::encode($oggetto);
utf8::encode($descrizione);
utf8::encode($tipologia);
utf8::encode($data);
}

print "Content-type: text/html\n\n";


print <<PRIMA_PARTE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Annuncio- SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Annuncio - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina di visualizzazione annuncio" />
		<meta name="keywords" content="Annuncio, Insertion, Siti, Web" />
		<meta name="language" content="italian it" />

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

				<!-- Da caricare nel caso l utente sia loggato  -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">$username</span>
					</div>
					<div class="minimal">
						<a class="edit" href="profileChange.cgi" hreflang="it" type="application/xhtml+xml">Modifica Profilo <img id="header_PEL" src="../media/edit_profile.png" alt="Iconcina di modifica profilo" title = "Modifica i dati del profilo"/></a>
						<a class="edit" href="logout.cgi" hreflang="it" type="application/xhtml+xml">Logout <img id="logout_logo" src="../media/logout.png" alt="Iconcina del logout" title = "esegui il logout"/></a>
					</div>
				</div>


			</div>

			<!-- PATH  -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable" xml:lang="en" lang="it">Visualizza annuncio</span>
			</div>
			<div id="nav_panel">
				<!-- MENÙ DI NAVIGAZIONE --> 
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<a href="home.cgi" xml:lang="en" lang="en" hreflang="it" >Home</a>

					<p>Tipologia Siti:</p>
					<ul>
						<li><a href="eCommerce.cgi" hreflang="it" ><span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="forum.cgi" hreflang="it" ><span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="social.cgi" hreflang="it" ><span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="personali.cgi" hreflang="it" >Personali</a></li>
						<li><a href="aziendali.cgi" hreflang="it" >Aziendali</a></li>
						<li><a href="blog.cgi" hreflang="it" ><span xml:lang="en" lang="en">Blog</span></a></li>
					</ul>
					
				</div>
EOF
if($session == undef){
	print <<PEZZO;
					<!-- MENÙ DI LOGIN-->
					<!-- Da caricare solo se l utente non è loggato-->
					<div id="nav_login" class="menu" title="Menù di Login del sito">
						<h3><span xml:lang="en" lang="en">Login</span></h3>
						<!-- Messaggio di errore -->
						<p id="cont_error" title="Messaggio di errore compilazione form login">
						</p>
						<!-- Form da compilare -->
						<form onsubmit="return loginControl()" method="post" action="checkLogin.cgi">
							<fieldset title="Campi da compilare per effettuare il Login">
								<legend>Campi da compilare per effettuare il Login</legend>
								<label for="login_user">Username</label>
								<input type="text" name="login_user" id="login_user"/><br/>
								<label for="login_password">Password</label>
								<input type="password" name="login_password" id="login_password"/><br/>
							</fieldset>
							<fieldset title="Procedi su Login per effetturare l'accesso">
								<legend>Operazione di Login</legend>
								<input type="submit" name="login_submit" id="login_submit" value="Accedi al sito" onkeypress="return loginControl()" />
							</fieldset>
						</form>
						<a class ="minimal" href="registration.cgi" hreflang="it" >Non ti sei ancora registrato?</a>
						<a class = "minimal" href="../html/pass_recovery.html" hreflang="it" >Non trovi più la <span xml:lang="en" lang="en">password?</span></a>
					</div>
PEZZO
}
else
{
	print <<PEZZO;
					<!-- MENÙ DI AMMINISTRAZIONE-->
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
PEZZO
}
print <<EOF;

			</div>

			<!-- Contenuti della pagina -->
			<div id="contents">
				<span id="ins_author">da: <a href="profile.cgi" hreflang="it" type="application/xhtml+xml">$autore</a> </span> 
				<span id="ins_date">in data: $data</span>
				<div id="cont_insertion">
					<p id="underline">
						<span class="insInfo">Tipologia:</span> $tipologia
					</p>
					<p id="title">
						<span>Titolo:</span> $titolo
					</p>
					<p class="underline">
						<span>Oggetto:</span> $oggetto
					</p>
					<p class="underline">
						<span>Descrizione:</span> </br> $descrizione
					</p>
EOF
#se l'autore è la stessa persona che visualizza la pagina allora non visualizza la possibilità di accetare l'inserizione
if($userUsername != $autore)
{
	print <<EOF;
						<form name="form_Accetazione" method="post" action="addAcception.cgi">
							<fieldset title="Accetta annuncio">
								<input  id="idUserInsertion" name="idUserInsertion" type="hidden" value='$idUserParam' />
								<input  id="idInsertion" name="idInsertion" type="hidden" value='$idInsertionParam' />
								<legend id="accept_insertion">Procedi per accettare l'annuncio</legend>
								<input class="buttons" id="submit_new" name="submit_new" type="submit" value="Accetta" />
							</fieldset>
						</form>
EOF
}
else
{
	print <<EOF;
						<form name="form_Eliminazione" method="post" action="removeInsertion.cgi">
							<fieldset title="Rimuovi annuncio">
								<input  id="idInsertion" name="idInsertion" type="hidden" value='$idInsertionParam' />
								<legend id="remove_insertion">Procedi per accettare l'annuncio</legend>
								<input class="buttons" id="submit_new" name="submit_new" type="submit" value="Rimuovi" />
							</fieldset>
						</form>		
EOF
}
print <<EOF;
				</div>
			</div>

			<!-- Div necessario per spostare il footer in fondo alla pagina -->
			<div id="push_block">
			</div>
		</div>

		<!-- FOOTER -->
		<div id="footer">
			<span title="Pagina validata con lo standard XHTML 1.0 Strict">
			    <a href="http://validator.w3.org/check?uri=referer" hreflang="en" type="application/xhtml+xml"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
			</span>
			<span title="CSS della pagina validato secondo lo standard">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" type="application/xhtml+xml"> 
			        <img id="footer_CSS_Validator" src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" />
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