-- Lists all genres of hbtn_0d_tvshows that are not linked to the show Dexter.
-- Select the genres whose id is not among the genre ids linked to Dexter
SELECT name FROM tv_genres WHERE id NOT IN (SELECT genre_id FROM tv_show_genres INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter') ORDER BY name;
