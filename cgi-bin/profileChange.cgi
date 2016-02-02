#!/usr/bin/perl

require 'functions/function.cgi';
require 'functions/session_function.cgi';

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
		<title>Modifica informazioni - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>		


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta name="title" content="Modifica info profilo - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina di modifica delle informazioni personali" />
		<meta name="keywords" content="Modifica, Profile, Logged, Siti, Web" />
		<meta name="language" content="italian it" />

		<script type="text/javascript" src="../js/control.js"></script>
		
	</head>
	<body>
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
					<div class="minimal">
						<a class="edit" href="profile.cgi" hreflang="it" type="application/xhtml+xml">Il tuo profilo <img id="profile_logo" src="../media/header_profile.png" alt="Iconcina del profilo" title = "Torna al tuo profilo"/></a>
						<a class="edit" href="logout.cgi" hreflang="it" type="application/xhtml+xml">Logout <img id="logout_logo" src="../media/logout.png" alt="Iconcina del logout" title = "esegui il logout"/></a>
					</div>
					
				</div>



			</div>

			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable"><a href="profile.cgi" hreflang="it" type="application/xhtml+xml"> Profilo utente</a></span> &gt;&gt; <span class="notable">Modifica profilo</span>
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

				<h3><span xml:lang="it" lang="it">Stai modificando i tuoi dati</span></h3>
				<div id="cont_profile_change">
					<p id="underline">
						Ricordati di cliccare su salva una volta che avrai terminato le modifiche
					</p>

					 <form onsubmit="return profileChangeControl()" method="post" action="profileChange.cgi">
					 	<fieldset title="Campi da compilare per effettuare il Login">
							<legend>Campi da compilare per poter modificare i propri dati</legend>
							<label for="name">Nome</label>
		  					<input id="name" type="text" name="name" maxlength="30" value="" tabindex="1"/>
		  					<label for="surname">Cognome</label>
		  					<input id="surname" type="text" name="surname" maxlength="30" value="" tabindex="2" />
		  					<label for="year">Anno di Nascita</label>
							<input type="text" name="year" id="year" tabindex="3"/>
							<label for="month">Mese di Nascita</label>
							<input type="text" name="month" id="month" tabindex="4"/>
							<label for="day">Giorno di Nascita</label>
							<input type="text" name="day" id="day" tabindex="5"/>
		  					<label for="email">Email</label>
		  					<input id="email" type="text" name="email" value="" tabindex="6" />

		  					<label for="password">Nuova password</label>
		  					<input id="password" type="text" name="password" value="" tabindex="7" />
		  					<label for="confirmPsw">Conferma nuova password</label>
		  					<input id="confirmPsw" type="text" name="confirmPsw" value="" tabindex="8" />

		  					<label for="bio">Biografia</label>
		  					<textarea id="bio" rows="10" cols="70" name="bio" tabindex="9"></textarea>
		  					<input class="buttons" type="submit" value="Salva" onkeypress="return profileChangeControl()" />
							<input class="buttons" type="reset" value="Azzera" />
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
