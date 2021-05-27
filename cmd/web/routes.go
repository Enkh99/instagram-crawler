package main

import (
	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
)

func (app *application) routes() *chi.Mux {
	r := chi.NewRouter()
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)
	r.Use(app.session.Enable)

	r.With(app.authenticate).Route("/api", func(r chi.Router) {
		r.Get("/scraped-data", app.GetScrapedDataHandler)
		r.Get("/follow-diff", app.GetFollowDiff)

	})

	r.Route("/pub", func(r chi.Router) {
		r.Post("/register", app.register)
		r.Post("/login", app.login)
	})

	return r
}
