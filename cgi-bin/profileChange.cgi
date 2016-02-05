#!/usr/bin/perl

require 'functions/function.cgi';
require 'functions/session_function.cgi';

my $session=getSession();

#prendo eventuali parametri in ingresso con il GET
my $cgi = new CGI;
my $msgParam = $cgi->param('msgError');

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

my $year= substr($date,0,4);
my $month= substr($date,5,2);
my $day= substr($date,8,2);

print "Content-type: text/html\n\n";

print <<PRIMA_PARTE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Modifica informazioni - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>		


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Modifica info profilo - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina di modifica delle informazioni personali" />
		<meta name="keywords" content="Modifica, Profile, Logged, Siti, Web" />
		<meta name="language" content="italian it" />

		<script type="text/javascript" src="../js/control.js"></script>
		
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


my $username = getSessionUsername($session);
utf8::encode($username);


print <<EOF;

				<!-- Da caricare nel caso utente sia loggato  -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">$username</span>
					</div>
					<div>
						<div class="edit" ><a href="profile.cgi"  id="img_P" hreflang="it" type="text/html">Il tuo profilo</a></div>
						<div class="edit" ><a href="logout.cgi" id="img_EL" hreflang="it" type="text/html">Esci</a></div>
					</div>
					
				</div>



			</div>

			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable"><a href="profile.cgi" hreflang="it" type="text/html"> Profilo utente</a></span> &gt;&gt; <span class="notable">Modifica profilo</span>
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
						<li><a href="siteMap.cgi" hreflang="it" ><span xml:lang="en" lang="en">Sitemap</span></a></li>
					</ul>
				</div>

				<!-- MENÙ DI AMMINISTRAZIONE-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<ul>
						<li><a href="addInsertions.cgi" hreflang="it" type="text/html">Nuova Inserzione</a></li>
						<li><a href="showInsertions.cgi" hreflang="it" type="text/html">Inserzioni Inserite</a></li>
						<li><a href="acceptedInsertions.cgi" hreflang="it" type="text/html">Inserzioni Accettate</a></li>
					</ul>
				</div>
			</div>

			<!-- Contenuti della pagina -->
			<div id="contents">

				<h3><span xml:lang="it" lang="it">Stai modificando i tuoi dati</span></h3>
				<div id="cont_profile_change">
					<p class="underline">
						Ricordati di procedere con il salvataggio una volta che avrai terminato le modifiche.
					</p>
					<p id="cont_msg" class="msgError" title="Messaggio di errore">
EOF
if(defined($msgParam))
{
	print $msgParam;
}
print <<EOF;
					</p>

					 <form onsubmit="return profileChangeControl()" method="post" action="changeUserData.cgi">
					 	<fieldset title="Campi da compilare per effettuare il Login">
							<legend>Campi da compilare per poter modificare i propri dati</legend>
							<label for="name">Nome</label>
		  					<input id="name" type="text" name="name" maxlength="30" value="$name" tabindex="1" onfocus="cleanField('name')"/>
		  					<label for="surname">Cognome</label>
		  					<input id="surname" type="text" name="surname" maxlength="30"  value="$surname" tabindex="2"  onfocus="cleanField('surname')"/>
		  					<label for="year">Anno di Nascita</label>
							<input type="text" name="year" id="year" value="$year" tabindex="3" onfocus="cleanField('year')"/>
							<label for="month">Mese di Nascita</label>
							<input type="text" name="month" id="month" value="$month" tabindex="4" onfocus="cleanField('month')"/>
							<label for="day">Giorno di Nascita</label>
							<input type="text" name="day" id="day" value="$day" tabindex="5" onfocus="cleanField('day')"/>
		  					<label for="email">Email</label>
		  					<input id="email" type="text" name="email" value="$email" tabindex="6"  onfocus="cleanField('email')"/>

		  					<label for="password">Nuova <span xml:lang="en" lang="en">Password</span></label>
		  					<input id="password" type="password" name="password" tabindex="7"  onfocus="cleanField('password')"/>
		  					<label for="confirmPsw">Ripeti la nuova <span xml:lang="en" lang="en">Password</span></label>
		  					<input id="confirmPsw" type="password" name="confirmPsw" tabindex="8"  onfocus="cleanField('confirmPsw')"/>

		  					<label for="bio" id="contaCaratteri">Biografia (max 2000 caratteri)</label>
		  					<textarea id="bio" rows="10" cols="70" name="bio" tabindex="9" onkeyup="changeCharCountdown()" onkeydown="changeCharCountdown()" onkeypress="changeCharCountdown()">$bio</textarea>

		  					<input class="buttons" type="submit" value="Salva" onkeypress="return profileChangeControl()" tabindex="10"/>
							<input class="buttons" type="reset" value="Azzera" tabindex="11"/>
	  					</fieldset>
					</form>
				</div>

			</div>

			<!-- Div necessario per spostare il footer in fondo alla pagina -->
			<div id="push-block">
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
