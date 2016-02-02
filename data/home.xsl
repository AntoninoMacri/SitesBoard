<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>
<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">



<head>
		<title xml:lang="en" lang="en">Home Page - SitesBoard</title> 

		<link href="../public_html/css/screen_xsl.css" rel="stylesheet" type="text/css" media="screen"/>

		<!-- Meta Tag -->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Home Page - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Home Page di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Home, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />
		
	</head>
	<body>
		<div id="container">



			<!-- HEADER-->
			<div id="header">
				<img id="header_logo" src="../public_html/media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>
			

			</div>
			
			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3><span xml:lang="en" lang="en">Home</span></h3>
				<div id="cont_welcome">Benvenuti nella sito SitesBoard. In questo sito potete vedere, proporre e anche accettare richieste di creazione di siti web.</div>

				<!--Annunci-->
				<xsl:for-each select="bacheca/persona/listaAnnunci/annuncio">
					<div>
						<h3><span style="font-weight:bold"><xsl:value-of select="titolo/text()"/></span></h3>
						<div>
							<xsl:value-of select="oggetto/text()"/>
						</div>
						<div>
							<xsl:value-of select="tipologia/text()"/>
						</div>
						<div>
							<xsl:value-of select="data/text()"/>
						</div>
					</div>
				</xsl:for-each>

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


</xsl:template>
</xsl:stylesheet>