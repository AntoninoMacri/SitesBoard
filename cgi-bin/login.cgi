#!/usr/bin/perl

require 'functions/function.cgi';
require 'functions/session_function.cgi';

my $session=getSession();

print "Content-type: text/html\n\n";
print <<EOF;

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Login - SitesBoard</title> 

		<link href="../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>


		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Login - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Form login utente per SitesBoard, il sito per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Login, Password, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />

		<script type="text/javascript" src="../js/control.js"></script>
	</head>
	<body>
		<div id="container">



			<!-- HEADER -->
			<div id="header">
				<a href="home.html" hreflang="it" ><img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>
			</div>



			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable"><span xml:lang="en" lang="en">Login</span></span>
			</div>

			<div id="nav_panel">




				<!-- MENÙ DI NAVIGAZIONE --> 
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<a href="home.cgi" xml:lang="en" lang="en" hreflang="it" >Home</a>
					<p>Tipologia Siti:</p>
					<ul>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="" hreflang="it" >Personali</a></li>
						<li><a href="" hreflang="it" >Aziendali</a></li>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">Blog</span></a></li>
					</ul>
				</div>

			</div>
			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3><span xml:lang="en" lang="en">Login</span></h3>

				<!-- Div contenuto del Login -->
				<div id="cont_login" title="Form da compilare per effettuare il Login">
					Se non disponi di un <span xml:lang="en" lang="en">username</span> e di una <span xml:lang="en" lang="en">password</span> allora prima di effettuare il <span xml:lang="en" lang="en">login</span> devi <a href="registration.html" hreflang="it">registrarti</a>.<br/>
					Se hai dimenticato la <span xml:lang="en" lang="en">password</span> allora prima di effettuare il <span xml:lang="en" lang="en">login</span> devi <a href="pass_recovery.html" hreflang="it">recuperarla</a>.
					<!-- Messaggio di errore  -->
					<p id="logErr" title="Messaggio di errore compilazione form login">
EOF

$err="Sei gi&agrave; loggato";
if($session == undef)
{
$err="<span xml:lang='en' lang='en'>Password</span> e <span xml:lang='en' lang='en'>Username</span> errati";
print $err;
print <<EOF;
					</p>
					<!-- Form da compilare  -->
					<form onsubmit="return loginControl()" method="post" action="checkLogin.cgi">
						<fieldset title="Campi da compilare per effettuare il Login">
							<legend>Campi da compilare per effettuare il Login</legend>
							<label for="login_user">Username</label>
							<input type="text" name="login_user" id="login_user"/><br/>
							<label for="login_password">Password</label>
							<input type="password" name="login_password" id="login_password"/><br/>
							<input type="submit" name="login_submit" id="login_submit" value="Accedi al sito" onkeypress="return loginControl()" />
							<input type="reset" name="login_reset" id="login_reset" value="Cancella i Campi" />
						</fieldset>
					</form>
EOF
}
else
	{
		print $err;
		print "</p>";
	}
print <<EOF;
				</div>
			</div>

			<!-- Div necessario per spostare il footer in fondo alla pagina  -->
			<div id="push_block">
			</div>
		</div>



		<!-- FOOTER  -->
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


EOF
exit;
