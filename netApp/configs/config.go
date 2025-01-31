package configs

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	PgDb DbConfig
	ChDb DbConfig
}

type DbConfig struct {
	Dsn string
}

func LoadConfig() *Config {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	return &Config{
		PgDb: DbConfig{
			Dsn: os.Getenv("PG_DSN"),
		},
		ChDb: DbConfig{
			Dsn: os.Getenv("CH_DSN"),
		},
	}
}
