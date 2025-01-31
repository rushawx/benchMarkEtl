package db

import (
	"netApp/configs"

	"gorm.io/driver/clickhouse"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Db struct {
	*gorm.DB
}

func NewPgDb(conf *configs.Config) (*Db, error) {
	db, err := gorm.Open(postgres.Open(conf.PgDb.Dsn), &gorm.Config{})
	if err != nil {
		return nil, err
	}
	return &Db{db}, nil
}

func NewChDb(conf *configs.Config) (*Db, error) {
	db, err := gorm.Open(clickhouse.Open(conf.ChDb.Dsn), &gorm.Config{})
	if err != nil {
		return nil, err
	}
	return &Db{db}, nil
}
