$(document).ready(function () {
	$.get("https://fourtonfish.com/hellosalut/?lang=fr", function (say) {
		$("DIV#hello").text(say.hello);
	});
});
