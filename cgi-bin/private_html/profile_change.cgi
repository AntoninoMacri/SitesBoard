<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="it">Modifica informazioni - SitesBoard</title> 


		<link href="../../css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../../css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../../css/print.css" rel="stylesheet" type="text/css" media="print"/>
		


		<!-- Meta Tag-->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Modifica info profilo - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina di modifica delle informazioni personali" />
		<meta name="keywords" content="Changes, Profile, Logged, Siti, Web" />
		<meta name="language" content="italian it" />
		<script type="text/javascript" src="../../javascript/control.js"></script>
	</head>
	<body>
		<div id="container">


			<!-- HEADER-->
			<div id="header">

				<a href="../../html/home.html" hreflang="it" type="application/xhtml+xml"><img id="header_logo" src="../../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>

				<!-- Da caricare nel caso l'utente sia loggato -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">Nome Cognome</span>
					</div>
				</div>

			</div>

			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable" xml:lang="en" lang="en">Modifica informazioni</span>
			</div>

			<div id="nav_panel">
				
				<!-- MENÙ DI NAVIGAZIONE -->
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<p>Tipologia Siti:</p>
					<ul>
						<li><a href="" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="" hreflang="it" type="application/xhtml+xml">Personali</a></li>
						<li><a href="" hreflang="it" type="application/xhtml+xml">Aziendali</a></li>
						<li><a href="" hreflang="it" type="application/xhtml+xml"><span xml:lang="en" lang="en">Blog</span></a></li>
					</ul>
				</div>

			</div>

			<!-- Contenuti della pagina -->
			<div id="contents">

				<h3><span xml:lang="it" lang="it">Stai modificando i tuoi dati</span></h3>
				<div id="cont_profile_change">
					<p class="info" id="underline">
					Ricordati di cliccare su salva una volta che avrai terminato le modifiche
					</p>

					<form onsubmit="return profileChangeControl()" name="profileChange" method="post" action="profile_changes.cgi">
						<label for="name">Nome</label>
	  					<input id="name" type="text" name="name" value="">
	  					<br><br>
	  					<label for="surname">Cognome</label>
	  					<input id="surname" type="text" name="surname" value="">
	  					<br><br>
	  					<label for="age">Età</label>
	  					<input id="age" type="text" name="age" value="">
	  					<br><br>
	  					<label for="username">Username</label>
	  					<input type="text" name="username" value="">
	  					<br><br>
	  					<label for="email">Email</label>
	  					<input id="email" type="text" name="email" value="">
	  					<br><br>

	  					<input class="buttons" type="submit" value="Salva">

						<input class="buttons" type="reset" value="Reset">

					</form>
				</div>

			</div>

			<!-- Div necessario per spostare il footer in fondo alla pagina -->
			<div id="push-block">
			</div>
		</div>

		<!-- Footer -->
		<div id="footer">
			<span>
			    <a href="http://validator.w3.org/check?uri=referer"><img
			      src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
			</span>
			<span>
			    <a href="http://jigsaw.w3.org/css-validator/check/referer">
			        <img style="border:0;width:88px;height:31px"
			            src="http://jigsaw.w3.org/css-validator/images/vcss"
			            alt="CSS Valido!" />
			    </a>
			</span>
		</div>
	</body>
</html>
