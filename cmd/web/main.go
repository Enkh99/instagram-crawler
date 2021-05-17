package main

import (
	"database/sql"
	"flag"
	"log"
	"net/http"
	"os"
	"time"

	"enkhod.net/snippetbox/pkg/datamanager"

	"github.com/golangcollege/sessions"
	_ "github.com/lib/pq"
)

var DBConnection = "host=localhost port=5432 user=postgres password=password dbname=insta sslmode=disable"

type application struct {
	errorLog *log.Logger
	infoLog  *log.Logger
	db       *sql.DB
	sdatas   *datamanager.ScrapedData
	session  *sessions.Session
}

func main() {
	addr := flag.String("addr", ":4000", "HTTP network address")
	secret := flag.String("secret", "s6Ndh+pPbnzHfafwefwef9Pk8qGWhTzbpa@ge", "Secret key")
	flag.Parse()

	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	errorLog := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)

	db, err := openDB(DBConnection)
	if err != nil {
		errorLog.Fatal(err)
	}

	session := sessions.New([]byte(*secret))
	session.Lifetime = 480 * time.Hour

	app := &application{
		errorLog: errorLog,
		infoLog:  infoLog,
		db:       db,
		session:  session,
	}

	srv := &http.Server{
		Addr:     *addr,
		ErrorLog: errorLog,
		Handler:  app.routes(),
	}

	infoLog.Printf("Starting server on %s", *addr)
	errorLog.Fatal(srv.ListenAndServe())
}

func openDB(dsn string) (*sql.DB, error) {
	db, err := sql.Open("postgres", dsn)
	if err != nil {
		return nil, err
	}
	if err = db.Ping(); err != nil {
		return nil, err
	}
	return db, nil
}
