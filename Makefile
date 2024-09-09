.PHONY=generate
generate:
	go run github.com/bufbuild/buf/cmd/buf@v1.39.0 generate

.PHONY=serve
serve:
	uv run python main.py

.PHONY=client
client:
	go run main.go
