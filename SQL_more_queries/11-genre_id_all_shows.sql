-- Lists all shows of hbtn_0d_tvshows with their genre id, or NULL if none is linked.
-- Select every show and keep those without a genre
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
