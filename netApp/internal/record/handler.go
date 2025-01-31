package record

import (
	"log"
	"net/http"
	"netApp/configs"
	"netApp/pkg/request"
	"netApp/pkg/response"
)

type RecordHandlerDeps struct {
	PgRecordRepository *RecordRepository
	ChRecordRepository *RecordRepository
	Config             *configs.Config
}

type RecordHandler struct {
	PgRecordRepository *RecordRepository
	ChRecordRepository *RecordRepository
	Config             *configs.Config
}

func NewRecordHandler(router *http.ServeMux, deps *RecordHandlerDeps) {
	handler := &RecordHandler{
		PgRecordRepository: deps.PgRecordRepository,
		ChRecordRepository: deps.ChRecordRepository,
		Config:             deps.Config,
	}

	router.HandleFunc("POST /records/post_pg", handler.CreateRecordPg())
	router.HandleFunc("POST /records/post_ch", handler.CreateRecordCh())
	router.HandleFunc("GET /records/get_pg", handler.GetRecordsPg())
	router.HandleFunc("GET /records/get_ch", handler.GetRecordsCh())
	router.HandleFunc("POST /records/replicate_pg_to_ch", handler.ReplicatePgToCh())
	router.HandleFunc("POST /records/replicate_ch_to_pg", handler.ReplicateChToPg())
	router.HandleFunc("DELETE /records/delete_pg", handler.DeleteRecordsPg())
	router.HandleFunc("DELETE /records/delete_ch", handler.DeleteRecordsCh())
}

func (h *RecordHandler) CreateRecordPg() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("CreateRecordPg")
		body, err := request.HandleBody[RecordCreateRequest](&w, r)
		if err != nil {
			return
		}
		record := NewRecord(body.Text)
		createdRecord, err := h.PgRecordRepository.CreateRecord(record)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		response.Json(w, createdRecord, http.StatusCreated)
	}
}

func (h *RecordHandler) CreateRecordCh() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("CreateRecordPg")
		body, err := request.HandleBody[RecordCreateRequest](&w, r)
		if err != nil {
			return
		}
		record := NewRecord(body.Text)
		createdRecord, err := h.ChRecordRepository.CreateRecord(record)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		response.Json(w, createdRecord, http.StatusCreated)
	}
}

func (h *RecordHandler) GetRecordsPg() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("GetRecordsPg")
		records, err := h.PgRecordRepository.GetRecords()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		response.Json(w, records, http.StatusOK)
	}
}

func (h *RecordHandler) GetRecordsCh() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("GetRecordsCh")
		records, err := h.ChRecordRepository.GetRecords()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		response.Json(w, records, http.StatusOK)
	}
}

func (h *RecordHandler) ReplicatePgToCh() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("ReplicatePgToCh")
		records, err := h.PgRecordRepository.GetRecords()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		for _, record := range records {
			_, err := h.ChRecordRepository.CreateRecord(&record)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
			}
		}
		response.Json(w, "Replicated", http.StatusOK)
	}
}

func (h *RecordHandler) ReplicateChToPg() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("ReplicateChToPg")
		records, err := h.ChRecordRepository.GetRecords()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		for _, record := range records {
			_, err := h.PgRecordRepository.CreateRecord(&record)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
			}
		}
		response.Json(w, "Replicated", http.StatusOK)
	}
}

func (h *RecordHandler) DeleteRecordsPg() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("DeleteRecordsPg")
		err := h.PgRecordRepository.DeleteRecords()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		response.Json(w, "Deleted", http.StatusOK)
	}
}

func (h *RecordHandler) DeleteRecordsCh() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("DeleteRecordsCh")
		err := h.ChRecordRepository.DeleteRecords()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		response.Json(w, "Deleted", http.StatusOK)
	}
}
