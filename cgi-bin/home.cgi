#!/usr/bin/perl

require "functions/session_function.cgi";
print "Content-type: text/html\n\n";
my $session=getSession();

print <<PRIMA_PARTE;
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="en">Home Page - SitesBoard</title> 

		<link href="css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="css/print.css" rel="stylesheet" type="text/css" media="print"/>



		<!-- Meta Tag-->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Home Page - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Home Page di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Home, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />
		
		<script type="text/javascript" src="js/control.js"></script>
	</head>
	<body>
		<div id="container">



			<!-- HEADER-->
			<div id="header">
				<img id="header_logo" src="media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>
PRIMA_PARTE

if($session != undef){
my $name = getSessionName();
my $surname = getSessionSurname();

print <<PEZZO;
				<!-- Da caricare nel caso l'utente sia loggato -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">$name $surname</span>
					</div>
					<div class="minimal">
						<a href="profile_change.cgi" hreflang="it" >Modifica Profilo</a>
						o <a href="logout.cgi" hreflang="it" >Esci</a>
					</div>
				</div>
			
PEZZO
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
					<p>Tipologia Siti:</p>
					<ul>
						<li><a href="bacheca_ecommerce.cgi" hreflang="it" ><span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="bacheca_forum.cgi" hreflang="it" ><span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="bacheca_social.cgi" hreflang="it" ><span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="bacheca_personali.cgi" hreflang="it" >Personali</a></li>
						<li><a href="bacheca_aziendali.cgi" hreflang="it" >Aziendali</a></li>
						<li><a href="bacheca_blog.cgi" hreflang="it" ><span xml:lang="en" lang="en">Blog</span></a></li>
					</ul>
					
				</div>
SECONDA_PARTE




if($session == undef){
print <<PEZZO;
				<!-- MENÙ DI LOGIN-->
				<!-- Da caricare solo se l'utente non è loggato-->
				<div id="nav_login" class="menu" title="Menù di Login del sito">
					<h3><span xml:lang="en" lang="en">Login</span></h3>
					<!-- Messaggio di errore -->
					<p id="logErr" title="Messaggio di errore compilazione form login">
						<span xml:lang="en" lang="en">Password</span> e <span xml:lang="en" lang="en">Username</span> errati
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
							<input type="submit" name="login_submit" id="login_submit" value="Accedi al sito" />
						</fieldset>
					</form>
					<a class ="minimal" href="../../html/registration.html" hreflang="it" >Non ti sei ancora registrato?</a>
					<a class = "minimal" href="../../html/pass_recovery.html" hreflang="it" >Non trovi più la <span xml:lang="en" lang="en">password?</span></a>
				</div>
PEZZO
}
else
{
print <<PEZZO;
				<!-- Da caricare se l'utente è loggato-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<a href="" hreflang="it" >Esempio 1</a>
					<a href="" hreflang="it" >Esempio 2</a>
					<a href="" hreflang="it" >Esempio 3</a>
				</div>
PEZZO

}



print <<FINE;
			</div>
			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3><span xml:lang="en" lang="en">Home</span></h3>
				<div id="cont_welcome">Benvenuti nella sito SitesBoard. In questo sito potete vedere, proporre e anche accettare richieste di creazione di siti web.
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
			    	<img class="img_validator" src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" />
			    </a>
			</span>
			<span title="CSS della pagina validato secondo lo standard">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" > 
			        <img class="img_validator" src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" />
			    </a>
			</span>
			<span title="Accessibile secondo lo standard WCAG2 Livello AAA">
			    <a href="http://www.w3.org/WAI/intro/wcag"  hreflang="en-US">
			        <img class="img_validator" src="https://www.totalvalidator.com/images/valid_n_wcag2_aaa.gif" alt="Pagina accessibile" />
			    </a>
			</span>
		</div>
	</body>
</html>

<!-- 
Aggiungere:
	- colori della pagina -> PROBLEMA
	
FINE
exit;
