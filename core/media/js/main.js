function set_lang(lang) {
	$.post("/i18n/setlang/", {language: lang}, 
			function(){ 
				location.reload(); 
			});
}