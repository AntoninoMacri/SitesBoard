#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI;

require 'functions/session_function.cgi';
require 'functions/function.cgi';

my $session=getSession();
my $name;

if($session != undef)
{
   $name = getSessionUsername($session);
}

my $tipo='Forum';
my @info=getBoardTipologia($tipo);


print "Content-type: text/html\n\n";

print <<PRIMA_PARTE;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="en">Forum - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Forum - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Bacheca Forum di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Forum, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />
		
	</head>
	<body>
		<a class="screen_reader" href="#contents" hreflang="it" type="application/xhtml+xml">Se desideri saltare al contenuto segui questo collegamento</a>
		<div id="container">



			<!-- HEADER-->
			<div id="header">
				<a href="home.cgi" hreflang="it"><img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
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
					<div class="minimal">
						<a class="edit" href="profile.cgi" hreflang="it" type="application/xhtml+xml">Il tuo profilo <img id="profile_logo" src="../media/header_profile.png" alt="Iconcina del profilo" title = "Vai al tuo profilo"/></a>
						<a class="edit" href="logout.cgi" hreflang="it" type="application/xhtml+xml">Logout <img id="logout_logo" src="../media/logout.png" alt="Iconcina del logout" title = "esegui il logout"/></a>
					</div>
				</div>
			
PEZZO2
}

print <<SECONDA_PARTE;

			</div>
			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable" xml:lang="en" lang="en"><a href="home.cgi" hreflang="it" type="application/xhtml+xml">Home</a></span> &gt;&gt; <span class="notable">Bacheca Forum</span>
			</div>


			<div id="nav_panel">

				<!-- MENÙ DI NAVIGAZIONE -->
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<ul>
						<li><span xml:lang="en" lang="en"><a href="home.cgi" hreflang="it" >Home Page</a></span></li>
						<li><a href="eCommerce.cgi" hreflang="it" ><span xml:lang="en" lang="en">Tipologia E-commerce</span></a></li>
						<li  class="current_pageL"><span xml:lang="en" lang="en">Tipologia Forum</span></li>
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
				<!-- Da caricare solo se l utente non è loggato-->
				<div id="nav_login" class="menu" title="Menù di Login del sito">
					<h3><span xml:lang="en" lang="en">Login</span></h3>
					<!-- Messaggio di errore -->
					<p class="msgError" title="Messaggio di errore compilazione form login">
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
				<!-- Da caricare se l utente è loggato-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<ul>
						<li><a href="addInsertions.cgi" hreflang="it" type="application/xhtml+xml">Nuova Inserzione</a></li>
						<li><a href="showInsertions.cgi" hreflang="it" type="application/xhtml+xml">Inserzioni Inserite</a></li>
						<li><a href="acceptedInsertions.cgi" hreflang="it" type="application/xhtml+xml">Inserzioni Accettate</a></li>
					</ul>
				</div>
PEZZO

}



print <<FINE;
			</div>
			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3><span xml:lang="en" lang="en">Forum</span></h3>
				<div id="cont_forum">
				<p class="underline">Ecco gli annunci disponibili per la tipologia <span xml:lang="en" lang="en">Forum</span>.
				<ul id="block_insertions">
				
FINE
for (my $i=0; $i <scalar(@info); $i++) {
	my $autore=$info[$i][0];
	my $titolo=$info[$i][1];
	my $oggetto=$info[$i][2];
	my $tipologia=$info[$i][4];
	my $data=$info[$i][5];
	my $id_annuncio=$info[$i][6];
	my $id_persona=$info[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);
	utf8::encode($oggetto);
	utf8::encode($tipologia);
	utf8::encode($data);

	print "<li>
				<dl class='block_insertion'>
					<dt>Titolo:</dt>
					<dd><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></dd>
					<dt>Tipologia:</dt>
					<dd>$tipologia</dd>
					<dt>Oggetto:</dt>
					<dd>$oggetto</dd>
					<dt>Autore:</dt>
					<dd><a href='userProfile.cgi?user=$autore'>$autore</a></dd>
					<dt>Data:</dt>
					<dd>$data</dd>
				</dl>
			</li>";
}


print <<FINE;
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
			    <a href="http://validator.w3.org/check?uri=referer" hreflang="en" >
			    	<img class="img_validator" src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
			</span>
			<span title="CSS della pagina validato secondo lo standard">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" > 
			        <img class="img_validator" src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" /></a>
			</span>
			<span title="Accessibile secondo lo standard WCAG2 Livello AAA">
			    <a href="http://www.w3.org/WAI/intro/wcag"  hreflang="en-US">
			        <img class="img_validator" src="https://www.totalvalidator.com/images/valid_n_wcag2_aaa.gif" alt="Pagina accessibile" />
			    </a>
			</span>
		</div>
	</body>
</html>
	
FINE
exit;
