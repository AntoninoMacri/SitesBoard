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

my $cgi = new CGI;
my $index = $cgi->param('index');
if(!defined($index)) { $index=0; }

my $nElementi=5;
my @board=getBoard();
my $size=scalar @board;
my @info=getBoardSplit($index,$nElementi,\@board);

$index_successivo=$index+$nElementi;
$index_precedente=$index-$nElementi;

if($index_precedente<0){ $index_precedente=0; }

print "Content-type: text/html\n\n";
print <<PRIMA_PARTE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="en">Home Page - SitesBoard</title> 


		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld, screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>
		<!--[if lt IE 9]>
			<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen"/>
			<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>
		<![endif]-->

		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Home Page - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Home Page di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Home, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />

		<script type="text/javascript" src="../js/control.js"></script>		

	</head>
	<body>
		<div class="screen_reader"><a href="#contents" hreflang="it" type="text/html">Se desideri saltare al contenuto segui questo collegamento</a></div>
		<div id="container">
			<!-- HEADER-->
			<div id="header">
				<img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/>
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
						<div class="edit" ><a href="profile.cgi"  id="img_P" hreflang="it" type="text/html">Il tuo profilo</a></div>
						<div class="edit" ><a href="logout.cgi" id="img_EL" hreflang="it" type="text/html">Esci</a></div>
					</div>
				</div>
			
PEZZO2
}

print <<SECONDA_PARTE;

			</div>
			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable" xml:lang="en" lang="en">Home</span>
			</div>


			<div id="nav_panel">

				<!-- MENÙ DI NAVIGAZIONE -->
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<ul>
						<li class="current_pageL"><span xml:lang="en" lang="en">Home Page</span></li>
						<li><a href="eCommerce.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="forum.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="social.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="personali.cgi" hreflang="it" >Tipologia Personali</a></li>
						<li><a href="aziendali.cgi" hreflang="it" >Tipologia Aziendali</a></li>
						<li><a href="blog.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Blog</span></a></li>
						<li><a href="siteMap.cgi" hreflang="it" ><span xml:lang="en" lang="en">Sitemap</span></a></li>
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
						<a class ="minimal" href="pass_recovery.cgi" hreflang="it" >Non trovi più la <span xml:lang="en" lang="en">password?</span></a>
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
				<h3><span xml:lang="en" lang="en">Home Page</span></h3>
				<div id="cont_welcome"> 
					<p class="underline">Benvenuti nella <span xml:lang="en" lang="en">Home</span> di <span xml:lang="en" lang="en">SitesBoard</span>. In questo sito potete vedere, proporre e anche accettare richieste di creazione di siti <span xml:lang="en" lang="en">web</span>.</p>
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

	#$tipologia accessibile
	$tipologia=addSpan($tipologia);

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
FINE
if($index_precedente>=0 && $index ne 0){
	print "<a href='home.cgi?index=$index_precedente' class='BI_PN' hreflang='it' type='application/xhtml+xml'>Precedente</a>";
}

if($index_successivo<$size){
	print "<a href='home.cgi?index=$index_successivo' class='BI_PN' hreflang='it' type='application/xhtml+xml'>Successiva</a>";
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
