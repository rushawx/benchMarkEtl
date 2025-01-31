package record

import (
	"time"

	"github.com/google/uuid"
)

type Record struct {
	ID        uuid.UUID
	Text      string
	CreatedAt time.Time
}

func NewRecord(text string) *Record {
	return &Record{
		ID:        uuid.New(),
		Text:      text,
		CreatedAt: time.Now(),
	}
}
