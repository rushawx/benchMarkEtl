package main

import (
	"fmt"
	"log"
	"net/http"
	"netApp/configs"
	"netApp/internal/record"
	"netApp/pkg/db"
)

func main() {
	conf := configs.LoadConfig()

	pgDb, err := db.NewPgDb(conf)
	if err != nil {
		log.Fatalf("failed to connect to pg: %v", err)
	}
	fmt.Printf("PG_DSN is %s\n", conf.PgDb.Dsn)

	chDb, err := db.NewChDb(conf)
	if err != nil {
		log.Fatalf("failed to connect to ch: %v", err)
	}
	fmt.Printf("CH_DSN is %s\n", conf.ChDb.Dsn)

	router := http.NewServeMux()

	recordPgRepository := record.NewRecordRepository(pgDb)
	recordChRepository := record.NewRecordRepository(chDb)

	record.NewRecordHandler(router, &record.RecordHandlerDeps{PgRecordRepository: recordPgRepository, ChRecordRepository: recordChRepository, Config: conf})

	server := http.Server{
		Addr:    ":8080",
		Handler: router,
	}

	log.Println("Server is running on port 8080")
	server.ListenAndServe()
}
