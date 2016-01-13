#!/usr/bin/perl

require "functions/session_function.cgi";
print "Content-type: text/html\n\n";
my $session=getSession();

print <<PRIMA_PARTE;
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="it">Profilo Utente - SitesBoard</title> 
		<link href="css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="css/print.css" rel="stylesheet" type="text/css" media="print"/>
		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Profilo Utente - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Pagina personale dell'utente loggato" />
		<meta name="keywords" content="Profile, Logged, Siti, Web" />
		<meta name="language" content="italian it" />
	</head>
	<body>
		<div id="container">
			<!-- HEADER  -->
			<div id="header">
				<a href="home.cgi" hreflang="it"><img id="header_logo" src="media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/></a>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>

PRIMA_PARTE

if($session != undef){
my $name = getSessionName($session);
my $surname = getSessionSurname($session);

print <<PEZZO;

				<!-- Da caricare nel caso l utente sia loggato  -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">Nome Cognome</span>
					</div>
					<div class="minimal">
						<a href="../html/profile_change.html" hreflang="it" type="application/xhtml+xml">Modifica Profilo<img id="header_PEL" src="../../media/profile_edit.png" alt="Iconcina di modifica profilo" title = "Modifica i dati del profilo"/></a>
					</div>
				</div>
PEZZO
}

print <<EOF;
			
			</div>

			<!-- PATH  -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable" xml:lang="en" lang="en">Profilo Utente</span>
			</div>
			<div id="nav_panel">
				<!-- Menù di navigazione -->
				<div id="nav_menu" class="menu">
					<h3>Menu</h3>
					<p>Annunci:</p>
					<ul>
						<li><a href="addInsertions.cgi" hreflang="it" type="application/xhtml+xml">Nuovo</a></li>
						<li><a href="showInsertions.html" hreflang="it" type="application/xhtml+xml">Inseriti</a></li>
						<li><a href="acceptedInsertions.html" hreflang="it" type="application/xhtml+xml">Accettati</a></li>
					</ul>
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
				<h3><span xml:lang="it" lang="it">Il tuo profilo</span></h3>
				<div id="cont_profile">
					<p class="info">
					Ti trovi all'interno dell'area personale del tuo profilo. Da qui è possibile gestire tutti i tuoi annunci o quelli a cui sei interessato.
					</p>
					<p class="info">
					In particolare puoi: visualizzare gli annunci da te inseriti. Visualizzare gli annunci che hai accettato in attesa di conclusione asta. Aggiungere un nuovo annuncio che apparirà nella bacheca di <span xml:lang="en">SitesBoard</span> in ordine, dal più vicino al più lontano, di scadenza. Cancellare i tuoi annunci che per qualche motivo non ti interessa più condividere. 
					</p>
					<p class="info" id="underline">
					Ricordati di fare salva quando hai portato a termine tutte le eventuali operazioni!
					</p>
					<form method="post" action="profile_changes.cgi">
						<label for="name">Nome:</label>
  					<br><br>
  					<label for="surname">Cognome:</label>
  					<br><br>
  					<label for="age">Età:</label id="age" >
  					<br><br>
  					<label for="username">Username:</label>
  					<br><br>
  					<label for="email">Email:</label>
  					<br><br>
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