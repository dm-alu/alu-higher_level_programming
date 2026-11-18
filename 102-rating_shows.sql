-- Lists all shows of hbtn_0d_tvshows_rate by their rating sum, best first.
-- Sum the rates of each show, counting shows without rates as 0
SELECT tv_shows.title, IFNULL(SUM(tv_show_ratings.rate), 0) AS rating FROM tv_shows LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id GROUP BY tv_shows.title ORDER BY rating DESC;
