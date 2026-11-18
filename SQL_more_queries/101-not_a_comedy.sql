-- Lists all shows of hbtn_0d_tvshows without the genre Comedy.
-- Select the shows whose id is not among the show ids linked to Comedy
SELECT title FROM tv_shows WHERE id NOT IN (SELECT show_id FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'Comedy') ORDER BY title;
