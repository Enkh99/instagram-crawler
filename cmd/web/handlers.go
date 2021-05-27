package main

import (
	"database/sql"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"

	"enkhod.net/snippetbox/pkg/datamanager"
)

type RegisterData struct {
	Username string
	Password string
	Link     string
}

func (app *application) register(w http.ResponseWriter, r *http.Request) {
	data := new(RegisterData)

	if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
		app.clientError(w, http.StatusBadRequest)
		return
	}

	if _, err := app.db.Exec("INSERT INTO users(username, password, link) VALUES ($1,$2,$3)", data.Username, data.Password, data.Link); err != nil {
		panic(err)
	}

	w.WriteHeader(http.StatusOK)

}

type LoginData struct {
	Username string
	Password string
}

func (app *application) login(w http.ResponseWriter, r *http.Request) {
	data := new(LoginData)

	if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
		app.clientError(w, http.StatusBadRequest)
		return
	}

	var userID int
	row := app.db.QueryRow("SELECT user_id FROM users WHERE username=$1 AND password=$2", data.Username, data.Password)
	if err := row.Scan(&userID); err != nil {
		app.clientError(w, http.StatusConflict)
		return
	}

	app.session.Put(r, "userID", userID)

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK"))
}

func (app *application) GetScrapedDataHandler(w http.ResponseWriter, r *http.Request) {
	scrapedData, err := datamanager.GetScrapedData(app.db, app.session.GetInt(r, "userID"))
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			w.WriteHeader(http.StatusForbidden)
			w.Write([]byte("null"))
			return
		} else {
			panic(err)
		}
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(scrapedData)
}
func (app *application) GetFollowDiff(w http.ResponseWriter, r *http.Request) {
	ss1, err := datamanager.GetFollowers(app.db, app.session.GetInt(r, "userID"))
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			w.WriteHeader(http.StatusForbidden)
			w.Write([]byte("null"))
			return
		} else {
			panic(err)
		}
	}
	ss2, err := datamanager.GetFollowings(app.db, app.session.GetInt(r, "userID"))
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			w.WriteHeader(http.StatusForbidden)
			w.Write([]byte("null"))
			return
		} else {
			panic(err)
		}
	}
	new, err := datamanager.GetNewFollowers(app.db, app.session.GetInt(r, "userID"))
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			w.WriteHeader(http.StatusForbidden)
			w.Write([]byte("null"))
			return
		} else {
			panic(err)
		}
	}
	lost, err := datamanager.GetLostFollowers(app.db, app.session.GetInt(r, "userID"))
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			w.WriteHeader(http.StatusForbidden)
			w.Write([]byte("null"))
			return
		} else {
			panic(err)
		}
	}

	// I'm not following back

	im_not := datamanager.Difference(ss1, ss2)
	count_im_not := len(im_not)
	fmt.Print(count_im_not)
	// Not following me back

	not := datamanager.Difference(ss2, ss1)
	count_not := len(not)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]interface{}{
		"New":        new,
		"Lost":       lost,
		"Not":        not,
		"NotCount":   count_not,
		"ImNot":      im_not,
		"CountImNot": count_im_not,
	})
}
