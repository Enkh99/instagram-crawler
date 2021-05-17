package main

import (
	"net/http"
)

func (app *application) authenticate(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		userID := app.session.GetInt(r, "userID")
		if userID == 0 {
			app.clientError(w, http.StatusForbidden)
			return
		}
		next.ServeHTTP(w, r)
	})
}
