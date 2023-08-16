-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT title
    FROM tv_shows
	JOIN tv_show_genres
    JOIN tv_genres ON (
		tv_genres.id = tv_show_genres.genre_id
        AND tv_show_genres.show_id = tv_shows.id
    )
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY title;
