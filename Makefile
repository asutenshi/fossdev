POETRY := ~/code/venvs/fossdev/bin/poetry
PRODUCT_SERVICE_IP ?= 127.0.0.1
PRODUCT_SERVICE_PORT ?= 8001

ORDER_SERVICE_IP ?= 127.0.0.1
ORDER_SERVICE_PORT ?= 8002

.PHONY: run run_product run_order

run:
	@make -j 2 run_product run_order

run_order:
	cd order_service && $(POETRY) run uvicorn src.app.main:app --host $(ORDER_SERVICE_IP) --port $(ORDER_SERVICE_PORT)

run_product:
	cd product_service && $(POETRY) run uvicorn src.app.main:app --host $(PRODUCT_SERVICE_IP) --port $(PRODUCT_SERVICE_PORT)
