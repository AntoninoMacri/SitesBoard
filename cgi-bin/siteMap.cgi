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


print "Content-type: text/html\n\n";
print <<PRIMA_PARTE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="en">Sitemap - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Sitemap - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Sitemap di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Sitemap, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />	

	</head>
	<body>
		<div class="screen_reader"><a href="#contents" hreflang="it" type="text/html">Se desideri saltare al contenuto segui questo collegamento</a></div>
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
				Ti trovi in: <span class="notable" xml:lang="en" lang="en">Sitemap</span>
			</div>


			<div id="nav_panel">

				<!-- MENÙ DI NAVIGAZIONE -->
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<ul>
						<li><a href="home.cgi" hreflang="it" ><span xml:lang="en" lang="en">Home Page</span></a></li>
						<li><a href="eCommerce.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="forum.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="social.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="personali.cgi" hreflang="it" >Tipologia Personali</a></li>
						<li><a href="aziendali.cgi" hreflang="it" >Tipologia Aziendali</a></li>
						<li><a href="blog.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Blog</span></a></li>
						<li class="current_pageL"><span xml:lang="en" lang="en">Sitemap</span></li>
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
				<!-- Da caricare se l utente è loggato-->
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
				<h3><span xml:lang="en" lang="en">Sitemap</span></h3>
				<div id="cont_map"> 
				<ul>
					<li><a href="home.cgi" hreflang="it"><span xml:lang="en" lang="en">Home Page</span></a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE
my @board=getBoard();
for (my $i=0; $i <scalar(@board); $i++) {
	my $autore=$board[$i][0];
	my $titolo=$board[$i][1];
	my $id_annuncio=$board[$i][6];
	my $id_persona=$board[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
					<li><a href="eCommerce.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">E-commerce</span></a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE

my $tipo='E-commerce';
my @ecomm=getBoardTipologia($tipo);

for (my $i=0; $i <scalar(@ecomm); $i++) {
	$autore=$ecomm[$i][0];
	$titolo=$ecomm[$i][1];
	$id_annuncio=$ecomm[$i][6];
	$id_persona=$ecomm[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
					<li><a href="forum.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Forum</span></a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE

my $tipo='Forum';
my @forum=getBoardTipologia($tipo);

for (my $i=0; $i <scalar(@forum); $i++) {
	$autore=$forum[$i][0];
	$titolo=$forum[$i][1];
	$id_annuncio=$forum[$i][6];
	$id_persona=$forum[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
				<li><a href="social.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Social</span></a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE

my $tipo='Social';
my @social=getBoardTipologia($tipo);

for (my $i=0; $i <scalar(@social); $i++) {
	$autore=$social[$i][0];
	$titolo=$social[$i][1];
	$id_annuncio=$social[$i][6];
	$id_persona=$social[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
					<li><a href="personali.cgi" hreflang="it" >Tipologia Personali</a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE

my $tipo='Personali';
my @pers=getBoardTipologia($tipo);

for (my $i=0; $i <scalar(@pers); $i++) {
	$autore=$pers[$i][0];
	$titolo=$pers[$i][1];
	$id_annuncio=$pers[$i][6];
	$id_persona=$pers[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
					<li><a href="aziendali.cgi" hreflang="it" >Tipologia Aziendali</a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE

my $tipo='Aziendali';
my @aziendali=getBoardTipologia($tipo);

for (my $i=0; $i <scalar(@aziendali); $i++) {
	$autore=$aziendali[$i][0];
	$titolo=$aziendali[$i][1];
	$id_annuncio=$aziendali[$i][6];
	$id_persona=$aziendali[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
					<li><a href="blog.cgi" hreflang="it" >Tipologia <span xml:lang="en" lang="en">Blog</span></a>
						<ul>
							<li><a href="registration.cgi" hreflang="it">Non ti sei ancora registrato?</a></li>
							<li><a href="pass_recovery.cgi" hreflang="it">Non trovi più la password?</a></li>
							<li><a href="profile.cgi" hreflang="it">Il tuo profilo</a>
								<ul>
									<li><a href="profileChange.cgi" hreflang="it">Modifica il tuo profilo</a></li>
								</ul>
							</li>
							<li><a href="logout.cgi" hreflang="it" xml:lang="en" lang="en">Logout</a></li>
							<li><a href="addInsertions.cgi" hreflang="it">Nuova Inserzione</a></li>
							<li><a href="showInsertions.cgi" hreflang="it">Inserzioni Inserite</a></li>
							<li><a href="acceptedInsertions.cgi" hreflang="it">Inserzioni Accettate</a></li>

FINE

my $tipo='Blog';
my @blog=getBoardTipologia($tipo);

for (my $i=0; $i <scalar(@blog); $i++) {
	$autore=$blog[$i][0];
	$titolo=$blog[$i][1];
	$id_annuncio=$blog[$i][6];
	$id_persona=$blog[$i][7];

	utf8::encode($autore);
	utf8::encode($titolo);

	print "
					<li><a href='insertion.cgi?idUser=$id_persona&amp;idInsertion=$id_annuncio'>$titolo</a></li>
					<li><a href='userProfile.cgi?user=$autore'>$autore</a></li>
		";
}


print <<FINE;
						</ul>
					</li>
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
