$(document).ready(function () {
	$.get(
		'https://swapi-api.alx-tools.com/api/films/?format=json',
		function (list) {
			list.fetches.forEach(function (movies) {
				$('<li>').text(movies.title).appendTo('ul#list_movies');
			});
		}
	);
});
