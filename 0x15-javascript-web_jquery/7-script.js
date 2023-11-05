$(document).ready(function () {
	$.get(
		'https://swapi-api.alx-tools.com/api/people/5/?format=json',
		function (character) {
			$('DIV#character').text(character.name);
		}
	);
});
