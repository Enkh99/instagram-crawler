package datamanager

import (
	"database/sql"
)

func GetScrapedData(db *sql.DB, userID int) (*ScrapedData, error) {
	data := new(ScrapedData)
	query := "select name, follower, following, post_number, total_comment, total_like from scraped_data where user_id=$1"
	row := db.QueryRow(query, userID)
	err := row.Scan(&data.Name, &data.Follower, &data.Following, &data.PostNumber, &data.TotalComment, &data.TotalLike)
	if err != nil {
		return data, err
	}
	return data, nil
}
func GetFollowers(db *sql.DB, userID int) ([]string, error) {
	var followers []string

	query := "select follower_account from followers where user_id=$1"
	rows, err := db.Query(query, userID)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	for rows.Next() {
		var follower string
		if err := rows.Scan(&follower); err != nil {
			return nil, err
		}
		followers = append(followers, follower)
	}

	if err := rows.Err(); err != nil {
		return nil, err
	}

	return followers, nil
}
func GetFollowings(db *sql.DB, userID int) ([]string, error) {
	var followings []string
	query := "select following_account from followings where user_id=$1"
	rows, err := db.Query(query, userID)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	for rows.Next() {
		var following string
		if err := rows.Scan(&following); err != nil {
			return nil, err
		}
		followings = append(followings, following)
	}

	if err := rows.Err(); err != nil {
		return nil, err
	}

	return followings, nil
}

func Difference(ss1 []string, ss2 []string) []string {
	var diff []string

	// Loop two times, first to find slice1 strings not in slice2,
	// second loop to find slice2 strings not in slice1
	for _, s1 := range ss1 {
		found := false
		for _, s2 := range ss2 {
			if s1 == s2 {
				found = true
				break
			}
		}
		// String not found. We add it to return slice
		if !found {
			diff = append(diff, s1)
		}
	}

	return diff
}
func GetNewFollowers(db *sql.DB, userID int) ([]string, error) {
	var newfollowers []string

	query := "select username from added_followers where user_id=$1"
	rows, err := db.Query(query, userID)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	for rows.Next() {
		var newfollower string
		if err := rows.Scan(&newfollower); err != nil {
			return nil, err
		}
		newfollowers = append(newfollowers, newfollower)
	}

	if err := rows.Err(); err != nil {
		return nil, err
	}

	return newfollowers, nil
}
func GetLostFollowers(db *sql.DB, userID int) ([]string, error) {
	var lostfollowers []string

	query := "select username from lost_followers where user_id=$1"
	rows, err := db.Query(query, userID)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	for rows.Next() {
		var lostfollower string
		if err := rows.Scan(&lostfollower); err != nil {
			return nil, err
		}
		lostfollowers = append(lostfollowers, lostfollower)
	}

	if err := rows.Err(); err != nil {
		return nil, err
	}

	return lostfollowers, nil
}

// func New(db *sql.DB, loc *time.Location) *ScrapedData {
// 	return &ScrapedData{
// 		DB:       db,
// 		Location: loc,
// 	}
// }

// var scrapedDataSelectColumnPart = `id, user_id, created_at, name, follower, following, post_number, total_comment, total_likes`

// func (repo *ScrapedData) scanScrapedData(s dbutil.Scanner) (*ScrapedData, error) {
// 	c := new(ScrapedData)
// 	if condition {

// 	}
// 	err := s.Scan(&c.ID, &c.UserID, &c.CreatedAt, &c.Name, &c.Follower, &c.Following, &c.PostNumber,
// 		&c.TotalComment, &c.TotalLike)
// 	if err != nil {
// 		return nil, err
// 	}

// 	// c.LastStatusChangedAt = c.LastStatusChangedAt.In(repo.Location)
// 	c.CreatedAt = c.CreatedAt.In(repo.Location)

// 	return c, nil
// }

// var followersDataSelectColumnPart = `user_id, follower`

// func (repo *Followers) scanFollowers(s dbutil.Scanner) (*Followers, error) {
// 	c := new(Followers)
// 	err := s.Scan(&c.UserID, &c.Follower)
// 	if err != nil {
// 		return nil, err
// 	}

// 	return c, nil
// }

// var followingsDataSelectColumnPart = `user_id, following`

// func (repo *Followings) scanFollowings(s dbutil.Scanner) (*Followings, error) {
// 	c := new(Followings)
// 	err := s.Scan(&c.UserID, &c.Following)
// 	if err != nil {
// 		return nil, err
// 	}

// 	return c, nil
// }

// func (repo *ScrapedData) GetScrapedData(user_id int) (*ScrapedData, error) {
// 	row := repo.DB.QueryRow(`SELECT `+scrapedDataSelectColumnPart+` FROM scraped_data WHERE user_id=$1`, user_id)

// 	scrapedData, err := repo.scanScrapedData(row)
// 	if err != nil {
// 		if errors.Is(err, sql.ErrNoRows) {
// 			return nil, ErrNotFound
// 		} else {
// 			return nil, err
// 		}
// 	}

// 	return scrapedData, nil
// }

// func (repo *Followers) GetFollowers(user_id int) (*Followers, error) {
// 	row := repo.DB.QueryRow(`SELECT `+followersDataSelectColumnPart+` FROM followers WHERE user_id=$1`, user_id)

// 	followers, err := repo.scanFollowers(row)
// 	if err != nil {
// 		if errors.Is(err, sql.ErrNoRows) {
// 			return nil, ErrNotFound
// 		} else {
// 			return nil, err
// 		}
// 	}

// 	return followers, nil
// }

// func (repo *Followings) GetFollowings(user_id int) (*Followings, error) {
// 	row := repo.DB.QueryRow(`SELECT `+followingsDataSelectColumnPart+` FROM followings WHERE user_id=$1`, user_id)

// 	followings, err := repo.scanFollowings(row)
// 	if err != nil {
// 		if errors.Is(err, sql.ErrNoRows) {
// 			return nil, ErrNotFound
// 		} else {
// 			return nil, err
// 		}
// 	}

// 	return followings, nil
// }
