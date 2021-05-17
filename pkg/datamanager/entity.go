package datamanager

import "time"

type ScrapedData struct {
	ID           int
	UserID       int
	CreatedAt    time.Time
	Name         string
	Follower     int
	Following    int
	PostNumber   int
	TotalComment int
	TotalLike    int
}

type Followers struct {
	ID              int
	UserID          int
	FollowerAccount string
}

type Followings struct {
	ID               int
	UserID           int
	FollowingAccount string
}
