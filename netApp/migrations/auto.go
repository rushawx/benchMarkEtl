package main

import (
	"netApp/internal/record"
	"os"

	"github.com/joho/godotenv"
	"gorm.io/driver/clickhouse"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func main() {
	err := godotenv.Load(".env")
	if err != nil {
		panic(err)
	}
	pgDb, err := gorm.Open(postgres.Open(os.Getenv("PG_DSN")), &gorm.Config{})
	if err != nil {
		panic(err)
	}
	pgDb.AutoMigrate(&record.Record{})
	chDb, err := gorm.Open(clickhouse.Open(os.Getenv("CH_DSN")), &gorm.Config{})
	if err != nil {
		panic(err)
	}
	chDb.AutoMigrate(&record.Record{})
}
